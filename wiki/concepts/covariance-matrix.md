---
type: concept
title: "协方差矩阵"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 线性代数, 协方差, 矩阵]
status: seed
complexity: intermediate
domain: Foundations
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/covariance]]"
  - "depends_on::[[concepts/random-vector]]"
  - "belongs_to::[[domains/Foundations]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/covariance]] | [[concepts/random-vector]]

---

# 协方差矩阵

## 定义

随机向量 $\mathbf{X} = (X_1, \ldots, X_n)^\top$ 的协方差矩阵：

$$\boldsymbol{\Sigma} = \text{Cov}(\mathbf{X}) = \mathbb{E}[(\mathbf{X} - \boldsymbol{\mu})(\mathbf{X} - \boldsymbol{\mu})^\top]$$

其中 $\Sigma_{ij} = \text{Cov}(X_i, X_j)$。

## 性质

- **对称**: $\Sigma_{ij} = \Sigma_{ji}$
- **半正定**: $\mathbf{a}^\top \boldsymbol{\Sigma} \mathbf{a} \geq 0$
- **对角线**: $\Sigma_{ii} = \text{Var}(X_i)$

## 在深度学习中的应用

- **BatchNorm**: 计算 batch 内的均值和方差（协方差矩阵的对角线）
- **PCA/SVD**: 对协方差矩阵做特征分解
- **多元高斯**: $p(\mathbf{x}) = \mathcal{N}(\boldsymbol{\mu}, \boldsymbol{\Sigma})$
- **白化**: 将数据变换为 $\Sigma = I$（去相关 + 归一化）
