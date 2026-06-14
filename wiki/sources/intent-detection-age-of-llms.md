---
type: source
title: "Intent Detection in the Age of LLMs"
created: 2026-06-14
updated: 2026-06-14
tags: [意图检测, LLM, TODS, 混合系统, OOS检测]
status: developing
complexity: intermediate
domain: Agents
sources: []
related:
  - "spawns::[[concepts/setfit]]"
  - "spawns::[[concepts/uncertainty-routing]]"
  - "spawns::[[concepts/negative-data-augmentation]]"
  - "spawns::[[concepts/out-of-scope-detection]]"
  - "spawns::[[concepts/adaptive-in-context-learning]]"
  - "spawns::[[concepts/intent-detection-tods]]"
  - "spawns::[[concepts/monte-carlo-dropout]]"
  - "spawns::[[insights/hybrid-beats-pure-llm]]"
  - "contrasts::[[sources/cagc-cvpr2024]]"
  - "belongs_to::[[domains/Agents]]"
thumbnail: ""
paper_pdf: "raw/papers/intent-detection-age-of-llms/paper.pdf"
venue: "EMNLP 2024 Industry Track"
year: 2024
authors: ["Gaurav Arora", "Shreya Jain", "Srujana Merugu"]
affiliation: ["Amazon", "IIT Jammu"]
---

# Intent Detection in the Age of LLMs

> EMNLP 2024 Industry Track | Amazon & IIT Jammu

## 📄 论文概要

本文研究如何在任务导向对话系统（TODS）中利用 LLM 进行意图检测。对比了 7 个 SOTA LLM（Claude 和 Mistral 系列）与 SetFit 微调模型的性能/延迟权衡，并提出三个核心贡献：

1. **混合系统**：基于 Monte Carlo Dropout 不确定性路由，仅在 SetFit 不确定时调用 LLM → F1 与 LLM 差距 <2%，延迟降低 ~50%
2. **负面数据增强**：通过关键词替换/删除生成 OOS 样本，SetFit F1 提升 >5%
3. **两步 OOS 检测**：利用 LLM 内部表示（decoder 层隐藏状态），Mistral-7B OOS 准确率和 F1 提升 >5%

### 一句话总结

**通过不确定性路由将 LLM 和轻量级 SetFit 结合，用 ~50% 的延迟达到 ~98% 的 LLM 准确率；同时揭示了 LLM OOS 检测的关键弱点，并提出了利用内部表示的有效改进方案。**

## 📊 关键数据

| 模型 | 平均 F1 | 平均延迟 (s) |
|------|---------|-------------|
| Claude v3 Haiku | 0.736 | 1.697 |
| Mistral Large | 0.735 | 3.565 |
| SetFit + 负面增强 | 0.658 | 0.030 |
| 混合系统 (SNA+Haiku, M=10) | 0.696 | 1.005 |

## 🔗 实验数据集

- **HINT3**：SOFMattress / Curekart / PowerPlay11（开源，单标签）
- **AID3**：ALC / ADP / OADP（内部，多标签）

## 📚 详细学习材料

- 论文摘要与关键结果：[[raw/papers/intent-detection-age-of-llms/summary.md]]
- 方法详解：[[raw/papers/intent-detection-age-of-llms/method.md]]
- 深度洞察：[[raw/papers/intent-detection-age-of-llms/insights.md]]
- 问答练习：[[raw/papers/intent-detection-age-of-llms/qa.md]]
- 思维框架：[[raw/papers/intent-detection-age-of-llms/mental-model.md]]
- 反思与扩展：[[raw/papers/intent-detection-age-of-llms/reflection.md]]

## 🏷️ 标签

`intent detection` · `hybrid routing` · `OOS detection` · `in-context learning` · `SetFit` · `Monte Carlo Dropout`
