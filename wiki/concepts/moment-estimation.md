---
type: concept
title: "矩估计"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 参数估计, 矩估计]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/point-estimation]]"
  - "depends_on::[[concepts/moment]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
  - "contrasts::[[concepts/mle]]"
---

## 🔗 关系链接

- depends_on: [[concepts/point-estimation]]
- depends_on: [[concepts/moment]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]
- contrasts: [[concepts/mle]]

---

# 矩估计

## 核心思想

**用样本矩估计总体矩，进而估计分布参数。**

这是最直观的参数估计方法：既然样本来自总体，那么样本的统计特征应该近似于总体的统计特征。

## 为什么可以估计的本质：频率稳定于概率

矩估计的理论根基在于：

> **频率稳定于概率。**

具体理解：
- **理想状态**：把分布的总体枚举出来
- 每种情况的样本数目 / 总样本数目 × 随机变量的函数
- 这正好可以用**离散的样本**进行计算

换言之，样本矩是总体矩的"天然近似"，因为样本频率会随样本量增大而趋近于总体概率。

## 矩估计的步骤

### 一阶矩估计

用**一阶样本矩**（样本均值）估计总体均值：

$$\bar{X} = \frac{1}{n}\sum_{i=1}^{n} X_i \approx E[X] = \mu$$

### 二阶矩估计

用**二阶样本矩**估计总体方差：

$$\frac{1}{n}\sum_{i=1}^{n} X_i^2 \approx E[X^2]$$

然后通过 $\text{Var}(X) = E[X^2] - (E[X])^2$ 求得方差。

### 一般步骤

1. 写出总体的前 $k$ 阶矩 $E[X^j]$（含未知参数 $\theta_1, \dots, \theta_k$）
2. 用样本矩 $\frac{1}{n}\sum X_i^j$ 替换总体矩
3. 解方程组，得到参数的估计值

## 与 MLE 的对比

| 维度 | 矩估计 | 极大似然估计（MLE） |
|------|--------|---------------------|
| 直觉 | 样本矩 ≈ 总体矩 | 最可能产生观测数据的参数 |
| 计算 | 解方程，通常简单 | 需要优化似然函数 |
| 最优性 | 不一定最优 | 渐近最优（一致性、渐近正态性） |
| 适用性 | 矩存在即可 | 需要分布的密度函数 |
| 无偏性 | 通常无偏 | 可能有偏 |

## 示例

**估计正态分布 $N(\mu, \sigma^2)$ 的参数：**

- 一阶矩方程：$\bar{X} = \mu$ → $\hat{\mu} = \bar{X}$
- 二阶矩方程：$\frac{1}{n}\sum X_i^2 = \mu^2 + \sigma^2$ → $\hat{\sigma}^2 = \frac{1}{n}\sum(X_i - \bar{X})^2$

注意：矩估计得到的方差估计量是 $\frac{1}{n}$ 而非 $\frac{1}{n-1}$，是有偏的。
