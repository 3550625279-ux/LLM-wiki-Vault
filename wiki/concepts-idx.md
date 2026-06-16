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

### 2. Architecture（架构）
- [[concepts/hyperbolic-geometry-llm]] — LLM 嵌入的双曲层次结构

### 3. Training（训练）
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

### 7. Agents（智能体）
- [[concepts/intent-detection-tods]] — 意图检测：TODS NLU 核心组件
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

### type: source
- [[sources/claude-code-config-and-mcp-flow]] — Claude Code 配置与 MCP 流程笔记 | status:seed | domain:Engineering
- [[sources/hyplora-neurips2025]] — HypLoRA 论文摘要 | status:developing | domain:Training
- [[sources/cagc-cvpr2024]] — CAGC: Contextual Augmented Global Contrast 论文摘要 | status:developing | domain:Multimodal
- [[sources/intent-detection-age-of-llms]] — Intent Detection in the Age of LLMs 论文摘要 | status:developing | domain:Agents
- [[sources/mineru-mcp-debugging-session]] — MinerU MCP 调试会话 | status:developing | domain:Engineering
- [[sources/terminal-and-environment-basics]] — 终端、PATH 与 Conda 环境基础 | status:developing | domain:Common Computer
- [[sources/llm-reasoning-ability]] — LLM是如何获得推理能力的（后训练四层技术栈） | status:developing | domain:Training

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
| 总节点数 | 58 |
| concept | 38 |
| entity | 2 |
| operation | 1 |
| insight | 5 |
| source | 7 |
| comparison | 2 |
| question/gap | 2 |
| mature 节点 | 0 |
| seed 节点 | 52 |
| 矛盾登记 | 0 |

*上次更新: 2026-06-16 | LLM推理能力后训练技术栈 ingest（16张图文，Training+Alignment+Inference三域）*
