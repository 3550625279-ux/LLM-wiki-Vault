---
type: concept
title: "池化层 (Pooling)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, CNN, 池化, 降采样]
status: seed
complexity: basic
domain: Architecture
sources: ["[[sources/pytorch-cnn-lenet-mnist]]"]
related:
  - "part_of::[[concepts/convolutional-neural-network]]"
  - "applied_in::[[concepts/lenet]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/pytorch-cnn-lenet-mnist]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- part_of: [[concepts/convolutional-neural-network]]
- applied_in: [[concepts/lenet]]
- produced_by: [[sources/pytorch-cnn-lenet-mnist]]

---

# 池化层 (Pooling)

## 核心作用

池化层通过对局部区域进行**聚合操作**，实现：
1. **降采样**：减少特征图的空间尺寸，降低后续计算量
2. **平移不变性**：小范围位移不影响输出
3. **扩大感受野**：间接让后续层看到更大的输入区域

## 两种主要池化

### 平均池化 (Average Pooling)

$$Y[i,j] = \frac{1}{k_h \cdot k_w} \sum_{m=0}^{k_h-1} \sum_{n=0}^{k_w-1} X[i \cdot s + m, j \cdot s + n]$$

- LeNet 原始设计使用平均池化
- 保留区域内的整体信息

### 最大池化 (Max Pooling)

$$Y[i,j] = \max_{m,n} X[i \cdot s + m, j \cdot s + n]$$

- 现代 CNN（如 VGG、ResNet）更常用
- 保留最显著的特征响应

## PyTorch 实现

```python
# LeNet 使用的平均池化
pool = nn.AvgPool2d(kernel_size=2, stride=2)
# [batch, 6, 28, 28] → [batch, 6, 14, 14]

# 现代常用的全局平均池化（替代全连接层）
gap = nn.AdaptiveAvgPool2d(1)
# [batch, 512, 7, 7] → [batch, 512, 1, 1]
```

## 手动实现

```python
def avg_pool2d_low_level(x, kernel_size=2, stride=2):
    for i in range(out_h):
        for j in range(out_w):
            window = x[:, :, i*stride:i*stride+kernel_size, j*stride:j*stride+kernel_size]
            out[:, :, i, j] = torch.mean(window, dim=(2, 3))
```
