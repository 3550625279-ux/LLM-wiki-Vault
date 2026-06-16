---
type: concept
title: "LoRA — 低秩适配"
created: 2026-06-13
updated: 2026-06-13
tags: [PEFT, 低秩分解, 参数高效微调, 微调]
status: seed
complexity: intermediate
domain: Training
sources: ["Hu et al. 2021"]
related:
  - "belongs_to::[[domains/Training]]"
  - "extended_by::[[concepts/hyplora]]"
  - "depends_on::[[concepts/svd]]"
  - "applied_in::[[concepts/qlora]]"
  - "produced_by::[[sources/hyplora-neurips2025]]"
thumbnail: ""
---

# LoRA — 低秩适配

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- extended_by: [[concepts/hyplora]]
- depends_on: [[concepts/svd]]
- applied_in: [[concepts/qlora]]
- produced_by: [[sources/hyplora-neurips2025]]

---

> **一句话**：通过注入可训练的低秩矩阵 ΔW = BA 来微调大模型，仅训练极少量参数即可达到全量微调的效果。

---

## 核心公式

```
z = Wx + ΔWx = Wx + BAx
```

- A ∈ ℝ^(r×d)，B ∈ ℝ^(k×r)，r ≪ min(d,k)
- 冻结原始权重 W，只训练 A 和 B
- 参数量从 d·k 降至 (d+k)·r

---

## 关键设计

1. **零初始化**：B 初始化为零，训练开始时 ΔW = BA = 0，不改变原始模型输出
2. **缩放因子**：通常有 α/r 缩放，控制适配强度
3. **应用位置**：通常应用于 Transformer 的 Q/K/V/O 投影矩阵

---

## 变体

- **QLoRA**：量化基座 + LoRA
- **LoRA+**：A 和 B 使用不同学习率
- **DoRA**：权重分解为方向和幅度
- **AdaLoRA**：自适应秩分配
- **HypLoRA**：双曲流形上的 LoRA

---

## 相关链接

- 扩展方法: [[concepts/hyplora]]
- 领域页: [[domains/Training]]
