---
type: source
title: "LLM是如何获得推理能力的？"
created: 2026-06-16
updated: 2026-06-16
tags: [后训练, 推理能力, SFT, RLHF, GRPO, CoT, 强化学习]
status: developing
complexity: intermediate
domain: Training
sources: []
raw_path: "raw/articles/llm-reasoning-ability/"
related:
  - "belongs_to::[[domains/training]]"
  - "spawns::[[concepts/post-training]]"
  - "spawns::[[concepts/sft]]"
  - "spawns::[[concepts/chain-of-thought]]"
  - "spawns::[[concepts/rlhf]]"
  - "spawns::[[concepts/process-reward-model]]"
  - "spawns::[[concepts/grpo]]"
  - "spawns::[[concepts/reward-hacking]]"
  - "spawns::[[concepts/test-time-compute]]"
  - "spawns::[[concepts/data-flywheel]]"
  - "spawns::[[concepts/aha-moment]]"
  - "spawns::[[entities/deepseek-r1]]"
  - "spawns::[[entities/deepseek-r1-zero]]"
  - "spawns::[[comparisons/orm-vs-prm]]"
  - "spawns::[[operations/sft-cot-data-pipeline]]"
thumbnail: ""
---

# LLM是如何获得推理能力的？

## 🔗 关系链接

- belongs_to: [[domains/training]]
- belongs_to: [[domains/alignment]]
- belongs_to: [[domains/inference]]

---

## 来源信息

- **作者**: 番茄的算法日记（小红书）
- **类型**: 技术科普长文（16张图文）
- **核心论点**: LLM的推理能力不是预训练"涌现"的，而是通过后训练（post-training）一步步构建出来的。以鸡兔同笼问题贯穿，拆解从SFT到PRM+PPO再到GRPO的完整技术栈。

## 核心内容摘要

### 主线：后训练四层递进

| 层级 | 方法 | 核心改进 |
|------|------|---------|
| 第一层 | SFT | 激活潜藏推理能力，从"续写模式"切换到"回答模式" |
| 第二层 | RLHF (RM+PPO) | 对齐偏好，但RM不评估推理过程 |
| 第三层 | PRM+PPO | 过程奖励模型，逐步骤打分，定位错误步骤 |
| 第四层 | GRPO | 绕开奖励模型，规则化奖励，DeepSeek-R1验证 |

### 辅线

1. **数据生产线**: 人工标注 → 教师蒸馏 → 程序合成 → Rejection Sampling
2. **训练方法论**: Online RL vs Offline DPO 的分野与融合
3. **推理时优化**: Test-Time Compute 的 scaling 与策略选择

### 关键洞察

- 预训练编码了大量推理模式但未被激活（"潜藏推理能力"）
- SFT本质是行为克隆，天花板是分布外泛化差 + 错误累积 + 无法自我纠错
- DeepSeek-R1-Zero 无SFT纯RL训练出现"Aha Moment"（自我反思涌现）
- LLM推理能力或许介于纯模式匹配和纯逻辑推理之间——"高效的模式补全"

### 诞生的节点

| 节点 | 类型 | 一句话 |
|------|------|-------|
| [[concepts/post-training]] | concept | 后训练：从预训练后的模型到可用推理模型的渐进构建过程 |
| [[concepts/sft]] | concept | 有监督微调：用指令-回答对训练模型从续写切换到回答 |
| [[concepts/chain-of-thought]] | concept | 推理链(CoT)：在回答中展示中间推理步骤，准确率从17%飙升到78% |
| [[concepts/rlhf]] | concept | RLHF：SFT→奖励模型→PPO的三阶段对齐管线 |
| [[concepts/process-reward-model]] | concept | PRM：对推理链每一步单独打分的过程奖励模型 |
| [[concepts/grpo]] | concept | GRPO：组内相对排序替代Value Network的强化学习 |
| [[concepts/reward-hacking]] | concept | 奖励Hacking：模型利用奖励信号漏洞的对抗行为 |
| [[concepts/test-time-compute]] | concept | 推理时计算：在推理阶段投入更多计算提升表现 |
| [[concepts/data-flywheel]] | concept | 数据飞轮：模型自我生成→筛选→再训练的迭代增强循环 |
| [[concepts/aha-moment]] | concept | Aha Moment：纯RL训练中推理能力自发涌现的现象 |
| [[entities/deepseek-r1]] | entity | DeepSeek-R1：GRPO验证推理能力可纯RL获得 |
| [[entities/deepseek-r1-zero]] | entity | DeepSeek-R1-Zero：无SFT纯RL训练的涌现推理能力 |
| [[comparisons/orm-vs-prm]] | comparison | ORM vs PRM：结果奖励与过程奖励的对比 |
| [[operations/sft-cot-data-pipeline]] | operation | CoT SFT数据生产线：四条主流路径获取推理链数据 |
