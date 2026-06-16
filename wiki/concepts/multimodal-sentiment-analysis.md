---
type: concept
title: "多模态情感分析"
created: 2026-06-16
updated: 2026-06-16
tags: [多模态, 情感分析, NLP]
status: seed
complexity: basic
domain: Multimodal
sources: ["综合来源"]
related:
  - "extended_by::[[concepts/multimodal-intent-recognition]]"
  - "belongs_to::[[domains/Multimodal]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Multimodal]]
- extended_by: [[concepts/multimodal-intent-recognition]]

---

# 多模态情感分析

## 定义

从多个模态（文本、语音、视觉）中联合判断说话者的情感状态（正面/负面/中性，或更细粒度的情绪类别）。

## 为什么需要多模态

- **文本**: "我很好" — 看起来是正面
- **语音**: 低沉、缓慢 — 实际是负面
- **视觉**: 眼神回避、嘴角下垂 — 验证负面

单模态可能被欺骗，多模态融合提供更准确的判断。

## 与 MIR 的关系

情感分析是 [[concepts/multimodal-intent-recognition]] 的前置任务。意图识别在此基础上更进一步：不仅判断情绪，还判断说话者想做什么（订餐、投诉、查询等）。
