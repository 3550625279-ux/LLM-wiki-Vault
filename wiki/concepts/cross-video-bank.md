---
type: concept
title: "Cross-video Bank 跨视频记忆库"
created: 2026-06-14
updated: 2026-06-14
tags: [跨视频建模, 记忆库, 场景相似度, 意图一致性]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["[[sources/cagc-cvpr2024]]"]
related:
  - "belongs_to::[[domains/Multimodal]]"
  - "part_of::[[concepts/context-augmented-transformer]]"
  - "extends::[[concepts/contrastive-learning]]"
  - "applied_in::[[concepts/multimodal-intent-recognition]]"
  - "contrasts::[[concepts/mini-batch-contrastive-learning]]"
  - "contrasts::[[comparisons/cagc-vs-baselines]]"
  - "produced_by::[[sources/cagc-cvpr2024]]"
thumbnail: ""
---

# Cross-video Bank 跨视频记忆库

## 定义

Cross-video Bank 是 CAGC 方法中的核心组件，用于存储每个视频对应的**高质量跨视频集合**。通过两阶段构建（场景相似度筛选 + 意图一致性去噪），确保跨视频源的质量，为后续的上下文增强和全局对比学习提供可靠的数据基础。

---

## 两阶段构建过程

### Stage 1: 基于场景相似度的初始构建

```
Step 1: 视频级特征提取（帧均值池化）
    v̄_i = (1/F) * Σ v_{frame(j)}^i

Step 2: 场景相似度 = L2 距离
    score(v_i, v_c) = Σ (v_c^t - v_i^t)²

Step 3: Top-k 检索
    Ω(v_i) = Top-k {v_c | min score(v_i, v_c)}
```

### Stage 2: 基于意图一致性的去噪

```
投票原则: 只保留意图标签与当前视频相同的跨视频
    Ω*(v_i) = {v_c ∈ Ω(v_i) | intent(v_c) == intent(v_i)}
    其中 1 ≤ k* ≤ k
```

---

## 设计动机

**为什么需要两阶段？**

仅靠场景相似度可能引入意图不相关的干扰视频。例如：
- 两个视频场景相似（都在聚会场景）
- 但一个在讲笑话（正向意图），一个在抱怨（负向意图）
- 直接使用场景相似的视频会误导模型

Stage 2 的意图一致性筛选解决了这个问题。

---

## 关键特点

| 特点 | 说明 |
|------|------|
| 筛选维度 | 场景相似度 + 意图一致性 |
| 相似度度量 | L2 距离（视频级特征） |
| 去噪机制 | 投票原则 |
| 可变大小 | k* 可能为 1 到 k |
| 预计算 | 两阶段构建，训练前完成 |

---

## 局限性

1. **预计算开销**：需要遍历整个训练集计算相似度
2. **Stage 2 依赖标签**：需要意图标签进行去噪
3. **静态 Bank**：无法增量更新
4. **L2 距离局限**：可能无法捕获语义层面的相似性

---

## 相关概念

- [[concepts/context-augmented-transformer]] — 使用 Bank 中的跨视频进行注意力计算
- [[concepts/contrastive-learning]] — Bank 中的跨视频为对比学习提供全局正/负样本
- [[concepts/multimodal-intent-recognition]] — CAGC 的目标任务

---

*Cross-video Bank | CAGC 论文核心组件 | CVPR 2024*
