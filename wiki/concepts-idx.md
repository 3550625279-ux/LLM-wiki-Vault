# Wiki Index — 全库目录

> 每次 ingest 后更新此文件。
> 格式: `- [[页面标题]] — 一行说明 | type:X | status:Y | domain:Z`

---

## 📁 目录结构

```
log.md                  ← 操作日志（vault 根目录，不入图谱）
wiki/
├── hot.md              ← 热缓存（会话快速恢复）
├── concepts-idx.md     ← 本文件（全库导航）
├── overview.md         ← 全局摘要和知识地图
├── domains/            ← 8个顶层领域综述
│   ├── foundations/
│   ├── architecture/
│   ├── training/
│   ├── alignment/
│   ├── inference/
│   ├── multimodal/
│   ├── agents/
│   └── engineering/
├── concepts/           ← 原理/算法/定义
├── entities/           ← 模型/论文/作者/机构 (entities-idx.md)
├── operations/         ← 代码/调参/工程实践 (operations-idx.md)
├── insights/           ← 个人洞察/避坑 (insights-idx.md)
├── sources/            ← 原始资料摘要页
├── comparisons/        ← 横向对比
├── questions/          ← 已回答问题 + gap页面
├── folds/              ← log折叠归档
├── canvases/           ← 可视化画布
└── meta/               ← 看板/lint/状态/矛盾
```

---

## 🌐 领域索引

### 1. Foundations（基础）
- [[concepts/hyperbolic-geometry]] — 双曲几何基础
- [[concepts/sample-space]] — 样本空间与事件
- [[concepts/random-variable]] — 随机变量
- [[concepts/pushforward-measure]] — 前推测度
- [[concepts/random-vector]] — 随机向量
- [[concepts/covariance]] — 协方差
- [[concepts/moment]] — 矩与高阶统计量
- [[concepts/information-entropy]] — 信息熵（香农熵与自信息）
- [[concepts/cross-entropy-loss]] — 交叉熵与深度学习损失函数
- [[concepts/kl-divergence]] — KL散度（相对熵）
- [[concepts/sgd-noise-generalization]] — SGD噪声与泛化
- [[concepts/point-estimation]] — 点估计：用一个数值估计未知参数
- [[concepts/moment-estimation]] — 矩估计：样本矩估计总体矩
- [[concepts/mle]] — 极大似然估计（MLE）
- [[concepts/maximum-likelihood]] — 极大似然估计（MLE别名） | NEW (lint-fix)
- [[concepts/order-statistics]] — 顺序统计量
- [[concepts/estimator-quality]] — 估计量评价：无偏性、有效性、相合性
- [[concepts/interval-estimation]] — 区间估计与枢轴量
- [[concepts/sample-vector]] — 样本向量：N次实验数据打包成高维空间中的点
- [[concepts/mean-as-projection]] — 均值的几何本质：正交投影
- [[concepts/centering-decoupling]] — 中心化：正交分解与信息解耦
- [[concepts/variance-geometric]] — 方差的几何意义
- [[concepts/degrees-of-freedom]] — 自由度与贝塞尔校正
- [[concepts/central-limit-theorem]] — 中心极限定理（CLT）
- [[concepts/sqrt-n-origin]] — √n的来源：方差可加性
- [[concepts/standard-deviation-l2]] — 标准差与L2范数
- [[concepts/batch-normalization]] — BatchNorm：批量归一化
- [[concepts/layer-normalization]] — LayerNorm：层归一化
- [[concepts/transformer-sqrt-d]] — Transformer的√d缩放
- [[concepts/one-hot-encoding]] — One-Hot 编码 | NEW
- [[concepts/variance]] — 方差 | NEW (lint-fix)
- [[concepts/covariance-matrix]] — 协方差矩阵 | NEW (lint-fix)
- [[concepts/cosine-similarity]] — 余弦相似度 | NEW (lint-fix)
- [[concepts/svd]] — 奇异值分解 (SVD) | NEW (lint-fix)

