---
type: concept
title: "多头注意力 (Multi-Head Attention)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 注意力, Transformer, 多头]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/scaled-dot-product-attention]]"
  - "depends_on::[[concepts/attention-mechanism]]"
  - "part_of::[[concepts/encoder-decoder-architecture]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/scaled-dot-product-attention]] | [[concepts/attention-mechanism]]
- part_of: [[concepts/encoder-decoder-architecture]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# 多头注意力 (Multi-Head Attention)

## 核心思想

单头注意力只能捕捉一种"关注模式"。多头注意力将 $Q, K, V$ 投影到 $h$ 个低维子空间，**并行**计算注意力，再拼接融合。

$$\text{MultiHead}(Q, K, V) = \text{Concat}(\text{head}_1, \ldots, \text{head}_h) W^O$$
$$\text{head}_i = \text{Attention}(QW_i^Q, KW_i^K, VW_i^V)$$

## 张量变形流程（核心难点）

```
输入: [B, seq_len, d_model]
  ↓ W_q 线性投影
[B, seq_len, num_hiddens]
  ↓ reshape
[B, seq_len, num_heads, d_k]     # d_k = num_hiddens / num_heads
  ↓ permute(0, 2, 1, 3)
[B, num_heads, seq_len, d_k]
  ↓ reshape (合并前两维)
[B * num_heads, seq_len, d_k]     # 可以送入标准点积注意力
  ↓ DotProductAttention
[B * num_heads, seq_len, d_k]
  ↓ reshape + permute (逆操作)
[B, seq_len, num_hiddens]
  ↓ W_o 线性投影
[B, seq_len, num_hiddens]
```

## PyTorch 实现

```python
class MultiHeadAttention(nn.Module):
    def __init__(self, key_size, query_size, value_size, num_hiddens, num_heads, dropout):
        super().__init__()
        self.num_heads = num_heads
        self.attention = DotProductAttention(dropout)
        self.W_q = nn.Linear(query_size, num_hiddens, bias=False)
        self.W_k = nn.Linear(key_size, num_hiddens, bias=False)
        self.W_v = nn.Linear(value_size, num_hiddens, bias=False)
        self.W_o = nn.Linear(num_hiddens, num_hiddens, bias=False)

    def forward(self, queries, keys, values, valid_lens):
        # 线性投影 + 拆分多头
        queries = transpose_qkv(self.W_q(queries), self.num_heads)
        keys = transpose_qkv(self.W_k(keys), self.num_heads)
        values = transpose_qkv(self.W_v(values), self.num_heads)

        if valid_lens is not None:
            valid_lens = torch.repeat_interleave(valid_lens, self.num_heads, dim=0)

        # 并行注意力
        output = self.attention(queries, keys, values, valid_lens)

        # 拼接 + 输出投影
        output_concat = transpose_output(output, self.num_heads)
        return self.W_o(output_concat)
```

## 关键变形函数

```python
def transpose_qkv(X, num_heads):
    """[B, seq, h] → [B*num_heads, seq, h/num_heads]"""
    X = X.reshape(X.shape[0], X.shape[1], num_heads, -1)
    X = X.permute(0, 2, 1, 3)
    return X.reshape(-1, X.shape[2], X.shape[3])

def transpose_output(X, num_heads):
    """逆操作: [B*num_heads, seq, h/num_heads] → [B, seq, h]"""
    X = X.reshape(-1, num_heads, X.shape[1], X.shape[2])
    X = X.permute(0, 2, 1, 3)
    return X.reshape(X.shape[0], X.shape[1], -1)
```

## 直觉理解

多头 = "团队合作"。每个头独立学习不同的注意力模式（如一个头关注语法依赖，另一个头关注语义相似性），最后通过 $W^O$ 进行特征融合。
