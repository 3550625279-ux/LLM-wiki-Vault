---
type: concept
title: "ResNet — 残差网络"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, CNN, 残差连接, 深层网络]
status: seed
complexity: intermediate
domain: Architecture
sources: ["He et al. 2015"]
related:
  - "depends_on::[[concepts/convolutional-neural-network]]"
  - "depends_on::[[concepts/batch-normalization]]"
  - "applied_in::[[concepts/multi-head-attention]]"
  - "belongs_to::[[domains/Architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/convolutional-neural-network]] | [[concepts/batch-normalization]]
- applied_in: [[concepts/multi-head-attention]]

---

# ResNet — 残差网络

## 核心思想

**残差连接 (Skip Connection)**：让网络学习残差映射而非直接映射。

$$\mathbf{y} = F(\mathbf{x}) + \mathbf{x}$$

其中 $F(\mathbf{x})$ 是需要学习的残差函数（通常是 2-3 层卷积）。

## 为什么有效

- **梯度高速公路**: 残差连接让梯度直接回传，解决深层网络的梯度消失
- **恒等映射兜底**: 即使 $F(\mathbf{x}) = 0$，输出仍等于输入，不会退化
- **实验验证**: ResNet-152 比 VGG-19 深 8 倍，但训练更容易

## 对 Transformer 的影响

残差连接是 Transformer 的标配组件：
```
Multi-Head Attention → Add (残差) → LayerNorm
Feed-Forward Network → Add (残差) → LayerNorm
```

没有残差连接，深层 Transformer（如 GPT-3 的 96 层）根本无法训练。
