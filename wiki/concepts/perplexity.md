---
type: concept
title: "困惑度 (Perplexity)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 评估指标, 语言模型, NLP]
status: seed
complexity: basic
domain: Training
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/cross-entropy-loss]]"
  - "depends_on::[[concepts/information-entropy]]"
  - "applied_in::[[concepts/recurrent-neural-network]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/cross-entropy-loss]] | [[concepts/information-entropy]]
- applied_in: [[concepts/recurrent-neural-network]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 困惑度 (Perplexity)

## 定义

$$\text{PPL} = \exp\left(\frac{1}{N} \sum_{i=1}^{N} -\log P(x_i | x_{<i})\right) = \exp(\text{avg cross-entropy loss})$$

## 直觉理解

- PPL = 1: 模型完美预测每个 token（$-\log P = 0$）
- PPL = V: 模型在 V 个 token 中均匀猜测（$-\log P = \log V$）
- PPL = 2: 模型每次在 2 个选项中犹豫

**越低越好。**

## 计算方式

```python
# 训练中累积 loss 和 token 数
total_loss += loss.item() * y.numel()
total_tokens += y.numel()

# 每 N 个 epoch 计算一次
ppl = math.exp(total_loss / total_tokens)
```

## 实验中的 PPL 变化

| 模型 | 语料 | Epoch 50 | Epoch 500 |
|------|------|----------|-----------|
| RNN | "hello world" × 100 | 1.25 | 1.13 |
| GRU | Time Machine | — | 被中断 |
| LSTM | Time Machine | 6.13 | 1.03 |

LSTM 从 PPL=6.13（还在乱码）收敛到 1.03（几乎完美），展示了门控机制的强大学习能力。
