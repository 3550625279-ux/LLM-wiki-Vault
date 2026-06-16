---
type: source
title: "CAGC: Contextual Augmented Global Contrast for Multimodal Intent Recognition"
created: 2026-06-14
updated: 2026-06-14
tags: [多模态意图识别, 全局对比学习, CVPR, 跨视频建模]
status: developing
complexity: intermediate
domain: Multimodal
sources: ["raw/papers/cagc-multimodal-intent/paper.pdf"]
related:
  - "spawns::[[concepts/context-augmented-transformer]]"
  - "spawns::[[concepts/global-context-guided-contrastive-learning]]"
  - "spawns::[[concepts/cross-video-bank]]"
  - "spawns::[[concepts/multimodal-intent-recognition]]"
  - "spawns::[[comparisons/cagc-vs-baselines]]"
  - "extends::[[concepts/contrastive-learning]]"
  - "belongs_to::[[domains/Multimodal]]"
thumbnail: ""
---

# CAGC: Contextual Augmented Global Contrast for Multimodal Intent Recognition

## 🔗 关系链接

- spawns: [[concepts/context-augmented-transformer]] | [[concepts/global-context-guided-contrastive-learning]] | [[concepts/cross-video-bank]] | [[concepts/multimodal-intent-recognition]] | [[comparisons/cagc-vs-baselines]]
- extends: [[concepts/contrastive-learning]]
- belongs_to: [[domains/Multimodal]]

---

> CVPR 2024 | Kaili Sun, Zhiwen Xie, Mang Ye, Huyin Zhang
> Wuhan University & Central China Normal University

---

## 📄 论文基本信息

| 属性 | 值 |
|------|-----|
| 会议 | CVPR 2024 |
| 页数 | 11 |
| 代码 | 未开源 |
| 数据集 | MIntRec (意图识别), CMU-MOSI (情感分析) |
| 难度 | Intermediate |

---

## 🔍 一句话摘要

提出 CAGC 方法，通过**跨视频上下文建模**和**全局对比学习**两个核心创新，解决多模态意图识别中因单独处理每个视频而产生的感知偏差和模态不一致性问题。

---

## 🎯 核心问题

现有 MIR 方法独立处理每个视频，忽略跨视频的全局上下文信息，导致：
1. **感知偏差**：无法区分同一句话在不同场景下的不同意图
2. **模态不一致**：局部对比学习（mini-batch 内）不足以解决模态差异

---

## 💡 关键贡献

1. **CAGC 框架**：从视频内和跨视频两个维度挖掘全局上下文
2. **Context-Augmented Transformer (CAT)**：渐进式引入跨视频上下文的注意力机制
3. **Cross-video Bank**：两阶段构建（场景相似度 + 意图一致性），确保跨视频源质量
4. **GCCL**：全局上下文引导的对比学习，将整个数据集的特征作为监督信号

---

## 📊 关键实验结果

| 数据集 | 指标 | CAGC | 最佳基线 | 提升 |
|--------|------|------|----------|------|
| MIntRec (20类) | ACC | 73.39% | 72.29% (MISA) | +1.10% |
| MIntRec (二分类) | ACC | 90.11% | 89.19% (MulT) | +0.92% |
| CMU-MOSI | ACC-2 | 85.70% | 85.52% (ConFEDE) | +0.18% |

---

## 🔧 关键超参数

| 参数 | 值 | 说明 |
|------|-----|------|
| α | 0.02 | 局部对比损失权重 |
| β | 0.02 | 全局对比损失权重 |
| τ | 0.7 | 对比学习温度 |
| Top-k* | 7 | 去噪后跨视频数 |
| 学习率 | 2e-5 | Adam 优化器 |
| 隐藏维度 | 768 | 注意力头数 = 8 |

---

## 📚 详细学习材料

完整学习材料位于 Vault 内：
- `raw/papers/cagc-multimodal-intent/README.md` — 总览
- `raw/papers/cagc-multimodal-intent/summary.md` — 论文摘要
- `raw/papers/cagc-multimodal-intent/method.md` — 方法详解
- `raw/papers/cagc-multimodal-intent/insights.md` — 核心洞察
- `raw/papers/cagc-multimodal-intent/qa.md` — 15 道练习题
- `raw/papers/cagc-multimodal-intent/mental-model.md` — 思维模型
- `raw/papers/cagc-multimodal-intent/reflection.md` — 反思与扩展
- `raw/papers/cagc-multimodal-intent/code/` — 代码演示
- `raw/papers/cagc-multimodal-intent/index.html` — 交互式探索器

---

*CAGC 论文源页面 | CVPR 2024 | 生成于 2026-06-14*
