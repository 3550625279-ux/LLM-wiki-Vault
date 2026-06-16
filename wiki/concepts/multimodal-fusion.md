---
type: concept
title: "多模态融合"
created: 2026-06-16
updated: 2026-06-16
tags: [多模态, 融合, 跨模态]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["综合来源"]
related:
  - "extended_by::[[concepts/multimodal-intent-recognition]]"
  - "belongs_to::[[domains/Multimodal]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Multimodal]]
- extended_by: [[concepts/multimodal-intent-recognition]]

---

# 多模态融合

## 核心问题

如何将来自不同模态（文本、语音、视觉）的信息整合为统一表示？

## 三种融合策略

| 策略 | 时机 | 优势 | 劣势 |
|------|------|------|------|
| **早期融合** | 输入层拼接 | 保留原始信息 | 维度爆炸、模态对齐难 |
| **晚期融合** | 各模态独立编码后合并 | 模块化、灵活 | 可能丢失跨模态交互 |
| **中间融合** | Transformer 层间交叉注意力 | 平衡信息保留与交互 | 设计复杂 |

## 在 MIR 中的应用

[[concepts/multimodal-intent-recognition]] 中，文本-语音-视觉三个模态通过交叉注意力机制在中间层融合，捕捉跨模态的语调-表情-语义一致性。
