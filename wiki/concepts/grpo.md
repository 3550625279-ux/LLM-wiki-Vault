---
type: concept
title: "组相对策略优化（GRPO）"
created: 2026-06-16
updated: 2026-06-16
tags: [GRPO, 强化学习, DeepSeek, 规则化奖励, 组内排序]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "extends::[[concepts/post-training]]"
  - "depends_on::[[concepts/rlhf]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "contrasts::[[concepts/rlhf]]"
  - "applied_in::[[entities/deepseek-r1]]"
---

# 组相对策略优化（GRPO）

## 🔗 关系链接

- belongs_to: [[domains/training]]
- extends: [[concepts/post-training]]
- depends_on: [[concepts/rlhf]]
- produced_by: [[sources/llm-reasoning-ability]]
- contrasts: [[concepts/rlhf]]
- applied_in: [[entities/deepseek-r1]]

---

## 定义

GRPO（Group Relative Policy Optimization）是DeepSeek-R1 (2025) 提出的强化学习算法，**绕开奖励模型和Value Network**，用规则化奖励函数和组内相对排序实现推理能力训练。

## 核心突破

> 不经过任何SFT，直接对基座模型做RL，模型就能自发学会推理。这颠覆了"必须先SFT再RL"的传统认知。

## 算法流程

1. **对同一问题生成 G=16 条推理链**（temperature=1.0）
2. **规则化奖励**（无需训练模型）：
   - 正确性奖励：答案对→1.0，错→0.0
   - 格式奖励：输出了"最终答案："→1.0，否→0.0
3. **计算组内标准化优势**（替代Value Network）：
   - μ = mean(所有路径奖励)
   - σ = std(所有路径奖励)
   - Â_i = (R_i - μ) / σ
4. **用 Â_i 替代 PPO中的优势 A，进行策略梯度更新**

## GRPO vs PPO

| 维度 | PPO | GRPO |
|------|-----|------|
| 奖励来源 | PRM（需额外训练） | 规则化函数（无需训练） |
| 优势计算 | A = R - V(s)，需Value Network | Â = (R-μ)/σ，组内相对排序 |
| KL约束 | 显式KL散度惩罚 | 有显式KL惩罚，但无需Value Network |
| 适用前提 | 通用 | 需可验证答案（数学、编程） |

> ⚠️ 注意：GRPO仍有对参考策略的KL散度约束（防止策略偏离太远），"组内排序天然替代KL"是一个常见误解。GRPO简化的是优势计算和奖励获取，而非KL约束。

## 相关节点

- [[concepts/rlhf]] — GRPO绕开了RLHF的RM+PPO管线
- [[concepts/reward-hacking]] — GRPO面临的奖励利用问题
- [[entities/deepseek-r1]] — GRPO的验证模型
- [[entities/deepseek-r1-zero]] — 纯GRPO训练的涌现推理
- [[concepts/aha-moment]] — GRPO训练中涌现的自我反思
