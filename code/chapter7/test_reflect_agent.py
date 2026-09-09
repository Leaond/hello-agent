from dotenv import  load_dotenv
from hello_agents import HelloAgentsLLM,ToolRegistry,CalculatorTool,ReflectionAgent
from my_simple_agent import MySimpleAgent

load_dotenv()

llm = HelloAgentsLLM()

reflection_agent = ReflectionAgent(
    name="豆包",
    llm=llm,

)
reflection_agent.run("请分析一下把一头大象放进冰箱里面需要几步？")

# 2. 自定义提示词
# code_prompts = {
#     "initial": "你是Python专家，请编写函数：{task}",
#     "reflect": "请审查代码的算法效率：\n任务：{task}\n代码：{content}",
#     "refine": "请根据反馈优化代码：\n任务：{task}\n反馈：{feedback}"
# }
# reflection_agent = ReflectionAgent(
#     name="豆包",
#     llm=llm,
#     custom_prompts=code_prompts
# )