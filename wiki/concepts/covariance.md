---
type: concept
title: "协方差"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 协方差, 相关系数]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/random-variable-random-vector]]", "[[sources/sample-vector-geometric]]"]
related:
  - "depends_on::[[concepts/random-vector]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/random-variable-random-vector]]"
  - "extends::[[concepts/variance]]"
  - "applied_in::[[concepts/covariance-matrix]]"
---

## 🔗 关系链接

- depends_on: [[concepts/random-vector]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/random-variable-random-vector]]
- extends: [[concepts/variance]]
- applied_in: [[concepts/covariance-matrix]]

---

# 协方差

## 核心定义

**协方差**衡量两个随机变量 X 和 Y 之间的线性关系：

```
Cov(X, Y) = E[(X − E[X])(Y − E[Y])]
```

### 公式拆解

分两步理解：

1. **中心化**：X̃ = X − E[X]，Ỹ = Y − E[Y]（减去均值，让变量以零为中心）
2. **乘积的期望**：E[X̃ · Ỹ]（两个中心化变量的"平均乘积"）

### 乘积符号规律

X̃ 和 Ỹ 的符号组合决定了协方差的正负：

| X̃ 的符号 | Ỹ 的符号 | 乘积 X̃Ỹ | 含义 |
|---|---|---|---|
| + | + | + | X 大时 Y 也大（正相关） |
| − | − | + | X 小时 Y 也小（正相关） |
| + | − | − | X 大时 Y 小（负相关） |
| − | + | − | X 小时 Y 大（负相关） |

**正协方差**：X 和 Y 倾向于同向变化
**负协方差**：X 和 Y 倾向于反向变化
**零协方差**：无线性相关（但可能有非线性关系）

## 几何意义：相关系数

**相关系数**将协方差标准化到 [-1, 1]：

```
ρ(X, Y) = Cov(X, Y) / (σ_X · σ_Y)
```

几何解释：**ρ = cos(θ)**，即两个随机变量（视为向量）之间夹角的余弦。

- ρ = 1：完全正相关（θ = 0°，同向）
- ρ = -1：完全负相关（θ = 180°，反向）
- ρ = 0：不相关（θ = 90°，正交）

### 向量视角

把随机变量 X 和 Y 看作向量空间中的向量：
- Cov(X, Y) = ⟨X̃, Ỹ⟩（内积）
- Var(X) = ⟨X̃, X̃⟩ = ||X̃||²（模的平方）
- ρ = cos(θ) = ⟨X̃, Ỹ⟩ / (||X̃|| · ||Ỹ||)

## 两种视角：理论 vs 数据

| | 理论视角（上帝视角） | 数据视角（凡人视角） |
|---|---|---|
| **已知** | 真实分布 P(X, Y) | N 个样本 (xᵢ, yᵢ) |
| **计算** | E[(X − μ_X)(Y − μ_Y)] | (1/N) Σ(xᵢ − x̄)(yᵢ − ȳ) |
| **性质** | 精确值 | 估计值（有抽样误差） |
| **称呼** | 总体协方差 | 样本协方差 |

在实际 ML 中，我们总是用数据视角——用有限样本估计理论量。

## AI 应用场景

### 特征选择

高协方差的特征对可能是冗余的：
- 如果 Cov(X₁, X₂) ≈ σ_X₁ · σ_X₂（ρ ≈ 1），两个特征携带几乎相同的信息
- 可以去掉一个，降低维度

### 协方差矩阵

多个随机变量两两之间的协方差构成**协方差矩阵** Σ：
- Σᵢⱼ = Cov(Xᵢ, Xⱼ)
- 对角线：Var(Xᵢ)
- 正定对称矩阵

这是 PCA、多元高斯分布、白化等技术的基础。

### Batch Normalization 的协方差效应

BatchNorm 归一化每个特征到零均值单位方差，但**不改变特征间的相关性**——协方差矩阵的结构被保留。

---

*创建: 2026-06-16 | 概率论基础系列*
