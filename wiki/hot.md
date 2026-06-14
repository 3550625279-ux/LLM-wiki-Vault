# Hot Cache — 会话快速恢复上下文

> 此文件由系统自动维护。每次会话开始时静默读取，不向用户输出。
> 每次 ingest / review / align 后更新。

---

## 🎯 当前学习重心

LLM 时代的意图检测 — 不确定性路由混合系统 + OOS 检测改进

## 📍 最近活跃节点

- [[sources/intent-detection-age-of-llms]] — EMNLP 2024 意图检测论文 (developing)
- [[concepts/intent-detection-tods]] — 意图检测 TODS NLU 核心组件 (seed)
- [[concepts/uncertainty-routing]] — 不确定性路由混合系统 (seed)
- [[concepts/out-of-scope-detection]] — 域外检测 OOS 识别 (seed)
- [[concepts/setfit]] — SetFit 对比微调句子转换器 (seed)
- [[concepts/adaptive-in-context-learning]] — 自适应上下文学习 (seed)
- [[insights/hybrid-beats-pure-llm]] — 混合系统胜过纯 LLM (seed)
- [[concepts/monte-carlo-dropout]] — MC Dropout (seed)
- [[concepts/negative-data-augmentation]] — 负面数据增强 (seed)

## 🧵 活跃线索 / 未解问题

- 不确定性路由能否推广到其他 NLP 任务（NER、情感分析、翻译）？
- LLM OOS 检测差的根本原因（RLHF 强化"总是回答"？）
- 知识蒸馏（LLM 生成合成数据训练 SetFit）是否比混合路由更优？
- 内部表示 OOS 检测能否推广到闭源 LLM？
- 负面数据增强与真实 OOS 分布的差距如何缩小？

## ⏭️ 下次继续点

- [ ] 重跑 lint 获取最新健康指标
- [ ] 为意图检测论文生成 Flux 概念插画（intent-detection-tods, uncertainty-routing）
- [ ] 创建 Agents 领域综述页
- [ ] 探索 SetFit + 知识蒸馏方案
- [ ] 将不确定性路由思想应用到其他领域笔记
- [ ] CAGC 与本文的方法论对比（混合策略 vs 端到端）

## 📊 库状态快照

- 总节点数: 31 (concept:19, insight:3, source:4, comparison:1, question:2)
- 领域覆盖: 7/8 (Foundations, Architecture, Training, **Agents**, **Engineering**, Inference, Multimodal)
- 最近 ingest: 2026-06-14 (Intent Detection in the Age of LLMs, EMNLP 2024)
- 最近修复: 2026-06-14 (系统健康全面修复)
- 最近 review: 无
- 开放 gap 数: 待 lint 统计
- 矛盾登记: 0

---

*上次更新: 2026-06-14 | 系统健康修复完成*
