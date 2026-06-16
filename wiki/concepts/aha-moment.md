---
type: concept
title: "Aha Moment（推理涌现）"
created: 2026-06-16
updated: 2026-06-16
tags: [aha-moment, 涌现, 自我反思, 纯RL, DeepSeek-R1-Zero]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "depends_on::[[concepts/grpo]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "applied_in::[[entities/deepseek-r1-zero]]"
---

# Aha Moment（推理涌现）

## 🔗 关系链接

- belongs_to: [[domains/training]]
- depends_on: [[concepts/grpo]]
- produced_by: [[sources/llm-reasoning-ability]]
- applied_in: [[entities/deepseek-r1-zero]]

---

## 定义

Aha Moment 是指DeepSeek-R1-Zero（纯RL，无SFT）在训练过程中出现的推理能力自发涌现行为——模型在推理途中重新审视之前的步骤，发现当前路径可能有问题，回溯到前面的步骤重新出发。

## 涌现过程示例

**训练早期 step ~100** — 基本推理：
```
步骤1: 设鸡x只，兔y只，x+y=35，2x+4y=94
步骤2: 解方程得 y=12，x=23
答案: 鸡23只，兔12只。
```

**训练中期 step ~3000** — 涌现反思：
```
步骤1: 设鸡x只，兔y只...
步骤2: 由第一个方程...
步骤3: 70+2y=94，所以2y=24，y=12
等等，让我重新检查一下：
  方程1: x+y=35
  方程2: 2x+4y=94
  代入验证: 2×23+4×12=46+48=94 ✓
  头数验证: 23+12=35 ✓
确认无误。答案: 鸡23只，兔12只。
```

## 核心特征

Aha Moment更核心的特征不是末尾加一个验证，而是**模型在推理途中重新审视之前的步骤**——发现当前路径可能有问题，回溯到前面的步骤重新出发。"等等"之后的反思不仅是验证，有时还包括改变推理方向。

> 这些行为从未被人类标注过，从未出现在训练数据中。模型在"答案正确就得分"的简单奖励压力下，自己发现：验证→更高正确率→更多奖励。

## 相关节点

- [[concepts/grpo]] — Aha Moment在GRPO训练中涌现
- [[concepts/reward-hacking]] — 对比：hacking是负面涌现，Aha是正面涌现
- [[entities/deepseek-r1-zero]] — 涌现行为的载体模型
- [[entities/deepseek-r1]] — 实际R1在R1-Zero基础上增加了冷启动SFT
