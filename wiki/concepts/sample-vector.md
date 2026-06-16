---
type: concept
title: "样本向量"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 统计学, 样本向量]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/sample-vector-geometric]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/sample-vector-geometric]]"
  - "applied_in::[[concepts/mean-as-projection]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/random-variable]]
- produced_by: [[sources/sample-vector-geometric]]
- applied_in: [[concepts/mean-as-projection]]

---

# 样本向量

## 核心定义

样本向量是将N次独立重复实验的观测值"打包"成高维空间中的一个点：

$$\mathbf{x} = [x_1, x_2, \ldots, x_N]^T \in \mathbb{R}^N$$

其中每个分量 $x_i$ 是一次实验的观测结果。

## 视角跃迁

从"上帝视角"到"凡人视角"的转变：

| 视角 | 信息量 | 描述 |
|------|--------|------|
| **上帝视角** | 知道真实分布 $P(X)$ | 掌握期望 $\mu$、方差 $\sigma^2$ 等总体参数 |
| **凡人视角** | 只有N个观测值 $\{x_1, x_2, \ldots, x_N\}$ | 需要从样本推断总体 |

统计学的核心任务就是：**从凡人视角尽可能还原上帝视角的信息**。

## 全1向量的两层意义

全1向量定义为：

$$\mathbf{1} = [1, 1, \ldots, 1]^T \in \mathbb{R}^N$$

### 第一层：代表"绝对平等"与"毫无波动"

全1向量的所有分量相等，表示一种"完全均匀"的状态：
- 每个时刻的贡献完全相同
- 没有任何变化或波动
- 是最简单的信号——常数信号

### 第二层：代表"最小二乘法的投影方向"

在最小二乘问题中，全1向量是"最佳常数逼近"的方向。当我们想找一个标量c来最好地逼近样本向量x时，实际上是在问：

> x在span(**1**)方向上的投影是多少？

## 平庸对角线

全1向量的张成空间：

$$\text{span}(\mathbf{1}) = \{c\mathbf{1} \mid c \in \mathbb{R}\}$$

这个一维子空间称为"平庸对角线"（trivial diagonal），因为它代表的是所有分量相等的向量集合。

几何意义：
- 这是 $\mathbb{R}^N$ 空间中的一条直线
- 直线上的每个点都代表一个"常数向量"
- 是最简单的子空间

## 几何直觉

样本向量的关键洞察：

1. **N次实验 = N维空间中的一个点**
   - 不再是一串数字，而是高维空间中的位置
   - 每个维度代表一次实验

2. **统计量 = 几何操作**
   - 均值 → 投影
   - 方差 → 距离
   - 相关系数 → 夹角

3. **从代数到几何的统一**
   - 代数公式变成几何关系
   - 统计性质变成空间结构

## 应用

样本向量的几何视角为以下概念提供了基础：
- [[concepts/mean-as-projection]] — 均值的几何本质
- [[concepts/centering-decoupling]] — 中心化与正交分解
- [[concepts/variance-geometric]] — 方差的几何意义
- [[concepts/degrees-of-freedom]] — 自由度与贝塞尔校正

---

*样本向量是统计学几何化的起点——把N次实验数据"打包"成高维空间中的一个点，为后续所有统计量的几何解释奠定基础。*