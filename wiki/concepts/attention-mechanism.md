---
type: concept
title: "注意力机制 (Attention Mechanism)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 注意力, Transformer, QKV]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/cross-entropy-loss]]"
  - "extends::[[concepts/additive-attention]]"
  - "extends::[[concepts/scaled-dot-product-attention]]"
  - "part_of::[[concepts/encoder-decoder-architecture]]"
  - "applied_in::[[concepts/multi-head-attention]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/cross-entropy-loss]]
- extends: [[concepts/additive-attention]] | [[concepts/scaled-dot-product-attention]]
- part_of: [[concepts/encoder-decoder-architecture]]
- applied_in: [[concepts/multi-head-attention]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# 注意力机制 (Attention Mechanism)

## 核心思想

注意力的本质：**动态的、内容相关的加权平均**。

给定查询 Q，对所有键 K 计算相似度分数，经过 Softmax 归一化为权重，再对值 V 做加权求和：

$$\text{Attention}(Q, K, V) = \text{softmax}(\text{score}(Q, K)) \cdot V$$

## Nadaraya-Watson 核回归（标量版本）

注意力机制的原型来自非参数核回归。给定训练数据 $(x_i, y_i)$，对查询 $x$ 的预测：

$$f(x) = \sum_{i=1}^{n} \alpha(x, x_i) y_i$$

其中注意力权重：
$$\alpha(x, x_i) = \frac{\exp(-\frac{1}{2}(x - x_i)^2)}{\sum_j \exp(-\frac{1}{2}(x - x_j)^2)}$$

**核心操作**：利用 PyTorch 广播机制计算距离矩阵：
```python
queries = x_test.reshape(-1, 1)  # [m, 1]
keys = x_train.reshape(1, -1)    # [1, n]
dist = (queries - keys) ** 2      # 广播 → [m, n]
```

## 带参数版本（NW Kernel）

引入可学习参数 $w$：

$$\alpha(x, x_i) = \text{softmax}(-\frac{1}{2}((x - x_i) \cdot w)^2)$$

$w$ 必须注册为 `nn.Parameter` 才能被 Autograd 追踪。

## QKV 范式

从标量到高维向量的升维：

| 角色 | 符号 | 含义 |
|------|------|------|
| Query | $\mathbf{q} \in \mathbb{R}^d$ | "我在找什么" |
| Key | $\mathbf{k} \in \mathbb{R}^d$ | "我有什么" |
| Value | $\mathbf{v} \in \mathbb{R}^v$ | "我的内容是什么" |

## 从标量到高维：升维瓶颈

NW 核回归的 $(q-k)^2$ 距离在高维空间失效。需要引入**注意力评分函数**：
- **加性注意力**: $\mathbf{w}_v^\top \tanh(\mathbf{W}_q \mathbf{q} + \mathbf{W}_k \mathbf{k})$
- **缩放点积注意力**: $\frac{\mathbf{q}^\top \mathbf{k}}{\sqrt{d}}$

## masked_softmax：处理变长序列

实际序列有 padding，需要屏蔽无效位置：
```python
def masked_softmax(X, valid_lens):
    # 将超出有效长度的值设为 -1e6
    X = sequence_mask(X.reshape(-1, shape[-1]), valid_lens, value=-1e6)
    return F.softmax(X.reshape(shape), dim=-1)
```

经过 softmax 后，被屏蔽位置的权重趋近于 0。
