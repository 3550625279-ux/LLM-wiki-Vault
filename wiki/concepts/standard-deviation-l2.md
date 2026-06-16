---
type: concept
title: "标准差与L2范数"
created: 2026-06-16
updated: 2026-06-16
tags: [统计学, 标准差, L2范数, MAD]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/variance-geometric]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/central-limit-theorem]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/variance-geometric]]
- produced_by: [[sources/central-limit-theorem]]

---

# 标准差与 L2 范数

## 标准差与 L2 范数的关系

给定数据 $x_1, x_2, \ldots, x_n$，中心化后的向量为 $x_c = (x_1 - \bar{x}, x_2 - \bar{x}, \ldots, x_n - \bar{x})$。

L2 范数：
$$\|x_c\|_2 = \sqrt{\sum_{i=1}^n (x_i - \bar{x})^2}$$

样本标准差：
$$\sigma = \sqrt{\frac{1}{n}\sum_{i=1}^n (x_i - \bar{x})^2}$$

两者的关系：
$$\sigma = \frac{\|x_c\|_2}{\sqrt{n}}$$

标准差 = 中心化向量的 L2 范数 ÷ $\sqrt{n}$。标准差就是"归一化后的 L2 范数"。

## 为什么"波动"是标准差而不是方差

| 度量 | 单位 | 可解释性 |
|------|------|----------|
| 方差 $\sigma^2$ | 原数据单位的平方 | 不直观（"平方米"） |
| 标准差 $\sigma$ | 与原数据一致 | 直观（"米"） |

标准差的单位与原数据一致，可以直接与数据值比较。说"身高标准差 5cm"比"身高方差 25cm²"有意义得多。

## 为什么"波动"是标准差而不是平均绝对偏差（MAD）

平均绝对偏差：$\text{MAD} = \frac{1}{n}\sum_{i=1}^n |x_i - \bar{x}|$

MAD 也能度量波动，且单位与原数据一致。但标准差有一个 MAD 不具备的关键性质：

**方差可加性**：$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y)$（独立时）

绝对偏差没有这个性质。正是方差可加性使得 $\sqrt{n}$ 出现在 CLT 中，使得标准差成为概率论的核心度量。

标准差统治统计学不是因为"更好"，而是因为它与方差可加性配合，形成了完整的数学链条。

## 完整链条

$$\|x_c\|_2 \xrightarrow{\div\sqrt{n}} \sigma \xrightarrow{\text{方差可加性}} \sigma\sqrt{n} \xrightarrow{\text{CLT标准化}} Z_n \xrightarrow{n\to\infty} N(0,1)$$

从 L2 范数出发，经过归一化得到标准差，利用方差可加性推导出 $\sqrt{n}$ 缩放，最终通过 CLT 标准化收敛到标准正态。

## L2 范数在概率论中的核心地位

L2 范数（而非 L1 或 L∞）占据概率论核心地位的原因：

1. **方差 = L2 距离的平方**：$\text{Var}(X) = E[(X - \mu)^2]$ 是 L2 度量
2. **正交分解**：L2 空间有内积结构，支持投影和正交分解
3. **CLT 依赖方差可加性**：而方差可加性是 L2 结构的直接推论
4. **高斯分布是 L2 的极值分布**：最大熵原理下，给定 L2 约束的分布是高斯分布
