---
type: concept
title: "SetFit（Sentence Transformer Fine-Tuning）"
created: 2026-06-14
updated: 2026-06-14
tags: [SetFit, 少样本学习, 句子转换器, 对比学习]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "extends::[[concepts/adaptive-in-context-learning]]"
  - "part_of::[[concepts/uncertainty-routing]]"
  - "applied_in::[[concepts/intent-detection-tods]]"
  - "contrasts::[[concepts/out-of-scope-detection]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# SetFit（Sentence Transformer Fine-Tuning）

## 定义

SetFit 是一种高效的少样本学习方法，通过对比微调句子转换器实现文本分类，无需提示模板或大量标注数据。由 Tunstall et al. (2022) 提出。

## 两阶段训练

```
阶段 1: 对比微调（Contrastive Fine-tuning）
├── 基础模型: MPNet (all-mpnet-base-v2)
├── 结构: Siamese 网络
├── 数据: 构造正/负句子对
└── 目标: 同意图句子表示靠近，不同意图远离

阶段 2: 分类头训练（Classification Head）
├── 输入: 阶段 1 编码器生成的句子表示
├── 结构: 线性层 + Sigmoid（支持多标签）
└── 训练: 标准监督学习
```

## 关键特点

| 特点 | 详情 |
|------|------|
| **数据效率** | 少样本即可训练（few-shot） |
| **推理速度** | p50 延迟仅 ~30ms |
| **无需提示** | 不像 LLM ICL 需要设计 prompt |
| **准确率** | 低于 LLM（F1 ~0.658 vs LLM ~0.736） |
| **OOS 检测** | 对 class design 更鲁棒但绝对能力有限 |

## 在混合系统中的角色

SetFit 在 [[concepts/uncertainty-routing]] 混合系统中充当"快速通道"：
- 大多数简单查询由 SetFit 直接处理（30ms）
- 仅在 MC Dropout 显示不确定时才路由到 LLM
- 配合 [[concepts/negative-data-augmentation]] 可提升 F1 >5%

## 超参数

| 参数 | 搜索范围 |
|------|---------|
| body_lr | 5e-6 ~ 5e-5 |
| head_lr | 1e-3 ~ 1e-2 |
| epochs | 3 ~ 10 |
| batch_size | {8, 16, 32, 64} |

使用 Optuna 进行搜索。MC Dropout rate = 0.1（hidden + attention layers）。

## 局限性

1. 准确率显著低于 LLM（~8% F1 差距）
2. OOS 泛化能力差（OADP 上 F1 下降 ~15%）
3. 需要重新训练以适应新意图
4. 对对比学习的数据对构造敏感

## 来源

- 原始论文: Tunstall et al., "Efficient Few-Shot Learning Without Prompts" (2022)
- 应用: [[sources/intent-detection-age-of-llms]]
