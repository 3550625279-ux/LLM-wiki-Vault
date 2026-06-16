---
type: concept
title: "方差的几何意义"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 统计学, 方差, L2范数]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/sample-vector-geometric]]", "[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/centering-decoupling]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/sample-vector-geometric]]"
  - "extends::[[concepts/moment]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/centering-decoupling]]
- produced_by: [[sources/sample-vector-geometric]]
- extends: [[concepts/moment]]

---

# 方差的几何意义

## 核心观点

方差不是人为定义的"离散程度度量"，而是中心化向量的物理能量。

## 样本方差的几何形式

样本方差的定义：

$$\text{Var}(X) = \frac{1}{N}\sum_{i=1}^N (x_i - \bar{x})^2$$

几何重写：

$$\text{Var}(X) = \frac{1}{N}\|\mathbf{x}_c\|^2$$

其中 $\mathbf{x}_c = \mathbf{x} - \bar{x}\mathbf{1}$ 是中心化向量。

**方差 = 中心化向量长度的平方 / N**

## 物理直觉：能量

方差是中心化向量的"物理能量"：

| 物理量 | 统计学对应 | 含义 |
|--------|------------|------|
| 质量 | 1/N（每个点的权重） | 均匀分布 |
| 速度 | $x_i - \bar{x}$（偏离均值的程度） | 波动大小 |
| 动能 | $\frac{1}{N}(x_i - \bar{x})^2$ | 单点能量 |
| 总动能 | $\frac{1}{N}\|\mathbf{x}_c\|^2$ | 方差 |

方差衡量的是数据的"总波动能量"。

## 转动惯量类比

方差与转动惯量有相同的数学结构：

| 物理量 | 公式 | 含义 |
|--------|------|------|
| 转动惯量 | $I = \sum m_i r_i^2$ | 物体绕轴转动的惯性 |
| 方差 | $\text{Var} = \frac{1}{N}\sum (x_i - \bar{x})^2$ | 数据绕均值的离散程度 |

- $m_i$ → 1/N（质量/权重）
- $r_i$ → $x_i - \bar{x}$（到轴心的距离）

**方差是统计学中的转动惯量。**

## 协方差的几何意义

两个变量X和Y的样本协方差：

$$\text{Cov}(X,Y) = \frac{1}{N}\sum_{i=1}^N (x_i - \bar{x})(y_i - \bar{y})$$

几何重写：

$$\text{Cov}(X,Y) = \frac{1}{N}(\mathbf{x}_c \cdot \mathbf{y}_c)$$

**协方差 = 两个中心化向量的内积（平均后）**

## 相关系数的几何意义

皮尔逊相关系数：

$$r = \frac{\text{Cov}(X,Y)}{\sqrt{\text{Var}(X)\text{Var}(Y)}} = \frac{\mathbf{x}_c \cdot \mathbf{y}_c}{\|\mathbf{x}_c\| \|\mathbf{y}_c\|} = \cos(\theta)$$

**相关系数 = 中心化向量夹角的余弦**

| 相关系数 | 夹角 | 含义 |
|----------|------|------|
| r = 1 | θ = 0° | 完全正相关 |
| r = 0 | θ = 90° | 线性无关 |
| r = -1 | θ = 180° | 完全负相关 |

## 独立方差可加 = 勾股定理

若两个中心化向量正交：$\mathbf{x}_c \perp \mathbf{y}_c$

则：

$$\text{Var}(X+Y) = \text{Var}(X) + \text{Var}(Y)$$

证明：

$$\|\mathbf{x}_c + \mathbf{y}_c\|^2 = \|\mathbf{x}_c\|^2 + \|\mathbf{y}_c\|^2 + 2\mathbf{x}_c \cdot \mathbf{y}_c$$

当 $\mathbf{x}_c \perp \mathbf{y}_c$ 时，$\mathbf{x}_c \cdot \mathbf{y}_c = 0$，所以：

$$\|\mathbf{x}_c + \mathbf{y}_c\|^2 = \|\mathbf{x}_c\|^2 + \|\mathbf{y}_c\|^2$$

除以N即得方差可加性。

**独立变量方差可加 = 勾股定理在统计学中的体现**

## 几何统一

| 统计概念 | 几何意义 |
|----------|----------|
| 方差 | 向量长度的平方 |
| 协方差 | 向量内积 |
| 相关系数 | 夹角余弦 |
| 独立方差可加 | 勾股定理 |

## 与其他概念的联系

- 方差依赖 [[concepts/centering-decoupling]] 的正交分解
- 方差扩展了 [[concepts/moment]] 的概念（二阶中心矩）
- 方差的几何解释为 [[concepts/degrees-of-freedom]] 奠定基础

---

*方差是中心化向量的物理能量——不是人为定义，而是向量长度的自然度量。*