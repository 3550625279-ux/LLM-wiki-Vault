---
type: concept
title: "对比学习 (Contrastive Learning)"
created: 2026-06-14
updated: 2026-06-14
tags: [对比学习, 表示学习, 自监督学习, 训练范式]
status: seed
complexity: intermediate
domain: Training
sources: []
related:
  - "belongs_to::[[domains/Training]]"
  - "applied_in::[[concepts/global-context-guided-contrastive-learning]]"
  - "applied_in::[[concepts/cross-video-bank]]"
  - "extended_by::[[concepts/global-context-guided-contrastive-learning]]"
thumbnail: ""
---

# 对比学习 (Contrastive Learning)

> **一句话**：通过拉近正样本对、推远负样本对来学习表示空间，是自监督和多模态对齐的核心训练范式。

---

## 核心思想

对比学习的目标是学习一个表示空间，使得：
- **正样本对**（语义相似的样本）在嵌入空间中距离**近**
- **负样本对**（语义不同的样本）在嵌入空间中距离**远**

## 关键方法演进

| 方法 | 年份 | 核心创新 |
|------|------|----------|
| SimCLR | 2020 | 大 batch + 数据增强构建正负对 |
| MoCo | 2020 | 动量编码器 + 队列维护负样本 |
| CLIP | 2021 | 图文对比，跨模态对齐 |
| GCCL | 2024 | 全局上下文引导，突破 mini-batch 限制 |

## 核心损失函数

**InfoNCE Loss**:
$$\mathcal{L} = -\log \frac{\exp(\text{sim}(z_i, z_j) / \tau)}{\sum_{k=1}^{N} \exp(\text{sim}(z_i, z_k) / \tau)}$$

- $\tau$：温度参数（控制分布锐度）
- $\text{sim}$：余弦相似度
- 关键超参数：温度 $\tau$、batch size、负样本数量

## 在本库中的应用

- [[concepts/global-context-guided-contrastive-learning]] — GCCL 将对比学习从 mini-batch 扩展到全数据集
- [[concepts/cross-video-bank]] — Bank 为对比学习提供跨视频正负样本
- [[sources/cagc-cvpr2024]] — CAGC 框架的核心训练信号

---

*占位页（seed）| 待后续 ingest 完善（SimCLR/MoCo/CLIP 论文）*
