---
type: concept
title: "加性注意力 (Additive Attention)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 注意力, Bahdanau, Seq2Seq]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/attention-mechanism]]"
  - "contrasts::[[concepts/scaled-dot-product-attention]]"
  - "applied_in::[[concepts/encoder-decoder-architecture]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/attention-mechanism]]
- contrasts: [[concepts/scaled-dot-product-attention]]
- applied_in: [[concepts/encoder-decoder-architecture]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# 加性注意力 (Additive Attention)

## 核心思想

当 Query 和 Key 的维度不同（$q \neq k$）时，无法直接用点积。加性注意力通过**投影到统一维度 $h$**，再用 tanh 激活后压缩为标量分数。

## 数学公式

$$a(\mathbf{q}, \mathbf{k}) = \mathbf{w}_v^\top \tanh(\mathbf{W}_q \mathbf{q} + \mathbf{W}_k \mathbf{k})$$

其中：
- $\mathbf{W}_q \in \mathbb{R}^{h \times q}$ — Query 投影矩阵
- $\mathbf{W}_k \in \mathbb{R}^{h \times k}$ — Key 投影矩阵
- $\mathbf{w}_v \in \mathbb{R}^h$ — 打分向量

## 张量流转（核心难点）

```python
class AdditiveAttention(nn.Module):
    def __init__(self, key_size, query_size, num_hiddens, dropout):
        self.W_q = nn.Linear(query_size, num_hiddens, bias=False)
        self.W_k = nn.Linear(key_size, num_hiddens, bias=False)
        self.W_v = nn.Linear(num_hiddens, 1, bias=False)

    def forward(self, queries, keys, values, valid_lens):
        # queries: [B, num_queries, query_size]
        # keys:    [B, num_keys, key_size]
        queries, keys = self.W_q(queries), self.W_k(keys)
        # → queries: [B, num_queries, h]
        # → keys:    [B, num_keys, h]

        # 广播相加，生成完整的匹配矩阵
        features = queries.unsqueeze(2) + keys.unsqueeze(1)
        # → [B, num_queries, 1, h] + [B, 1, num_keys, h]
        # → [B, num_queries, num_keys, h]

        scores = self.W_v(torch.tanh(features)).squeeze(-1)
        # → [B, num_queries, num_keys]

        self.attention_weights = masked_softmax(scores, valid_lens)
        return torch.bmm(self.dropout(self.attention_weights), values)
```

## unsqueeze + 广播的关键理解

定义层时理解成**单样本**，传播时展开成 **batch**：
- `queries.unsqueeze(2)` → 在第2维插入长度1的轴 → 触发广播
- 广播机制自动扩展，无需显式 for 循环
- 最终 features 形状 `(B, num_queries, num_keys, h)` 确保每个 query 与每个 key 做融合
