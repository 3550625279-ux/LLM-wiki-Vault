---
type: source
title: "中心极限定理与归一化"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, CLT, 归一化, 深度学习]
status: developing
complexity: intermediate
domain: Foundations
sources: []
related:
  - "belongs_to::[[domains/Foundations]]"
  - "spawns::[[concepts/central-limit-theorem]]"
  - "spawns::[[concepts/sqrt-n-origin]]"
  - "spawns::[[concepts/standard-deviation-l2]]"
  - "spawns::[[concepts/batch-normalization]]"
  - "spawns::[[concepts/layer-normalization]]"
  - "spawns::[[concepts/transformer-sqrt-d]]"
raw_path: ""
thumbnail: ""
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- spawns: [[concepts/central-limit-theorem]] | [[concepts/sqrt-n-origin]] | [[concepts/standard-deviation-l2]] | [[concepts/batch-normalization]] | [[concepts/layer-normalization]] | [[concepts/transformer-sqrt-d]]

---

## 资料概要

本文件是概率论学习笔记的第三篇。核心问题：大量独立随机变量相加后分布趋向什么形状？标准化操作（减均值、除标准差）在神经网络中如何落地？从CLT的数学陈述出发，经过√n的推导、标准差的精确定义，最终到达BatchNorm、LayerNorm和Transformer的√d缩放。

## 核心逻辑链

```
独立变量相加 → 正负抵消(σ√n) → CLT趋向正态 → 标准化 → 神经网络加权和 → BN/LN → √d缩放
```

## 八节内容摘要

| 节 | 主题 | 核心概念 |
|----|------|---------|
| 1 | CLT核心 | Sₙ的漂移行为, 标准化和Zₙ→N(0,1) |
| 2 | 标准化手术 | 减nμ(中心化) + 除以σ√n(缩放) |
| 3 | √n来源 | 方差可加性→Var(Sₙ)=nσ²→σ√n |
| 4 | 标准差精确定义 | σ=L2范数/√n, 为什么选标准差而非MAD |
| 5 | CLT在神经网络 | 加权和~正态(启发式), 归一化有效原因(优化理论) |
| 6 | BN vs LN | BN概率论基础扎实, LN工程上更实用 |
| 7 | √d缩放 | Var(q·k)=d, 除以√d修正, 防止softmax饱和 |
| 8 | 综合梳理 | 方差归一化是贯穿始终的主线 |

## 关键洞察

- **√n来自方差可加性**，没有更深的原因
- CLT提供**直觉**而非**因果解释**，归一化有效主因是优化理论
- **BN概率论基础扎实**(大数定律适用)，**LN概率论基础弱但工程实用**
- **√d缩放与CLT的√n同源**：独立变量求和导致方差线性增长
- 方差归一化是**从骰子到Transformer的贯穿主线**

## 诞生的节点

- [[concepts/central-limit-theorem]] — 中心极限定理
- [[concepts/sqrt-n-origin]] — √n的来源
- [[concepts/standard-deviation-l2]] — 标准差与L2范数
- [[concepts/batch-normalization]] — BatchNorm
- [[concepts/layer-normalization]] — LayerNorm
- [[concepts/transformer-sqrt-d]] — Transformer的√d缩放
