---
type: concept
title: "Transformer的√d缩放"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, Transformer, 注意力机制, √d]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/layer-normalization]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/central-limit-theorem]]"
  - "applied_in::[[concepts/scaled-dot-product-attention]]"
  - "applied_in::[[concepts/transformer]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/layer-normalization]]
- produced_by: [[sources/central-limit-theorem]]
- applied_in: [[concepts/scaled-dot-product-attention]] | [[concepts/transformer]]

---

# Transformer 的 √d 缩放

## 问题：点积方差随维度增长

在 Transformer 的注意力机制中，Query 和 Key 做点积来计算注意力分数：

$$\text{score}(q, k) = q \cdot k = \sum_{i=1}^d q_i k_i$$

假设 $q_i$ 和 $k_i$ 是独立的，均值为 0，方差为 1。

## 推导

单个分量的乘积：

$$\text{Var}(q_i k_i) = E[q_i^2 k_i^2] - (E[q_i k_i])^2 = E[q_i^2]E[k_i^2] - 0 = 1 \times 1 = 1$$

$d$ 个独立分量求和（利用方差可加性）：

$$\text{Var}(q \cdot k) = \sum_{i=1}^d \text{Var}(q_i k_i) = d$$

**点积的方差 = $d$**，标准差 = $\sqrt{d}$。

## 方差归一化链条

$$\text{LayerNorm}(\text{Var}=1) \xrightarrow{Q \cdot K} \text{Var}=d \xrightarrow{\div\sqrt{d}} \text{Var}=1$$

1. LayerNorm 保证每个 token 的特征方差 = 1
2. 点积后方差膨胀为 $d$（方差可加性）
3. 除以 $\sqrt{d}$ 把方差压回 1

## Softmax 饱和问题

不除以 $\sqrt{d}$ 时，当 $d$ 较大（如 64、128）：

- 点积值的典型范围是 $[-\sqrt{d}, \sqrt{d}]$，即 $[-8, 8]$ 或更大
- Softmax 输入值差异大时，输出接近 one-hot
- **梯度几乎为零**，训练停滞

## 除以 √d 的修正效果

除以 $\sqrt{d}$ 后：

- 方差回到 1，标准差 = 1
- 点积值典型范围 $[-3, 3]$
- Softmax 处于非饱和区域，梯度有效

## 与 CLT 的 √n 同源

**除以 $\sqrt{d}$ 和 CLT 中的 $\sqrt{n}$ 是同一个数学现象的两个实例。**

| 场景 | 变量 | 方差膨胀 | 归一化因子 |
|------|------|----------|-----------|
| CLT | $n$ 个 i.i.d. 随机变量之和 | $n\sigma^2$ | $\sqrt{n}$ |
| 注意力 | $d$ 个独立分量之积的和 | $d$ | $\sqrt{d}$ |

根源相同：**独立变量求和导致方差线性增长，需要除以 $\sqrt{n}$（或 $\sqrt{d}$）修正。**

这就是为什么 Transformer 论文中那个看似随意的 $\sqrt{d}$ 其实有着深刻的概率论根基——它和中心极限定理中的 $\sqrt{n}$ 同源，都是方差可加性的直接后果。
