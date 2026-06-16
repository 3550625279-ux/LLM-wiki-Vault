---
type: source
title: "样本向量的几何视角"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 统计学, 样本向量, 几何视角]
status: developing
complexity: intermediate
domain: Foundations
sources: []
related:
  - "belongs_to::[[domains/Foundations]]"
  - "spawns::[[concepts/sample-vector]]"
  - "spawns::[[concepts/mean-as-projection]]"
  - "spawns::[[concepts/centering-decoupling]]"
  - "spawns::[[concepts/variance-geometric]]"
  - "spawns::[[concepts/degrees-of-freedom]]"
  - "spawns::[[concepts/sgd-noise-generalization]]"
raw_path: ""
thumbnail: ""
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- spawns: [[concepts/sample-vector]] | [[concepts/mean-as-projection]] | [[concepts/centering-decoupling]] | [[concepts/variance-geometric]] | [[concepts/degrees-of-freedom]] | [[concepts/sgd-noise-generalization]]

---

## 资料概要

本文件是四篇系列笔记的第二篇。回答核心问题：当我们只有N次实验的有限数据时，如何用线性代数的第一性原理重构统计学的全部概念？这是从"上帝视角（知道真实分布）"到"凡人视角（只有N个观测值）"的视角跃迁。

## 核心逻辑链

```
样本向量x ∈ Rᴺ → 正交投影 → 均值x̄ → 正交分解 → 中心化 → 方差/协方差/相关系数 → 自由度N-1 → 大数定律 → SGD
```

## 六节内容摘要

| 节 | 主题 | 核心概念 |
|----|------|---------|
| 1 | 样本向量空间 | Rᴺ中的样本向量, 全1向量**1**的几何意义 |
| 2 | 均值=正交投影 | L(c)=\|\|x-c**1**\|\|²的最小二乘解 = x̄ |
| 3 | 中心化 | 正交分解: x = x̄**1** + x_c, 信息解耦 |
| 4 | 统计几何复盘 | 方差=长度², 协方差=内积, 相关系数=cos(θ), 勾股定理 |
| 5 | 自由度 | 正交约束砍掉一个维度, N-1的几何根源 |
| 6 | 大数定律 | Rᴺ点积→无穷维积分, SGD蒙特卡洛近似 |

## 关键洞察

- **均值不是人为规定的算术平均**，而是高维几何中正交投影的最小二乘最优解
- **方差=中心化向量的L2范数平方/N**，不是随意定义的分散度量
- **独立方差可加=勾股定理**，正交性直接后果
- **除以N-1不是教条**，而是自由度的几何体现
- **大数定律**是从Rᴺ点积到无穷维积分的收敛桥梁

## 诞生的节点

- [[concepts/sample-vector]] — 样本向量
- [[concepts/mean-as-projection]] — 均值的几何本质
- [[concepts/centering-decoupling]] — 中心化与信息解耦
- [[concepts/variance-geometric]] — 方差的几何意义
- [[concepts/degrees-of-freedom]] — 自由度与贝塞尔校正
- [[concepts/sgd-noise-generalization]] — SGD噪声与泛化
