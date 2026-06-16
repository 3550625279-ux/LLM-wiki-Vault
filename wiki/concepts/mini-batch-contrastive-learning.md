---
type: concept
title: "Mini-Batch 对比学习"
created: 2026-06-16
updated: 2026-06-16
tags: [对比学习, 小批量, 表示学习]
status: seed
complexity: intermediate
domain: Training
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/contrastive-learning]]"
  - "contrasts::[[concepts/cross-video-bank]]"
  - "belongs_to::[[domains/Training]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/contrastive-learning]]
- contrasts: [[concepts/cross-video-bank]]

---

# Mini-Batch 对比学习

## 核心思想

在每个 mini-batch 内构造正负样本对，通过对比损失拉近正样本、推远负样本。

## 与 Cross-video Bank 的对比

| 特性 | Mini-Batch 对比学习 | Cross-video Bank |
|------|-------------------|-----------------|
| 负样本来源 | 当前 batch 内的其他样本 | 跨视频的持久化记忆库 |
| 时间复杂度 | $O(B^2)$（batch 内两两比较） | $O(B \cdot K)$（K 为记忆库大小） |
| 跨视频能力 | 弱（batch 内样本可能来自同一视频） | 强（显式存储跨视频表示） |
| 场景一致性 | 不保证 | 通过场景相似度匹配保证 |

[[concepts/cross-video-bank]] 的核心创新就是用持久化记忆库替代 mini-batch 内的临时负样本，解决了跨视频场景下负样本质量不足的问题。
