---
type: concept
title: "区间估计与枢轴量"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 区间估计, 枢轴量]
status: seed
complexity: advanced
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/estimator-quality]]"
  - "depends_on::[[concepts/order-statistics]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
---

## 🔗 关系链接

- depends_on: [[concepts/estimator-quality]]
- depends_on: [[concepts/order-statistics]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]

---

# 区间估计与枢轴量

## 核心思想

> **构造枢轴量，利用枢轴量的分布反解出统计量和真实值的不等式。**

点估计只给出一个数值，无法衡量不确定性。区间估计给出一个区间 $[L, U]$，使得真实参数以一定概率落在这个区间内。

## 枢轴量的定义

**枢轴量** $Q$ 是一个包含样本和未知参数的函数，其分布**不依赖于任何未知参数**。

$$Q = Q(X_1, \dots, X_n; \theta)$$

关键：$Q$ 的分布是已知的（如标准正态、卡方、t、F），因此可以查表求分位数。

## 枢轴量的四种分布情形

### 1. 正态分布：方差已知，估计期望

**场景**：$X_i \sim N(\mu, \sigma^2)$，$\sigma^2$ 已知，求 $\mu$ 的置信区间。

**枢轴量**：

$$Z = \frac{\bar{X} - \mu}{\sigma / \sqrt{n}} \sim N(0, 1)$$

**置信区间**（双侧）：

$$\bar{X} \pm z_{\alpha/2} \cdot \frac{\sigma}{\sqrt{n}}$$

也适用于单侧区间估计。

### 2. 卡方分布：期望已知，估计方差

**场景**：$X_i \sim N(\mu, \sigma^2)$，$\mu$ 已知，求 $\sigma^2$ 的置信区间。

**枢轴量**：

$$\chi^2 = \frac{\sum_{i=1}^{n}(X_i - \mu)^2}{\sigma^2} \sim \chi^2(n)$$

**置信区间**（单区间）：

$$\left[\frac{\sum(X_i - \mu)^2}{\chi^2_{\alpha/2}(n)}, \frac{\sum(X_i - \mu)^2}{\chi^2_{1-\alpha/2}(n)}\right]$$

### 3. t 分布：方差未知，估计期望

**场景**：$X_i \sim N(\mu, \sigma^2)$，$\sigma^2$ 未知，求 $\mu$ 的置信区间。

**核心**：正态分布的方差未知时，用 t 分布替代正态分布。

**枢轴量**：

$$T = \frac{\bar{X} - \mu}{S / \sqrt{n}} \sim t(n-1)$$

其中 $S^2 = \frac{1}{n-1}\sum(X_i - \bar{X})^2$。

**置信区间**：

$$\bar{X} \pm t_{\alpha/2}(n-1) \cdot \frac{S}{\sqrt{n}}$$

**另一种情形**：均值未知，用卡方分布和正交变换证明方差的 t 分布枢轴量。

### 4. F 分布：双区间估计方差

**场景**：两个正态总体，均值已知或未知，比较方差。

**枢轴量**：

$$F = \frac{S_1^2 / \sigma_1^2}{S_2^2 / \sigma_2^2} \sim F(n_1-1, n_2-1)$$

（卡方分布之比，差个自由度）

## 分位数表的使用

### 分位数的定义

$x_\alpha$ 满足：从 $x_\alpha$ 到无穷远处的面积为 $\alpha$。

$$P(X > x_\alpha) = \alpha$$

### 各分布分位数的性质

| 分布 | 对称性 | 分位数关系 |
|------|--------|-----------|
| **正态分布** | 关于 0 对称 | $x_\alpha + x_{1-\alpha} = 0$ |
| **t 分布** | 关于 0 对称 | $t_\alpha + t_{1-\alpha} = 0$ |
| **卡方分布** | 不对称 | 只有简单的大小关系 |
| **F 分布** | 不对称 | 倒数关系：$F_\alpha(m,n) = \frac{1}{F_{1-\alpha}(n,m)}$ |

### F 分布的倒数关系

这是一个重要的计算技巧：

$$F_\alpha(m, n) = \frac{1}{F_{1-\alpha}(n, m)}$$

当查表只给出较小自由度的 $F$ 值时，可以用这个关系反求。

## 置信水平的选择

- 90% 置信区间：$\alpha = 0.10$
- 95% 置信区间：$\alpha = 0.05$（最常用）
- 99% 置信区间：$\alpha = 0.01$

置信水平越高，区间越宽——不确定性越大，需要更大的区间来"覆盖"真实值。
