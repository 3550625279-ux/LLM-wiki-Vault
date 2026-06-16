---
type: entity
title: "DeepSeek-R1"
created: 2026-06-16
updated: 2026-06-16
tags: [DeepSeek, R1, GRPO, 推理模型, 2025]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "implements::[[concepts/grpo]]"
  - "applied_in::[[concepts/data-flywheel]]"
---

# DeepSeek-R1

## 🔗 关系链接

- belongs_to: [[domains/training]]
- produced_by: [[sources/llm-reasoning-ability]]
- implements: [[concepts/grpo]]
- applied_in: [[concepts/data-flywheel]]

---

## 概述

DeepSeek-R1 (2025) 是DeepSeek发布的推理模型，最大突破是验证了一个实验事实：**不经过任何SFT，直接对基座模型做RL，模型就能自发学会推理。**

## 完整训练流程

```
DeepSeek-V3-Base
    ↓ GRPO（纯RL，无SFT）
R1-Zero（涌现推理，但格式不稳定：语言混杂、输出冗余）
    ↓ 用R1-Zero产出的推理链 + 通用SFT数据 做冷启动SFT
SFT模型（格式规范 + 推理保留）
    ↓ 第二轮RL: 推理任务用GRPO + 通用任务用RLHF
    ↓ 第二轮SFT: Rejection Sampling生成推理数据 + 通用能力数据
    ↓ 第三轮RL: 最终精调
R1（最终模型）
```

## 关键细节

第二轮RL不是纯粹的GRPO——推理部分用GRPO（规则化奖励），通用部分（写作、QA等）仍用标准RLHF（RM+PPO）。这解释了R1如何在获得推理能力的同时保持通用能力不退化。

## 蒸馏实验

DeepSeek-R1的蒸馏实验揭示了大模型生产+小模型消费的分工模式。

## 相关节点

- [[concepts/grpo]] — R1的核心训练算法
- [[concepts/data-flywheel]] — 蒸馏实验验证
- [[entities/deepseek-r1-zero]] — R1的前身（纯RL版）
- [[concepts/aha-moment]] — R1训练中的涌现行为
