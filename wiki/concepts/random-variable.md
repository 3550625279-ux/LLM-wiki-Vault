---
type: concept
title: "随机变量"
created: 2026-06-16
updated: 2026-06-16
tags: [概率论, 基础, 随机变量]
status: seed
complexity: basic
domain: Foundations
sources: ["[[sources/random-variable-random-vector]]"]
related:
  - "depends_on::[[concepts/sample-space]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/random-variable-random-vector]]"
  - "extends::[[concepts/random-vector]]"
  - "applied_in::[[concepts/cross-entropy-loss]]"
---

## 🔗 关系链接

- depends_on: [[concepts/sample-space]]
- belongs_to: [[domains/Foundations]]
- produced_by: [[sources/random-variable-random-vector]]
- extends: [[concepts/random-vector]]
- applied_in: [[concepts/cross-entropy-loss]]

---

# 随机变量

## 核心定义

**随机变量**是一个函数 X: Ω → R，将样本空间中的每个样本点 ω 映射到一个实数。

```
X(ω) = x,  其中 ω ∈ Ω, x ∈ R
```

## 关键洞察：映射本身是 100% 确定的

这是理解随机变量最关键的一点：

> **映射 X 本身是完全确定的函数**，不存在任何随机性。随机性的唯一来源是输入 ω 的不可预知性。

类比理解：
- **Hash Function**：给定输入，输出完全确定。但你不知道下一个输入是什么
- **特征提取器**：图片 → 数值向量的映射是确定的，但你不知道下一张图片是什么

### Python 代码演示

```python
import random

# 随机变量 X：掷骰子结果
def X(omega):
    """这是一个完全确定的函数"""
    return omega  # 直接映射，100% 确定

# 随机性来自 omega 的产生过程
omega = random.randint(1, 6)  # 这一步才是随机的
x = X(omega)                  # 这一步完全确定
print(f"omega={omega}, X(omega)={x}")
```

映射 `X(omega)` 永远返回 `omega` 本身——它是确定性的。不确定性来自 `random.randint` 产生的 ω。

## 指示随机变量

**指示随机变量** I_A(ω) 是最简单的一类随机变量：

```
I_A(ω) = 1,  若 ω ∈ A
I_A(ω) = 0,  若 ω ∉ A
```

- 只输出 0 或 1
- 用于将"事件是否发生"转化为数值
- 期望 E[I_A] = P(A)（事件概率 = 指示变量的期望）

### One-Hot 编码

**One-Hot 编码**是一组指示随机变量构成的编码方式：

对于有 K 个类别的分类问题，定义 K 个指示变量：
- I₁(ω) = 1 当且仅当类别 = 1
- I₂(ω) = 1 当且仅当类别 = 2
- ...
- Iₖ(ω) = 1 当且仅当类别 = K

输出向量 [I₁, I₂, ..., Iₖ] 就是 One-Hot 编码，恰好有一个位置为 1。

## AI 应用场景

### 分类标签

在分类任务中，标签 Y 本质上是一个随机变量：
- Y: Ω → {0, 1, ..., K-1}（离散随机变量）
- 每个样本 ω 对应一个类别标签 Y(ω)

### Softmax 输出

模型的 Softmax 输出 P(y|x) 给出了随机变量 Y 在条件 x 下的概率分布：
- 不是随机变量本身，而是随机变量的**概率分布**

### 与损失函数的关系

交叉熵损失 H(Y, P) 直接建立在随机变量的分布之上——理解随机变量是理解损失函数的前提。

---

*创建: 2026-06-16 | 概率论基础系列*
