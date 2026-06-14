---
type: concept
title: "Global Context-guided Contrastive Learning (GCCL) 全局上下文引导对比学习"
created: 2026-06-14
updated: 2026-06-14
tags: [对比学习, 全局对比, 模态对齐, InfoNCE]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["[[sources/cagc-cvpr2024]]"]
related:
  - "belongs_to::[[domains/Multimodal]]"
  - "depends_on::[[concepts/cross-video-bank]]"
  - "extends::[[concepts/contrastive-learning]]"
  - "part_of::[[concepts/multimodal-intent-recognition]]"
  - "contrasts::[[concepts/mini-batch-contrastive-learning]]"
  - "contrasts::[[comparisons/cagc-vs-baselines]]"
  - "produced_by::[[sources/cagc-cvpr2024]]"
thumbnail: ""
---

# GCCL: Global Context-guided Contrastive Learning

## 定义

GCCL 是 CAGC 方法中的全局上下文引导对比学习方案。与传统 mini-batch 内的局部对比不同，GCCL 利用整个训练数据集的**全局上下文特征**作为监督信号，增强跨模态对齐，减少模态差异。

---

## 两层对比结构

### 局部对比 (Local Contrast)

在 mini-batch 内构造正负样本对：

```
Anchor:  文本特征 h_t
正样本:  同意图标签的听觉/视觉特征
负样本:  不同意图标签的听觉/视觉特征

L_ta = InfoNCE(h_t, h_a)   # 文本-听觉
L_tv = InfoNCE(h_t, h_v)   # 文本-视觉
```

### 全局对比 (Global Contrast)

跨整个数据集构造正负样本对：

```
Anchor:  文本特征 h_t
正样本:  跨视频中意图相同的全局融合特征 h_g
负样本:  跨视频中意图不同的全局融合特征 h_g

L_g = InfoNCE(h_t, h_g)
```

---

## 为什么文本作为锚点？

研究表明文本模态在意图识别中具有最大的重要性（Han et al., 2021）。因此：
- 文本 = 最可靠的意图信号 → 作为 anchor
- 视觉/听觉 = 文本的增强版本 → 作为正/负样本

---

## 训练损失

```
L_total = L_task + α(L_ta + L_tv) + β·L_g
```

| 符号 | 含义 | 默认值 |
|------|------|--------|
| L_task | 意图分类交叉熵 | - |
| α | 局部对比权重 | 0.02 |
| β | 全局对比权重 | 0.02 |
| τ | 温度参数 | 0.7 |

---

## 与传统对比学习的区别

| 维度 | Mini-batch 对比 | GCCL 全局对比 |
|------|----------------|---------------|
| 对比范围 | 当前 batch | 整个数据集 |
| 监督信号 | 样本特征 | 跨视频上下文特征 |
| 信息丰富度 | 有限 | 更丰富 |
| 计算开销 | 低 | 较高 |

---

## 消融实验

| 变体 | ACC (20类) | 性能下降 |
|------|-----------|---------|
| 完整 CAGC | 73.39% | - |
| 去掉 L_g | 72.22% | -1.17% |
| 去掉 L_l | 72.31% | -1.08% |
| 去掉 L_g 和 L_l | 71.66% | -1.73% |

全局和局部对比互补，去掉任何一个都会显著降低性能。

---

## 相关概念

- [[concepts/contrastive-learning]] — GCCL 的基础
- [[concepts/cross-video-bank]] — 全局对比的数据来源
- [[concepts/context-augmented-transformer]] — 生成全局融合特征的模块

---

*GCCL 全局上下文引导对比学习 | CAGC 论文核心组件 | CVPR 2024*
