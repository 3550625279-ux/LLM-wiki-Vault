---
type: concept
title: "前推测度"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 测度论, 前推测度]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/random-variable-random-vector]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/random-variable-random-vector]]"
---

## 🔗 关系链接

- depends_on: [[concepts/random-variable]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/random-variable-random-vector]]

---

# 前推测度

## 核心定义

**前推测度**（Pushforward Measure）是随机变量将概率从样本空间 Ω "推"到实数轴 R 上的结果。

给定随机变量 X: Ω → R，前推测度 P_X 定义为：

```
P_X(B) = P({ω ∈ Ω | X(ω) ∈ B})
```

其中 B 是实数轴上的一个可测集合（如区间、单点等）。

### 直觉理解

想象一个搬运过程：
1. 原始概率 P 分布在样本空间 Ω 上
2. 随机变量 X 将每个 ω 映射到实数 x
3. 前推测度 P_X 把概率"搬运"到实数轴上

**X 是搬运工，P_X 是搬运后的结果。**

## 计算示例：抛两次硬币

设 Ω = {HH, HT, TH, TT}，每个样本点概率为 1/4。

定义随机变量 X = 正面出现的次数：
- X(HH) = 2
- X(HT) = 1
- X(TH) = 1
- X(TT) = 0

前推测度 P_X：
```
P_X({0}) = P({TT})     = 1/4
P_X({1}) = P({HT, TH}) = 2/4 = 1/2
P_X({2}) = P({HH})     = 1/4
```

| x | 0 | 1 | 2 |
|---|---|---|---|
| P_X(x) | 1/4 | 1/2 | 1/4 |

这就是二项分布 B(2, 1/2)——前推测度把"抛硬币"的物理实验变成了实数轴上的概率分布。

## 重大意义

前推测度的核心价值：

> **把复杂的物理现象的概率，变成纯粹的实数轴上的数学分布。**

一旦得到 P_X，我们就可以：
- 用 CDF（累积分布函数）描述：F_X(x) = P_X((-∞, x])
- 用 PDF/PMF 描述分布的密度
- 计算期望、方差等统计量
- 进行假设检验、置信区间等统计推断

**不需要再关心原始样本空间 Ω 是什么**——所有信息都压缩到了实数轴上。

## AI 应用场景

### 神经网络输出的概率分布

神经网络的最后一层输出经过 Softmax 后，得到的就是一个前推测度：
- 输入空间（如图片空间）被映射到概率单纯形
- 模型学习的就是这个从前推测度

### 生成模型

生成模型的目标是学习数据的前推测度 P_X：
- GAN 的判别器在比较两个前推测度（真实分布 vs 生成分布）
- Diffusion Model 通过逐步去噪学习逆映射

---

*创建: 2026-06-16 | 概率论基础系列*
