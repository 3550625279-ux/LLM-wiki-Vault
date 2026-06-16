---
type: concept
title: "点估计"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 参数估计, 点估计]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
  - "extends::[[concepts/moment-estimation]]"
  - "extends::[[concepts/mle]]"
---

## 🔗 关系链接

- depends_on: [[concepts/random-variable]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]
- extends: [[concepts/moment-estimation]]
- extends: [[concepts/mle]]

---

# 点估计

## 核心定义

**点估计**是指通过有限样本构造一个统计量，用**一个数值**来估计未知的分布参数。

## 核心洞察：估计量本身也是随机变量

这是理解点估计最关键的一点：

> **估计量本身也是随机变量，具有随机性。** 每次采样得到的样本不同，构造出的估计值也不同。

例如，用样本均值 $\bar{X}$ 估计总体均值 $\mu$：
- 第一次采样：$\bar{X}_1 = 3.2$
- 第二次采样：$\bar{X}_2 = 3.8$
- 第三次采样：$\bar{X}_3 = 3.5$

每次得到的值不同，但围绕真实值波动。这就是估计量的随机性。

## 为什么可以估计？

**频率稳定于概率**——这是参数估计的理论根基。

当样本量 $n \to \infty$ 时，样本统计量会稳定到总体参数。大数定律保证了这一点。

## 两种主要方法

### 1. 矩估计（Method of Moments）

用样本矩估计总体矩，进而求解分布参数。

- 一阶样本矩（样本均值）→ 估计总体均值
- 二阶样本矩 → 估计总体方差

详见 [[concepts/moment-estimation]]

### 2. 极大似然估计（MLE）

把观测样本视为随机向量的一次取值，寻找使似然函数最大的参数值。

详见 [[concepts/mle]]

## 点估计 vs 区间估计

| 维度 | 点估计 | 区间估计 |
|------|--------|----------|
| 输出 | 一个数值 | 一个区间 |
| 信息量 | 只给出"最佳猜测" | 给出不确定性的范围 |
| 方法 | 矩估计、MLE | 枢轴量法 |
| 评价标准 | 无偏性、有效性、相合性 | 置信水平 |

## 相关概念

- 点估计的**质量评价**：[[concepts/estimator-quality]]（无偏性、有效性、相合性）
- 从点估计到**区间估计**：[[concepts/interval-estimation]]（枢轴量法）
- 特殊统计量：[[concepts/order-statistics]]（顺序统计量）
