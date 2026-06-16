---
type: concept
title: "BatchNorm：批量归一化"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, 归一化, BatchNorm]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/random-variable-random-vector]]", "[[sources/central-limit-theorem]]"]
related:
  - "depends_on::[[concepts/central-limit-theorem]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/random-variable-random-vector]]"
  - "contrasts::[[concepts/layer-normalization]]"
  - "applied_in::[[concepts/resnet]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/central-limit-theorem]]
- produced_by: [[sources/random-variable-random-vector]]
- contrasts: [[concepts/layer-normalization]]
- applied_in: [[concepts/resnet]]

---

# BatchNorm：批量归一化

## BN 的操作

对同一特征位置，跨 batch 内所有样本计算统计量：

$$\mu_B = \frac{1}{m}\sum_{i=1}^m x_i, \quad \sigma_B^2 = \frac{1}{m}\sum_{i=1}^m (x_i - \mu_B)^2$$

标准化：

$$\hat{x}_i = \frac{x_i - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}$$

## 可学习参数 γ 和 β

标准化后，网络还学习两个参数：

$$y_i = \gamma \hat{x}_i + \beta$$

- $\gamma$（缩放）：学习最优标准差
- $\beta$（偏移）：学习最优均值

**直觉**：如果网络发现某层"不标准化"效果更好，它可以学到 $\gamma = \sigma_B$、$\beta = \mu_B$，把标准化完全撤销。BN 不是强制归一化，而是给网络一个"选择归一化程度"的能力。

## 数学手术验证

标准化后的统计性质：

- **一阶矩归零**：$E[\hat{x}] = 0$
- **二阶矩归一**：$\text{Var}(\hat{x}) = 1$

验证：$E[\hat{x}] = E\left[\frac{x - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}}\right] = \frac{E[x] - \mu_B}{\sqrt{\sigma_B^2 + \epsilon}} = 0$

## BN 有效的学术争议

### 原始论文的解释（Ioffe & Szegedy, 2015）

**Internal Covariate Shift (ICS)**：训练过程中，每层输入的分布不断变化，导致训练困难。BN 通过稳定每层输入的分布来加速训练。

### 后续研究的反驳

Santurkar et al. (2018) "How Does Batch Normalization Help Optimization?" 指出：

- BN 并没有显著减少 ICS
- BN 真正的作用是**平滑损失函数景观（Loss Landscape Smoothing）**
- 使损失函数的梯度更 Lipschitz 连续，优化更稳定

## 概率论视角：大数定律直接适用

BN 的核心假设是 batch 内样本独立。当 batch size $m$ 足够大时：

- $\mu_B \to E[x]$（大数定律）
- $\sigma_B^2 \to \text{Var}(x)$（大数定律）

这就是为什么 BN 在大 batch size 下效果好、小 batch size 下不稳定的原因。小 batch 时统计量噪声大，归一化不准确。

## 与 LayerNorm 的对比

见 [[concepts/layer-normalization]] 的 BN vs LN 对比表。
