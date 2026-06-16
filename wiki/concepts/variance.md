---
type: concept
title: "方差"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 统计, 方差, 基础]
status: seed
complexity: basic
domain: Foundations
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "depends_on::[[concepts/moment]]"
  - "extended_by::[[concepts/covariance]]"
  - "belongs_to::[[domains/Foundations]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/random-variable]] | [[concepts/moment]]
- extended_by: [[concepts/covariance]]

---

# 方差

## 定义

$$\text{Var}(X) = \mathbb{E}[(X - \mu)^2] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2$$

方差衡量随机变量偏离均值的程度，是二阶中心矩。

## 性质

- $\text{Var}(aX + b) = a^2 \text{Var}(X)$（线性变换）
- 独立变量: $\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$（**方差可加性** → 见 [[concepts/sqrt-n-origin]]）
- 标准差 $\sigma = \sqrt{\text{Var}(X)}$（与原始数据同量纲）

## 在深度学习中的意义

- **权重初始化**: Xavier/Kaiming 初始化的核心就是控制每层输出的方差
- **BatchNorm / LayerNorm**: 都是在归一化方差
- **Transformer √d**: 点积方差随维度增长，需要除以 $\sqrt{d}$（见 [[concepts/transformer-sqrt-d]]）
