---
type: comparison
title: "CAGC vs 多模态意图识别基线方法对比"
created: 2026-06-14
updated: 2026-06-14
tags: [多模态意图识别, 对比学习, 跨视频建模]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["[[sources/cagc-cvpr2024]]"]
related:
  - "contrasts::[[concepts/context-augmented-transformer]]"
  - "contrasts::[[concepts/global-context-guided-contrastive-learning]]"
  - "produced_by::[[sources/cagc-cvpr2024]]"
thumbnail: ""
---

# CAGC vs 多模态意图识别基线方法对比

## 🔗 关系链接

- contrasts: [[concepts/context-augmented-transformer]] | [[concepts/global-context-guided-contrastive-learning]]
- produced_by: [[sources/cagc-cvpr2024]]

---

## 对比对象

| 方法 | 会议/年份 | 核心思想 | 与 CAGC 的关系 |
|------|----------|---------|---------------|
| **MAG-BERT** | EMNLP 2020 | 多模态适应门控，在 BERT 微调时注入非语言信息 | CAGC 的直接基线 |
| **MulT** | ACL 2019 | 跨模态 Transformer，使用跨模态注意力 | CAGC 的直接基线 |
| **MISA** | ACMMM 2020 | 模态不变/特定双子空间投影 | CAGC 的直接基线（最强） |
| **ConFEDE** | ACL 2022 | 统一对比学习框架，样本内+样本间对比 | 相关方法，CAGC 在 CMU-MOSI 上对比 |
| **HyCon** | - | 层次化对比学习用于多模态情感 | 相关方法 |

---

## 核心差异

### 1. 建模范围

| 方法 | 建模范围 | 局限 |
|------|---------|------|
| MAG-BERT | 单个视频 | 忽略跨视频上下文 |
| MulT | 单个视频 | 跨模态但不跨视频 |
| MISA | 单个视频 | 模态子空间投影但无全局信息 |
| **CAGC** | **跨视频** | ✅ 利用跨视频上下文消歧 |

### 2. 对比学习策略

| 方法 | 对比范围 | 监督信号 |
|------|---------|---------|
| ConFEDE | mini-batch 内 | 样本特征 |
| HyCon | mini-batch 内 | 样本特征 |
| **CAGC (GCCL)** | **整个数据集** | **全局上下文特征** |

### 3. 跨视频上下文质量

| 方法 | 是否有跨视频机制 | 视频源筛选 |
|------|----------------|-----------|
| 通用跨视频方法 | ✅ | 仅场景相似度 |
| **CAGC** | ✅ | **场景相似度 + 意图一致性** |

---

## 实验结果对比

### MIntRec（意图识别）

| 方法 | 20类 ACC | 20类 F1 | Binary ACC |
|------|----------|---------|------------|
| MAG-BERT | 72.65 | 68.64 | 89.24 |
| MulT | 72.52 | 69.25 | 89.19 |
| MISA | 72.29 | 69.32 | 89.21 |
| **CAGC** | **73.39** | **70.09** | **90.11** |

### CMU-MOSI（情感分析）

| 方法 | ACC-2 | F1 | ACC-7 |
|------|-------|-----|-------|
| MISA | 82.10 | 82.0 | 41.4 |
| Self-MM | 85.46 | 85.43 | 46.67 |
| ConFEDE | 85.52 | 85.52 | 42.27 |
| **CAGC** | **85.70** | **85.60** | 44.80 |

**注意**: CAGC 在 CMU-MOSI 上提升不如 MIntRec 显著，可能因为情感分析对跨视频上下文的依赖程度低于意图识别。

---

## 设计哲学对比

```
MAG-BERT:   "在微调时融入非语言信息" → 模态适应
MulT:       "跨模态注意力替代自注意力" → 跨模态交互
MISA:       "分解为模态不变+特定子空间" → 表示分解
ConFEDE:    "样本内+样本间统一对比" → 局部对比增强
CAGC:       "跨视频上下文 + 全局对比" → 全局上下文建模
```

---

*CAGC vs 基线方法对比 | CVPR 2024*
