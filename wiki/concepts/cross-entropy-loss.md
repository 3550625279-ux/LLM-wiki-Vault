---
type: concept
title: "交叉熵与深度学习损失函数"
created: 2026-06-16
updated: 2026-06-16
tags: [信息论, 交叉熵, 损失函数, 深度学习]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/information-theory-loss]]"]
related:
  - "depends_on::[[concepts/information-entropy]]"
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/information-theory-loss]]"
  - "applied_in::[[concepts/llm-training]]"
  - "applied_in::[[concepts/recurrent-neural-network]]"
  - "applied_in::[[concepts/encoder-decoder-architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/information-entropy]] | [[concepts/random-variable]]
- produced_by: [[sources/information-theory-loss]]
- applied_in: [[concepts/llm-training]] | [[concepts/recurrent-neural-network]] | [[concepts/encoder-decoder-architecture]]

---

## 交叉熵定义

给定真实分布 P 和预测分布 Q，交叉熵为：

$$H(P, Q) = -\sum_{i} P(x_i) \log Q(x_i)$$

- **直觉**：用 Q 的编码方案去编码 P 的数据时，每个符号平均需要的比特数
- 若 Q 越接近 P，交叉熵越小；若 Q = P，交叉熵等于 P 的自身熵

## Gibbs 不等式

$$H(P, Q) \geq H(P)$$

等号当且仅当 $P = Q$ 时成立。

**推导思路**：利用不等式 $\ln x \leq x - 1$（等号当且仅当 $x = 1$）：

$$D_{KL}(P \| Q) = \sum_i P(x_i) \ln \frac{P(x_i)}{Q(x_i)} = -\sum_i P(x_i) \ln \frac{Q(x_i)}{P(x_i)} \geq -\sum_i P(x_i) \left(\frac{Q(x_i)}{P(x_i)} - 1\right) = 0$$

## 核心等式

$$H(P, Q) = H(P) + D_{KL}(P \| Q)$$

交叉熵 = 真实熵 + KL 散度。

这个等式揭示了深度学习损失函数的本质结构：
- $H(P)$ 是常数（人类语料库的固有熵，不可优化）
- 最小化 $H(P, Q)$ 等价于最小化 $D_{KL}(P \| Q)$

## LLM 训练的本质

LLM 的训练目标是让模型分布 Q 逼近人类语言分布 P：

1. **PyTorch 的 `nn.CrossEntropyLoss`** 计算的就是 $H(P, Q)$
2. **标签是 One-Hot 向量时**：$P$ 只在 $y_{\text{true}}$ 处为 1，其余为 0
   - 交叉熵退化为：$H(P, Q) = -\log Q(y_{\text{true}})$
   - 即只需要关注模型对正确答案的预测概率
3. **最小化交叉熵**等价于**最小化 KL 散度**，等价于**最大化似然**

## One-Hot 标签下的推导

当标签为 one-hot（$P = [0, \ldots, 1, \ldots, 0]$，只有第 $k$ 位为 1）：

$$H(P, Q) = -\sum_i P(x_i) \log Q(x_i) = -1 \cdot \log Q(x_k) = -\log Q(y_{\text{true}})$$

只有正确类别对应的一项存活，这就是为什么分类任务的交叉熵损失就是"负对数似然"。