### 2. Architecture（架构）
- [[concepts/hyperbolic-geometry-llm]] — LLM 嵌入的双曲层次结构
- [[concepts/convolutional-neural-network]] — 卷积神经网络 (CNN) | NEW
- [[concepts/lenet]] — LeNet-5 经典 CNN 架构 | NEW
- [[concepts/pooling-layer]] — 池化层 (AvgPool/MaxPool) | NEW
- [[concepts/recurrent-neural-network]] — 循环神经网络 (RNN) | NEW
- [[concepts/gru]] — 门控循环单元 (GRU) | NEW
- [[concepts/lstm]] — 长短期记忆网络 (LSTM) | NEW
- [[concepts/attention-mechanism]] — 注意力机制 (QKV) | NEW
- [[concepts/additive-attention]] — 加性注意力 (Bahdanau) | NEW
- [[concepts/scaled-dot-product-attention]] — 缩放点积注意力 | NEW
- [[concepts/multi-head-attention]] — 多头注意力 | NEW
- [[concepts/encoder-decoder-architecture]] — 编码器-解码器架构 | NEW
- [[concepts/transformer]] — Transformer 完整架构 | NEW (lint-fix)
- [[concepts/resnet]] — ResNet 残差网络 | NEW (lint-fix)
- [[concepts/vae]] — 变分自编码器 (VAE) | NEW (lint-fix)

### 3. Training（训练）
- [[concepts/backpropagation-through-time]] — 时间反向传播 (BPTT) | NEW
- [[concepts/gradient-clipping]] — 梯度裁剪 | NEW
- [[concepts/llm-training]] — LLM 训练目标 | NEW (lint-fix)
- [[concepts/qlora]] — QLoRA 量化低秩适配 | NEW (lint-fix)
- [[concepts/teacher-forcing]] — Teacher Forcing 训练技巧 | NEW
- [[concepts/perplexity]] — 困惑度 (Perplexity) 评估指标 | NEW
- [[concepts/lora]] — LoRA 低秩适配
- [[concepts/hyplora]] — HypLoRA 双曲低秩适配
- [[concepts/setfit]] — SetFit 对比微调句子转换器少样本学习
- [[concepts/negative-data-augmentation]] — 负面数据增强：关键词替换/删除生成 OOS 样本
- [[concepts/contrastive-learning]] — 对比学习：拉近正样本推远负样本的表示学习范式
- [[concepts/post-training]] — 后训练：从预训练到可用推理模型的四层递进构建
- [[concepts/sft]] — 有监督微调：从续写模式切换到回答模式
- [[concepts/chain-of-thought]] — 推理链(CoT)：展示中间推理步骤，准确率从17%到78%
- [[concepts/process-reward-model]] — 过程奖励模型(PRM)：对推理链每一步单独打分
- [[concepts/grpo]] — 组相对策略优化(GRPO)：绕开奖励模型的RL算法
- [[concepts/data-flywheel]] — 数据飞轮：RL反哺SFT的迭代增强循环
- [[concepts/aha-moment]] — Aha Moment：纯RL训练中推理能力自发涌现

### 4. Alignment（对齐）
- [[concepts/rlhf]] — 基于人类反馈的强化学习(RLHF)：SFT→RM→PPO三阶段对齐
- [[concepts/reward-hacking]] — 奖励Hacking：模型利用奖励信号漏洞的对抗行为

### 5. Inference（推理）
- [[concepts/test-time-compute]] — 推理时计算扩展：Self-Consistency / Best-of-N / MCTS

### 6. Multimodal（多模态）
- [[concepts/multimodal-intent-recognition]] — 多模态意图识别 (MIR) 任务定义与挑战
- [[concepts/cross-video-bank]] — Cross-video Bank 跨视频记忆库（两阶段构建）
- [[concepts/context-augmented-transformer]] — CAT 上下文增强 Transformer（渐进式注意力）
- [[concepts/global-context-guided-contrastive-learning]] — GCCL 全局上下文引导对比学习
- [[concepts/multimodal-fusion]] — 多模态融合 | NEW (lint-fix)
- [[concepts/multimodal-sentiment-analysis]] — 多模态情感分析 | NEW (lint-fix)

### 7. Agents（智能体）
- [[concepts/function-calling]] — Function Calling 函数调用 | NEW (lint-fix)
- [[concepts/intent-detection-tods]] — 意图检测：TODS NLU 核心组件
- [[concepts/function-calling]] — Function Calling 函数调用 | NEW (lint-fix)
- [[concepts/out-of-scope-detection]] — 域外检测：OOS 识别与 LLM 的弱点
- [[concepts/adaptive-in-context-learning]] — 自适应上下文学习：动态检索 ICL 示例

### 8. Engineering（工程）
- [[concepts/mcp-protocol]] — MCP 协议架构与 JSON-RPC 2.0
- [[concepts/claude-code-configuration]] — Claude Code 7 层配置文件体系
- [[concepts/mcp-tool-calling-flow]] — MCP 工具调用 5 阶段全链路
- [[concepts/uncertainty-routing]] — 不确定性路由：混合系统设计模式
- [[concepts/inference-engine]] — 推理引擎：模型文件 vs 执行引擎
- [[concepts/cuda-and-dll]] — CUDA 与 DLL：GPU 计算基础设施

