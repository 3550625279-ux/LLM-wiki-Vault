---
type: concept
title: "门控循环单元 (GRU)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, GRU, 门控, RNN, 序列建模]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/recurrent-neural-network]]"
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "contrasts::[[concepts/lstm]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/recurrent-neural-network]] | [[concepts/backpropagation-through-time]]
- contrasts: [[concepts/lstm]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 门控循环单元 (GRU)

## 核心思想

GRU（Cho et al., 2014）通过两个**门控信号**选择性地保留或遗忘信息，解决标准 RNN 的梯度消失问题。

## 数学公式

### 1. 更新门和重置门

$$\mathbf{z}_t = \sigma(\mathbf{W}_z \mathbf{x}_t + \mathbf{U}_z \mathbf{h}_{t-1} + \mathbf{b}_z)$$
$$\mathbf{r}_t = \sigma(\mathbf{W}_r \mathbf{x}_t + \mathbf{U}_r \mathbf{h}_{t-1} + \mathbf{b}_r)$$

- **更新门 $\mathbf{z}_t$**: 控制旧信息vs新信息的混合比例
- **重置门 $\mathbf{r}_t$**: 控制历史信息对候选状态的影响

### 2. 候选隐藏状态

$$\tilde{\mathbf{h}}_t = \tanh(\mathbf{W}_h \mathbf{x}_t + \mathbf{U}_h (\mathbf{r}_t \odot \mathbf{h}_{t-1}) + \mathbf{b}_h)$$

重置门"过滤"历史信息后再与当前输入融合。

### 3. 最终隐藏状态

$$\mathbf{h}_t = (1 - \mathbf{z}_t) \odot \mathbf{h}_{t-1} + \mathbf{z}_t \odot \tilde{\mathbf{h}}_t$$

- $\mathbf{z}_t \to 1$: 采纳新信息，遗忘旧信息
- $\mathbf{z}_t \to 0$: 保留旧信息，忽略新输入

## PyTorch 实现

```python
class GRU(nn.Module):
    def __init__(self, vocab_size, num_hiddens):
        super().__init__()
        self.gru = nn.GRU(input_size=vocab_size, hidden_size=num_hiddens)
        self.linear = nn.Linear(num_hiddens, vocab_size)
        self.vocab_size = vocab_size

    def forward(self, inputs, state):
        X = F.one_hot(inputs.T, self.vocab_size).type(torch.float32)
        Y, state = self.gru(X, state)
        outputs = self.linear(Y.reshape(-1, Y.shape[-1]))
        return outputs, state
```

## GRU vs LSTM

| 特性 | GRU | LSTM |
|------|-----|------|
| 门数量 | 2（更新门+重置门） | 3（输入门+遗忘门+输出门） |
| 细胞状态 | 无独立 $c_t$ | 有独立 $c_t$ |
| 参数量 | 更少 | 更多 |
| 训练速度 | 更快 | 更慢 |
| 长序列性能 | 复杂任务稍弱 | 通常更强 |
