---
type: concept
title: "极大似然估计 (MLE)"
created: 2026-06-16
updated: 2026-06-16
tags: [统计, MLE, 参数估计]
status: seed
complexity: intermediate
domain: Foundations
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/mle]]"
  - "belongs_to::[[domains/Foundations]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Foundations]]
- depends_on: [[concepts/mle]]

---

# 极大似然估计 (MLE)

> **重定向**: 此页面是 `concepts/mle` 的别名入口。详细内容请参见 → [[concepts/mle]]

MLE 的核心：选择使观测数据出现概率最大的参数值：

$$\hat{\theta}_{MLE} = \arg\max_\theta \prod_{i=1}^{n} f(x_i | \theta) = \arg\max_\theta \sum_{i=1}^{n} \log f(x_i | \theta)$$

最小化负对数似然 = 最小化交叉熵 = 训练神经网络的默认目标。
