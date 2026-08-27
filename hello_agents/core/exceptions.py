'''
Date: 2026-08-27 08:47:52
LastEditors: liuzhengliang
LastEditTime: 2026-08-27 08:55:29
Description: 
'''
"""异常体系"""

class HelloAgentsException(Exception):
    """HelloAgents 基础异常类"""
    pass

class LLMException(HelloAgentsException):
    """LLM相关异常"""
    pass

class AgentException(HelloAgentsException):
    """Agent相关异常"""
    pass

class ConfigException(HelloAgentsException):
    """配置相关异常"""
    pass

class ToolException(HelloAgentsException):
    """工具相关异常"""
    pass
