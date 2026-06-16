---
type: concept
title: "奇异值分解 (SVD)"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 矩阵分解, SVD, 低秩近似]
status: seed
complexity: intermediate
domain: Foundations
sources: ["综合来源"]
related:
  - "extended_by::[[concepts/lora]]"
  - "belongs_to::[[domains/Foundations]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- extended_by: [[concepts/lora]]

---

# 奇异值分解 (SVD)

## 定义

任意矩阵 $\mathbf{A} \in \mathbb{R}^{m \times n}$ 可分解为：

$$\mathbf{A} = \mathbf{U} \boldsymbol{\Sigma} \mathbf{V}^\top$$

- $\mathbf{U} \in \mathbb{R}^{m \times m}$: 左奇异向量（正交矩阵）
- $\boldsymbol{\Sigma} \in \mathbb{R}^{m \times n}$: 奇异值（对角矩阵，非负递减）
- $\mathbf{V} \in \mathbb{R}^{n \times n}$: 右奇异向量（正交矩阵）

## 低秩近似

保留最大的 $r$ 个奇异值：

$$\mathbf{A} \approx \mathbf{U}_r \boldsymbol{\Sigma}_r \mathbf{V}_r^\top = \mathbf{B}\mathbf{C}$$

其中 $\mathbf{B} = \mathbf{U}_r \boldsymbol{\Sigma}_r \in \mathbb{R}^{m \times r}$，$\mathbf{C} = \mathbf{V}_r^\top \in \mathbb{R}^{r \times n}$。

**这就是 LoRA 的数学基础**：将大矩阵 $\mathbf{A} \in \mathbb{R}^{d \times d}$ 分解为两个低秩矩阵 $\mathbf{B} \in \mathbb{R}^{d \times r}$ 和 $\mathbf{C} \in \mathbb{R}^{r \times d}$，参数量从 $d^2$ 降到 $2dr$。

## Eckart-Young 定理

秩 $r$ 的最佳近似（Frobenius 范数意义下）就是截断 SVD。
