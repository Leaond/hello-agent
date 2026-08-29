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

        step = {
            "tool_name":tool_name,
            "input_template":input_template,
            "output_key":output_key or f"step_{len(self.steps)}_result"
        }
        self.steps.append(step)
        print(f"✅ 工具链 '{self.name}' 添加步骤: {tool_name}")