### 9. Common Computer（通用计算机基础）
- [[concepts/terminal-and-shell]] — 终端与 Shell 基础
- [[concepts/npm-and-npx]] — npm 与 npx：JavaScript 包管理
- [[concepts/path-environment-variable]] — PATH 环境变量机制
- [[concepts/process-environment-inheritance]] — 进程环境变量继承链
- [[concepts/windows-registry-env]] — Windows 注册表与环境变量存储
- [[concepts/conda-environments]] — Conda 环境管理与激活机制

---

## 🏷️ 节点类型索引

### type: concept
- [[concepts/mcp-protocol]] — MCP 协议架构与 JSON-RPC 2.0 | status:seed | domain:Engineering
- [[concepts/claude-code-configuration]] — Claude Code 7层配置文件体系 | status:seed | domain:Engineering
- [[concepts/mcp-tool-calling-flow]] — MCP 工具调用 5 阶段全链路 | status:seed | domain:Engineering
- [[concepts/uncertainty-routing]] — 不确定性路由：混合系统设计模式 | status:seed | domain:Engineering
- [[concepts/hyperbolic-geometry]] — 双曲几何基础（Lorentz/Poincaré模型） | status:seed | domain:Foundations
- [[concepts/monte-carlo-dropout]] — MC Dropout 贝叶斯不确定性估计 | status:seed | domain:Foundations
- [[concepts/sample-space]] — 样本空间与事件 | status:seed | domain:Foundations
- [[concepts/random-variable]] — 随机变量 | status:seed | domain:Foundations
- [[concepts/pushforward-measure]] — 前推测度 | status:seed | domain:Foundations
- [[concepts/random-vector]] — 随机向量 | status:seed | domain:Foundations
- [[concepts/covariance]] — 协方差 | status:seed | domain:Foundations
- [[concepts/moment]] — 矩与高阶统计量 | status:seed | domain:Foundations
- [[concepts/point-estimation]] — 点估计 | status:seed | domain:Foundations
- [[concepts/moment-estimation]] — 矩估计 | status:seed | domain:Foundations
- [[concepts/mle]] — 极大似然估计（MLE） | status:seed | domain:Foundations
- [[concepts/order-statistics]] — 顺序统计量 | status:seed | domain:Foundations
- [[concepts/estimator-quality]] — 估计量评价：无偏性、有效性、相合性 | status:seed | domain:Foundations
- [[concepts/interval-estimation]] — 区间估计与枢轴量 | status:seed | domain:Foundations
- [[concepts/hyperbolic-geometry-llm]] — LLM 嵌入的双曲层次结构 | status:seed | domain:Architecture
- [[concepts/lora]] — LoRA 低秩适配 | status:seed | domain:Training
- [[concepts/hyplora]] — HypLoRA 双曲低秩适配 | status:seed | domain:Training
- [[concepts/setfit]] — SetFit 对比微调句子转换器 | status:seed | domain:Training
- [[concepts/negative-data-augmentation]] — 负面数据增强 | status:seed | domain:Training
- [[concepts/contrastive-learning]] — 对比学习表示学习范式 | status:seed | domain:Training
- [[concepts/multimodal-intent-recognition]] — 多模态意图识别 (MIR) | status:seed | domain:Multimodal
- [[concepts/cross-video-bank]] — Cross-video Bank 跨视频记忆库 | status:seed | domain:Multimodal
- [[concepts/context-augmented-transformer]] — CAT 上下文增强 Transformer | status:seed | domain:Multimodal
- [[concepts/global-context-guided-contrastive-learning]] — GCCL 全局上下文引导对比学习 | status:seed | domain:Multimodal
- [[concepts/intent-detection-tods]] — 意图检测 TODS NLU 核心组件 | status:seed | domain:Agents
- [[concepts/out-of-scope-detection]] — 域外检测 OOS 识别 | status:seed | domain:Agents
- [[concepts/adaptive-in-context-learning]] — 自适应上下文学习 | status:seed | domain:Agents
- [[concepts/inference-engine]] — 推理引擎：AI 模型的执行引擎 | status:seed | domain:Engineering
- [[concepts/cuda-and-dll]] — CUDA 与 DLL：GPU 计算基础设施 | status:seed | domain:Engineering
- [[concepts/terminal-and-shell]] — 终端与 Shell 基础 | status:seed | domain:Common Computer
- [[concepts/npm-and-npx]] — npm 与 npx：JavaScript 包管理 | status:seed | domain:Common Computer
- [[concepts/path-environment-variable]] — PATH 环境变量 | status:seed | domain:Common Computer
- [[concepts/process-environment-inheritance]] — 进程环境变量继承链 | status:seed | domain:Common Computer
- [[concepts/windows-registry-env]] — Windows 注册表与环境变量存储 | status:seed | domain:Common Computer
- [[concepts/conda-environments]] — Conda 环境管理与激活机制 | status:seed | domain:Common Computer
- [[concepts/post-training]] — 后训练四层递进架构 | status:seed | domain:Training
- [[concepts/sft]] — 有监督微调：从续写到回答 | status:seed | domain:Training
- [[concepts/chain-of-thought]] — 推理链CoT | status:seed | domain:Training
- [[concepts/process-reward-model]] — 过程奖励模型PRM | status:seed | domain:Training
- [[concepts/grpo]] — 组相对策略优化GRPO | status:seed | domain:Training
- [[concepts/reward-hacking]] — 奖励Hacking | status:seed | domain:Alignment
- [[concepts/test-time-compute]] — 推理时计算扩展 | status:seed | domain:Inference
- [[concepts/data-flywheel]] — 数据飞轮 | status:seed | domain:Training
- [[concepts/aha-moment]] — Aha Moment推理涌现 | status:seed | domain:Training
- [[concepts/rlhf]] — 基于人类反馈的强化学习 | status:seed | domain:Alignment
- [[concepts/information-entropy]] — 信息熵（香农熵与自信息） | status:seed | domain:Foundations
- [[concepts/cross-entropy-loss]] — 交叉熵与深度学习损失函数 | status:seed | domain:Foundations
- [[concepts/kl-divergence]] — KL散度（相对熵） | status:seed | domain:Foundations
- [[concepts/sgd-noise-generalization]] — SGD噪声与泛化 | status:seed | domain:Foundations
- [[concepts/sample-vector]] — 样本向量：N次实验数据打包成高维空间中的点 | status:seed | domain:Foundations
- [[concepts/mean-as-projection]] — 均值的几何本质：正交投影 | status:seed | domain:Foundations
- [[concepts/centering-decoupling]] — 中心化：正交分解与信息解耦 | status:seed | domain:Foundations
- [[concepts/variance-geometric]] — 方差的几何意义 | status:seed | domain:Foundations
- [[concepts/degrees-of-freedom]] — 自由度与贝塞尔校正 | status:seed | domain:Foundations
- [[concepts/central-limit-theorem]] — 中心极限定理（CLT） | status:seed | domain:Foundations
- [[concepts/sqrt-n-origin]] — √n的来源：方差可加性 | status:seed | domain:Foundations
- [[concepts/standard-deviation-l2]] — 标准差与L2范数 | status:seed | domain:Foundations
- [[concepts/batch-normalization]] — BatchNorm：批量归一化 | status:seed | domain:Foundations
- [[concepts/layer-normalization]] — LayerNorm：层归一化 | status:seed | domain:Foundations
- [[concepts/transformer-sqrt-d]] — Transformer的√d缩放 | status:seed | domain:Foundations
- [[concepts/one-hot-encoding]] — One-Hot 编码 | status:seed | domain:Foundations
- [[concepts/convolutional-neural-network]] — 卷积神经网络 (CNN) | status:seed | domain:Architecture
- [[concepts/lenet]] — LeNet-5 经典CNN架构 | status:seed | domain:Architecture
- [[concepts/pooling-layer]] — 池化层 | status:seed | domain:Architecture
- [[concepts/recurrent-neural-network]] — 循环神经网络 (RNN) | status:seed | domain:Architecture
- [[concepts/gru]] — 门控循环单元 (GRU) | status:seed | domain:Architecture
- [[concepts/lstm]] — 长短期记忆网络 (LSTM) | status:seed | domain:Architecture
- [[concepts/attention-mechanism]] — 注意力机制 (QKV) | status:seed | domain:Architecture
- [[concepts/additive-attention]] — 加性注意力 | status:seed | domain:Architecture
- [[concepts/scaled-dot-product-attention]] — 缩放点积注意力 | status:seed | domain:Architecture
- [[concepts/multi-head-attention]] — 多头注意力 | status:seed | domain:Architecture
- [[concepts/encoder-decoder-architecture]] — 编码器-解码器架构 | status:seed | domain:Architecture
- [[concepts/backpropagation-through-time]] — 时间反向传播 (BPTT) | status:seed | domain:Training
- [[concepts/gradient-clipping]] — 梯度裁剪 | status:seed | domain:Training
- [[concepts/teacher-forcing]] — Teacher Forcing | status:seed | domain:Training
- [[concepts/perplexity]] — 困惑度 | status:seed | domain:Training

