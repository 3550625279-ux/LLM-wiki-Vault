---
type: concept
title: "有监督微调（SFT）"
created: 2026-06-16
updated: 2026-06-16
tags: [SFT, 后训练, 指令微调, 推理激活]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "extends::[[concepts/post-training]]"
  - "depends_on::[[concepts/chain-of-thought]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "contrasts::[[concepts/grpo]]"
---

# 有监督微调（SFT）

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- extends: [[concepts/post-training]]
- depends_on: [[concepts/chain-of-thought]]
- produced_by: [[sources/llm-reasoning-ability]]
- contrasts: [[concepts/grpo]]

---

## 定义

有监督微调（Supervised Fine-Tuning, SFT）是后训练的第一层，使用精心构造的（指令, 回答）对作为训练数据，教会模型从"续写模式"切换到"回答模式"。

## 两个阶段

### 2.1 通用SFT：教模型"听懂指令"

**代表工作**: FLAN (Wei et al., 2021), InstructGPT (Ouyang et al., 2022)

- 用指令-回答对做监督微调
- 模型学会"看到问题应该回答"
- **不足**: 回答不含推理过程，直接给答案，复杂题错误率暴增

### 2.2 推理链SFT：教模型"展开推理"

**关键发现**: Wei et al. 2022 的CoT论文——让模型展示中间步骤，推理准确率从17%飙升到78%。

训练数据格式从 `问题→答案` 升级为 `问题→推理链→答案`

## SFT的天花板（三个根本性瓶颈）

1. **分布外泛化差**: 训练数据全是代数推理→无法自发发明反证法
2. **错误累积**: 推理链超过5步，每步的小误差会累积放大
3. **无法自我纠错**: 一旦推理方向错了，没有"回退重来"的机制

> 结论：仅靠模仿，无法超越被模仿者。

## 相关节点

- [[concepts/post-training]] — SFT是后训练第一层
- [[concepts/chain-of-thought]] — 推理链数据格式
- [[concepts/rlhf]] — SFT之后的对齐阶段
- [[concepts/grpo]] — 绕开SFT的纯RL方法
- [[operations/sft-cot-data-pipeline]] — CoT数据的四条生产线
