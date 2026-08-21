'''
Date: 2026-08-17 16:21:24
LastEditors: liuzhengliang
LastEditTime: 2026-08-18 10:01:32
Description: LangGraph的三个要素：状态、节点、边
    状态：整个图的执行过程全都围绕 一个全局共享的状态 展开，这个状态可以存储包含任何你想要保存的信息，例如上下文、历史、中间结果、迭代次数等
    节点：定义了一个具体的执行步骤，例如调用llm或者调用工具。每个节点都是一个函数，都接受一个当前的状态，并且返回一个更新后的状态。节点是执行具体工作的单元
    边：定义了一个节点到领一个节点的跳转逻辑
'''

import asyncio

from typing import List, TypedDict, Annotated

from langchain_core.messages import HumanMessage,AIMessage,SystemMessage
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph,START,END
from langgraph.graph.message import add_messages
from langgraph.checkpoint.memory import InMemorySaver

import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()


# 定义一个贯穿整个工作流的全局状态。这是一个共享的数据结构，它在图的每个节点之间传递，作为工作流的持久化上下文。
class SearchState(TypedDict):
    messages: Annotated[List,add_messages]
    user_query:str
    search_query:str
    search_results:str
    final_answer:str
    step:str
    
# 初始化模型和Tavily客户端
llm = ChatOpenAI(
    model=os.getenv("LLM_MODEL_ID"),
    api_key=os.getenv("LLM_API_KEY"),
    base_url=os.getenv("LLM_BASE_URL"),
    temperature=0.7
)

# 初始化Tavily客户端
tavily_client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

# 定义节点
# 理解
def understand_query_node(state: SearchState) -> SearchState:
    """ 步骤1 理解用户查询并生成搜索关键字"""

#     获取最新的用户消息
    user_message = ""
    for msg in reversed(state['messages']):
        if isinstance(msg,HumanMessage):
            user_message = msg.content
            break

    understand_prompt = f""""分析用户的查询：{user_message}"
    请完成两个任务：
        1. 简洁总结用户想要了解什么
        2. 生成最适合搜索的关键词（中英文均可，要精准）
        
        格式：
        理解：[用户需求总结]
        搜索词：[最佳搜索关键词]"""
    response = llm.invoke([SystemMessage(content=understand_prompt)])

#     提取搜索关键词
    response_text = response.content
    search_query = user_message

    if "搜索词：" in response_text:
        search_query = response_text.split("搜索词：")[1].strip()
    elif "搜索关键词：" in response_text:
        search_query = response_text.split("搜索关键词：")[1].strip()

    return  {
        "user_query": response.content,
        "search_query": search_query,
        "step":"understand",
        "messages":[AIMessage(content=f"我理解您的需求：{response.content}")]
    }

# 搜索
def tavily_search_node(state: SearchState) -> SearchState:
    """步骤2 使用 Tavily API 进行搜索"""
    search_query = state["search_query"]

    try:
        print(f"🔍 正在搜索: {search_query}")

#         调用api进行搜索
        response = tavily_client.search(
            query=search_query,
            search_depth="basic",
            include_answer= True,
            include_raw_content=False,
            max_results=5
        )

#         处理搜索结果
        search_results = ""

        if response.get("answer"):
            search_results = f"综合答案：\n{response['answer']}\n\n"

            # 添加具体的搜索结果
            if response.get("results"):
                search_results += "相关信息：\n"
                for i, result in enumerate(response["results"][:3], 1):
                    title = result.get("title", "")
                    content = result.get("content", "")
                    url = result.get("url", "")
                    search_results += f"{i}. {title}\n{content}\n来源：{url}\n\n"

            if not search_results:
                search_results = "抱歉，没有找到相关信息。"

            return {
                "search_results": search_results,
                "step": "searched",
                "messages": [AIMessage(content=f"✅ 搜索完成！找到了相关信息，正在为您整理答案...")]
            }

    except Exception as e:
        error_msg = f"搜索时发生错误: {str(e)}"
        print(f"❌ {error_msg}")

        return {
            "search_results": f"搜索失败：{error_msg}",
            "step": "search_failed",
            "messages": [AIMessage(content="❌ 搜索遇到问题，我将基于已有知识为您回答")]
        }


