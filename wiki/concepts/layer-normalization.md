---
type: concept
title: "LayerNorm：层归一化"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, 归一化, LayerNorm, Transformer]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/batch-normalization]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/central-limit-theorem]]"
  - "contrasts::[[concepts/batch-normalization]]"
  - "applied_in::[[concepts/encoder-decoder-architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/batch-normalization]]
- produced_by: [[sources/central-limit-theorem]]
- contrasts: [[concepts/batch-normalization]]
- applied_in: [[concepts/encoder-decoder-architecture]]

---

# LayerNorm：层归一化

## LN 的操作

对同一样本的所有特征求统计量：

$$\mu_L = \frac{1}{d}\sum_{i=1}^d x_i, \quad \sigma_L^2 = \frac{1}{d}\sum_{i=1}^d (x_i - \mu_L)^2$$

标准化：

$$\hat{x}_i = \frac{x_i - \mu_L}{\sqrt{\sigma_L^2 + \epsilon}}$$

## 概率论基础较弱

与 BN 不同，LN 的概率论基础较弱：

- BN 跨 batch 统计，样本独立，大数定律直接适用
- LN 在同一 token 的不同特征上统计，**这些特征通常不是来自同一分布的独立样本**

例如，Transformer 中一个 token 的 768 维隐藏向量，每个维度可能编码完全不同的语义信息。把它们当作"独立样本"来算均值方差，在概率论上没有严格依据。

## LN 有效的几何解释

尽管概率论基础弱，LN 有一个强大的几何解释：

归一化后，所有 token 向量的 **L2 范数 = $\sqrt{n}$**（$n$ 为特征维度）。

验证：$\|\hat{x}\|_2^2 = \sum_{i=1}^n \hat{x}_i^2 = \sum_{i=1}^n \frac{(x_i - \mu_L)^2}{\sigma_L^2} = \frac{n \sigma_L^2}{\sigma_L^2} = n$

这意味着：
- 所有 token 向量在超球面上均匀分布
- **点积只反映方向相似性**，不受向量长度干扰
- 注意力分数的比较变得公平

## 工程动机

| 特性 | BN | LN |
|------|----|----|
| 依赖 batch size | 是 | 否 |
| 推理时行为 | 需要 running mean/var | 每个样本独立计算 |
| 适用序列长度 | 固定 | 可变 |
| 适合场景 | CNN（固定特征分布） | Transformer（变长序列） |

LN 不依赖 batch size，每个 token 独立归一化，这使其成为 Transformer 的标准选择。

## BN vs LN 对比表

| 维度 | BatchNorm | LayerNorm |
|------|-----------|-----------|
| 统计维度 | 跨 batch，同一特征 | 同一样本，所有特征 |
| 概率论基础 | 强（大数定律） | 弱（特征未必独立） |
| 几何解释 | 统计量稳定 | L2 范数归一化 |
| batch size 依赖 | 是 | 否 |
| 典型应用 | CNN、ResNet | Transformer、GPT |
| 推理时 | 用 running statistics | 每次重新计算 |
| 序列长度 | 不敏感 | 不敏感 |
