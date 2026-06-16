---
type: concept
title: "数据飞轮（Data Flywheel）"
created: 2026-06-16
updated: 2026-06-16
tags: [数据飞轮, STaR, ReST, 蒸馏, 迭代自训练]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "depends_on::[[concepts/sft]]"
  - "depends_on::[[concepts/grpo]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "applied_in::[[entities/deepseek-r1]]"
---

# 数据飞轮（Data Flywheel）

## 🔗 关系链接

- belongs_to: [[domains/training]]
- depends_on: [[concepts/sft]]
- depends_on: [[concepts/grpo]]
- produced_by: [[sources/llm-reasoning-ability]]
- applied_in: [[entities/deepseek-r1]]

---

## 定义

数据飞轮是指后训练各阶段之间存在**双向数据流动**，形成自我增强的迭代循环：RL产出的高质量推理链反哺SFT，SFT后的模型又让RL有更高的起点。

## 两种循环模式

### 8.1 迭代自训练（STaR / ReST）

STaR (Zelikman et al., 2022) 和 ReST (Gulcehre et al., 2023)：

1. 模型对问题生成推理链
2. 筛选出推理正确且答案正确的样本
3. 用这些样本对模型再做SFT
4. 更强的模型生成更高质量的推理链
5. 重复

### 8.2 大模型生产 + 小模型消费

DeepSeek-R1的蒸馏实验揭示的分工模式：

```
大模型（数百B参数）→ RL训练 → 发现好的推理路径
                                    ↓
                           生成高质量推理链数据
                                    ↓
小模型（数B~数十B参数）→ SFT → 习得推理能力（不自己做RL）
```

> **经济学意义**: RL训练的探索成本由大模型承担，小模型通过廉价的SFT获取推理能力。

## 相关节点

- [[concepts/sft]] — 飞轮的数据消费端
- [[concepts/grpo]] — 飞轮的数据生产端
- [[concepts/test-time-compute]] — Rejection Sampling与飞轮相关
- [[entities/deepseek-r1]] — 蒸馏实验验证
