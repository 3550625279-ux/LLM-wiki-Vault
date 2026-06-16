---
type: concept
title: "缩放点积注意力 (Scaled Dot-Product Attention)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 注意力, Transformer, 点积, √d]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/attention-mechanism]]"
  - "depends_on::[[concepts/transformer-sqrt-d]]"
  - "contrasts::[[concepts/additive-attention]]"
  - "part_of::[[concepts/multi-head-attention]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/attention-mechanism]] | [[concepts/transformer-sqrt-d]]
- contrasts: [[concepts/additive-attention]]
- part_of: [[concepts/multi-head-attention]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# 缩放点积注意力 (Scaled Dot-Product Attention)

## 核心思想

当 $Q$ 和 $K$ 维度相同时（$q = k = d$），直接用矩阵乘法计算注意力分数，然后除以 $\sqrt{d}$ 防止 Softmax 饱和。

## 数学公式

$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d}}\right) V$$

## 为什么要除以 $\sqrt{d}$

见 [[concepts/transformer-sqrt-d]] 的详细推导。核心结论：

- 点积的方差 = $d$（方差可加性）
- $d$ 很大时（如 512），点积值范围极大 → Softmax 输出接近 one-hot → **梯度消失**
- 除以 $\sqrt{d}$ 将方差压回 1，保持 Softmax 在非饱和区工作

**这是 NW 核回归中 $w$ 过大导致"Softmax 死亡饱和区"问题在高维空间的重演。**

## PyTorch 实现

```python
class DotProductAttention(nn.Module):
    def __init__(self, dropout):
        super().__init__()
        self.dropout = nn.Dropout(dropout)

    def forward(self, queries, keys, values):
        d = queries.shape[-1]
        # QK^T / sqrt(d)
        scores = torch.bmm(queries, keys.transpose(1, 2)) / math.sqrt(d)
        self.attention_weights = F.softmax(scores, dim=-1)
        # 加权求和
        return torch.bmm(self.dropout(self.attention_weights), values)
```

## 与加性注意力的对比

| 特性 | 缩放点积注意力 | 加性注意力 |
|------|-------------|-----------|
| 适用条件 | $Q$ 和 $K$ 维度相同 | 维度可以不同 |
| 计算方式 | 矩阵乘法（GPU 友好） | 逐元素相加 + tanh |
| 复杂度 | $O(n^2 d)$ | $O(n^2 h d)$ |
| 主流使用 | Transformer 原始论文 | Bahdanau Seq2Seq |
| 硬件效率 | 高（直接调用 CUDA GEMM） | 较低 |
