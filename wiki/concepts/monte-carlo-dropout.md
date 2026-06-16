---
type: concept
title: "Monte Carlo Dropout"
created: 2026-06-14
updated: 2026-06-14
tags: [MC Dropout, 不确定性估计, 贝叶斯深度学习]
status: seed
complexity: intermediate
domain: Foundations
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Foundations]]"
  - "applied_in::[[concepts/uncertainty-routing]]"
  - "extends::[[concepts/setfit]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# Monte Carlo Dropout

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- applied_in: [[concepts/uncertainty-routing]]
- extends: [[concepts/setfit]]
- produced_by: [[sources/intent-detection-age-of-llms]]

---

## 定义

Monte Carlo (MC) Dropout 是一种用标准 Dropout 网络近似贝叶斯不确定性估计的方法。由 Gal & Ghahramani (2016) 提出，证明 Dropout 训练的网络在推理时保持 Dropout 开启并多次前向传播，可以近似变分贝叶斯推断。

## 核心原理

```
标准推理: Dropout OFF → 单次前向传播 → 确定性输出
MC Dropout: Dropout ON → M 次前向传播（每次掩码不同）→ 分布估计

每次前向传播 ≈ 从后验分布 q(θ) 中采样一次
M 次采样的统计量 ≈ 预测分布的估计
```

**形式化**：
```
p(y|x, D) ≈ (1/M) Σ p(y|x, θ_m),  θ_m ~ q(θ)

预测均值 = (1/M) Σ ŷ_m
预测方差 = (1/M) Σ (ŷ_m - ŷ_mean)²  ← 不确定性估计
```

## 不确定性类型

| 类型 | 含义 | MC Dropout 能否捕获 |
|------|------|-------------------|
| **认知不确定性** (Epistemic) | 模型参数的不确定性，可通过更多数据减少 | ✅ 可以 |
| **偶然不确定性** (Aleatoric) | 数据固有噪声，不可减少 | ❌ 不能 |

## 在意图检测中的应用

来自 [[sources/intent-detection-age-of-llms]] 的实现：
- **Dropout 率**：0.1（同时在 hidden layers 和 attention layers）
- **采样数 M**：通常 10 次
- **不确定性度量**：不直接用概率方差，而是统计预测标签的一致性

```
M=10 次采样标签: [A, A, A, B, A, A, A, A, A, A]
unique_labels = 2 > 1 → 不确定

M=10 次采样标签: [A, A, A, A, A, A, A, A, A, A]
unique_labels = 1 → 确定
```

## 优势

1. **实现简单**：只需在推理时保持 Dropout 开启，无需修改训练过程
2. **理论保证**：Gal & Ghahramani 证明了与贝叶斯推断的近似关系
3. **通用性**：可用于任何带 Dropout 的网络
4. **零额外训练成本**：与标准训练完全一致

## 局限

1. 只捕获认知不确定性，不捕获偶然不确定性
2. 需要足够大的 M（太小则估计不稳定）
3. Dropout 率需要调优（任务依赖）
4. 推理成本线性增加 M 倍
5. 是贝叶斯推断的粗糙近似

## 来源

- 原始论文: Gal & Ghahramani, "Dropout as a Bayesian Approximation" (2016)
- 应用: [[sources/intent-detection-age-of-llms]]
