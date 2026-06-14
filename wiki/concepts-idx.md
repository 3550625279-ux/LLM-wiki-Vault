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

### 4. Alignment（对齐）
*(待 ingest 填充)*

### 5. Inference（推理）
*(待 ingest 填充)*

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

### type: entity
- [[sources/hyplora-neurips2025]] — HypLoRA 论文 (NeurIPS 2025) | status:developing | domain:Training

### type: operation
*(待 ingest 填充)*

### type: insight
- [[insights/llm-embedding-geometry]] — LLM 嵌入空间具有内在双曲结构 | status:seed | domain:Architecture
- [[insights/hybrid-beats-pure-llm]] — 混合系统胜过纯 LLM | status:seed | domain:Engineering

### type: source
- [[sources/claude-code-config-and-mcp-flow]] — Claude Code 配置与 MCP 流程笔记 | status:seed | domain:Engineering
- [[sources/hyplora-neurips2025]] — HypLoRA 论文摘要 | status:developing | domain:Training
- [[sources/cagc-cvpr2024]] — CAGC: Contextual Augmented Global Contrast 论文摘要 | status:developing | domain:Multimodal
- [[sources/intent-detection-age-of-llms]] — Intent Detection in the Age of LLMs 论文摘要 | status:developing | domain:Agents

### type: comparison
- [[comparisons/cagc-vs-baselines]] — CAGC vs MAG-BERT/MulT/MISA/ConFEDE 对比 | status:seed | domain:Multimodal

### type: question / gap
- [[questions/hyplora-thought-experiments]] — HypLoRA 思想实验与开放问题 | status:seed | domain:Training
- [[questions/hyplora-research-directions]] — HypLoRA 未来研究方向 | status:seed | domain:Training

---

## 📊 统计

| 指标 | 数值 |
|------|------|
| 总节点数 | 31 |
| concept | 19 |
| entity | 0 |
| operation | 0 |
| insight | 3 |
| source | 4 |
| comparison | 1 |
| question/gap | 2 |
| mature 节点 | 0 |
| seed 节点 | 29 |
| 矛盾登记 | 0 |

*上次更新: 2026-06-14 | 系统健康修复 + contrastive-learning 占位页*
