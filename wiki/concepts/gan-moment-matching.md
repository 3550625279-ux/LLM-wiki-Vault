---
type: concept
title: "GAN 矩匹配"
created: 2026-06-16
updated: 2026-06-16
tags: [生成模型, GAN, 矩匹配, 统计]
status: seed
complexity: advanced
domain: Architecture
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/moment]]"
  - "depends_on::[[concepts/covariance]]"
  - "belongs_to::[[domains/Architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/moment]] | [[concepts/covariance]]

---

# GAN 矩匹配

## 核心思想

矩匹配（Moment Matching）是 GAN 训练的一种替代方法：不训练判别器，而是直接让生成样本的统计矩（均值、方差、高阶矩）匹配真实数据的统计矩。

## 数学形式

$$\min_G \sum_{k=1}^{K} \left\| \mathbb{E}_{x \sim p_{data}}[x^k] - \mathbb{E}_{z \sim p_z}[G(z)^k] \right\|^2$$

其中 $k$ 阶矩 $\mathbb{E}[x^k]$ 就是 [[concepts/moment]] 中定义的 $k$ 阶原点矩。

## 与标准 GAN 的对比

| 特性 | 标准 GAN | 矩匹配 GAN |
|------|---------|-----------|
| 判别器 | 需要训练 | 不需要 |
| 训练稳定性 | 模式崩溃风险 | 更稳定 |
| 生成质量 | 通常更好 | 可能模糊 |
| 理论保证 | 较弱 | 矩收敛 → 分布收敛 |

## 与 [[concepts/moment]] 的关系

矩匹配直接应用了统计矩的定义：如果两个分布的所有阶矩都相等（在一定条件下），则两个分布相同。这为 GAN 提供了更坚实的数学基础。
