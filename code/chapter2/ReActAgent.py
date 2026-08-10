'''
Date: 2026-08-06 10:51:23
LastEditors: liuzhengliang
LastEditTime: 2026-08-10 15:30:30
Description: 模拟基于ReActagent范式的智能体搭建
'''

import os
from typing import Any, Dict
from serp_api import search
from dotenv import load_dotenv
from llm_client import HelloAgentsLLM
import re

# 加载环境变量
load_dotenv()

# ReAct 提示词模板
REACT_PROMPT_TEMPLATE = """
请注意，你是一个有能力调用外部工具的智能助手。

可用工具如下:
{tools}

请严格按照以下格式进行回应:

Thought: 你的思考过程，用于分析问题、拆解任务和规划下一步行动。
Action: 你决定采取的行动，必须是以下格式之一:
- `{{tool_name}}[{{tool_input}}]`:调用一个可用工具。
- `Finish[最终答案]`:当你认为已经获得最终答案时。
- 当你收集到足够的信息，能够回答用户的最终问题时，你必须在Action:字段后使用 Finish[最终答案] 来输出最终答案。

现在，请开始解决以下问题:
Question: {question}
History: {history}
"""



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
            print(f"当前完整提示词----：{prompt}")

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
            print(f"我将调用以下工具来查询：{tool_name,tool_input}")
            tool_function = self.tool_executor.getTool(tool_name)
            if not tool_function:
                observation = f"错误:未找到名为 '{tool_name}' 的工具。"
            else:
                observation = tool_function(tool_input) # 调用真实工具
            
            print(f"👀 观察: {observation}")

            # 将本轮的Action和Observation添加到历史记录中
            self.history.append(f"Action: {action}")
            self.history.append(f"Observation: {observation}")
        
        # 循环结束
        print("已达到最大步数，流程终止。")
        return None
    
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
    print("你好，请问有什么想要咨询的？")
    question = input("input: ")

    llm_client = HelloAgentsLLM()
    tool_exector = ToolExecutor()
    tool_exector.regiserTool("Search","搜索引擎",search)
    max_steps=8

    agent = ReActAgent(llm_client=llm_client,tool_exector=tool_exector,max_steps=max_steps)
    agent.run(question)