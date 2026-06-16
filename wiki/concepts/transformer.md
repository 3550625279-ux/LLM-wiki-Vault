---
type: concept
title: "Transformer 架构"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, Transformer, 注意力, 自注意力, 架构]
status: seed
complexity: advanced
domain: Architecture
sources: ["Vaswani et al. 2017"]
related:
  - "depends_on::[[concepts/scaled-dot-product-attention]]"
  - "depends_on::[[concepts/multi-head-attention]]"
  - "depends_on::[[concepts/layer-normalization]]"
  - "depends_on::[[concepts/encoder-decoder-architecture]]"
  - "extends::[[concepts/recurrent-neural-network]]"
  - "applied_in::[[concepts/context-augmented-transformer]]"
  - "belongs_to::[[domains/Architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/scaled-dot-product-attention]] | [[concepts/multi-head-attention]] | [[concepts/layer-normalization]] | [[concepts/encoder-decoder-architecture]]
- extends: [[concepts/recurrent-neural-network]]
- applied_in: [[concepts/context-augmented-transformer]]

---

# Transformer 架构

## 核心思想

**"Attention Is All You Need"**（Vaswani et al., 2017）——完全抛弃循环和卷积，仅用注意力机制构建序列到序列模型。

## 架构组件

### Encoder Block（×N）
```
输入嵌入 + 位置编码
    ↓
Multi-Head Self-Attention (Q=K=V=输入)
    ↓ Add & LayerNorm (残差连接)
Feed-Forward Network (两层线性 + ReLU)
    ↓ Add & LayerNorm
输出
```

### Decoder Block（×N）
```
目标嵌入 + 位置编码
    ↓
Masked Multi-Head Self-Attention (防止看到未来)
    ↓ Add & LayerNorm
Multi-Head Cross-Attention (Q=decoder, K=V=encoder输出)
    ↓ Add & LayerNorm
Feed-Forward Network
    ↓ Add & LayerNorm
输出
```

## 关键创新

| 创新 | 解决的问题 | 对应页面 |
|------|-----------|---------|
| Self-Attention | 替代 RNN 的序列依赖 | [[concepts/scaled-dot-product-attention]] |
| Multi-Head | 捕捉多种注意力模式 | [[concepts/multi-head-attention]] |
| 位置编码 | 注入序列位置信息 | 正弦/余弦编码 |
| 残差连接 | 缓解深层网络梯度消失 | Add & Norm |
| LayerNorm | 稳定训练 | [[concepts/layer-normalization]] |

## 为什么 Transformer 击败 RNN

| 特性 | RNN | Transformer |
|------|-----|------------|
| 并行度 | 串行（$O(T)$步） | 全并行（$O(1)$步） |
| 长距离依赖 | 受限于梯度消失 | 直接 attention 任意距离 |
| 计算复杂度 | $O(T \cdot d^2)$ | $O(T^2 \cdot d)$ |
| GPU 利用率 | 低 | 高 |

## 后续影响

- **Encoder-only**: BERT（双向注意力，理解任务）
- **Decoder-only**: GPT 系列（因果注意力，生成任务）← LLM 主流
- **Encoder-Decoder**: T5, BART（翻译/摘要）
