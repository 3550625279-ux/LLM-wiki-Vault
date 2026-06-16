---
title: "Foundations — 数学与理论基础"
type: domain
status: seed
domain: Foundations
tags: [math, probability, optimization, information-theory]
created: 2026-06-13
updated: 2026-06-16
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

## 🧮 已有节点

- [x] [[concepts/hyperbolic-geometry]] — 双曲几何基础（Lorentz/Poincaré 模型） | status:seed
- [x] [[concepts/monte-carlo-dropout]] — Monte Carlo Dropout 不确定性估计 | status:seed
- [x] [[concepts/sample-space]] — 样本空间与事件 | status:seed
- [x] [[concepts/random-variable]] — 随机变量 | status:seed
- [x] [[concepts/pushforward-measure]] — 前推测度 | status:seed
- [x] [[concepts/random-vector]] — 随机向量 | status:seed
- [x] [[concepts/covariance]] — 协方差 | status:seed
- [x] [[concepts/moment]] — 矩与高阶统计量 | status:seed
- [x] [[concepts/information-entropy]] — 信息熵（香农熵与自信息） | status:seed
- [x] [[concepts/cross-entropy-loss]] — 交叉熵与深度学习损失函数 | status:seed
- [x] [[concepts/kl-divergence]] — KL散度（相对熵） | status:seed
- [x] [[concepts/sgd-noise-generalization]] — SGD噪声与泛化 | status:seed
- [x] [[concepts/point-estimation]] — 点估计：用一个数值估计未知参数 | status:seed
- [x] [[concepts/moment-estimation]] — 矩估计：样本矩估计总体矩 | status:seed
- [x] [[concepts/mle]] — 极大似然估计（MLE） | status:seed
- [x] [[concepts/order-statistics]] — 顺序统计量 | status:seed
- [x] [[concepts/estimator-quality]] — 估计量评价：无偏性、有效性、相合性 | status:seed
- [x] [[concepts/interval-estimation]] — 区间估计与枢轴量 | status:seed
- [x] [[concepts/sample-vector]] — 样本向量：N次实验数据打包成高维空间中的点 | status:seed
- [x] [[concepts/mean-as-projection]] — 均值的几何本质：正交投影 | status:seed
- [x] [[concepts/centering-decoupling]] — 中心化：正交分解与信息解耦 | status:seed
- [x] [[concepts/variance-geometric]] — 方差的几何意义 | status:seed
- [x] [[concepts/degrees-of-freedom]] — 自由度与贝塞尔校正 | status:seed
- [x] [[concepts/central-limit-theorem]] — 中心极限定理（CLT） | status:seed
- [x] [[concepts/sqrt-n-origin]] — √n的来源：方差可加性 | status:seed
- [x] [[concepts/standard-deviation-l2]] — 标准差与L2范数 | status:seed
- [x] [[concepts/batch-normalization]] — BatchNorm：批量归一化 | status:seed
- [x] [[concepts/layer-normalization]] — LayerNorm：层归一化 | status:seed
- [x] [[concepts/transformer-sqrt-d]] — Transformer的√d缩放 | status:seed

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/hyperbolic-geometry]]
- `contains::` [[concepts/monte-carlo-dropout]]
- `contains::` [[concepts/sample-space]]
- `contains::` [[concepts/random-variable]]
- `contains::` [[concepts/pushforward-measure]]
- `contains::` [[concepts/random-vector]]
- `contains::` [[concepts/covariance]]
- `contains::` [[concepts/moment]]
- `contains::` [[concepts/point-estimation]]
- `contains::` [[concepts/moment-estimation]]
- `contains::` [[concepts/mle]]
- `contains::` [[concepts/order-statistics]]
- `contains::` [[concepts/estimator-quality]]
- `contains::` [[concepts/interval-estimation]]
- `contains::` [[concepts/information-entropy]]
- `contains::` [[concepts/cross-entropy-loss]]
- `contains::` [[concepts/kl-divergence]]
- `contains::` [[concepts/sgd-noise-generalization]]
- `contains::` [[concepts/sample-vector]]
- `contains::` [[concepts/mean-as-projection]]
- `contains::` [[concepts/centering-decoupling]]
- `contains::` [[concepts/variance-geometric]]
- `contains::` [[concepts/degrees-of-freedom]]
- `contains::` [[concepts/central-limit-theorem]]
- `contains::` [[concepts/sqrt-n-origin]]
- `contains::` [[concepts/standard-deviation-l2]]
- `contains::` [[concepts/batch-normalization]]
- `contains::` [[concepts/layer-normalization]]
- `contains::` [[concepts/transformer-sqrt-d]]

## 🔴 关键缺口

- `gradient-descent` — 优化基础
- `svd` — SVD 与低秩近似（理解 LoRA 需要）
- `adam-optimizer` — Adam 优化器原理
- `bayes-theorem` — 贝叶斯定理

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
concept 节点: 29 (目标: 15+) ✅ 超额完成
entity 节点:  0
source 节点:  5 (概率论系列)
maturity:    seed
```
