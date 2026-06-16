---
type: concept
title: "随机向量"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 随机向量, 多维随机变量]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/random-variable-random-vector]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/random-variable-random-vector]]"
  - "applied_in::[[concepts/batch-normalization]]"
---

## 🔗 关系链接

- depends_on: [[concepts/random-variable]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/random-variable-random-vector]]
- applied_in: [[concepts/batch-normalization]]

---

# 随机向量

## 核心定义

**随机向量**是由多个随机变量组成的向量函数：

```
V(ω) = [X₁(ω), X₂(ω), ..., Xₖ(ω)]ᵀ
```

其中 X₁, X₂, ..., Xₖ 都是定义在同一个样本空间 Ω 上的随机变量。

### 直觉理解

> **从不同角度给同一物体拍照。**

- 同一个随机事件 ω（同一个物体）
- 多个随机变量 X₁, X₂, ..., Xₖ（不同角度的相机）
- 每个变量给出一个数值（每张照片给出一个视角的像素）
- 组合起来就是随机向量（多视角的完整描述）

## 关键辨析：随机向量 vs 概率分布向量

这两个概念容易混淆，但本质完全不同：

| | 随机向量 | 概率分布向量 (PMF) |
|---|---|---|
| **定义** | 多个函数作用于同一个 ω | 一个随机变量所有可能取值的概率 |
| **输入** | 同一个 ω | 不需要输入（已统计完毕） |
| **输出** | 实数向量 [x₁, x₂, ..., xₖ] | 概率向量 [p₁, p₂, ..., pₖ]，满足 Σpᵢ = 1 |
| **随机性** | 输出依赖 ω，有随机性 | 本身是确定的概率值 |
| **示例** | [身高, 体重, 年龄] | Softmax 输出 [0.1, 0.7, 0.2] |

### Softmax 输出是什么？

**Softmax 输出是概率分布向量，不是随机向量。**

- Softmax 输出 [0.1, 0.7, 0.2] 表示 P(y=0)=0.1, P(y=1)=0.7, P(y=2)=0.2
- 这是一个随机变量（类别标签 Y）的概率质量函数 PMF
- 它不是多个随机变量的组合

如果把 Softmax 输出看作随机向量，那意味着每个分量都是一个随机变量——但实际上它们共享同一个随机事件 ω（同一个输入样本），且满足 Σpᵢ = 1 的约束。

## 联合分布

随机向量的核心概念是**联合分布**：

```
F(x₁, x₂, ..., xₖ) = P(X₁ ≤ x₁, X₂ ≤ x₂, ..., Xₖ ≤ xₖ)
```

联合分布完整描述了所有分量之间的依赖关系。

### 边缘分布

从联合分布中可以提取任意子集的**边缘分布**：

```
P(X₁ ≤ x₁) = lim_{x₂→∞, ..., xₖ→∞} F(x₁, x₂, ..., xₖ)
```

直觉：把其他维度"积分掉"，只保留感兴趣的维度。

## AI 应用场景

### 特征向量

机器学习中的特征向量就是一个随机向量：
- 每个特征 Xᵢ 是一个随机变量
- 样本 x = [x₁, x₂, ..., xₖ]ᵀ 是随机向量 V(ω) 的一个实现
- 训练数据就是从联合分布中采样的结果

### Batch Normalization

BatchNorm 的核心操作：
1. 对每个特征维度（随机变量 Xᵢ）独立计算均值和方差
2. 归一化：X̃ᵢ = (Xᵢ - μᵢ) / σᵢ

这本质上是在对随机向量的每个分量做独立的标准化。

---

*创建: 2026-06-16 | 概率论基础系列*
