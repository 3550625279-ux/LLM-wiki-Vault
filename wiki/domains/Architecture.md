---
title: "Architecture — 模型架构"
type: domain
status: developing
domain: Architecture
tags: [transformer, attention, positional-encoding, normalization, moe, cross-video-attention]
created: 2026-06-13
updated: 2026-06-14
confidence: high
---

# Architecture — 模型架构

> **领域使命**: 理解 Transformer 系列模型的内部结构。
> **核心主张**: 现代 LLM 几乎全部建立在 Transformer 变体之上，理解原版 Transformer 是一切的起点。

---

## 📌 领域地图

```
Architecture
├── Transformer 基础
│   ├── Attention Mechanism (核心)
│   ├── Multi-Head Attention
│   ├── Feed-Forward Network
│   ├── Residual Connections
│   └── Layer Normalization
│
├── 注意力机制扩展 ✅ NEW
│   ├── [[concepts/context-augmented-transformer]] — CAT 渐进式跨视频注意力
│   ├── Cross-Attention (标准交叉注意力)
│   └── Co-Attention (多模态协同注意力)
│
├── 位置编码
│   ├── Absolute Positional Encoding
│   ├── Relative Positional Encoding
│   ├── RoPE (Rotary Position Embedding) ← 当前主流
│   └── ALiBi
│
├── 架构变体
│   ├── Encoder-only (BERT 系列)
│   ├── Decoder-only (GPT 系列) ← LLM 主流
│   ├── Encoder-Decoder (T5/BART)
│   └── Prefix LM
│
├── 规模化技术
│   ├── Mixture of Experts (MoE)
│   ├── Sparse Attention
│   └── Long Context 方法
│
└── 效率优化
    ├── Flash Attention (IO-aware)
    ├── Flash Attention 2/3
    ├── Linear Attention
    └── Multi-Query Attention / GQA
```

---

## 🧮 已有节点

- [x] [[concepts/hyperbolic-geometry-llm]] — LLM 嵌入的双曲层次结构（幂律分布+δ-双曲性） | status:seed
- [x] [[concepts/context-augmented-transformer]] — CAT 渐进式跨视频注意力（CAGC 核心架构） | status:seed

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/hyperbolic-geometry-llm]]
- `contains::` [[concepts/context-augmented-transformer]]

## 🔴 关键缺口

- `attention-mechanism` — QKV 机制，softmax，O(n²) — **所有架构知识的基础**
- `multi-head-attention` — 多头并行，信息整合
- `flash-attention` — IO-aware 算法，内存效率
- `rotary-position-embedding` — RoPE, 当前主流位置编码
- `layer-normalization` — Pre-Norm vs Post-Norm
- `mixture-of-experts` — MoE 稀疏激活
- `grouped-query-attention` — GQA 减少 KV Cache

---

## 🔗 领域间关系

- `depends_on::` [[domains/foundations]] — 需要线性代数和概率论
- `precedes::` [[domains/training]] — 架构决定训练效率
- `precedes::` [[domains/inference]] — 架构决定推理成本
- `applied_in::` [[domains/multimodal]] — ViT 等多模态模型基于 Transformer
- `applied_in::` [[domains/agents]] — Agent 的 backbone 是 LLM

---

## 💡 领域关键洞察

- Attention 的本质: 动态的、内容相关的加权平均
- Decoder-only 成为主流的原因: 训练效率 + 自回归生成天然适合
- Pre-Norm (在残差之前做 LayerNorm) 训练更稳定，现代大模型标配
- Flash Attention 不改变数学结果，只改变内存访问模式

---

## ⚠️ 活跃矛盾/争议

- Linear Attention vs Softmax Attention: 线性近似能否匹敌全精度注意力？
- MoE 真正优于 Dense 模型的场景？参数量 vs 激活量的权衡

---

## 📖 推荐资料

- [ ] Vaswani et al. 2017 "Attention Is All You Need" (必读)
- [ ] Illustrated Transformer (Jay Alammar 博客)
- [ ] Flash Attention 1/2 论文 (Dao et al.)
- [ ] Mistral/Llama 2/3 技术报告

---

## 📊 领域统计

```
concept 节点: 2 (目标: 12+)
entity 节点:  0 (目标: 8+)
maturity:    developing
```
