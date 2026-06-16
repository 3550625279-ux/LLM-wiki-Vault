---
type: concept
title: "意图检测（Intent Detection for TODS）"
created: 2026-06-14
updated: 2026-06-14
tags: [意图检测, NLU, TODS, 对话系统]
status: seed
complexity: intermediate
domain: Agents
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Agents]]"
  - "part_of::[[concepts/out-of-scope-detection]]"
  - "extends::[[concepts/multimodal-intent-recognition]]"
  - "applied_in::[[concepts/setfit]]"
  - "applied_in::[[concepts/adaptive-in-context-learning]]"
  - "applied_in::[[concepts/uncertainty-routing]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 意图检测（Intent Detection for TODS）

## 🔗 关系链接

- belongs_to: [[domains/Agents]]
- part_of: [[concepts/out-of-scope-detection]]
- extends: [[concepts/multimodal-intent-recognition]]
- applied_in: [[concepts/setfit]] | [[concepts/adaptive-in-context-learning]] | [[concepts/uncertainty-routing]]
- produced_by: [[sources/intent-detection-age-of-llms]]

---

## 定义

意图检测是任务导向对话系统（TODS）自然语言理解层的核心组件，负责将用户在每个对话轮次的查询映射到系统可执行的动作。

```
用户查询 → [意图检测系统] → 已知意图 / OOS（拒绝）
例: "帮我查订单状态" → 查询订单意图
例: "今天天气真好" → OOS（不属于任何已知意图）
```

## 任务特征

意图检测不同于标准文本分类，有以下独特挑战：

| 特征 | 说明 |
|------|------|
| **OOS 拒绝** | 必须能识别不属于任何已知意图的查询（开放集识别） |
| **意图范围差异大** | 从非常宽泛（"产品推荐"）到非常具体（"按电池寿命推荐笔记本"） |
| **少样本** | 每个意图可能只有少量训练样本 |
| **数据不平衡** | 训练数据来自非 ML 专家的 bot 开发者 |
| **多标签** | 一个查询可能同时映射多个意图 |

## 方法演进

```
监督分类 (BERT) → 少样本学习 (SetFit) → LLM ICL → 混合系统
```

1. **传统方法**：监督分类 / 句子转换器 → 数据需求大、OOS 差
2. **LLM 方法**：自适应 ICL + CoT → 准确率高但延迟大、成本高
3. **混合系统**：不确定性路由 → 兼顾准确率和延迟（核心创新）

## 意图体系设计洞察

来自控制实验的关键发现：
- **细粒度标签** > 宽泛标签（对 LLM 的 OOS 检测更友好）
- **小标签空间** > 大标签空间（标签越多，OOS 检测退化越严重）

## 应用场景

- 客户服务对话机器人
- 语音助手（Alexa、Siri）
- 智能客服系统
- RAG 系统中的知识源路由

## 相关节点

- OOS 检测：[[concepts/out-of-scope-detection]]
- 多模态意图识别（不同领域但相关概念）：[[concepts/multimodal-intent-recognition]]
- 方法实现：[[concepts/setfit]]、[[concepts/uncertainty-routing]]
- 来源论文：[[sources/intent-detection-age-of-llms]]
