---
type: concept
title: "时间反向传播 (BPTT)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, BPTT, 梯度, RNN, 训练]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/recurrent-neural-network]]"
  - "depends_on::[[concepts/gradient-clipping]]"
  - "applied_in::[[concepts/recurrent-neural-network]]"
  - "applied_in::[[concepts/gru]]"
  - "applied_in::[[concepts/lstm]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/recurrent-neural-network]] | [[concepts/gradient-clipping]]
- applied_in: [[concepts/recurrent-neural-network]] | [[concepts/gru]] | [[concepts/lstm]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 时间反向传播 (BPTT)

## 核心思想

BPTT 是标准反向传播在时间维度上的扩展。RNN 在时间步 $t$ 的损失，需要沿着时间轴回溯，计算对所有历史权重的梯度。

## 数学推导

损失函数 $L$ 是所有时间步输出的总和。对权重 $\mathbf{W}_{hh}$ 的梯度：

$$\frac{\partial L}{\partial \mathbf{W}_{hh}} = \sum_{t=1}^{T} \frac{\partial L_t}{\partial \mathbf{W}_{hh}} = \sum_{t=1}^{T} \sum_{k=1}^{t} \frac{\partial L_t}{\partial \mathbf{h}_t} \left(\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}\right) \frac{\partial \mathbf{h}_k}{\partial \mathbf{W}_{hh}}$$

其中 $\frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}} = \text{diag}(\tanh'(z_j)) \cdot \mathbf{W}_{hh}$

## 梯度消失/爆炸

关键项 $\prod_{j=k+1}^{t} \frac{\partial \mathbf{h}_j}{\partial \mathbf{h}_{j-1}}$ 是 $\mathbf{W}_{hh}$ 的矩阵连乘：

- **$\|\mathbf{W}_{hh}\| > 1$**: 连乘指数增长 → **梯度爆炸**
- **$\|\mathbf{W}_{hh}\| < 1$**: 连乘指数衰减 → **梯度消失**

这是标准 RNN 无法学习长距离依赖的根本原因。GRU 和 LSTM 通过门控机制缓解此问题。

## Truncated BPTT

实际训练中，完整 BPTT 的计算代价太高（$O(T^2)$）。截断BPTT只回传 $k$ 步：

1. 前向传播 $k$ 个时间步
2. 只在这 $k$ 步内反向传播
3. 截断计算图（`state.detach_()`），但保留隐状态的数值

这就是为什么顺序采样（路线B）中 `state.detach_()` 的意义：**保留记忆，截断梯度**。
