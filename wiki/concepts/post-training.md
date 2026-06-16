---
type: concept
title: "后训练（Post-Training）"
created: 2026-06-16
updated: 2026-06-16
tags: [后训练, 训练流程, SFT, RLHF]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "extends::[[concepts/lora]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
---

# 后训练（Post-Training）

## 🔗 关系链接

- belongs_to: [[domains/training]]
- extends: [[concepts/lora]]
- produced_by: [[sources/llm-reasoning-ability]]

---

## 定义

后训练（post-training）是指在大规模预训练之后，通过一系列技术手段将模型从"续写语料的基座模型"转化为"能执行特定任务的可用模型"的过程。

## 核心论点

> 大模型的推理能力不是预训练"涌现"的，而是通过后训练一步步构建出来的。

## 后训练四层递进架构

```
预训练 → 语料中编码了潜藏推理模式，但未被激活
    ↓
后训练四层：
  第一层：SFT（行为激活）— 教模型"听懂指令" + "展开推理"
  第二层：RLHF（对齐偏好）— RM + PPO，但不评估推理过程
  第三层：PRM+PPO（推理专用RL）— 过程奖励，逐步骤打分
  第四层：GRPO（纯RL推理）— 规则化奖励，绕开奖励模型
```

## 与预训练的关系

| 维度 | 预训练 | 后训练 |
|------|--------|--------|
| 目标 | next-token prediction | 行为激活 + 能力强化 |
| 数据 | 海量无标注语料 | 精心构造的指令-回答对 + 奖励信号 |
| 推理能力 | 编码了推理模式但未激活 | 激活 → 定向 → 强化 |
| 输出模式 | 续写语料 | 回答问题 |

## 相关节点

- [[concepts/sft]] — 后训练第一层
- [[concepts/rlhf]] — 后训练第二层
- [[concepts/process-reward-model]] — 后训练第三层
- [[concepts/grpo]] — 后训练第四层
