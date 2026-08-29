'''
Date: 2026-08-24 11:34:58
LastEditors: liuzhengliang
LastEditTime: 2026-08-28 17:30:56
Description: 
'''
"""工具链管理器 - HelloAgents工具链式调用支持"""

from typing import  List,Dict,Any,Optional
from .registry import ToolRegistry

class ToolChain:
    """工具链 - 支持多个工具的顺序执行"""

    def __init__(self,name:str,description:str):
        self.name = name
        self.description = description
        self.steps:List[Dict[str,Any]] = []

    def add_step(self,tool_name:str,input_template:str,output_key:str = None) :
        """
        添加工具执行步骤
        
        Args:
            tool_name: 工具名称
            input_template: 输入模板，支持变量替换，如 "{input}" 或 "{search_result}"
            output_key: 输出结果的键名，用于后续步骤引用
        """
        step = {
            "tool_name":tool_name,
            "input_template":input_template,
            "output_key":output_key or f"step_{len(self.steps)}_result"
        }
        self.steps.append(step)
        print(f"✅ 工具链 '{self.name}' 添加步骤: {tool_name}")

    def execute(self,registry: ToolRegistry,input_data:str,context:Dict[str,Any] = None) -> strr:
        """
        执行工具链
            Args：
                registry: 工具链注册表
                input_data: 初始输入数据
                context：执行上下文，用于变量替换

            returns：
                最终的执行结果
        """
        if not self.steps:
            return "❌ 工具链为空，无法执行"

        if context is None:
            context = {}
        context["input"] = input_data
        final_result = input_data

        for i,step in enumerate(self.steps):
            tool_name = step["tool_name"]
            input_template = step["input_template"]
            output_key = step["output_key"]

            print(f"📝 执行步骤 {i+1}/{len(self.steps)}: {tool_name}")

            # 替换模板中的变量
            try:
                actual_input = input_template.format(**context)
            except KeyError as e:
                return f"❌ 模板变量替换失败: {e}"

#             执行工具
            try:
                result = registry.execute_tool(tool_name,actual_input)
                context[output_key] = result
                final_result = result
                print(f"✅ 步骤 {i + 1} 完成")
            except Exception as e:
                return f"❌ 工具 '{tool_name}' 执行失败: {e}"

            print(f"🎉 工具链 '{self.name}' 执行完成")
            return final_result
































