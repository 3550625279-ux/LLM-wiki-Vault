---
type: concept
title: "梯度裁剪 (Gradient Clipping)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, 梯度, 训练技巧, RNN]
status: seed
complexity: basic
domain: Training
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "applied_in::[[concepts/recurrent-neural-network]]"
  - "applied_in::[[concepts/gru]]"
  - "applied_in::[[concepts/lstm]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/pytorch-rnn-gru-lstm]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/backpropagation-through-time]]
- applied_in: [[concepts/recurrent-neural-network]] | [[concepts/gru]] | [[concepts/lstm]]
- produced_by: [[sources/pytorch-rnn-gru-lstm]]

---

# 梯度裁剪 (Gradient Clipping)

## 问题：梯度爆炸

RNN 展开 $T$ 步时，梯度包含 $\mathbf{W}_{hh}^T$ 的矩阵连乘。当 $\|\mathbf{W}_{hh}\| > 1$ 时，梯度指数增长，参数更新量极大，训练崩溃。

## 解决方案：范数裁剪

当所有参数的梯度总范数超过阈值 $\theta$ 时，等比例缩小：

$$\text{if } \|\mathbf{g}\| > \theta: \quad \mathbf{g} \leftarrow \frac{\theta}{\|\mathbf{g}\|} \cdot \mathbf{g}$$

## 手动实现

```python
def grad_clipping(net, theta):
    params = [p for p in net.parameters() if p.requires_grad]
    norm = torch.sqrt(sum([torch.sum(p.grad**2) for p in params]))
    if norm > theta:
        for param in params:
            param.grad[:] *= theta / norm
```

## PyTorch 内置版本

```python
torch.nn.utils.clip_grad_norm_(net.parameters(), max_norm=1.0)
```

## 使用时机

在 `loss.backward()` 之后、`optimizer.step()` 之前：
```python
loss.backward()
grad_clipping(net, 1)  # 或 clip_grad_norm_(net.parameters(), 1)
optimizer.step()
```

## 直觉理解

梯度裁剪就像给优化器装了一个"限速器"：正常情况下不限制，但当梯度突然爆炸时（训练初期尤其常见），强制把它拉回安全范围。
