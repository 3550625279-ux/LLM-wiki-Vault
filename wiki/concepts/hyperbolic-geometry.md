---
type: concept
title: "双曲几何基础"
created: 2026-06-13
updated: 2026-06-13
tags: [双曲几何, Lorentz模型, Poincaré圆盘, 非欧几何, 层次表示]
status: seed
complexity: advanced
domain: Foundations
sources: ["Nickel & Kiela 2017", "Nickel & Kiela 2018"]
related:
  - "belongs_to::[[domains/Foundations]]"
  - "applied_in::[[concepts/hyplora]]"
  - "applied_in::[[concepts/hyperbolic-geometry-llm]]"
  - "produced_by::[[sources/hyplora-neurips2025]]"
thumbnail: ""
---

# 双曲几何基础

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- applied_in: [[concepts/hyplora]] | [[concepts/hyperbolic-geometry-llm]]
- produced_by: [[sources/hyplora-neurips2025]]

---

> **一句话**：具有恒定负曲率的非欧几何，体积呈指数增长，天然适合表示树状层次结构。

---

## 为什么需要双曲几何

| 空间类型 | 体积增长 | 适合表示 |
|----------|----------|----------|
| 欧几里得 | 多项式 V(r) ∝ rⁿ | 平坦结构 |
| 球面 | 先增后减 | 环状/闭合结构 |
| **双曲** | **指数 V(r) ∝ eʳ** | **树状层次** |

语言的层次结构（"动物"→"猫"→"暹罗猫"）在欧氏空间中会拥挤失真，在双曲空间中则有充足空间分离。

---

## Lorentz 双曲面模型

n 维 Lorentz 双曲面，曲率 -1/K（K > 0）：

```
L_K^n = {x ∈ ℝ^(n+1) : ⟨x,x⟩_L = -K,  x₀ > 0}
```

Lorentz 内积：⟨x,y⟩_L = -x₀y₀ + Σᵢ xᵢyᵢ

- **x₀**（时间维度）：始终为正
- **x₁...xₙ**（空间维度）：编码语义信息
- **曲率 K**：控制弯曲程度，K 越小越弯曲

---

## 关键操作

### 指数映射 Π_K exp
将切空间中的向量"推"到双曲面上。

### 对数映射 Π_K log
将双曲面上的点"拉"回切空间。

### 性质
- 两者互逆：log(exp(x)) = x
- **抵消效应**：连续应用 exp→log 会完全抵消，这是传统双曲神经网络的关键问题

---

## Poincaré 圆盘模型

双曲空间的另一种等距表示：

```
圆面积: A(r) = 2π(cosh(r)-1) ∼ eʳ  (r→∞)
圆周长: C(r) = 2π sinh(r) ∼ eʳ     (r→∞)
```

指数体积增长 = 树状结构的天然容器。

---

## δ-双曲性

Gromov 四点条件度量空间的"树程度"：

```
[a,c]_w ≥ min([a,b]_w, [b,c]_w) - δ
```

- δ = 0：完美树
- δ → 1：远离树结构（如球面 δ ≈ 0.99）

---

## 相关链接

- 应用于 LLM: [[concepts/hyperbolic-geometry-llm]]
- 方法应用: [[concepts/hyplora]]
- 领域页: [[domains/Foundations]]
