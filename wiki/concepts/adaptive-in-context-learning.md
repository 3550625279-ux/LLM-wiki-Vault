---
type: concept
title: "自适应上下文学习（Adaptive In-Context Learning）"
created: 2026-06-14
updated: 2026-06-14
tags: [ICL, 上下文学习, LLM, 提示工程]
status: seed
complexity: intermediate
domain: Agents
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Agents]]"
  - "extends::[[concepts/intent-detection-tods]]"
  - "part_of::[[concepts/uncertainty-routing]]"
  - "contrasts::[[concepts/setfit]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 自适应上下文学习（Adaptive In-Context Learning）

## 定义

自适应上下文学习是一种 LLM 推理策略：根据当前查询，从训练数据中动态检索最相关的示例作为 ICL 示例嵌入 prompt 中，引导 LLM 完成任务。相比固定 ICL 示例，"自适应"体现在**每个查询的 ICL 示例不同**。

## 工作流程

```
离线阶段:
1. 用句子转换器（BGE）编码所有训练样本 → 存入向量数据库
2. 用 LLM 为每个意图生成描述

在线推理:
1. 编码用户查询 → 查询向量 v_q
2. 对每个意图: 检索相似度 > t 的 Top-K 最相似训练样本
3. 构建 Prompt:
   [任务指令] + [意图描述列表] + [ICL 示例（按相似度降序）] + [用户查询]
4. LLM 生成推理链（CoT）→ 输出意图预测
```

## 关键技术细节

| 技巧 | 原因 |
|------|------|
| **标签名随机化** | 防止 LLM 依赖标签名的表面语义（Label-xx 替换） |
| **ICL 示例按相似度降序** | 最相关的示例对 LLM 影响最大 |
| **标签顺序固定** | 避免 LLM 对 prompt 中位置的偏好 |
| **意图描述由 LLM 生成** | 用 Claude v3 Sonnet 统一生成，保持一致性 |

## 超参数

| 参数 | 搜索范围 | 说明 |
|------|---------|------|
| k（ICL 示例数） | {0, 1, 5, 10, 20} | 不是越多越好 |
| t（检索阈值） | {1e-5, 0.3, 0.5, 0.7} | 控制示例质量 |

**发现**：k 有最优值，过多 ICL 示例可能引入噪声或超出上下文窗口。

## 与标准 ICL 的区别

| 维度 | 标准 ICL | 自适应 ICL |
|------|---------|-----------|
| 示例选择 | 固定/随机 | 按查询相似度动态检索 |
| 示例来源 | 人工挑选 | 向量检索自动生成 |
| 每个查询 | 相同示例 | 不同示例 |
| 可扩展性 | 受限于人工标注 | 自动适应新数据 |

## 与向量检索的关系

本文的自适应 ICL 检索机制与 [[concepts/cross-video-bank]] 的 embedding 检索方法类似——都使用 embedding 相似度检索 top-K 最相关条目。区别在于应用场景不同（对话意图 vs 视频理解）。

## 来源

- 应用: [[sources/intent-detection-age-of-llms]]
- 检索器: BAAI/bge-base-en-v1.5
