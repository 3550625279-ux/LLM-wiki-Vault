---
type: concept
title: "循环神经网络 (RNN)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, RNN, 序列建模, BPTT]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/one-hot-encoding]]"
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "extends::[[concepts/gru]]"
  - "extends::[[concepts/lstm]]"
  - "contrasts::[[concepts/convolutional-neural-network]]"
  - "applied_in::[[concepts/encoder-decoder-architecture]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/one-hot-encoding]] | [[concepts/backpropagation-through-time]]
- extends: [[concepts/gru]] | [[concepts/lstm]]
- contrasts: [[concepts/convolutional-neural-network]]
- applied_in: [[concepts/encoder-decoder-architecture]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 循环神经网络 (RNN)

## 核心思想

RNN 通过**隐藏状态 $\mathbf{h}_t$** 在时间步之间传递信息，使网络具备"记忆"能力。每个时间步的输出不仅取决于当前输入，还取决于之前所有输入的累积影响。

## 数学公式

$$\mathbf{h}_t = \tanh(\mathbf{W}_{xh} \mathbf{x}_t + \mathbf{W}_{hh} \mathbf{h}_{t-1} + \mathbf{b}_h)$$
$$\mathbf{o}_t = \mathbf{W}_{hy} \mathbf{h}_t + \mathbf{b}_y$$

形状演进（batch_size = b, vocab = v, hidden = h）：
- 输入单步: $(b, v)$ — one-hot 后
- 隐状态: $(b, h)$ — 跨时间步传递
- 输出单步: $(b, v)$ — 映射回词表大小

## PyTorch 实现

```python
class RNN(nn.Module):
    def __init__(self, vocab_size, num_hiddens):
        super().__init__()
        self.rnn = nn.RNN(input_size=vocab_size, hidden_size=num_hiddens)
        self.linear = nn.Linear(num_hiddens, vocab_size)
        self.vocab_size = vocab_size

    def forward(self, inputs, state):
        # inputs: [batch, seq_len] → one_hot → [seq_len, batch, vocab_size]
        X = F.one_hot(inputs.T, self.vocab_size).type(torch.float32)
        Y, state = self.rnn(X, state)
        output = self.linear(Y.reshape(-1, Y.shape[-1]))
        return output, state

    def begin_state(self, device, batch_size):
        return torch.zeros((self.rnn.num_layers, batch_size, self.num_hiddens), device=device)
```

## 完整训练流程

1. **数据准备**: 文本 → 清洗(re.sub) → 词表(collections.Counter) → 索引化
2. **数据迭代**: offset随机偏移 → unfold切窗口 → 区分X/Y → 打乱 → 分batch
3. **训练循环**: 每个epoch → 每个batch → 前向传播 → 交叉熵损失 → 反向传播 → 梯度裁剪 → 更新参数
4. **预测**: 前缀驱动生成（warm-up状态） → 自回归逐字符生成

## 关键工程细节

- **one-hot编码**: `F.one_hot(inputs.T, vocab_size).type(torch.float32)` — 必须转float32
- **转置 inputs.T**: PyTorch RNN 要求输入为 `(seq_len, batch, features)`
- **梯度裁剪**: `torch.nn.utils.clip_grad_norm_(params, theta)` — 防止BPTT梯度爆炸
- **perplexity 困惑度**: $PPL = \exp(\text{avg\_loss})$，越低越好，1.0 = 完美预测

## 两种采样策略

| 策略 | 数据形态 | 状态管理 | 适用场景 |
|------|---------|---------|---------|
| **随机采样** | 打乱窗口顺序 | 每batch重置state | 数据增强、短序列 |
| **顺序划分** | reshape为batch行矩阵 | 跨batch继承state (detach_) | 长序列建模（Truncated BPTT） |

**结论**: 学术研究中推荐顺序划分（路线B），保留真实的长距离上下文记忆。
