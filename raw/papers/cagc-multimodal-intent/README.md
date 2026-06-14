# CAGC: Contextual Augmented Global Contrast for Multimodal Intent Recognition

> **CVPR 2024** | Wuhan University & Central China Normal University
> **作者**: Kaili Sun, Zhiwen Xie, Mang Ye, Huyin Zhang

---

## 📖 一句话概述

本文提出 **CAGC** 方法，通过**跨视频上下文建模**和**全局对比学习**两个核心创新，解决多模态意图识别中因单独处理每个视频而产生的感知偏差和模态不一致性问题。

---

## 🎯 难度与适用场景

| 维度 | 评估 |
|------|------|
| **难度等级** | Intermediate |
| **论文性质** | Architecture-based（新架构设计） |
| **方法复杂度** | 多阶段训练 + 三个新颖组件 |
| **预计学习时间** | 4-6 小时 |
| **前置知识** | Transformer、对比学习、多模态融合基础 |

---

## 🗂️ 材料导航

| 文件 | 内容 | 建议阅读顺序 |
|------|------|:---:|
| [summary.md](summary.md) | 背景、问题、贡献、实验结果 | ⭐ 先读 |
| [method.md](method.md) | 方法细节、算法流程、架构图 | ⭐ 核心 |
| [insights.md](insights.md) | 核心洞察、设计动机、局限性 | ⭐ 必读 |
| [qa.md](qa.md) | 15道练习题（基础/中级/高级） | 学完自测 |
| [mental-model.md](mental-model.md) | 思维模型、知识定位 | 建立全景 |
| [reflection.md](reflection.md) | 开放问题、扩展方向 | 深入思考 |
| [code/](code/) | 可运行的代码演示 | 动手实践 |
| [index.html](index.html) | 交互式概念探索器 | 辅助理解 |

---

## 🔑 核心要点

1. **跨视频上下文很重要**：单独处理每个视频会丢失全局场景信息，导致意图理解偏差
2. **Cross-video Bank 是关键创新**：通过意图倾向+场景相似度双重筛选，确保跨视频源的质量
3. **全局对比 > 局部对比**：用全局特征作为监督信号，比 mini-batch 内对比学习效果更好
4. **文本模态是锚点**：实验表明文本在意图识别中最重要，作为对比学习的 anchor

---

## 📊 关键实验结果

| 数据集 | 指标 | CAGC | 最佳基线 | 提升 |
|--------|------|------|----------|------|
| MIntRec (20类) | ACC | **73.39%** | 72.29% (MISA) | +1.10% |
| MIntRec (二分类) | ACC | **90.11%** | 89.19% (MulT) | +0.92% |
| CMU-MOSI | ACC-2 | **85.70%** | 85.52% (ConFEDE) | +0.18% |

---

## 📁 文件夹结构

```
raw/papers/cagc-multimodal-intent/
├── README.md          ← 你在这里
├── paper.pdf          ← 原始论文
├── meta.json          ← 结构化元数据
├── summary.md         ← 论文摘要
├── method.md          ← 方法详解
├── insights.md        ← 核心洞察
├── qa.md              ← 练习题
├── mental-model.md    ← 思维模型
├── reflection.md      ← 反思与扩展
├── index.html         ← 交互式探索器
├── code/              ← 代码演示
│   └── cross_video_bank_demo.py
└── images/            ← 论文图片
```

---

*CAGC 论文学习材料 | 生成于 2026-06-14*
