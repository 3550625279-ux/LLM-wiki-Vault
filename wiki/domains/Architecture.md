---
title: "Architecture — 模型架构"
type: domain
status: seed
domain: Architecture
tags: [transformer, attention, positional-encoding, normalization, moe]
created: 2026-06-13
updated: 2026-06-13
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

## 🧮 核心概念节点

### Attention 系列
- [ ] [[concepts/attention-mechanism]] — QKV 机制，softmax，O(n²)
- [ ] [[concepts/multi-head-attention]] — 多头并行，信息整合
- [ ] [[concepts/self-attention-vs-cross-attention]] — 自注意力 vs 交叉注意力
- [ ] [[concepts/flash-attention]] — IO-aware 算法，内存效率

### 位置编码
- [ ] [[concepts/rotary-position-embedding]] — RoPE 原理与优势
- [ ] [[concepts/positional-encoding-absolute]] — 原始 sin/cos 编码

### 规范化
- [ ] [[concepts/layer-normalization]] — Pre-Norm vs Post-Norm
- [ ] [[concepts/rmsnorm]] — RMSNorm 为什么更流行

### 架构创新
- [ ] [[concepts/mixture-of-experts]] — MoE 稀疏激活
- [ ] [[concepts/grouped-query-attention]] — GQA 减少 KV Cache

### 经典论文
- [ ] [[entities/attention-is-all-you-need]] — Vaswani 2017，奠基之作
- [ ] [[entities/bert]] — 双向编码器
- [ ] [[entities/gpt-series]] — 自回归语言模型系列

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
concept 节点: 0 (目标: 12+)
entity 节点:  0 (目标: 8+)
maturity:    seed
```
