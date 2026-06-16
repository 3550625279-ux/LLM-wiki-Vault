---
type: concept
title: "变分自编码器 (VAE)"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, 生成模型, VAE, 隐变量]
status: seed
complexity: advanced
domain: Architecture
sources: ["Kingma & Welling 2013"]
related:
  - "depends_on::[[concepts/kl-divergence]]"
  - "depends_on::[[concepts/cross-entropy-loss]]"
  - "belongs_to::[[domains/Architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/kl-divergence]] | [[concepts/cross-entropy-loss]]

---

# 变分自编码器 (VAE)

## 核心思想

VAE 是一种**生成模型**，通过学习数据的隐变量表示来生成新样本。核心是用变分推断近似后验分布。

## 损失函数（ELBO）

$$\mathcal{L} = \underbrace{\mathbb{E}_{q(z|x)}[\log p(x|z)]}_{\text{重构损失}} - \underbrace{D_{KL}(q(z|x) \| p(z))}_{\text{正则项}}$$

- **重构损失**: 解码器从隐变量重构输入的质量（交叉熵或 MSE）
- **KL 散度正则项**: 让编码器输出的分布 $q(z|x)$ 接近先验 $p(z) = \mathcal{N}(0, I)$

这正是 [[concepts/kl-divergence]] 的直接应用——KL 散度衡量编码器分布与标准正态的偏离程度。

## 重参数化技巧

$$z = \mu + \sigma \odot \epsilon, \quad \epsilon \sim \mathcal{N}(0, I)$$

将采样操作从计算图中分离，使得梯度可以通过 $\mu$ 和 $\sigma$ 反向传播。
