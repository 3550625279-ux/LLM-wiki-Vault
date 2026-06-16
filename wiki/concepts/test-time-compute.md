---
type: concept
title: "推理时计算（Test-Time Compute）"
created: 2026-06-16
updated: 2026-06-16
tags: [test-time-compute, 推理时扩展, self-consistency, MCTS, scaling]
status: seed
complexity: advanced
domain: Inference
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/Inference]]"
  - "depends_on::[[concepts/chain-of-thought]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
---

# 推理时计算（Test-Time Compute）

## 🔗 关系链接

- belongs_to: [[domains/Inference]]
- depends_on: [[concepts/chain-of-thought]]
- produced_by: [[sources/llm-reasoning-ability]]

---

## 定义

Test-Time Compute 是指在模型推理阶段（而非训练阶段）投入更多计算资源来提升推理表现的策略。2024年以来被系统化研究。

## 三种策略

### 1. 并行采样 + 多数投票（Self-Consistency, Wang et al., 2022）

- 采样 N 次（temperature=0.7）
- 选择出现次数最多的答案作为最终输出
- **优点**: 简单有效
- **缺点**: 需要答案可枚举

### 2. Best-of-N + Verifier

- 不投票，而是用验证器（ORM/PRM）对N条推理链打分，选最高分的一条
- **与Self-Consistency区别**: 不需要答案重复出现，只要验证器认为最好就选它

### 3. 搜索 + 验证（MCTS / Beam Search）

- 将推理过程构建为搜索树
- PRM对每个节点打分，低分路径剪枝，选择最高分路径

## Test-Time Compute的Scaling Law

Snell et al. (2024, ICLR 2025) 实验结论：

- 推理时计算量 ×4 → 匹配参数量 ×14 的模型表现
- **收益递减**: 计算量持续增加后，边际收益快速下降
- **策略分化**: 简单任务适合并行采样，困难任务需要搜索+验证

## 相关节点

- [[concepts/chain-of-thought]] — CoT是Test-Time Compute的基础
- [[concepts/process-reward-model]] — PRM作为验证器
- [[concepts/data-flywheel]] — 数据飞轮中的Rejection Sampling与此相关
