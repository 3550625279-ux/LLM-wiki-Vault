---
type: concept
title: "LLM 嵌入的双曲几何结构"
created: 2026-06-13
updated: 2026-06-13
tags: [嵌入几何, 双曲性, 幂律分布, 层次结构, token嵌入]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/hyplora-neurips2025]]"]
related:
  - "belongs_to::[[domains/Architecture]]"
  - "implements::[[concepts/hyperbolic-geometry]]"
  - "applied_in::[[concepts/hyplora]]"
  - "extends::[[concepts/lora]]"
  - "produced_by::[[sources/hyplora-neurips2025]]"
thumbnail: ""
---

# LLM 嵌入的双曲几何结构

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- extends: [[concepts/lora]]
- produced_by: [[sources/hyplora-neurips2025]]

---

> **一句话**：LLM 的 token 嵌入天然具有双曲（树状）层次结构，高频词聚集在原点附近，低频词向外扩散，形成幂律分布。

---

## 三个关键发现

### 发现 1：全局幂律分布

Token 频率服从幂律分布 P(k) ∼ k^(-γ)，γ ≈ 1.9。

```
高频 token (Group 1): to, in, have, that, is  →  频率 ~4900，范数 ~0.35
中频 token (Group 2): how, much, many, time    →  频率 ~2700，范数 ~0.46
类名词 (Group 3): animal, fruit, number, color  →  频率 ~290，范数 ~0.50
具体词 (Group 4): dog, apple, purple, red       →  频率 ~100，范数 ~0.57
```

跨模型一致性：LLaMA-7B、LLaMA-13B、LLaMA3-8B、Gemma-7B 均呈现相同模式。

### 发现 2：局部 δ-双曲性

使用 Gromov 四点条件测量每个 prompt 中 token 嵌入的 δ-双曲性：

| 模型 | MAWPS | SVAMP | GSM8K | AQuA |
|------|-------|-------|-------|------|
| LLaMA-7B | 0.08±0.02 | 0.09±0.01 | 0.10±0.01 | 0.10±0.01 |
| LLaMA3-8B | 0.06±0.01 | 0.07±0.01 | 0.07±0.01 | 0.08±0.01 |

δ ≈ 0 表示完美树，LLM 嵌入的 δ ≈ 0.06-0.12，非常接近树结构。

### 发现 3：幂律 ↔ 双曲几何的理论连接

在 Poincaré 圆盘模型中，圆面积指数增长 A(r) ∼ eʳ。由此推导：

```
P(k) ∼ k^(-(1-ζ))，其中 γ = 2/ζ + 1
```

幂律分布是双曲空间中 token 嵌入的数学必然结果。

---

## 核心洞察

- LLM 嵌入空间不是"扁平"的欧氏空间，而是具有内在的层次几何结构
- 这种结构是训练过程自然涌现的（next-token prediction → 层次化嵌入）
- 欧几里得空间表示本质上非欧几里得（双曲）的结构，是一种"妥协"
- 几何分析可以指导方法设计（分析驱动的研究范式）

---

## 相关链接

- 方法应用: [[concepts/hyplora]]
- 基础理论: [[concepts/hyperbolic-geometry]]
- 原始论文: [[raw/papers/hyperbolic-fine-tuning-llms/paper.pdf]]
