---
type: concept
title: "√n的来源：方差可加性"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 方差可加性, √n]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/variance-geometric]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/central-limit-theorem]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/variance-geometric]]
- produced_by: [[sources/central-limit-theorem]]

---

# √n 的来源：方差可加性

## 方差可加性

对于两个独立随机变量 $X$ 和 $Y$，有：

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

### 详细推导

展开方差的定义：

$$\text{Var}(X + Y) = E[(X + Y - E[X + Y])^2]$$

$$= E[((X - \mu_X) + (Y - \mu_Y))^2]$$

$$= E[(X - \mu_X)^2] + 2E[(X - \mu_X)(Y - \mu_Y)] + E[(Y - \mu_Y)^2]$$

$$= \text{Var}(X) + 2\text{Cov}(X, Y) + \text{Var}(Y)$$

当 $X$ 和 $Y$ 独立时，$\text{Cov}(X, Y) = 0$，交叉项消失：

$$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$$

## 从方差到 √n

对于 $n$ 个独立同分布的随机变量，每个方差为 $\sigma^2$：

$$\text{Var}(S_n) = \text{Var}(X_1 + X_2 + \cdots + X_n) = n\sigma^2$$

取标准差：

$$\sigma(S_n) = \sqrt{n\sigma^2} = \sigma\sqrt{n}$$

**√n 就是从方差开方来的，没有更深的原因。** 方差可加 → 总方差 = n倍 → 标准差 = √n 倍。

## 抵消效应的直觉：醉汉随机走路

一个醉汉从原点出发，每步随机向左或向右走一步。走 $n$ 步后：

- **期望位置** = 0（左右抵消）
- **平均距离**（标准差）≈ $\sqrt{n}$ 步

### 最坏情况 vs 实际情况

| 情形 | 距离 | 概率 |
|------|------|------|
| 全部同向 | $n$ | 极小（$2^{-n}$） |
| 实际平均 | $\sqrt{n}$ | 大部分情况 |

正负部分抵消，使得净位移远小于最大可能位移。$\sqrt{n}$ 正是这种"部分抵消"的量化表达。

## 与 CLT 的关系

$\sqrt{n}$ 出现在 CLT 的分母中不是巧合——它直接来自方差可加性。CLT 标准化公式的分母 $\sigma\sqrt{n}$ 就是 $S_n$ 的标准差。