### type: entity
- [[sources/hyplora-neurips2025]] — HypLoRA 论文 (NeurIPS 2025) | status:developing | domain:Training
- [[entities/deepseek-r1]] — DeepSeek-R1 推理模型 | status:seed | domain:Training
- [[entities/deepseek-r1-zero]] — DeepSeek-R1-Zero 纯RL推理涌现 | status:seed | domain:Training

### type: operation
- [[operations/sft-cot-data-pipeline]] — CoT SFT数据四条生产线 | status:seed | domain:Training

### type: insight
- [[insights/llm-embedding-geometry]] — LLM 嵌入空间具有内在双曲结构 | status:seed | domain:Architecture
- [[insights/hybrid-beats-pure-llm]] — 混合系统胜过纯 LLM | status:seed | domain:Engineering
- [[insights/when-import-succeeds-but-runtime-fails]] — import 成功 ≠ 能运行 | status:seed | domain:Engineering
- [[insights/path-search-priority-is-isolation]] — PATH 从前往后搜索 = 环境隔离的核心手段 | status:seed | domain:Common Computer
- [[insights/rnn-hyperparameter-analysis]] — RNN 调参四要素分析 | status:seed | domain:Training

### type: source
- [[sources/claude-code-config-and-mcp-flow]] — Claude Code 配置与 MCP 流程笔记 | status:seed | domain:Engineering
- [[sources/hyplora-neurips2025]] — HypLoRA 论文摘要 | status:developing | domain:Training
- [[sources/cagc-cvpr2024]] — CAGC: Contextual Augmented Global Contrast 论文摘要 | status:developing | domain:Multimodal
- [[sources/intent-detection-age-of-llms]] — Intent Detection in the Age of LLMs 论文摘要 | status:developing | domain:Agents
- [[sources/mineru-mcp-debugging-session]] — MinerU MCP 调试会话 | status:developing | domain:Engineering
- [[sources/terminal-and-environment-basics]] — 终端、PATH 与 Conda 环境基础 | status:developing | domain:Common Computer
- [[sources/llm-reasoning-ability]] — LLM是如何获得推理能力的（后训练四层技术栈） | status:developing | domain:Training
- [[sources/parameter-estimation-notes]] — 参数估计学习笔记 | status:seed | domain:Foundations
- [[sources/random-variable-random-vector]] — 随机变量与随机向量 | status:developing | domain:Foundations
- [[sources/sample-vector-geometric]] — 样本向量的几何视角 | status:developing | domain:Foundations
- [[sources/central-limit-theorem]] — 中心极限定理与归一化 | status:developing | domain:Foundations
- [[sources/information-theory-loss]] — 信息论与深度学习损失函数 | status:developing | domain:Foundations
- [[sources/pytorch-cnn-lenet-mnist]] — CNN/LeNet-5 手写数字识别全流程 | status:developing | domain:Architecture
- [[sources/transformer-attention-seq2seq]] — 注意力机制与Seq2Seq模型 | status:developing | domain:Architecture
- [[sources/pytorch-rnn-gru-lstm]] — RNN/GRU/LSTM从零实现与对比 | status:developing | domain:Architecture

### type: comparison
- [[comparisons/cagc-vs-baselines]] — CAGC vs MAG-BERT/MulT/MISA/ConFEDE 对比 | status:seed | domain:Multimodal
- [[comparisons/orm-vs-prm]] — ORM+PPO vs PRM+PPO 结果奖励与过程奖励对比 | status:seed | domain:Training

### type: question / gap
- [[questions/hyplora-thought-experiments]] — HypLoRA 思想实验与开放问题 | status:seed | domain:Training
- [[questions/hyplora-research-directions]] — HypLoRA 未来研究方向 | status:seed | domain:Training

---

## 📊 统计

| 指标 | 数值 |
|------|------|
| 总节点数 | 112 |
| concept | 81 |
| entity | 2 |
| operation | 1 |
| insight | 6 |
| source | 15 |
| comparison | 2 |
| question/gap | 2 |
| mature 节点 | 0 |
| seed 节点 | 106 |
| 矛盾登记 | 0 |

*上次更新: 2026-06-16 | lint修复：补充13个缺失概念页 + 2处死链重定向*
