---
type: insight
title: "RNN 调参四要素：batch_size / num_steps / num_hiddens / 优化器"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, RNN, 调参, 超参数]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/recurrent-neural-network]]"
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "applied_in::[[concepts/gru]]"
  - "applied_in::[[concepts/lstm]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/recurrent-neural-network]] | [[concepts/backpropagation-through-time]]
- applied_in: [[concepts/gru]] | [[concepts/lstm]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# RNN 调参四要素

## 1. batch_size（批大小）

| 维度 | 大 Batch | 小 Batch |
|------|---------|---------|
| GPU利用率 | 高（喂饱计算单元） | 低（大量闲置） |
| 梯度质量 | 方向准确 | 有噪音（随机性） |
| 泛化能力 | 易陷入局部最优 | 震荡反而帮助跳出局部最优 |
| 顺序采样影响 | 平行轨道越多，每条越短 | 轨道更长，记忆更完整 |

## 2. num_steps（时间步长）

决定 BPTT 的截断长度：
- **短步长（如 3-5）**: 只学短期拼写规则，学不到跨越句子的语法
- **长步长（如 100+）**: 理论上能记长上下文，但梯度消失/爆炸风险剧增

## 3. num_hiddens（隐藏层维度）

隐状态 $\mathbf{h}_t$ 是**信息瓶颈**：
- **太小（32）**: 容量不足，欠拟合
- **太大（2048）**: 参数量 $O(h^2)$ 增长，过拟合 + 训练慢

## 4. 优化器选择

| 优化器 | 特点 | 适用 |
|--------|------|------|
| SGD | 严格沿梯度反方向，在峡谷地形震荡 | 简单任务 |
| Adam | 动量（惯性冲过小坑）+ 自适应学习率（陡处刹车，平处加速） | 复杂序列任务 |

**结论**：告别纯 SGD，换用 Adam（lr=0.001~0.01）是快速收敛的关键。

## 一句话总结

- 想加速 → 增大 batch_size
- 想学长句子 → 增大 num_steps + 确保 state 跨 batch 传递
- 想提升智商 → 适度增大 num_hiddens
- 想快速收敛 → 用 Adam 替代 SGD
