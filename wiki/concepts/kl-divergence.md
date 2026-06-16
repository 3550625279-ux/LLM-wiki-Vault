---
type: concept
title: "KL散度"
created: 2026-06-16
updated: 2026-06-16
tags: [信息论, KL散度, 相对熵]
status: seed
complexity: advanced
domain: Foundations
sources: ["[[sources/information-theory-loss]]"]
related:
  - "depends_on::[[concepts/cross-entropy-loss]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/information-theory-loss]]"
  - "applied_in::[[concepts/llm-training]]"
  - "applied_in::[[concepts/vae]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/cross-entropy-loss]]
- produced_by: [[sources/information-theory-loss]]
- applied_in: [[concepts/llm-training]] | [[concepts/vae]]

---

## KL 散度定义

Kullback-Leibler 散度（也称相对熵）衡量两个分布之间的"距离"：

$$D_{KL}(P \| Q) = \sum_i P(x_i) \log \frac{P(x_i)}{Q(x_i)}$$

- 等价形式：$D_{KL}(P \| Q) = H(P, Q) - H(P)$
- **前提条件**：Q 对 P 绝对连续（即 $P(x) > 0$ 处必须 $Q(x) > 0$），否则 $D_{KL} = +\infty$

## 关键性质

### 非负性

$$D_{KL}(P \| Q) \geq 0$$

等号当且仅当 $P = Q$（由 Gibbs 不等式保证）。注意 KL 散度不是真正的距离度量，因为它不满足三角不等式。

### 非对称性

$$D_{KL}(P \| Q) \neq D_{KL}(Q \| P)$$

这种非对称性在实际应用中有深远的影响，产生了两种截然不同的优化行为。

## Forward KL vs Reverse KL

### Forward KL（$D_{KL}(P \| Q)$）— Mode-Covering

$$D_{KL}(P \| Q) = \sum_i P(x_i) \log \frac{P(x_i)}{Q(x_i)}$$

- 当 $P(x_i) > 0$ 而 $Q(x_i) \to 0$ 时，惩罚趋向 $+\infty$
- **行为**：Q 必须覆盖 P 的所有支撑，宁可铺开也不能遗漏
- **代价**：Q 可能在 P 的概率为零处也分配概率（过覆盖）
- **直觉**：宁可错杀一千，不可放过一个

### Reverse KL（$D_{KL}(Q \| P)$）— Mode-Seeking

$$D_{KL}(Q \| P) = \sum_i Q(x_i) \log \frac{Q(x_i)}{P(x_i)}$$

- 当 $Q(x_i) > 0$ 而 $P(x_i) \to 0$ 时，惩罚趋向 $+\infty$
- **行为**：Q 只在 P 的高概率区域集中，宁可忽略低概率模式
- **代价**：Q 可能遗漏 P 的次要模式（欠覆盖）
- **直觉**：集中火力攻一个山头

### 数值例子：双峰分布

假设 P 是双峰分布（两个峰分别在 x=0 和 x=5）：
- **Forward KL 优化的 Q**：两个峰都被覆盖，但可能中间区域也被填充
- **Reverse KL 优化的 Q**：只覆盖其中一个峰，另一个峰被忽略

## 在 AI 任务中的选择

| 任务 | 使用的 KL 方向 | 原因 |
|------|----------------|------|
| LLM 训练 | Forward KL | 不能遗漏低频模式，否则模型对罕见语言现象一无所知 |
| VAE 解码器 | Reverse KL | 生成更锐利的样本，避免模糊平均 |
| 知识蒸馏 | Forward KL | 学生需要覆盖教师的全部知识 |
| RL 中的策略优化 | Reverse KL | 策略集中在高回报区域 |

## 与交叉熵的关系

$$H(P, Q) = H(P) + D_{KL}(P \| Q)$$

在深度学习中最小化交叉熵，本质上就是在最小化 KL 散度。由于 $H(P)$ 是数据的固有属性（常数），两者在梯度优化中完全等价。
