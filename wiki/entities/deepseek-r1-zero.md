---
type: entity
title: "DeepSeek-R1-Zero"
created: 2026-06-16
updated: 2026-06-16
tags: [DeepSeek, R1-Zero, 纯RL, 涌现推理, 2025]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "implements::[[concepts/grpo]]"
  - "produced_by::[[concepts/aha-moment]]"
---

# DeepSeek-R1-Zero

## 🔗 关系链接

- belongs_to: [[domains/training]]
- produced_by: [[sources/llm-reasoning-ability]]
- implements: [[concepts/grpo]]

---

## 概述

DeepSeek-R1-Zero是DeepSeek-R1的前身，**不经过任何SFT，直接对DeepSeek-V3-Base做纯GRPO训练**。它在训练中出现了被称为"Aha Moment"的推理能力自发涌现行为。

## 训练配置

- 基座模型: DeepSeek-V3-Base
- 训练方法: 纯GRPO（无SFT冷启动）
- 奖励: 规则化函数（正确性 + 格式）

## 涌现行为

- 推理步骤逐渐增加
- 出现自我反思（"等等，让我重新检查一下"）
- 模型在推理中途重新审视之前步骤，发现错误并回溯

## 局限

- 格式不稳定：语言混杂、输出冗余
- 这些问题在DeepSeek-R1中通过冷启动SFT解决

## 相关节点

- [[entities/deepseek-r1]] — R1在R1-Zero基础上增加了冷启动SFT
- [[concepts/grpo]] — R1-Zero的核心训练算法
- [[concepts/aha-moment]] — R1-Zero中的涌现行为
