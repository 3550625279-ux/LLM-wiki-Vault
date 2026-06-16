---
type: concept
title: "Context-Augmented Transformer (CAT) 上下文增强 Transformer"
created: 2026-06-14
updated: 2026-06-14
tags: [注意力机制, 跨视频上下文, 渐进式学习, Transformer]
status: seed
complexity: intermediate
domain: Multimodal
sources: ["[[sources/cagc-cvpr2024]]"]
related:
  - "belongs_to::[[domains/Multimodal]]"
  - "belongs_to::[[domains/Architecture]]"
  - "depends_on::[[concepts/cross-video-bank]]"
  - "extends::[[concepts/attention-mechanism]]"
  - "part_of::[[concepts/multimodal-intent-recognition]]"
  - "contrasts::[[comparisons/cagc-vs-baselines]]"
  - "produced_by::[[sources/cagc-cvpr2024]]"
thumbnail: ""
---

# Context-Augmented Transformer (CAT) 上下文增强 Transformer

## 🔗 关系链接

- belongs_to: [[domains/Multimodal]] | [[domains/Architecture]]
- depends_on: [[concepts/attention-mechanism]]
- contrasts: [[comparisons/cagc-vs-baselines]]
- produced_by: [[sources/cagc-cvpr2024]]

---

## 定义

CAT 是 CAGC 方法中的上下文增强注意力模块，通过**渐进式地**引入 Cross-video Bank 中的跨视频特征，捕获长程上下文依赖关系，从而缓解意图理解中的感知偏差。

---

## 核心算法（Algorithm 1）

```
输入: Q = h_v (当前视频视觉特征)
      K, V = h_c (跨视频视觉特征集合)
输出: h_m (长程上下文依赖特征)

for j = 1, ..., k* do:
    K_c = h_c^{1:j+1}      # 渐进式扩展 Key
    K, V = K_c
    M_j = softmax(Q·K^T / √d) · V    # 上下文增强注意力
    M_j = mean(M_j)                     # 对跨视频维度取均值
    存储 M_j

h_m = 所有 M_j 的累积
```

**关键特征**：逐步扩展 K/V，从 1 个跨视频增加到 k* 个。

---

## 渐进式 vs 一次性

| 对比维度 | 标准 Transformer | CAT 渐进式 |
|---------|-----------------|-----------|
| K/V 范围 | 一次性所有跨视频 | 逐步扩展 |
| 噪声敏感性 | 高 | 低 |
| 学习策略 | 一次性学习 | 课程学习（先简单后复杂） |
| 信息引入 | 同时引入 | 渐进引入 |

---

## 特征融合

```
h_mv = LayerNorm(h_m + h_v)            # 残差融合
h_cv = LayerNorm(Linear(h_mv) + h_mv)  # 非线性增强
```

h_cv 是最终的上下文增强视觉特征，用于后续的全局多模态融合。

---

## 为什么渐进式更好？

1. **课程学习效果**：先学习最相关的上下文，再扩展到更多
2. **减少噪声累积**：每步只引入少量新信息
3. **更好的梯度流**：渐进式结构提供更平滑的梯度传播
4. **可解释性**：可以观察每步引入的跨视频影响

---

## 消融实验

| 变体 | ACC (20类) | 性能下降 |
|------|-----------|---------|
| 完整 CAGC | 73.39% | - |
| 去掉 CAT | 71.31% | **-2.08%** |

CAT 是 CAGC 中**最关键**的组件。

---

## 相关概念

- [[concepts/cross-video-bank]] — CAT 的数据来源
- [[concepts/global-context-guided-contrastive-learning]] — 与 CAT 协同工作的对比学习方案
- [[concepts/multimodal-intent-recognition]] — CAGC 的目标任务

---

*CAT 上下文增强 Transformer | CAGC 论文核心组件 | CVPR 2024*
