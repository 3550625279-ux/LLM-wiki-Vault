---
type: concept
title: "QLoRA — 量化低秩适配"
created: 2026-06-16
updated: 2026-06-16
tags: [PEFT, LoRA, 量化, 微调, 4-bit]
status: seed
complexity: intermediate
domain: Training
sources: ["Dettmers et al. 2023"]
related:
  - "depends_on::[[concepts/lora]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/hyplora-neurips2025]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/lora]]
- produced_by: [[sources/hyplora-neurips2025]]

---

# QLoRA — 量化低秩适配

## 核心思想

将预训练模型权重量化为 **4-bit**（NF4 格式），冻结后在其上注入 LoRA 低秩适配器。单张 48GB GPU 即可微调 65B 参数模型。

## 三大技术创新

1. **NF4 (4-bit NormalFloat)**: 信息论最优的 4-bit 量化格式，专为正态分布权重设计
2. **双重量化**: 对量化常数本身再做一次量化，进一步节省内存
3. **分页优化器**: 利用 CPU-GPU 内存分页，处理显存峰值

## 内存对比

| 方法 | 65B 模型显存需求 | 精度损失 |
|------|----------------|---------|
| 全量微调 FP16 | ~780 GB | 无 |
| LoRA FP16 | ~160 GB | 极小 |
| **QLoRA NF4** | **~48 GB** | 极小 |

## 与 LoRA 的关系

QLoRA = **Q**uantization + **LoRA**。底层仍是 [[concepts/lora]] 的低秩矩阵注入，只是基座模型被压缩到了 4-bit。
