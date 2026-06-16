---
type: concept
title: "长短期记忆网络 (LSTM)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, LSTM, 门控, RNN, 序列建模]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/recurrent-neural-network]]"
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "contrasts::[[concepts/gru]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/recurrent-neural-network]] | [[concepts/backpropagation-through-time]]
- contrasts: [[concepts/gru]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 长短期记忆网络 (LSTM)

## 核心思想

LSTM（Hochreiter & Schmidhuber, 1997）引入独立的**细胞状态 $\mathbf{c}_t$** 作为信息高速公路，通过三个门精确控制信息的写入、遗忘和输出。

## 数学公式

### 1. 三个门

$$\mathbf{f}_t = \sigma(\mathbf{W}_f \mathbf{x}_t + \mathbf{U}_f \mathbf{h}_{t-1} + \mathbf{b}_f) \quad \text{(遗忘门)}$$
$$\mathbf{i}_t = \sigma(\mathbf{W}_i \mathbf{x}_t + \mathbf{U}_i \mathbf{h}_{t-1} + \mathbf{b}_i) \quad \text{(输入门)}$$
$$\mathbf{o}_t = \sigma(\mathbf{W}_o \mathbf{x}_t + \mathbf{U}_o \mathbf{h}_{t-1} + \mathbf{b}_o) \quad \text{(输出门)}$$

### 2. 细胞状态更新

$$\tilde{\mathbf{c}}_t = \tanh(\mathbf{W}_c \mathbf{x}_t + \mathbf{U}_c \mathbf{h}_{t-1} + \mathbf{b}_c)$$
$$\mathbf{c}_t = \mathbf{f}_t \odot \mathbf{c}_{t-1} + \mathbf{i}_t \odot \tilde{\mathbf{c}}_t$$

### 3. 隐藏状态输出

$$\mathbf{h}_t = \mathbf{o}_t \odot \tanh(\mathbf{c}_t)$$

## 关键区别：LSTM 的 state 是元组

```python
class LSTM(nn.Module):
    def forward(self, inputs, state):
        X = F.one_hot(inputs.T, self.vocab_size).type(torch.float32)
        Y, (h_n, c_n) = self.lstm(X, state)  # 注意这里返回元组
        outputs = self.linear(Y.reshape(-1, Y.shape[-1]))
        return outputs, (h_n, c_n)

    def begin_state(self, device, batch_size):
        # LSTM 需要同时初始化 h_0 和 c_0
        return (torch.zeros((1, batch_size, self.num_hiddens), device=device),
                torch.zeros((1, batch_size, self.num_hiddens), device=device))
```

训练时 detach 也需要分别处理两个张量：
```python
state = (state[0].detach_(), state[1].detach_())
```

## 实验结果（Time Machine 语料）

| Epoch | 困惑度 | 生成文本 |
|-------|--------|---------|
| 50 | 6.13 | hellollllllllll... |
| 200 | 2.07 | helloorldhelloorld... |
| 500 | **1.03** | helloworldhelloworld... |

LSTM 从完全乱码逐步收敛到完美复现 "hello world" 模式。
