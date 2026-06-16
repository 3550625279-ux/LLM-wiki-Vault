---
type: concept
title: "中心化：正交分解与信息解耦"
created: 2026-06-16
updated: 2026-06-16
tags: [线性代数, 统计学, 中心化, 正交分解]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/sample-vector-geometric]]"]
related:
  - "depends_on::[[concepts/mean-as-projection]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/sample-vector-geometric]]"
  - "applied_in::[[concepts/cosine-similarity]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/mean-as-projection]]
- produced_by: [[sources/sample-vector-geometric]]
- applied_in: [[concepts/cosine-similarity]]

---

# 中心化：正交分解与信息解耦

## 核心观点

中心化不是简单的"减去均值"，而是将样本向量正交分解为两个独立的信息分量。

## 正交分解

任意样本向量x可以唯一分解为：

$$\mathbf{x} = \underbrace{\bar{x}\mathbf{1}}_{\text{投影分量}} + \underbrace{\mathbf{x}_c}_{\text{残差分量}}$$

其中：
- $\bar{x}\mathbf{1}$ 是x在span(**1**)上的投影（直流量）
- $\mathbf{x}_c = \mathbf{x} - \bar{x}\mathbf{1}$ 是中心化向量（交流量）

这两个分量正交：$\bar{x}\mathbf{1} \perp \mathbf{x}_c$

## 中心化向量的正交性

中心化向量必然垂直于全1空间：

$$\mathbf{x}_c \cdot \mathbf{1} = \sum_{i=1}^N (x_i - \bar{x}) = \sum x_i - N\bar{x} = 0$$

几何意义：
- 中心化操作将x投影到span(**1**)的正交补空间
- 这个正交补空间是N-1维的
- 中心化向量在这个子空间中

## 信号处理类比

| 信号处理 | 统计学 | 含义 |
|----------|--------|------|
| 直流分量(DC) | 均值 $\bar{x}\mathbf{1}$ | 信号的平均水平 |
| 交流分量(AC) | 中心化向量 $\mathbf{x}_c$ | 信号的波动部分 |
| 去除DC偏置 | 中心化操作 | 关注变化而非绝对值 |

中心化 = 去掉直流分量，只保留交流分量

## 强化学习类比

Q函数的分解与中心化有相同的结构：

$$Q(s,a) = \underbrace{V(s)}_{\text{状态价值}} + \underbrace{A(s,a)}_{\text{优势函数}}$$

| 分解 | 含义 |
|------|------|
| $V(s)$ | 状态s的"平均水平"（直流量） |
| $A(s,a)$ | 动作a相对于平均水平的优势（交流量） |

两者都是将一个量分解为"平均水平" + "偏离部分"。

## 光照不变性例子

这是中心化最重要的应用之一——消除虚假相关。

### 问题场景

两张图片的像素向量：
- 图片A：$\mathbf{a} = [100, 101, 99, 100, 101]^T$（正常光照）
- 图片B：$\mathbf{b} = [200, 202, 198, 200, 202]^T$（强光照射，像素值翻倍）

### 不中心化时

余弦相似度：

$$\cos(\theta) = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\| \|\mathbf{b}\|} \approx 0.99995$$

**结论：几乎完全相似！**

但这是虚假相关——两张图的内容相同，只是光照不同。

### 中心化后

$$\mathbf{a}_c = [0, 1, -1, 0, 1]^T$$
$$\mathbf{b}_c = [0, 2, -2, 0, 2]^T$$

中心化后的余弦相似度：

$$\cos(\theta_c) = \frac{\mathbf{a}_c \cdot \mathbf{b}_c}{\|\mathbf{a}_c\| \|\mathbf{b}_c\|} = 1.0$$

**仍然相似，但现在是正确的相似——因为内容确实相同。**

### 关键洞察

- 中心化消除了"亮度"这个虚假因素
- 保留了"结构"这个真实信息
- 类似于：比较两个人的身高差异时，应该看身高差，而不是绝对身高

## 信息解耦

中心化的本质是**信息解耦**：

| 分量 | 包含的信息 | 丢弃的信息 |
|------|------------|------------|
| 均值 $\bar{x}$ | 整体水平、绝对大小 | 内部结构、变化模式 |
| 中心化向量 $\mathbf{x}_c$ | 内部结构、变化模式 | 整体水平、绝对大小 |

这种解耦使得：
1. 比较不同量级的对象成为可能
2. 关注相对变化而非绝对值
3. 消除系统性偏差

## 与其他概念的联系

- 中心化依赖 [[concepts/mean-as-projection]] 的投影几何
- 中心化是 [[concepts/variance-geometric]] 的前提（方差需要中心化向量）
- 中心化用于定义 [[concepts/cosine-similarity]] 的改进版本

---

*中心化 = 正交分解 = 信息解耦。去掉直流量，保留交流量，关注变化而非绝对值。*