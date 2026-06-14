---
type: concept
title: "Multimodal Intent Recognition (MIR) 多模态意图识别"
created: 2026-06-14
updated: 2026-06-14
tags: [多模态, 意图识别, 跨模态融合]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["[[sources/cagc-cvpr2024]]"]
related:
  - "belongs_to::[[domains/Multimodal]]"
  - "extends::[[concepts/multimodal-sentiment-analysis]]"
  - "applied_in::[[sources/cagc-cvpr2024]]"
  - "depends_on::[[concepts/multimodal-fusion]]"
  - "produced_by::[[sources/cagc-cvpr2024]]"
thumbnail: ""
---

# Multimodal Intent Recognition (MIR) 多模态意图识别

## 定义

多模态意图识别 (MIR) 是通过整合**语言、视觉和听觉**三种模态来理解人类意图的任务。与单模态意图识别不同，MIR 面临模态间表达不一致、意图歧义等独特挑战。

---

## 任务背景

### 单模态意图识别
- **文本意图**：从文字中理解意图（对话系统、文本修订）
- **视觉意图**：从图像中理解意图（政治决策、图像描述）

### 多模态意图识别
- 同时利用语言、视觉、听觉三种模态
- 处理模态间的异质性和不一致性
- 通过多模态互补提高意图理解准确性

---

## 核心挑战

1. **意图歧义**：同一句话在不同场景下可能表达不同意图
2. **模态不一致**：三种模态可能给出矛盾的信号
3. **上下文依赖**：意图理解需要考虑说话者所处的场景
4. **模态对齐**：不同模态的序列长度和特征维度不同

---

## 典型数据集

| 数据集 | 规模 | 任务 | 模态 |
|--------|------|------|------|
| MIntRec | 2,224 样本 | 意图识别（20类/二分类） | 文本+视觉+听觉 |
| CMU-MOSI | 2,199 样本 | 情感分析（-3到3） | 文本+视觉+听觉 |

---

## 代表方法

| 方法 | 核心思想 |
|------|---------|
| MAG-BERT | 多模态适应门控 |
| MulT | 跨模态 Transformer |
| MISA | 模态不变/特定表示 |
| **CAGC** | 跨视频上下文 + 全局对比学习 |

---

## 相关概念

- [[concepts/context-augmented-transformer]] — CAGC 的核心模块
- [[concepts/global-context-guided-contrastive-learning]] — CAGC 的对比学习方案
- [[concepts/cross-video-bank]] — CAGC 的跨视频记忆库

---

*MIR 多模态意图识别 | CAGC 论文目标任务 | CVPR 2024*
