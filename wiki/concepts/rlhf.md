---
type: concept
title: "基于人类反馈的强化学习（RLHF）"
created: 2026-06-16
updated: 2026-06-16
tags: [RLHF, 强化学习, 奖励模型, PPO, 对齐]
status: seed
complexity: advanced
domain: Alignment
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/Alignment]]"
  - "extends::[[concepts/post-training]]"
  - "depends_on::[[concepts/sft]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "contrasts::[[concepts/grpo]]"
---

# 基于人类反馈的强化学习（RLHF）

## 🔗 关系链接

- belongs_to: [[domains/Alignment]]
- extends: [[concepts/post-training]]
- depends_on: [[concepts/sft]]
- produced_by: [[sources/llm-reasoning-ability]]
- contrasts: [[concepts/grpo]]

---

## 定义

RLHF（Reinforcement Learning from Human Feedback）是后训练的第二层，由InstructGPT (Ouyang et al., 2022) 建立的三阶段管线，通过人类偏好对齐模型行为。

## 三阶段管线

### 阶段一：SFT（同 [[concepts/sft]]）

### 阶段二：训练奖励模型（Reward Model, RM）

给RM看同一个问题的两个回答，人类标注哪个更好，RM学习预测偏好。

- 训练信号来自 **pair-wise比较**（Bradley-Terry模型），而非绝对分数
- 训练目标：最大化 P(A > B) = σ(r(A) - r(B))

### 阶段三：PPO强化学习

用RM作为奖励函数，优化策略模型。

**PPO核心公式（简化）**：
```
L_CLIP = E_t[min(r_t(θ)·Â_t, clip(r_t(θ), 1-ε, 1+ε)·Â_t)]
```
- r_t(θ) = π_θ(a_t|s_t) / π_old(a_t|s_t) — 新旧策略概率比
- Â_t = R - V(s_t) — 优势函数
- ε = 0.2 — clip范围

## RLHF对推理的三重不足

1. **RM不评估推理过程**: 只看"回答好不好"，不看"推理对不对"
2. **SFT数据不含推理链**: InstructGPT的SFT阶段，标注员直接写答案
3. **奖励信号过于粗糙**: 整个回答只有一个标量奖励

## 相关节点

- [[concepts/sft]] — RLHF第一阶段
- [[concepts/process-reward-model]] — 解决RLHF对推理评估不足的问题
- [[concepts/grpo]] — 绕开RM的替代方案
- [[concepts/reward-hacking]] — RLHF的已知问题
- [[entities/deepseek-r1]] — GRPO验证的推理模型
