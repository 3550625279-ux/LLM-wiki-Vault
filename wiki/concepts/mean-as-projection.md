---
type: concept
title: "均值的几何本质：正交投影"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 统计学, 均值, 正交投影]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/sample-vector-geometric]]"]
related:
  - "depends_on::[[concepts/sample-vector]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/sample-vector-geometric]]"
  - "applied_in::[[concepts/centering-decoupling]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/sample-vector]]
- produced_by: [[sources/sample-vector-geometric]]
- applied_in: [[concepts/centering-decoupling]]

---

# 均值的几何本质：正交投影

## 核心观点

**均值不是人为规定的算术约定，而是高维几何中必然得出的最小二乘极值解。**

当我们计算 $\bar{x} = \frac{1}{N}\sum_{i=1}^N x_i$ 时，实际上是在做正交投影。

## 问题形式化

给定样本向量 $\mathbf{x} = [x_1, x_2, \ldots, x_N]^T$，找一个标量c，使得损失函数最小：

$$L(c) = \|\mathbf{x} - c\mathbf{1}\|^2 = \sum_{i=1}^N (x_i - c)^2$$

这问的是：**用一个常数c来最好地近似所有观测值，应该取什么值？**

## 推导

对L(c)求导并令其为零：

$$\frac{dL}{dc} = -2\sum_{i=1}^N (x_i - c) = 0$$

$$\sum_{i=1}^N x_i - Nc = 0$$

$$c = \frac{1}{N}\sum_{i=1}^N x_i = \bar{x}$$

**结论：最小二乘最优的常数恰好是算术平均值。**

## 几何统一

从正交投影的角度理解：

$$\text{proj}_{\mathbf{1}}(\mathbf{x}) = \frac{\mathbf{x} \cdot \mathbf{1}}{\mathbf{1} \cdot \mathbf{1}} \cdot \mathbf{1} = \frac{\sum x_i}{N} \cdot \mathbf{1} = \bar{x}\mathbf{1}$$

均值 $\bar{x}$ 就是投影的坐标系数。

几何意义：
- $\bar{x}\mathbf{1}$ 是x在span(**1**)上的投影向量
- $\bar{x}$ 是这个投影的坐标
- 投影操作自动完成"最小二乘最优常数逼近"

## 为什么是正交投影？

投影的残差向量：

$$\mathbf{x} - \bar{x}\mathbf{1} \perp \text{span}(\mathbf{1})$$

验证正交性：

$$(\mathbf{x} - \bar{x}\mathbf{1}) \cdot \mathbf{1} = \sum(x_i - \bar{x}) = \sum x_i - N\bar{x} = 0$$

残差确实垂直于全1空间，这是正交投影的定义。

## 信息压缩的必然结果

均值作为正交投影的深层意义：

1. **压缩必然丢信息**
   - 从N维压缩到1维，不可能保留所有信息
   - 必须选择保留哪些信息

2. **最小二乘 = 最优压缩**
   - 在所有可能的常数逼近中，均值使误差最小
   - 是信息论意义上的最优压缩

3. **几何必然性**
   - 不是人为选择，而是空间结构的自然结果
   - 任何人在做"最优常数逼近"时都会得到均值

## 与其他概念的联系

- 均值是 [[concepts/sample-vector]] 在平庸对角线上的投影坐标
- 均值用于定义 [[concepts/centering-decoupling]]（中心化操作）
- 均值的几何解释为 [[concepts/variance-geometric]] 奠定基础

---

*均值是压缩信息时必然得出的最小二乘最优解——不是人为规定的算术约定，而是高维几何的自然结果。*