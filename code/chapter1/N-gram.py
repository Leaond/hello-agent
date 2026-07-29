'''
Date: 2026-06-25 11:11:12
LastEditors: liuzhengliang
LastEditTime: 2026-07-29 11:38:32
Description: 模拟N-gram模型，N=2
'''
import collections

# 示例语料库
corpus = "datawhale agent learns datawhale agent works"
tokens = corpus.split()
total_tokens = len(tokens)

print(tokens,total_tokens)

# 1. 计算 P(datawhale)
count_datawhale = tokens.count("datawhale")
p_datawhale = count_datawhale/total_tokens

# 2. 计算P(agent|datawhale)
# 先计算bigrams用于后续步骤
bigrams = zip(tokens,tokens[1:])
bigrams_counts = collections.Counter(bigrams)
# Counter({
# ('datawhale', 'agent'): 2,
# ('agent', 'learns'): 1, 
# ('learns', 'datawhale'): 1, 
# ('agent', 'works'): 1
# })
count_agent_datawhale = bigrams_counts[('datawhale','agent')]
p_agent_datawhale = count_agent_datawhale / count_datawhale
print(p_agent_datawhale)

# 3. 计算P(learns|agent)
count_agent = tokens.count("agent")
count_learns_agents = bigrams_counts[('agent','learns')]
p_learns_agents = count_learns_agents/count_agent
print(p_learns_agents)

#4. 计算句子‘datawhale agent learns’的概率
p_sentence = p_datawhale *p_agent_datawhale *p_learns_agents
print(p_sentence)