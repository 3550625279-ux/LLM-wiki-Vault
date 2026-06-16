---
type: concept
title: "估计量的评价：无偏性、有效性、相合性"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 估计量评价, 无偏性, 有效性, 相合性]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/point-estimation]]"
  - "depends_on::[[concepts/order-statistics]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
---

## 🔗 关系链接

- depends_on: [[concepts/point-estimation]]
- depends_on: [[concepts/order-statistics]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]

---

# 估计量的评价：无偏性、有效性、相合性

## 前提：估计量是随机变量

> **估计量 $\hat{\theta}$ 是随机变量**，每次采样得到的估计值不尽相同。

因此，我们需要一套标准来评价一个估计量"好不好"。

## 1. 无偏性（Unbiasedness）

### 定义

$$E[\hat{\theta}] = \theta$$

即估计量的期望等于真实参数值。**采样的平均值就是真实值。**

### 直觉

无偏意味着"不系统性地高估或低估"。多次采样取平均，误差相互抵消。

### 渐近无偏估计

$$E[\hat{\theta}_n] \to \theta \quad (n \to \infty)$$

- 存在一类 **iid 但渐近无偏** 的估计量
- 小样本时有偏，但随样本量增大偏差消失
- 例如：样本方差 $S^2 = \frac{1}{n}\sum(X_i - \bar{X})^2$ 是 $\sigma^2$ 的渐近无偏估计（但 $\frac{1}{n-1}$ 版本才是严格无偏的）

## 2. 有效性（Efficiency）

### 核心思想

针对**两种无偏估计量**的比较——**方差小的更有效**。

$$\text{Var}(\hat{\theta}_1) < \text{Var}(\hat{\theta}_2) \implies \hat{\theta}_1 \text{ 更有效}$$

### Cramér-Rao 下界

任何无偏估计量的方差都有一个理论下界：

$$\text{Var}(\hat{\theta}) \geq \frac{1}{nI(\theta)}$$

其中 $I(\theta)$ 是 Fisher 信息量：

$$I(\theta) = E\left[\left(\frac{\partial \ln f(X;\theta)}{\partial \theta}\right)^2\right]$$

- 达到 Cramér-Rao 下界的估计量称为**有效估计量**
- MLE 在大样本下渐近达到这个下界

## 3. 相合性（Consistency）

### 定义

$$\hat{\theta}_n \xrightarrow{P} \theta \quad \text{或} \quad \hat{\theta}_n \xrightarrow{a.s.} \theta$$

即估计量依概率（或几乎必然）收敛到真实参数值。

### 与大数定律的联系

**辛钦弱大数定律**：
- iid 样本的均值估计量依概率收敛到期望
- $\bar{X}_n \xrightarrow{P} E[X]$
- 这是最常用的相合性证明工具

**切比雪夫弱大数定律**：
- 方差有界时也可推导相合性
- 一般很少用切比雪夫，因为 iid + 均值 = 期望 → 辛钦更常用

### 特殊情况：iid 但渐近无偏的估计量

方差的相合性证明技巧：
- 借助**依概率收敛的保四则运算和乘积性质**
- 顺序统计量相关：拆开利用概率直接算极限

## 三者的关系

```
              相合性 (大样本保证)
                  ↑
                  |
    无偏性 ←→ 有效性
   (期望正确)  (方差最小)
```

- **无偏性 + 有效性** → 小样本下的"好"估计量
- **相合性** → 大样本下的"好"估计量
- 一个理想的估计量应当同时具备：无偏、有效、相合
- 实践中往往需要权衡——MLE 可能有偏但渐近最优
