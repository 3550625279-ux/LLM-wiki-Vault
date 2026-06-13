---
title: "Foundations — 数学与理论基础"
type: domain
status: seed
domain: Foundations
tags: [math, probability, optimization, information-theory]
created: 2026-06-13
updated: 2026-06-13
confidence: high
---

# Foundations — 数学与理论基础

> **领域使命**: 为所有 AI/ML 概念提供数学根基。这里的知识是最稳定的，很少被推翻。
> **学习建议**: 不需要全部精通，但需要"够用"——能看懂论文公式，理解优化行为。

---

## 📌 领域地图

```
Foundations
├── 线性代数
│   ├── 矩阵乘法、转置、逆
│   ├── 特征值与特征向量
│   ├── SVD (奇异值分解)
│   └── 张量操作
│
├── 概率论与统计
│   ├── 条件概率、贝叶斯定理
│   ├── 常见分布 (Gaussian/Categorical/Dirichlet)
│   ├── 期望、方差、协方差
│   ├── 最大似然估计 (MLE)
│   └── 贝叶斯推断
│
├── 信息论
│   ├── 熵 (Shannon Entropy)
│   ├── 交叉熵损失函数
│   ├── KL 散度
│   └── 互信息
│
├── 优化理论
│   ├── 梯度下降 (SGD/Momentum/Adam)
│   ├── 学习率调度
│   ├── 二阶方法简介
│   └── 非凸优化挑战
│
└── 统计学习理论
    ├── 偏差-方差 trade-off
    ├── 正则化原理
    └── 泛化边界 (简介)
```

---

## 🧮 核心概念节点

### 线性代数
- [ ] [[concepts/matrix-multiplication]] — 矩阵乘法与注意力的关系
- [ ] [[concepts/svd]] — SVD 与低秩近似
- [ ] [[concepts/eigendecomposition]] — 特征分解

### 概率论
- [ ] [[concepts/bayes-theorem]] — 贝叶斯定理
- [ ] [[concepts/maximum-likelihood-estimation]] — MLE
- [ ] [[concepts/gaussian-distribution]] — 高斯分布在 AI 中的角色

### 信息论
- [ ] [[concepts/entropy]] — 熵的定义与直觉
- [ ] [[concepts/cross-entropy-loss]] — 为什么用交叉熵训练 LLM
- [ ] [[concepts/kl-divergence]] — KL 散度与 RLHF

### 优化
- [ ] [[concepts/gradient-descent]] — 梯度下降变体
- [ ] [[concepts/adam-optimizer]] — Adam 为什么有效
- [ ] [[concepts/learning-rate-schedule]] — 预热 + 余弦退火

---

## 🔗 领域间关系

- `precedes::` [[domains/architecture]] — 理解架构需要线性代数
- `precedes::` [[domains/training]] — 理解训练需要优化理论
- `precedes::` [[domains/alignment]] — 理解对齐需要信息论（KL散度）

---

## 💡 领域关键洞察

- 深度学习为什么能泛化？理论上还没有令人满意的答案。
- Adam 不是最优优化器，但实践中最鲁棒。
- 交叉熵损失 = 最大化训练集上的对数似然。

---

## 📖 推荐资料

- [ ] 3Blue1Brown "Essence of Linear Algebra" 系列
- [ ] Bishop "Pattern Recognition and Machine Learning" Ch.1-2
- [ ] Goodfellow et al. "Deep Learning" Ch.2-4
- [ ] Information Theory, Inference, and Learning Algorithms (MacKay)

---

## 📊 领域统计

```
concept 节点: 0 (目标: 15+)
entity 节点:  0
maturity:    seed
```
