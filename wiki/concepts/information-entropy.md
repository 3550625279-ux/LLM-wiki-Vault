---
type: concept
title: "信息熵"
created: 2026-06-16
updated: 2026-06-16
tags: [信息论, 熵, 信息量]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/information-theory-loss]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/information-theory-loss]]"
  - "applied_in::[[concepts/cross-entropy-loss]]"
  - "applied_in::[[concepts/kl-divergence]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/random-variable]]
- produced_by: [[sources/information-theory-loss]]
- applied_in: [[concepts/cross-entropy-loss]] | [[concepts/kl-divergence]]

---

## 核心洞察

概率分布之间的"距离"不能用欧氏距离（MSE），要用信息量（比特）。

MSE 在概率空间中的缺陷：对概率空间的几何结构是"盲"的。当模型输出一个概率分布时，MSE 无法感知概率归一化约束、分布的支撑集结构等关键信息。

香农的洞察：用比特而非尺子来衡量分布差异。

## 自信息（Information Content）

事件 A 的自信息量：

$$I(A) = -\log P(A)$$

- **直觉**：事件越不可能发生，发生时携带的信息量越大
- **为什么用对数**：独立事件的信息量可加。若 A、B 独立，则 $I(A \cap B) = I(A) + I(B)$，对应 $P(A \cap B) = P(A) \cdot P(B)$ 的乘法结构
- **例子**：公平硬币抛出正面，$I(\text{正面}) = -\log_2(0.5) = 1 \text{ bit}$

## 香农熵（Shannon Entropy）

概率分布 P 的香农熵：

$$H(P) = -\sum_{i} P(x_i) \log P(x_i)$$

- **直觉**：每次观测平均能获得多少信息量；也即描述该分布所需的最小平均比特数
- **性质**：
  - **非负性**：$H(P) \geq 0$
  - **最大值**：均匀分布时取最大值 $\log_2(n)$，其中 n 为支撑集大小
  - **凹性**：$H$ 是关于 P 的凹函数（混合分布的熵不小于各分布熵的加权平均）

## 例子

| 分布 | 熵值 | 说明 |
|------|------|------|
| 公平骰子 (n=6) | $H \approx 2.585$ bits | 每次掷骰子平均获得约 2.585 bits 信息 |
| 偏倚硬币 (P=0.9, 0.1) | $H \approx 0.469$ bits | 高度确定性，信息量低 |
| 确定事件 (P=1) | $H = 0$ | 无不确定性，无信息量 |

## 与深度学习的联系

信息熵是交叉熵损失函数和 KL 散度的理论基石。在 LLM 训练中，人类语料库的固有熵 H(P) 是一个常数，模型优化的目标是让预测分布 Q 尽可能接近真实分布 P。
