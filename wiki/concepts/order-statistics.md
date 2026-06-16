---
type: concept
title: "顺序统计量"
created: 2026-06-16
updated: 2026-06-16
tags: [统计推断, 顺序统计量]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/parameter-estimation-notes]]"]
related:
  - "depends_on::[[concepts/random-variable]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/parameter-estimation-notes]]"
  - "applied_in::[[concepts/quantile]]"
---

## 🔗 关系链接

- depends_on: [[concepts/random-variable]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/parameter-estimation-notes]]
- applied_in: [[concepts/quantile]]

---

# 顺序统计量

## 定义

$X_{(k)}$ 表示把 $n$ 个样本随机变量按递增排序后，**第 $k$ 大的那个**。

$$X_{(1)} \leq X_{(2)} \leq \dots \leq X_{(n)}$$

- $X_{(1)} = \min(X_1, \dots, X_n)$ —— 最小值（极小值）
- $X_{(n)} = \max(X_1, \dots, X_n)$ —— 最大值（极大值）
- $X_{(\lceil n/2 \rceil)}$ —— 样本中位数

## 关键性质：顺序统计量也是随机变量

> 因为样本 $X_1, \dots, X_n$ 是随机变量，所以它们的排序结果 $X_{(k)}$ 也是随机变量。

每次采样，排序后的第 $k$ 个值都可能不同。

## 分布函数的推导

### 核心思路

$F_{X_{(k)}}(x) = P(X_{(k)} \leq x)$

等价于：**至少有 $k$ 个样本 $\leq x$**。

### 推导过程

令 $Y$ = 样本中 $\leq x$ 的个数。由于每个样本独立地以概率 $F(x)$ 落在 $(-\infty, x]$ 内：

$$Y \sim B(n, F(x))$$

因此：

$$F_{X_{(k)}}(x) = P(Y \geq k) = \sum_{j=k}^{n} \binom{n}{j} [F(x)]^j [1-F(x)]^{n-j}$$

### 密度函数

对 $F_{X_{(k)}}(x)$ 求导，得到密度函数：

$$f_{X_{(k)}}(x) = \frac{n!}{(k-1)!(n-k)!} [F(x)]^{k-1} [1-F(x)]^{n-k} f(x)$$

## 极值的分布

### 最小值 $X_{(1)}$

$$F_{X_{(1)}}(x) = 1 - [1-F(x)]^n$$

$$f_{X_{(1)}}(x) = n[1-F(x)]^{n-1} f(x)$$

### 最大值 $X_{(n)}$

$$F_{X_{(n)}}(x) = [F(x)]^n$$

$$f_{X_{(n)}}(x) = n[F(x)]^{n-1} f(x)$$

## 应用

- **样本中位数**：$X_{(\lceil n/2 \rceil)}$，是稳健的位置估计量
- **极值理论**：研究 $X_{(1)}$ 和 $X_{(n)}$ 的渐近分布
- **分位数**：[[concepts/quantile]] 的计算依赖于顺序统计量
- **非参数统计**：基于顺序统计量的检验方法
