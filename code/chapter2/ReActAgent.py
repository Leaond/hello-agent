'''
Date: 2026-08-06 10:51:23
LastEditors: liuzhengliang
LastEditTime: 2026-08-06 16:26:08
Description: 结合前面几节完成的工具，现在模拟ReActagent范式完成智能体搭建
'''

import os
from typing import Any, Dict,List
from serpapi import SerpApiClient
from dotenv import load_dotenv
from openai import OpenAI
import re

# 加载环境变量
load_dotenv()

class HelloAgentsLLM:
    """完成定制客户端，用于调用任何兼容OpenAI接口的服务，并默认使用流式响应

    """
    def __init__(self,model:str = None,apiKey:str = None,baseUrl:str = None,timeout:int = None) -> None:
        """初始化客户端
        """
        self.model = model or os.getenv("LLM_MODEL_ID")
        apiKey = apiKey or os.getenv("LLM_API_KEY")
        baseUrl = baseUrl or os.getenv("LLM_BASE_URL")
        timeout = timeout or int(os.getenv("LLM_TIMEOUT",60))

        if not all([self.model,apiKey,baseUrl]):
            raise ValueError("模型ID、API密钥和服务地址必须被提供或在.env文件中定义。")
        
        self.client = OpenAI(api_key=apiKey,base_url=baseUrl,timeout=timeout)

    
    def think(self,messages:List[Dict[str,str]],temperature:float = 0)-> str:
        """调用大语言模型进行思考，并返回其响应
        """
        print(f"正在调用 {self.model} 模型...")
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                temperature=temperature,
                stream = True,
            )

            # 处理流式响应
            print("大语言模型响应成功：")
            collected_content = []
          
            for chunk in response:
                if not chunk.choices:
                    continue
                content = chunk.choices[0].delta.content or ""
                print(content, end="", flush=True)
                collected_content.append(content)
            print()  # 在流式输出结束后换行
            return "".join(collected_content)

        except Exception as e:
            print(f"❌ 调用LLM API时发生错误: {e}")
            return None

def search(query:str)-> str:
    """一个基于SerpApi的实战网页搜索引擎工具。
    他会只能等解析搜索结果，优先返回直接答案和指示图谱信息
    """
    print(f"正在执行网页搜素：{query}")
    try:
        api_key = os.getenv("SERPAPI_API_KEY")
        if not api_key:
            return "错误:SERPAPI_API_KEY 未在 .env 文件中配置。"

        params = {
            "engine":"google",
            "q":query,
            "api_key":api_key,
            "gl":"cn",# 国家代码
            "hl":"zh-cn" # 语言代码
        }

        client = SerpApiClient(params)
        results = client.get_dict()

        # 智能解析：优先寻找最直接的答案
        if "answer_box_list" in results:
            return "\n".join(results["answer_box_list"])
        if "answer_box" in results and "answer" in results["answer_box"]:
            return results["answer_box"]["answer"]
        if "knowledge_graph" in results and "description" in results["knowledge_graph"]:
            return results["knowledge_graph"]["description"]
        if "organic_results" in results and results["organic_results"]:
            # 如果没有直接答案，则返回前三个有机结果的摘要
            snippets = [
                f"[{i+1}] {res.get('title', '')}\n{res.get('snippet', '')}"
                for i, res in enumerate(results["organic_results"][:3])
            ]
            return "\n\n".join(snippets)
        
        return f"对不起，没有找到关于 '{query}' 的信息。"

    except Exception as e:
        return f"搜索时发生错误: {e}"

class ToolExecutor:
    """一个工具执行器，负责管理和执行工具
    """
    def __init__(self) -> None:
        self.tools:Dict[str,Dict[str,Any]] = {}
    
    def regiserTool(self,name:str,description:str,func:callable):
        """向工具箱中注册一个新工具
        """
        if name in self.tools:
            print(f"警告:工具 '{name}' 已存在，将被覆盖。")
        self.tools[name] = {"description": description, "func": func}
        print(f"工具 '{name}' 已注册。")

    def getTool(self,name:str)->callable:
        """根据名称获取一个工具的执行函数
        """
        return self.tools.get(name,{}).get("func")

    def getAvailableTools(self)->str:
        """获取所有可用工具的格式化描述文字
        """
        return "\n".join([
            f"-{name}:{info['description']}"
            for name,info in self.tools.items()
        ])

class ReActAgent:
    def __init__(self,llm_client: HelloAgentsLLM,tool_exector:ToolExecutor,max_steps:int = 5) -> None:
        self.llm_client = llm_client
        self.tool_executor=tool_exector
        self.max_steps = max_steps
        self.history = []
    
    def run(self, question:str):
        """运行ReAct智能体来回答一个问题
        """
        self.history = [] # 每次运行时重置历史记录
        current_step = 0

        while current_step<self.max_steps:
            current_step+=1
            print(f"--- 第 {current_step} 步 ---")
            
            # 1.格式化提示词
            tools_desc = self.tool_executor.getAvailableTools()
            history_str = "\n".join(self.history)
            prompt = REACT_PROMPT_TEMPLATE.format(
                tools=tools_desc,
                question=question,
                history=history_str
            )

            # 2. 
            messages = [{"role": "user", "content": prompt}]
            response_text = self.llm_client.think(messages=messages)

            if not response_text:
                print("错误:LLM未能返回有效响应。")
                break

            # 3.解析LLM的输出
            thought,action = self._parse_output(response_text)

            if thought:
                print(f"思考: {thought}")
            if not action:
                print("警告:未能解析出有效的Action，流程终止。")
                break
            
            # 4. 执行Action
            if action.startswith("Finish"):
                final_answer = re.match(r"Finish\[(.*)\]",action).group(1)
                print(f"🎉 最终答案: {final_answer}")
                return final_answer
            
            tool_name,tool_input = self._parse_action(action)
            if not tool_function:
                observation = f"错误:未找到名为 '{tool_name}' 的工具。"
            else:
                observation = tool_function(tool_input) # 调用真实工具
    
    def _parse_output(self,text:str):
        """解析LLM的输出，提取Thought和Action
        """
        # Thought: 匹配到Action：或者文本末尾
        thought_match = re.search(r"Thought:\s*(.*?)(?=\nAction:|$)",text,re.DOTALL)
        # Action: 匹配到文本末尾
        action_match = re.search(r"Action:\s*(.*?)$",text,re.DOTALL)
        thought = thought_match.group(1).strip() if thought_match else None
        action = action_match.group(1).strip() if action_match else None
        return thought,action

    def _parse_action(self,action_text:str):
        """解析action字符串，提取工具名称和输入
        """

        match = re.match(r"(\w+)\[(.*)\]",action_text,re.DOTALL)
        if match:
            return match.group(1),match.group(2)
        return None,None


# --- 工具初始化与使用示例 ---
if __name__ == '__main__':
    # 1.初始化工具执行器
    toolExecutor = ToolExecutor()

    # 2.注册我们的实战搜索工具
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    toolExecutor.regiserTool("Search",search_description,search)

    # 3.打印可用的工具
    print("\n--- 可用的工具 ---")
    print(toolExecutor.getAvailableTools())

    # 4.智能体的Action调用
    print("\n--- 执行 Action: Search['英伟达最新的GPU型号是什么'] ---")
    tool_name = "Search"
    tool_input = "英伟达最新的GPU型号是什么"
    tool_function = toolExecutor.getTool(tool_name)
    if tool_function:
        observation = tool_function(tool_input)
        print("--- 观察 (Observation) ---")
        print(observation)
    else:
        print(f"错误:未找到名为 '{tool_name}' 的工具。")