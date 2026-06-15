# AI Agent 核心词汇表

| 英文 | 音标 | 词性 | 中文 | 含义 |
|------|------|------|------|------|
| Perception | /pəˈsepʃən/ | n. | 感知 | 智能体通过传感器获取环境信息的能力，是智能体与外部世界交互的第一步 |
| Sensors | /ˈsensərz/ | n. | 传感器 | 智能体用于感知外部环境的输入设备或接口，如摄像头、麦克风、API数据流等 |
| Actuators | /ˈæktʃuˌeɪtərz/ | n. | 执行器 | 智能体用于对环境施加影响的输出设备或接口，如机械臂、扬声器、API调用等 |
| Autonomy | /ɔːˈtɒnəmi/ | n. | 自主性 | 智能体无需人工干预、独立做出决策并采取行动的能力 |
| Application Programming Interface (API) | /ˌæplɪˈkeɪʃən ˈproʊɡræmɪŋ ˈɪntərfeɪs/ | n. | 应用程序编程接口 | 允许不同软件系统之间相互通信和数据交换的标准化接口规范 |
| Large Language Model (LLM) | /lɑːrdʒ ˈlæŋɡwɪdʒ ˈmɒdəl/ | n. | 大语言模型 | 基于海量文本数据训练的大规模神经网络模型，能够理解和生成自然语言，如 GPT、DeepSeek 等 |
| Simple Reflex Agent | /ˈsɪmpəl ˈriːfleks ˈeɪdʒənt/ | n. | 反射智能体 | 最简单的智能体类型，仅根据当前感知直接映射到动作，不考虑历史状态，类似条件反射 |
| Model-Based Reflex Agent | /ˈmɒdəl beɪst ˈriːfleks ˈeɪdʒənt/ | n. | 基于模型的反射智能体 | 维护一个内部世界模型来跟踪不可观测的环境状态，在此基础上做出决策的智能体 |
| Goal-Based Agent | /ɡoʊl beɪst ˈeɪdʒənt/ | n. | 基于目标的智能体 | 具有明确目标，通过搜索和规划选择能够达成目标的行动序列的智能体 |
| Utility-Based Agent | /juːˈtɪlɪti beɪst ˈeɪdʒənt/ | n. | 基于效用的智能体 | 使用效用函数衡量不同状态的"满意程度"，选择期望效用最大的行动的智能体 |
| Learning Agent | /ˈlɜːrnɪŋ ˈeɪdʒənt/ | n. | 学习型智能体 | 能够从经验中学习并不断改善自身行为的智能体，包含学习元素、评判元素、执行元素和问题生成器 |
| Reinforcement Learning (RL) | /ˌriːɪnˈfɔːrsmənt ˈlɜːrnɪŋ/ | n. | 强化学习 | 智能体通过与环境交互、获得奖励或惩罚信号来学习最优策略的机器学习方法 |
| Generative Pre-trained Transformer (GPT) | /ˈdʒenərətɪv priː treɪnd trænsˈfɔːrmər/ | n. | 生成式预训练 Transformer | OpenAI 开发的基于 Transformer 架构的大语言模型系列，通过无监督预训练再微调的方式构建 |
| Reactivity | /ˌriːækˈtɪvɪti/ | n. | 反应性 | 智能体能够及时感知环境变化并做出响应的能力，是智能体的基本特性之一 |
| Deliberation | /dɪˌlɪbəˈreɪʃən/ | n. | 规划性 | 智能体在行动前进行推理、规划和目标导向思考的能力，与反应性相对 |
| Stochastic Parrot | /stəˈkæstɪk ˈpærət/ | n. | "随机鹦鹉" | 对大语言模型的批判性比喻，认为 LLM 只是在统计意义上拼接文本，并不真正"理解"语言含义 |
| Agent Loop | /ˈeɪdʒənt luːp/ | n. | 智能体循环 | 智能体持续运行的感知→思考→行动→观察的循环流程，是 ReAct 等 Agent 框架的核心机制 |
| Prompt Engineering | /prɒmpt ˌendʒɪˈnɪərɪŋ/ | n. | 提示工程 | 通过精心设计输入提示词来引导大语言模型生成期望输出的技术和方法论 |
| Assertions | /əˈsɜːrʃənz/ | n. | 断言 | 程序中用于验证某个条件必须为真的语句，若条件为假则抛出错误，常用于调试和测试 |
| Knowledge Base | /ˈnɒlɪdʒ beɪs/ | n. | 知识库 | 存储结构化知识（事实、规则、概念）的数据库，是专家系统和知识图谱的核心组成部分 |
| Production Rules | /prəˈdʌkʃən ruːlz/ | n. | 产生式规则 | 以"IF 条件 THEN 动作"形式表示的知识规则，是专家系统中最常用的知识表示方式 |
| Inference Engine | /ˈɪnfərəns ˈendʒɪn/ | n. | 推理机 | 专家系统的核心组件，负责根据知识库中的规则和事实进行逻辑推理以得出结论 |
| Forward Chaining | /ˈfɔːrwərd ˈtʃeɪnɪŋ/ | n. | 正向链 | 从已知事实出发，不断触发匹配的规则，推导出新事实，直到达到目标的推理方式（数据驱动） |
| Backward Chaining | /ˈbækwərd ˈtʃeɪnɪŋ/ | n. | 反向链 | 从目标出发，逆向寻找能够证明目标成立的规则和事实的推理方式（目标驱动） |
| Pattern Matching & Text Substitution | /ˈpætərn ˈmætʃɪŋ ænd tekst ˌsʌbstɪˈtjuːʃən/ | n. | 模式匹配与文本替换 | 通过识别文本中的特定模式并将其替换为预定义响应的技术，是早期对话系统（如 ELIZA）的核心机制 |
| Emergence | /ɪˈmɜːrdʒəns/ | n. | 涌现 | 系统在整体层面出现的、无法从单个组成部分预测的新性质或行为，LLM 的推理能力被认为是一种涌现现象 |
