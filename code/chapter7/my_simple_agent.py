'''
Date: 2026-08-19 16:16:49
LastEditors: liuzhengliang
LastEditTime: 2026-08-21 09:37:25
Description: 
'''
import re
from typing import Optional, Iterator, List
from hello_agents1 import SimpleAgent, HelloAgentsLLM, Config, Message,ToolRegistry


class MySimpleAgent(SimpleAgent):
    """ 重写的简单对话Agent
    展示如何基于框架基类构建自定义Agent
    """

    def __init__(
            self,
            name:str,
            llm:HelloAgentsLLM,
            system_prompt:Optional[str]=None,
            config:Optional[Config]=None,
            tool_registry: ToolRegistry | None =None,
            enable_tool_calling:bool = True
    ) -> None:
        super().__init__(name,llm,system_prompt,config)
        self.tool_registry =tool_registry
        self.enable_tool_calling =enable_tool_calling and tool_registry is not None

    def run(self, input_text: str,max_tool_iterations:int = 3, **kwargs) -> str:
        """
        重写的运行方法 - 实现简单对话逻辑，支持可选工具调用
        """

        print(f"🤖 {self.name} 正在处理: {input_text}")

    #     构建消息列表
        messages = []

    #     添加系统消息（可能包含工具信息）
        enhanced_system_prompt = self._get_enhanced_system_prompt()
        messages.append({"role":"system","content":enhanced_system_prompt})

    #   添加历史消息
        for msg in self._history:
            messages.append({"role":msg.role,"content":msg.content})
    #     添加当前用户消息
        messages.append({"role":"user","content":input_text})

    #     如果没有启用工具调用，使用简单对话逻辑
        if not self.enable_tool_calling:
            response = self.llm.invoke(messages,**kwargs)
            self.add_message(Message(input_text,"user"))
            self.add_message(Message(response,"assistant"))
            print(f"✅ {self.name} 响应完成")
            return response
        return  self._run_with_tools(messages,input_text,max_tool_iterations,**kwargs)

    def stream_run(self, input_text: str, **kwargs) -> Iterator[str]:
        """流式运行"""
        print(f"🌊 {self.name} 开始流式处理: {input_text}")

        messages = []

        if self.system_prompt:
            messages.append({"role":"system","content":self.system_prompt})

        for msg in self._history:
            messages.append({"role":msg.role,"content":msg.content})

        messages.append({"role":"user","content":input_text})

    # #     流式调用llm
        full_response = ""
        print("📝 实时响应: ", end="")

        for chunk in self.llm.stream_invoke(messages,**kwargs):
            full_response += chunk
            print(chunk, end="", flush=True)
            yield chunk

        print()  # 换行

    #     保存完整对话到历史记录
        self.add_message(Message(input_text,"user"))
        self.add_message(Message(full_response,"assistant"))
        print(f"✅ {self.name} 流式响应完成")

    def add_tool(self,tool) ->None:
        """添加工具到Agent（便利方法）"""
        if not self.tool_registry:
            from hello_agents1 import ToolRegistry
            self.tool_registry = ToolRegistry()
            self.enable_tool_calling = True

        self.tool_registry.register_tool(tool)
        print(f"🔧 工具 '{tool.name}' 已添加")

    def has_tools(self) ->bool:
        """检查是否有可用工具"""
        return self.enable_tool_calling and self.tool_registry is not None

    def remove_tool(self,tool_name:str) ->bool:
        """移除tool 便利方法"""
        if self.tool_registry:
            self.tool_registry.unregistry(tool_name)
            return True
        return False

    def list_tools(self) -> list:
        if self.tool_registry:
            return  self.tool_registry.list_tools()
        return []

    def _get_enhanced_system_prompt(self) ->str:
        """构建增强的系统提示词，包含工具信息"""
        base_prompt = self.system_prompt or "你是一个全能的AI助手"

        if not self.enable_tool_calling or not self.tool_registry:
            return base_prompt

    #     获取工具描述
        tools_description = self.tool_registry.get_tools_description()
        if not tools_description or tools_description == "暂无可用工具":
            return  base_prompt

        tools_section = "\n\n## 可用工具\n"
        tools_section += "你可以使用以下工具来帮助回答问题:\n"
        tools_section += tools_description + "\n"

        tools_section += "\n## 工具调用格式\n"
        tools_section += "当需要使用工具时，请使用以下格式:\n"
        tools_section += "`[TOOL_CALL:{tool_name}:{parameters}]`\n"
        tools_section += "例如:`[TOOL_CALL:search:Python编程]` 或 `[TOOL_CALL:memory:recall=用户信息]`\n\n"
        tools_section += "工具调用结果会自动插入到对话中，然后你可以基于结果继续回答。\n"

        return base_prompt + tools_section

    def _run_with_tools(self,messages:list,input_text:str,max_tool_iterations:int,**kwargs) -> str:
        """支持工具调用的运行逻辑"""
        current_iteration = 0
        final_response = ""

        # 调用工具逻辑
        while current_iteration <max_tool_iterations:
    #         调用llm
            response = self.llm.invoke(messages,**kwargs)

    #         检查是否有工具调用
            tool_calls = self._parse_tool_calls(response)
            if tool_calls:
                print(f"🔧 检测到 {len(tool_calls)} 个工具调用")
    #             执行所有工具调用并手机结果
                tool_results = []
                clean_response = response

                for call in tool_calls:
                    result = self._execute_tool_call(call['tool_name'],call['parameters'])
                    tool_results.append(result)
    #                 从响应中移除工具调用标记
                    clean_response = clean_response.replace(call['original'],'')

    #             构建包含工具结果的消息
                messages.append({"role":"assistant","content":clean_response})

                tool_results_text = "\n\n".join(tool_results)
                messages.append({"role": "user", "content": f"工具执行结果:\n{tool_results_text}\n\n请基于这些结果给出完整的回答。"})

                current_iteration +=1
                continue
            final_response = response
            break

        # 如果超过最大迭代次数，获取最后一次回答
        if current_iteration >= max_tool_iterations and not final_response:
            final_response = self.llm.invoke(messages, **kwargs)

            # 保存到历史记录
        self.add_message(Message(input_text, "user"))
        self.add_message(Message(final_response, "assistant"))
        print(f"✅ {self.name} 响应完成")

        return final_response

    def _parse_tool_calls(self,text:str):
        """解析llm回答是否有工具调用"""
        pattern = r'\[TOOL_CALL:([^:]+):([^\]]+)\]'
        matches = re.findall(pattern,text)

        tool_calls = []
        for tool_name,parameters in matches:
            tool_calls.append({
                "tool_name":tool_name,
                "parameters":parameters.strip(),
                "original":f'[TOOL_CALL:{tool_name}:{parameters}]'
            })

        return tool_calls

    def _execute_tool_call(self,tool_name:str,parameters:str) ->str:
        """执行工具调用"""
        if not self.tool_registry:
            return f"❌ 错误:未配置工具注册表"

        try:
    #         只能参数解析
            if tool_name == 'calculator':
    #             计算器工具直接接入表达式
                result = self.tool_registry.excute_tool(tool_name,parameters)
            else:
    #             其他工具解析
                param_dict = self._parse_tool_parameters(tool_name,parameters)
                tool = self.tool_registry.get_tool(tool_name)
                if not tool:
                    return f"❌ 错误:未找到工具 '{tool_name}'"
                result = tool.run(param_dict)
            return f"🔧 工具 {tool_name} 执行结果:\n{result}"

        except Exception as e:
            return f"❌ 工具调用失败:{str(e)}"

    def _parse_tool_parameters(self,tool_name:str,parameters:str) ->dict:
        """解析工具参数"""
        param_dict = {}

        if '=' in parameters:
    #         key=value格式
            if ',' in parameters:
    #             多参数
                pairs = parameters.split(',')
                for pair in pairs:
                    key,value = pair.split('=',1)
                    param_dict[key.strip()] = value.strip()
            else:
                # 单个参数:key=value
                key, value = parameters.split('=', 1)
                param_dict[key.strip()] = value.strip()

        else:
            # 直接传入参数，根据工具类型智能推断
            if tool_name == 'search':
                param_dict = {'query': parameters}
            elif tool_name == 'memory':
                param_dict = {'action': 'search', 'query': parameters}
            else:
                param_dict = {'input': parameters}

        return param_dict

    def add_message(self, message: Message):
        """添加消息到历史记录"""
        # self._history.append({"role":"system","content":})
        pass
    
    def clear_history(self):
        """清空历史记录"""
        self._history.clear()
    
    def get_history(self) -> list[Message]:
        """获取历史记录"""
        return self._history.copy()
    
    def __str__(self) -> str:
        return f"Agent(name={self.name}, provider={self.llm.provider})"