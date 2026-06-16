---
type: concept
title: "极大似然估计（MLE）"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 参数估计, MLE]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/point-estimation]]"
  - "depends_on::[[concepts/random-vector]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
  - "contrasts::[[concepts/moment-estimation]]"
  - "applied_in::[[concepts/maximum-likelihood]]"
---

## 🔗 关系链接

- depends_on: [[concepts/point-estimation]]
- depends_on: [[concepts/random-vector]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]
- contrasts: [[concepts/moment-estimation]]
- applied_in: [[concepts/maximum-likelihood]]

---

# 极大似然估计（MLE）

## 核心思想

**把样本（随机变量）放到向量里面，组成 $n$ 维随机向量。观测看作是在随机向量的分布中随机取值。**

## 关键洞察：最大似然原理

> **我们取到的一组观测值，大概率位于联合密度分布函数的最值点附近。**

直觉解释：
- 假设参数 $\theta$ 的真实值是 $\theta_0$
- 在 $\theta_0$ 下，观测到当前样本的概率（密度）最大
- 因为我们"恰好"观测到了这组数据，它应该是"最可能"发生的
- 所以使似然最大的参数值，就是对真实参数的最佳估计

这就是**最大似然原理**的核心。

## 似然函数的定义

给定样本 $X_1, X_2, \dots, X_n$，其联合密度函数为：

$$f(x_1, x_2, \dots, x_n; \theta)$$

**似然函数** $L(\theta)$ 就是把联合密度看作 $\theta$ 的函数：

$$L(\theta) = f(x_1, x_2, \dots, x_n; \theta)$$

对于 iid 样本：

$$L(\theta) = \prod_{i=1}^{n} f(x_i; \theta)$$

## 对数似然函数

由于连乘不方便计算（容易下溢），通常取对数：

$$\ell(\theta) = \ln L(\theta) = \sum_{i=1}^{n} \ln f(x_i; \theta)$$

MLE 的求解：

$$\hat{\theta}_{MLE} = \arg\max_{\theta} \ell(\theta)$$

通过对 $\ell(\theta)$ 求导并令导数为零来求解。

## MLE 的优良性质

| 性质 | 含义 |
|------|------|
| **一致性** | $\hat{\theta}_n \xrightarrow{P} \theta_0$（依概率收敛到真实值） |
| **渐近正态性** | $\sqrt{n}(\hat{\theta}_n - \theta_0) \xrightarrow{d} N(0, I(\theta_0)^{-1})$ |
| **渐近有效性** | 方差达到 Cramér-Rao 下界（大样本下最优） |
| **不变性** | 若 $\hat{\theta}$ 是 $\theta$ 的 MLE，则 $g(\hat{\theta})$ 是 $g(\theta)$ 的 MLE |

## 与矩估计的对比

| 维度 | 矩估计 | MLE |
|------|--------|-----|
| 原理 | 样本矩 ≈ 总体矩 | 最可能产生观测的参数 |
| 计算 | 解方程 | 优化似然函数 |
| 最优性 | 不保证最优 | 渐近最优 |
| 适用条件 | 矩存在 | 需要密度函数 |
| 小样本表现 | 可能更好 | 可能有偏 |

## 在机器学习中的应用

MLE 是机器学习中最核心的估计方法之一：
- **交叉熵损失** = 最大化训练集上的对数似然
- **高斯混合模型** 的参数估计
- **EM 算法** 的基础
