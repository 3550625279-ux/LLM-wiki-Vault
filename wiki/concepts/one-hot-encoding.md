---
type: concept
title: "One-Hot 编码"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 编码, 基础, NLP]
status: seed
complexity: basic
domain: Foundations
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "applied_in::[[concepts/recurrent-neural-network]]"
  - "applied_in::[[concepts/convolutional-neural-network]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- applied_in: [[concepts/recurrent-neural-network]] | [[concepts/convolutional-neural-network]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# One-Hot 编码

## 核心思想

将离散类别索引转换为稀疏的二进制向量。类别 $i$（共 $V$ 类）编码为长度 $V$ 的向量，仅第 $i$ 位为 1，其余为 0。

## PyTorch 实现

```python
inputs = torch.tensor([1, 0, 2])  # 3个样本，类别分别为 1, 0, 2
vocab_size = 4

oh = F.one_hot(inputs, num_classes=vocab_size)
# tensor([[0, 1, 0, 0],   # 类别 1
#          [1, 0, 0, 0],   # 类别 0
#          [0, 0, 1, 0]])  # 类别 2
# 默认类型: torch.int64
```

## 必须转 float32

RNN 的输入必须是浮点数，one-hot 输出是整数：
```python
X = F.one_hot(inputs.T, vocab_size).type(torch.float32)
```

## RNN 中的转置

PyTorch `nn.RNN` 要求输入为 `(seq_len, batch, features)`：
```python
# inputs 形状: [batch, seq_len]
X = F.one_hot(inputs.T, vocab_size).type(torch.float32)
# inputs.T 形状: [seq_len, batch]
# one_hot 后: [seq_len, batch, vocab_size]
```

## 本质

One-hot 编码是**最简单的嵌入方式**——相当于用单位矩阵的行向量表示每个类别。现代模型更常用 `nn.Embedding`（查表式稠密嵌入），但在教学中 one-hot 更直观。
