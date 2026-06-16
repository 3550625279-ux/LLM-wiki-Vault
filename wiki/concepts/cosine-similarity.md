---
type: concept
title: "余弦相似度"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 相似度, 向量, 基础]
status: seed
complexity: basic
domain: Foundations
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/covariance]]"
  - "belongs_to::[[domains/Foundations]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/covariance]]

---

# 余弦相似度

## 定义

$$\cos(\mathbf{a}, \mathbf{b}) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \cdot \|\mathbf{b}\|} = \frac{\sum_i a_i b_i}{\sqrt{\sum_i a_i^2} \cdot \sqrt{\sum_i b_i^2}}$$

衡量两个向量方向的相似程度，值域 $[-1, 1]$。

## 与相关系数的关系

皮尔逊相关系数 = **中心化后的余弦相似度**：

$$\rho(X, Y) = \cos(\mathbf{X} - \bar{X}, \mathbf{Y} - \bar{Y})$$

## 在深度学习中的应用

- **注意力机制**: 缩放点积注意力 $\frac{QK^T}{\sqrt{d}}$ 本质是归一化后的余弦相似度
- **对比学习**: 正样本对余弦相似度最大化，负样本对最小化
- **嵌入检索**: 语义搜索用余弦相似度排序
