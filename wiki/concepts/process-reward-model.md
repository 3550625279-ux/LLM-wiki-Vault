---
type: concept
title: "过程奖励模型（PRM）"
created: 2026-06-16
updated: 2026-06-16
tags: [PRM, 奖励模型, 过程奖励, 推理验证, 逐步打分]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "extends::[[concepts/rlhf]]"
  - "depends_on::[[concepts/chain-of-thought]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "contrasts::[[comparisons/orm-vs-prm]]"
---

# 过程奖励模型（PRM）

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- extends: [[concepts/rlhf]]
- depends_on: [[concepts/chain-of-thought]]
- produced_by: [[sources/llm-reasoning-ability]]
- contrasts: [[comparisons/orm-vs-prm]]

---

## 定义

过程奖励模型（Process Reward Model, PRM, Lightman et al., 2024）是一种对推理链每一步单独打分的奖励模型，解决了ORM（结果奖励模型）只看最终答案的问题。

## ORM的问题

ORM输入完整推理链+最终答案，输出1个标量奖励。**问题**: 推理过程全错但答案蒙对 → 高奖励。

## PRM的核心改进

**不对整条推理链打分，而是对每一步单独打分。**

```
【第1步输入】
问题 + 推理前缀: 步骤1: ...
【第1步输出】得分: 0.98（正确）

【第2步输入】
问题 + 推理前缀: 步骤1... 步骤2: ...
【第2步输出】得分: 0.99（正确）

【错误步骤输入】
问题 + 推理前缀: 步骤1... 步骤2: ... (错误)
【错误步骤输出】得分: 0.03
```

**关键**: 每到一个步骤的结束位置就输入一次，逐步骤打分。

## PRM架构

基于SFT模型初始化，将最后一层的词表输出头替换为二分类头。

## 完整管线：SFT → PRM → PPO

1. **策略模型生成多条推理链** — 同一问题采样多条推理路径
2. **PRM逐步骤打分** — 高质量路径获得高总奖励
3. **PPO参数更新** — 增大高奖励路径概率，减小低奖励路径概率

## PRM的代价

对一条5步推理链，需要5个逐步标注；ORM只需1个终局标注。标注量乘以推理链长度。

## 相关节点

- [[comparisons/orm-vs-prm]] — ORM vs PRM详细对比
- [[concepts/rlhf]] — PRM是对RLHF中RM的改进
- [[concepts/grpo]] — 绕开PRM的替代方案
