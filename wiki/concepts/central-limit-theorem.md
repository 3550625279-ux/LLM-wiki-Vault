---
type: concept
title: "中心极限定理（CLT）"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, CLT, 正态分布]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/variance-geometric]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/central-limit-theorem]]"
  - "applied_in::[[concepts/batch-normalization]]"
  - "applied_in::[[concepts/layer-normalization]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/variance-geometric]]
- produced_by: [[sources/central-limit-theorem]]
- applied_in: [[concepts/batch-normalization]] | [[concepts/layer-normalization]]

---

# 中心极限定理（CLT）

## 数学陈述

设 $X_1, X_2, \ldots, X_n$ 是 $n$ 个独立同分布（i.i.d.）的随机变量，均值为 $\mu$，方差为 $\sigma^2$。

定义部分和 $S_n = X_1 + X_2 + \cdots + X_n$，则标准化和：

$$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}}$$

的分布收敛到标准正态 $N(0, 1)$，即：

$$\lim_{n \to \infty} P(Z_n \leq z) = \Phi(z)$$

其中 $\Phi$ 是标准正态分布的累积分布函数。

## 关键区分

**不是 $S_n$ 自己变成标准正态**，而是标准化后的 $Z_n$ 趋向标准正态。

$S_n$ 的分布始终在漂移——均值为 $n\mu$，方差为 $n\sigma^2$，中心和尺度都在变化。CLT 说的是：经过标准化手术把中心拉回 0、把尺度压回 1 之后，形状趋近正态。

## 标准化手术的两步

1. **中心化（减 $n\mu$）**：把分布的中心从 $n\mu$ 拉回到 0
2. **缩放（除以 $\sigma\sqrt{n}$）**：把分布的宽度从 $\sigma\sqrt{n}$ 压回 1

两步合在一起：$Z_n = \frac{S_n - n\mu}{\sigma\sqrt{n}}$

## 气球类比

想象 $S_n$ 的分布像一个不断膨胀的气球：

- **形状**始终近似正态（CLT 的核心保证）
- **中心**在 $n\mu$ 处不断漂移
- **大小**（标准差 $\sigma\sqrt{n}$）在不断膨胀

标准化就是把这个膨胀的气球"缩放回单位大小、移到原点"的操作。

## CLT 的强大之处：普适性

CLT 最惊人的性质是**普适性**——不管原始分布是什么形状（均匀分布、指数分布、离散分布……），只要满足独立同分布且方差有限，标准化和都会趋向正态。

这就是正态分布在自然界和工程中无处不在的根本原因。

## 与深度学习的连接

- [[concepts/batch-normalization]]：BN 利用 CLT 保证 batch 内统计量（均值、方差）在大 batch 下稳定
- [[concepts/layer-normalization]]：LN 的概率论基础较弱，但几何解释使其有效
- [[concepts/transformer-sqrt-d]]：注意力机制中的 $\sqrt{d}$ 缩放，其根源与 CLT 中的 $\sqrt{n}$ 同源
