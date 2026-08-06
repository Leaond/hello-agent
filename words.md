<!--
 * @Date: 2026-06-15 17:42:09
 * @LastEditors: liuzhengliang
 * @LastEditTime: 2026-08-06 08:47:55
 * @Description: 快速预览md文档：Ctrl + Shift + V → 新标签页打开预览、Ctrl + K, V → 侧边栏并排预览
-->

# AI Agent 核心词汇表

| 序号 | 英文                                      | 音标                                        | 词性 | 中文                     | 含义                                                                                                 |
| ---- | ----------------------------------------- | ------------------------------------------- | ---- | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| 1    | Perception                                | /pəˈsepʃən/                                 | n.   | 感知                     | 智能体通过传感器获取环境信息的能力，是智能体与外部世界交互的第一步                                   |
| 2    | Sensors                                   | /ˈsensərz/                                  | n.   | 传感器                   | 智能体用于感知外部环境的输入设备或接口，如摄像头、麦克风、API数据流等                                |
| 3    | Actuators                                 | /ˈæktʃuˌeɪtərz/                             | n.   | 执行器                   | 智能体用于对环境施加影响的输出设备或接口，如机械臂、扬声器、API调用等                                |
| 4    | Autonomy                                  | /ɔːˈtɒnəmi/                                 | n.   | 自主性                   | 智能体无需人工干预、独立做出决策并采取行动的能力                                                     |
| 5    | Application Programming Interface (API)   | /ˌæplɪˈkeɪʃən ˈproʊɡræmɪŋ ˈɪntərfeɪs/       | n.   | 应用程序编程接口         | 允许不同软件系统之间相互通信和数据交换的标准化接口规范                                               |
| 6    | Large Language Model (LLM)                | /lɑːrdʒ ˈlæŋɡwɪdʒ ˈmɒdəl/                   | n.   | 大语言模型               | 基于海量文本数据训练的大规模神经网络模型，能够理解和生成自然语言，如 GPT、DeepSeek 等                |
| 7    | Simple Reflex Agent                       | /ˈsɪmpəl ˈriːfleks ˈeɪdʒənt/                | n.   | 反射智能体               | 最简单的智能体类型，仅根据当前感知直接映射到动作，不考虑历史状态，类似条件反射                       |
| 8    | Model-Based Reflex Agent                  | /ˈmɒdəl beɪst ˈriːfleks ˈeɪdʒənt/           | n.   | 基于模型的反射智能体     | 维护一个内部世界模型来跟踪不可观测的环境状态，在此基础上做出决策的智能体                             |
| 9    | Goal-Based Agent                          | /ɡoʊl beɪst ˈeɪdʒənt/                       | n.   | 基于目标的智能体         | 具有明确目标，通过搜索和规划选择能够达成目标的行动序列的智能体                                       |
| 10   | Utility-Based Agent                       | /juːˈtɪlɪti beɪst ˈeɪdʒənt/                 | n.   | 基于效用的智能体         | 使用效用函数衡量不同状态的"满意程度"，选择期望效用最大的行动的智能体                                 |
| 11   | Learning Agent                            | /ˈlɜːrnɪŋ ˈeɪdʒənt/                         | n.   | 学习型智能体             | 能够从经验中学习并不断改善自身行为的智能体，包含学习元素、评判元素、执行元素和问题生成器             |
| 12   | Reinforcement Learning (RL)               | /ˌriːɪnˈfɔːrsmənt ˈlɜːrnɪŋ/                 | n.   | 强化学习                 | 智能体通过与环境交互、获得奖励或惩罚信号来学习最优策略的机器学习方法                                 |
| 13   | Generative Pre-trained Transformer (GPT)  | /ˈdʒenərətɪv priː treɪnd trænsˈfɔːrmər/     | n.   | 生成式预训练 Transformer | OpenAI 开发的基于 Transformer 架构的大语言模型系列，通过无监督预训练再微调的方式构建                 |
| 14   | Reactivity                                | /ˌriːækˈtɪvɪti/                             | n.   | 反应性                   | 智能体能够及时感知环境变化并做出响应的能力，是智能体的基本特性之一                                   |
| 15   | Deliberation                              | /dɪˌlɪbəˈreɪʃən/                            | n.   | 规划性                   | 智能体在行动前进行推理、规划和目标导向思考的能力，与反应性相对                                       |
| 16   | Stochastic Parrot                         | /stəˈkæstɪk ˈpærət/                         | n.   | "随机鹦鹉"               | 对大语言模型的批判性比喻，认为 LLM 只是在统计意义上拼接文本，并不真正"理解"语言含义                  |
| 17   | Agent Loop                                | /ˈeɪdʒənt luːp/                             | n.   | 智能体循环               | 智能体持续运行的感知→思考→行动→观察的循环流程，是 ReAct 等 Agent 框架的核心机制                      |
| 18   | Prompt Engineering                        | /prɒmpt ˌendʒɪˈnɪərɪŋ/                      | n.   | 提示工程                 | 通过精心设计输入提示词来引导大语言模型生成期望输出的技术和方法论                                     |
| 19   | Assertions                                | /əˈsɜːrʃənz/                                | n.   | 断言                     | 程序中用于验证某个条件必须为真的语句，若条件为假则抛出错误，常用于调试和测试                         |
| 20   | Knowledge Base                            | /ˈnɒlɪdʒ beɪs/                              | n.   | 知识库                   | 存储结构化知识（事实、规则、概念）的数据库，是专家系统和知识图谱的核心组成部分                       |
| 21   | Production Rules                          | /prəˈdʌkʃən ruːlz/                          | n.   | 产生式规则               | 以"IF 条件 THEN 动作"形式表示的知识规则，是专家系统中最常用的知识表示方式                            |
| 22   | Inference Engine                          | /ˈɪnfərəns ˈendʒɪn/                         | n.   | 推理机                   | 专家系统的核心组件，负责根据知识库中的规则和事实进行逻辑推理以得出结论                               |
| 23   | Forward Chaining                          | /ˈfɔːrwərd ˈtʃeɪnɪŋ/                        | n.   | 正向链                   | 从已知事实出发，不断触发匹配的规则，推导出新事实，直到达到目标的推理方式（数据驱动）                 |
| 24   | Backward Chaining                         | /ˈbækwərd ˈtʃeɪnɪŋ/                         | n.   | 反向链                   | 从目标出发，逆向寻找能够证明目标成立的规则和事实的推理方式（目标驱动）                               |
| 25   | Pattern Matching & Text Substitution      | /ˈpætərn ˈmætʃɪŋ ænd tekst ˌsʌbstɪˈtjuːʃən/ | n.   | 模式匹配与文本替换       | 通过识别文本中的特定模式并将其替换为预定义响应的技术，是早期对话系统（如 ELIZA）的核心机制           |
| 26   | Emergence                                 | /ɪˈmɜːrdʒəns/                               | n.   | 涌现                     | 系统在整体层面出现的、无法从单个组成部分预测的新性质或行为，LLM 的推理能力被认为是一种涌现现象       |
| 27   | Distributed Artificial Intelligence (DAI) | /dɪˈstrɪbjuːtɪd ˌɑːrtɪfɪʃəl ɪnˈtelɪdʒəns/   | n.   | 分布式人工智能           | 将人工智能系统分布在多个计算节点上协同工作的技术范式，强调并行处理和分布式问题求解                   |
| 28   | Multi-Agent System (MAS)                  | /ˈmʌlti ˈeɪdʒənt ˈsɪstəm/                   | n.   | 多智能体系统             | 由多个智能体组成的系统，各智能体可自主决策并通过交互协作或竞争来完成个体或全局目标                   |
| 29   | Decentralized Control                     | /diːˈsentrəlaɪzd kənˈtroʊl/                 | n.   | 去中心化控制             | 控制权分散在多个节点而非集中于单一中心的控制方式，每个节点可独立做出局部决策                         |
| 30   | Emergent Computation                      | /ɪˈmɜːrdʒənt ˌkɒmpjuˈteɪʃən/                | n.   | 涌现式计算               | 通过简单组件的局部交互产生复杂全局行为的计算范式，整体行为无法从单个组件的行为预测                   |
| 31   | Agent Sociality                           | /ˈeɪdʒənt ˌsoʊʃiˈælɪti/                     | n.   | 智能体的社会性           | 智能体在多智能体环境中表现出的社交能力，包括协作、协调、协商和社会规范遵从等行为                     |
| 32   | Codebase Cognitive Debt                   | /ˈkoʊdbeɪs ˈkɒɡnɪtɪv det/                   | n.   | 代码库认知债务           | 由于代码库复杂度增长导致开发者理解和维护代码所需认知负担持续累积的隐性技术负债                       |
| 33   | Connectionism                             | /kəˈnekʃənɪzəm/                             | n.   | 联结主义                 | 认知科学和人工智能的理论流派，认为智能源于简单处理单元之间的连接和交互，是神经网络的理论基础         |
| 34   | Cumulative Reward                         | /ˈkjuːmjəleɪtɪv rɪˈwɔːrd/                   | n.   | 累积奖励                 | 强化学习中智能体在一段时间内获得的所有奖励信号的总和，是策略优化的目标函数                           |
| 35   | Natural Language Processing (NLP)         | /ˈnætʃərəl ˈlæŋɡwɪdʒ ˈproʊsesɪŋ/            | n.   | 自然语言处理             | 让计算机理解、解释和生成人类自然语言的交叉学科，融合了计算机科学、语言学和机器学习                   |
| 36   | Pre-training                              | /priː ˈtreɪnɪŋ/                             | n.   | 预训练                   | 在大规模数据集上进行初步模型训练的过程，使模型学习通用的特征和知识表示，为后续微调奠定基础           |
| 37   | Fine-tuning                               | /faɪn ˈtjuːnɪŋ/                             | n.   | 微调                     | 在预训练模型的基础上，使用特定任务的标注数据进行进一步训练，使模型适应特定应用场景                   |
| 38   | Self-supervised Learning                  | /self ˈsjuːpərvaɪzd ˈlɜːrnɪŋ/               | n.   | 自监督学习               | 从无标注数据中自动构造监督信号进行训练的方法，如语言模型通过预测被遮蔽的词来学习                     |
| 39   | Emergent Abilities                        | /ɪˈmɜːrdʒənt əˈbɪlɪtiz/                     | n.   | 涌现能力                 | 大语言模型在规模增大到某个阈值后突然出现的新能力，如少样本学习、推理等，无法仅从小模型行为预测       |
| 40   | In-context Learning                       | /ɪn ˈkɒntekst ˈlɜːrnɪŋ/                     | n.   | 上下文学习               | 大语言模型无需更新参数，仅通过提示词中的示例和指令来适应新任务的能力，又称提示学习                   |
| 41   | Chain-of-Thought (CoT)                    | /tʃeɪn əv θɔːt/                             | n.   | 思维链                   | 一种提示技术，引导大语言模型将复杂推理分解为中间步骤逐步推导，显著提升逻辑推理能力                   |
| 42   | Reflection                                | /rɪˈflekʃən/                                | n.   | 反思                     | 智能体对自身输出或决策进行审视和评估的过程，用于发现错误并改进后续行为                               |
| 43   | Self-criticism                            | /self ˈkrɪtɪsɪzəm/                          | n.   | 自我批判                 | 智能体主动审查和质疑自身推理过程或输出结果的能力，是提升输出质量和可靠性的重要机制                   |
| 44   | Recurrent Neural Network (RNN)            | /rɪˈkʌrənt ˈnjʊərəl ˈnetwɜːrk/              | n.   | 循环神经网络             | 一种具有循环连接、能够处理序列数据的神经网络，通过隐藏状态传递历史信息，常用于自然语言和时间序列建模 |
| 45   | Verification                              | /ˌverɪfɪˈkeɪʃən/                            | n.   | 验证                     | 对模型输出、代码或系统行为是否符合预期规范进行检查确认的过程，是保障可靠性的重要手段                 |
| 46   | Conventions                               | /kənˈvenʃənz/                               | n.   | 约定惯例                 | 开发或实践中约定成俗的命名、风格和结构规范，遵循约定可提升代码可读性与团队协作效率                   |
| 47   | Convolutional Layer                       | /ˌkɒnvəˈluːʃənl ˈleɪər/                     | n.   | 卷积层                   | 卷积神经网络的核心组件，通过卷积核在输入上滑动提取局部特征，具备参数共享和平移不变性                 |
| 48   | Activation Function                       | /ˌæktɪˈveɪʃən ˈfʌŋkʃən/                     | n.   | 激活函数                 | 神经网络中对神经元输出施加非线性变换的函数，如 ReLU、Sigmoid，使网络能够拟合复杂的非线性关系         |
| 49   | Pooling Layer                             | /ˈpuːlɪŋ ˈleɪər/                            | n.   | 池化层                   | 卷积神经网络中用于降低特征图空间尺寸的层，如最大池化、平均池化，有助于减少参数量并提升平移鲁棒性     |
| 50   | Gradient                                  | /ˈɡreɪdiənt/                                | n.   | 梯度                     | 多元函数各变量偏导数组成的向量，指向函数上升最快的方向，是神经网络反向传播优化的基础                 |
| 51   | Chat Completions API                      | /tʃæt kəmˈpliːʃənz eɪ piː aɪ/               | n.   | 对话补全 API             | OpenAI 等提供商提供的多轮对话接口规范，接收消息列表并返回模型生成的回复，是构建 Agent 应用的基础 API |
| 52   | Self-Attention                            | /self əˈtenʃən/                             | n.   | 自注意力                 | Transformer 的核心机制，允许序列中每个位置关注其他所有位置并计算加权表示，有效捕获长距离依赖         |
| 53   | Normalization                             | /ˌnɔːrməlaɪˈzeɪʃən/                         | n.   | 归一化                   | 将数据或中间激活值缩放到统一尺度的处理过程，可加速神经网络训练并提升数值稳定性                       |
| 54   | Dimension                                 | /dɪˈmenʃən/                                 | n.   | 维度                     | 向量、矩阵或张量中轴的数量或长度，反映数据的展开方式，如词向量维度、隐藏层维度等                     |
| 55   | Numerical                                 | /njuːˈmerɪkəl/                              | adj. | 数值的                   | 与数字相关的，常用于描述数值计算、数值稳定性、数值方法等计算机与数学中的数量化特征                   |
| 56   | Standard Normal Distribution              | /ˈstændərd ˈnɔːrməl ˌdɪstrɪˈbjuːʃən/        | n.   | 标准正态分布             | 均值为 0、方差为 1 的正态分布，是概率论和统计学中的基础分布，常用于神经网络参数初始化                |
| 57   | Layer Normalization                       | /ˈleɪər ˌnɔːrməlaɪˈzeɪʃən/                  | n.   | 层归一化                 | 对单个样本在特征维度上进行归一化的技术，广泛应用于 Transformer，不依赖批量大小且对序列任务友好       |
| 58   | Neural Networks                           | /ˈnjʊərəl ˈnetwɜːrks/                       | n.   | 神经网络                 | 模仿生物神经系统结构的计算模型，由多层互相连接的神经元组成，是现代深度学习的基础架构                 |
| 59   | Dot Product                               | /dɒt ˈprɒdʌkt/                              | n.   | 点积                     | 两个向量对应元素相乘后求和的运算，反映向量相似度，是注意力机制中计算相关得分的基本运算               |
| 60   | Tokenization                              | /ˌtoʊkənaɪˈzeɪʃən/                          | n.   | 分词                     | 将文本切分为模型可处理的最小单元（token）的过程，是大语言模型输入处理的第一步                        |
| 61   | Feedforward Neural Network (FFN)          | /ˈfiːdfɔːrwərd ˈnjʊərəl ˈnetwɜːrk/          | n.   | 前馈神经网络             | 信息仅从输入层单向传向输出层、无循环连接的神经网络，是 Transformer 中对位置独立处理的子模块          |
| 62   | Weights                                   | /weɪts/                                     | n.   | 权重                     | 神经网络中连接神经元的可学习参数，控制输入信号的传递强度，通过反向传播不断更新以拟合数据             |
| 63   | Biases                                    | /ˈbaɪəsɪz/                                  | n.   | 偏置                     | 神经元中与权重并存的可学习常数项，平移激活函数的输入，提升模型拟合能力和表达能力                     |
| 64   | Standard Operating Procedure (SOP)        | /ˈstændərd ˈɒpəreɪtɪŋ prəˈsiːdʒər/          | n.   | 标准作业程序             | 为保证操作一致性和可复现性而制定的标准化流程文档，规定完成特定任务的详细步骤和规范                   |

前馈神经网络语言模型 (Feedforward Neural Network Language Model)
负采样（Negative Sampling）
分层 Softmax（Hierarchical Softmax）
投影层（Projection Layer）
门控机制 (Gating Mechanism)
长短时记忆网络 (Long Short-Term Memory, LSTM)
缩放点积注意力（Scaled Dot-Product Attention）。
自回归 (Autoregressive)
掩码自注意力 (Masked Self-Attention)
零样本提示 (Zero-shot Prompting)
单样本提示 (One-shot Prompting)
少样本提示 (Few-shot Prompting)
指令调优 (Instruction Tuning)
思维链 (Chain-of-Thought, CoT)
分词 (Tokenization)
分词器 (Tokenizer)
词元 (Token)
“未登录词” (Out-Of-Vocabulary, OOV)
子词分词 (Subword Tokenization)
字节对编码 (Byte-Pair Encoding, BPE)
核采样Top‑p （Nucleus Sampling）
probability（概率）
模型蒸馏（Model Distillation）
有机结果（Organic Results）
