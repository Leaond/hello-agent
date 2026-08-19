'''
Date: 2026-08-19 10:15:10
LastEditors: liuzhengliang
LastEditTime: 2026-08-19 11:33:46
Description: 
'''
from dotenv import load_dotenv
from my_llm import MyLLM

load_dotenv()

# llm=MyLLM(provider="modelscope")

# 连接本地模型
llm=MyLLM(
    provider="ollama",
    base_url="http://localhost:11434/v1",
    api_key="ollama",
    model="llama3"
    )

messages = [{"role": "user", "content": "你好，请介绍一下你自己。"}]

response_stream = llm.think(messages=messages)

print("ModelScope Response:")
for chunk in response_stream:
    # chunk在my_llm库中已经打印过一遍，这里只需要pass即可
    print(chunk, end="", flush=True)
    # pass