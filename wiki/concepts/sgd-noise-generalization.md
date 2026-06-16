---
type: concept
title: "SGD噪声与泛化"
created: 2026-06-16
updated: 2026-06-16
tags: [深度学习, SGD, 泛化, 信息论]
status: seed
complexity: advanced
domain: Foundations
sources: ["[[sources/information-theory-loss]]", "[[sources/sample-vector-geometric]]"]
related:
  - "depends_on::[[concepts/kl-divergence]]"
  - "depends_on::[[concepts/mean-as-projection]]"
  - "belongs_to::[[domains/Foundations]]"
  - "produced_by::[[sources/information-theory-loss]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/kl-divergence]] | [[concepts/mean-as-projection]]
- produced_by: [[sources/information-theory-loss]]

---

## SGD 的蒙特卡洛近似本质

SGD 用 mini-batch 梯度近似全数据集梯度，本质是蒙特卡洛采样：

$$\nabla L_{SGD}(\theta) = \frac{1}{|S|} \sum_{i \in S} \nabla \ell(\theta; x_i) \approx \nabla L_{true}(\theta)$$

这种近似引入了随机性，而这种随机性并非缺陷——它是深度学习泛化能力的关键来源之一。

## SGD 噪声的定义

SGD 噪声为：

$$\xi(\theta) = \nabla L_{SGD}(\theta) - \nabla L_{true}(\theta)$$

噪声的方差与 batch size 成反比：$\text{Var}(\xi) \propto \frac{1}{|S|}$。

## 噪声的两个关键作用

### 1. 逃离 Sharp Minimum

- **Sharp minimum**（窄深的坑）：损失曲面曲率大，梯度在坑壁上变化剧烈
- SGD 的噪声在 sharp minimum 中产生较大的随机扰动，足以把参数推离不稳定的平衡点
- 相当于在优化过程中持续施加"震荡"

### 2. 选择性地倾向 Flat Minimum

- **Flat minimum**（宽浅的坑）：损失曲面曲率小，噪声扰动后参数仍在坑内
- SGD 噪声充当了一个天然的筛选器：flat minimum 对噪声鲁棒，sharp minimum 对噪声敏感
- 长期训练后，参数几乎必然落入 flat minimum

## 信息论解释

Flat minimum 可以从信息论角度理解为**高熵解**：

| 最小值类型 | 熵 | 泛化行为 |
|-----------|-----|---------|
| Sharp minimum | 低熵 | 模型对训练数据"记忆"精确，参数空间的不确定性小 |
| Flat minimum | 高熵 | 模型捕捉更一般的规律，参数空间的不确定性大 |

**信息论直觉**：
- Sharp minimum 中，模型精确编码了训练数据的每一个细节（低熵 = 过拟合）
- Flat minimum 中，模型只编码数据的一般模式（高熵 = 泛化）

这与信息瓶颈理论（Information Bottleneck）相呼应：好的泛化需要"遗忘"训练数据的细节，只保留与任务相关的信息。

## 与归一化的联系

Batch Normalization（BN）和 Layer Normalization（LN）的正则化效果与 SGD 噪声互补：

- **BN/LN**：平滑损失曲面（降低 Lipschitz 常数），使优化更容易找到 flat minimum
- **SGD 噪声**：在平滑后的曲面上进一步筛选 flat minimum
- 两者结合的效果大于各自单独的效果

## 线性缩放规则

当 batch size 增大 k 倍时，SGD 噪声方差缩小 k 倍。为了保持相同的噪声水平（即相同的泛化特性），需要：

$$\eta_{new} = k \cdot \eta_{old}$$

即**学习率与 batch size 等比例缩放**。这个经验法则被称为"线性缩放规则"（Linear Scaling Rule），在实践中被广泛采用。

> 但注意：当 batch size 过大时，噪声过小，SGD 退化为 GD，泛化能力反而下降。这限制了 batch size 不能无限增大。