# 回答
def generate_answer_node(state: SearchState) -> SearchState:
    """步骤3：基于搜索结果生成最终答案"""

    # 检查是否有搜索结果
    if state["step"] == "search_failed":
        # 如果搜索失败，基于LLM知识回答
        fallback_prompt = f"""搜索API暂时不可用，请基于您的知识回答用户的问题：
        
        用户问题：{state['user_query']}
        
        请提供一个有用的回答，并说明这是基于已有知识的回答。"""

        response = llm.invoke([SystemMessage(content=fallback_prompt)])

        return {
            "final_answer": response.content,
            "step": "completed",
            "messages": [AIMessage(content=response.content)]
        }

    # 基于搜索结果生成答案
    answer_prompt = f"""基于以下搜索结果为用户提供完整、准确的答案：

        用户问题：{state['user_query']}
        
        搜索结果：
        {state['search_results']}
        
        请要求：
        1. 综合搜索结果，提供准确、有用的回答
        2. 如果是技术问题，提供具体的解决方案或代码
        3. 引用重要信息的来源
        4. 回答要结构清晰、易于理解
        5. 如果搜索结果不够完整，请说明并提供补充建议"""

    response = llm.invoke([SystemMessage(content=answer_prompt)])

    return {
        "final_answer": response.content,
        "step": "completed",
        "messages": [AIMessage(content=response.content)]
    }

# 构建搜索工作流
def create_search_assistant():
    workflow = StateGraph(SearchState)

#     添加三个节点
    workflow.add_node("understand",understand_query_node)
    workflow.add_node("search",tavily_search_node)
    workflow.add_node("answer",generate_answer_node)

#     添加边，设置线性流程
    workflow.add_edge(START,"understand")
    workflow.add_edge("understand","search")
    workflow.add_edge("search", "answer")
    workflow.add_edge("answer", END)

#     编译图
    memory = InMemorySaver()
    app = workflow.compile(checkpointer=memory)

    return app

# 定义主函数
async def main():
    """主函数：运行智能搜索助手"""

    # 检查API密钥
    if not os.getenv("TAVILY_API_KEY"):
        print("❌ 错误：请在.env文件中配置TAVILY_API_KEY")
        return

    app = create_search_assistant()

    print("🔍 智能搜索助手启动！")
    print("我会使用Tavily API为您搜索最新、最准确的信息")
    print("支持各种问题：新闻、技术、知识问答等")
    print("(输入 'quit' 退出)\n")

    session_count = 0

    while True:
        user_input = input("🤔 您想了解什么: ").strip()

        if user_input.lower() in ['quit', 'q', '退出', 'exit']:
            print("感谢使用！再见！👋")
            break

        if not user_input:
            continue

        session_count += 1
        config = {"configurable": {"thread_id": f"search-session-{session_count}"}}

        # 初始状态
        initial_state = {
            "messages": [HumanMessage(content=user_input)],
            "user_query": "",
            "search_query": "",
            "search_results": "",
            "final_answer": "",
            "step": "start"
        }

        try:
            print("\n" + "=" * 60)

            # 执行工作流
            async for output in app.astream(initial_state, config=config):
                for node_name, node_output in output.items():
                    if "messages" in node_output and node_output["messages"]:
                        latest_message = node_output["messages"][-1]
                        if isinstance(latest_message, AIMessage):
                            if node_name == "understand":
                                print(f"🧠 理解阶段: {latest_message.content}")
                            elif node_name == "search":
                                print(f"🔍 搜索阶段: {latest_message.content}")
                            elif node_name == "answer":
                                print(f"\n💡 最终回答:\n{latest_message.content}")

            print("\n" + "=" * 60 + "\n")

        except Exception as e:
            print(f"❌ 发生错误: {e}")
            print("请重新输入您的问题。\n")


if __name__=="__main__":
    asyncio.run(main())