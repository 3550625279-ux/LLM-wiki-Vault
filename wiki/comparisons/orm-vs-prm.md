---
type: comparison
title: "ORM+PPO vs PRM+PPO"
created: 2026-06-16
updated: 2026-06-16
tags: [ORM, PRM, PPO, 奖励模型对比, 推理强化]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "depends_on::[[concepts/rlhf]]"
  - "depends_on::[[concepts/process-reward-model]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "contrasts::[[concepts/process-reward-model]]"
  - "contrasts::[[concepts/grpo]]"
---

# ORM+PPO vs PRM+PPO

## 🔗 关系链接

- belongs_to: [[domains/training]]
- depends_on: [[concepts/rlhf]]
- depends_on: [[concepts/process-reward-model]]
- produced_by: [[sources/llm-reasoning-ability]]

---

## 对比表

| 维度 | ORM+PPO | PRM+PPO |
|------|---------|---------|
| **奖励粒度** | 只看最终答案 | 每一步单独打分 |
| **代表工作** | DeepSeekMath (Shao et al., 2024) | Let's Verify Step by Step (Lightman et al., 2024) |
| **优势** | 标注成本低，工程简单 | 能精确定位错误步骤 |
| **劣势** | 模型可能蒙对答案 | 标注成本极高 |

## 定位

- **ORM+PPO** = 推理强化的基础版
- **PRM+PPO** = 精细化版

> 大多数实际系统会先用ORM+PPO跑通，再考虑升级到PRM。

## 传统管线（ORM+PPO或PRM+PPO）的局限

1. **数据瓶颈**: SFT推理链 + PRM逐步标注，两者都极贵
2. **奖励模型偏差**: PRM本身是模型，可能对某些推理风格系统性地偏高/偏低打分
3. **训练不稳定**: PPO对超参敏感，KL散度约束需要精心调参
4. **天花板受限于SFT**: SFT模型推理上限低，RL提升空间有限

## 相关节点

- [[concepts/rlhf]] — ORM+PPO基于RLHF
- [[concepts/process-reward-model]] — PRM详细说明
- [[concepts/grpo]] — GRPO绕开了两种管线
