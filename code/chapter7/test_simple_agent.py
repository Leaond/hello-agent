'''
Date: 2026-08-20 16:22:15
LastEditors: liuzhengliang
LastEditTime: 2026-08-21 13:57:47
Description: 
'''
from dotenv import  load_dotenv
from hello_agents1 import  HelloAgentsLLM,
from hello_agents1.tools import CalculatorTool
from code.chapter7.my_simple_agent import MySimpleAgent

load_dotenv()

llm = HelloAgentsLLM()

# 1. 基础非流式对话
# print("===基础对话")
basic_agent = MySimpleAgent(
    name="基础助手",
    llm=llm,
    system_prompt="你是一个友好的AI助手，请用简洁明了的方式回答问题"

)
# response1 = basic_agent.stream_run("你好，请介绍一下自己")
# print(f"基础对话响应: {response1}\n")

# 2. 带固定工具的agent
# tool_registry = ToolRegistry()
# calculator = CalculatorTool()
# tool_registry.register_tool(calculator)
#
# enhanced_agent = MySimpleAgent(
#     name="增强助手",
#     llm=llm,
#     system_prompt="你是一个智能助手，可以使用工具来帮助用户。",
#     tool_registry=tool_registry,
#     enable_tool_calling=True
# )
# response2 = enhanced_agent.run("请计算15*8+22")
# print(f"工具增强响应: {response2}\n")

# 3. 流式响应
# print("=== 测试3:流式响应 ===")
# print("流式响应: ", end="")
# for chunk in basic_agent.stream_run("请解释什么是人工智能"):
#     pass


# 测试4:动态添加工具
print("\n=== 测试4:动态工具管理 ===")
print(f"添加工具前: {basic_agent.has_tools()}")
basic_agent.add_tool(calculator)
print(f"添加工具后: {basic_agent.has_tools()}")
print(f"可用工具: {basic_agent.list_tools()}")

# 查看对话历史
print(f"\n对话历史: {len(basic_agent.get_history())} 条消息")
