---
type: concept
title: "LeNet-5 卷积网络"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, CNN, LeNet, MNIST, 经典架构]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[sources/pytorch-cnn-lenet-mnist]]"]
related:
  - "depends_on::[[concepts/convolutional-neural-network]]"
  - "depends_on::[[concepts/pooling-layer]]"
  - "extends::[[concepts/convolutional-neural-network]]"
  - "produced_by::[[sources/pytorch-cnn-lenet-mnist]]"
  - "belongs_to::[[domains/Architecture]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/convolutional-neural-network]] | [[concepts/pooling-layer]]
- extends: [[concepts/convolutional-neural-network]]
- produced_by: [[sources/pytorch-cnn-lenet-mnist]]

---

# LeNet-5 卷积网络

## 架构概述

LeNet-5（Yann LeCun, 1998）是最早成功应用的 CNN 架构，用于手写数字识别。其经典结构为：

```
输入(1×32×32) → C1(6@5×5) → S2(AvgPool 2×2) → C3(16@5×5) → S4(AvgPool 2×2) → C5(120@5×5) → F6(84) → Output(10)
```

| 层 | 类型 | 输出尺寸 | 说明 |
|----|------|---------|------|
| C1 | Conv2d(1→6, 5×5) | 6×28×28 | 第一层特征提取 |
| S2 | AvgPool(2×2, stride=2) | 6×14×14 | 降采样 |
| C3 | Conv2d(6→16, 5×5) | 16×10×10 | 深层特征 |
| S4 | AvgPool(2×2, stride=2) | 16×5×5 | 降采样 |
| C5 | Conv2d(16→120, 5×5) | 120×1×1 | 等效全连接 |
| F6 | Linear(120→84) | 84 | 全连接层 |
| Output | Linear(84→10) | 10 | 分类输出 |

## 关键特征

- **激活函数**: 原始使用 `tanh`（非 ReLU），现代复现常用 ReLU
- **池化层**: 原始使用**平均池化**（非最大池化）
- **输入尺寸**: 原始输入 32×32，MNIST 为 28×28，需 padding 或 resize

## PyTorch 标准实现

```python
class LeNet5(nn.Module):
    def __init__(self):
        super().__init__()
        self.c1 = nn.Conv2d(1, 6, kernel_size=5)
        self.s2 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.c3 = nn.Conv2d(6, 16, kernel_size=5)
        self.s4 = nn.AvgPool2d(kernel_size=2, stride=2)
        self.c5 = nn.Conv2d(16, 120, kernel_size=5)
        self.f6 = nn.Linear(120, 84)
        self.output = nn.Linear(84, 10)
        self.tanh = nn.Tanh()

    def forward(self, x):
        x = self.tanh(self.c1(x))
        x = self.s2(x)
        x = self.tanh(self.c3(x))
        x = self.s4(x)
        x = self.tanh(self.c5(x))
        x = x.view(x.size(0), -1)  # 展平
        x = self.tanh(self.f6(x))
        return self.output(x)
```

## 数据预处理要点

MNIST 28×28 → LeNet 需要 32×32，两种方案：
1. `np.pad` 填充 2 像素（TensorFlow 版本）
2. `transforms.Resize((32, 32))`（PyTorch 版本）

归一化方案差异：
- `(0.5,) / (0.5,)` → 映射到 [-1, 1]
- `(0.1307,) / (0.3081,)` → MNIST 的全局均值/标准差（更标准）

## 底层实现（不使用 nn.Module）

核心思路：手动管理 `torch.Tensor` 参数（设 `requires_grad=True`），手写卷积和池化函数，手动执行梯度下降。

```python
class LowLevelLeNet:
    def __init__(self):
        self.params = {
            'c1_w': torch.randn(6, 1, 5, 5) * 0.1,
            'c1_b': torch.zeros(6),
            # ... 每层的权重和偏置
        }
        for p in self.params.values():
            p.requires_grad = True
```

手动训练循环：`param -= lr * param.grad; param.grad.zero_()`
