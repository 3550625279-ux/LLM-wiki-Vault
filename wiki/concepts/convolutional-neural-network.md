---
type: concept
title: "卷积神经网络 (CNN)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, CNN, 卷积, 计算机视觉, 架构]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[sources/pytorch-cnn-lenet-mnist]]"]
related:
  - "depends_on::[[concepts/one-hot-encoding]]"
  - "extends::[[concepts/recurrent-neural-network]]"
  - "contrasts::[[concepts/recurrent-neural-network]]"
  - "part_of::[[concepts/lenet]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/pytorch-cnn-lenet-mnist]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/one-hot-encoding]]
- extends: [[concepts/recurrent-neural-network]]
- contrasts: [[concepts/recurrent-neural-network]]
- part_of: [[concepts/lenet]]
- produced_by: [[sources/pytorch-cnn-lenet-mnist]]

---

# 卷积神经网络 (CNN)

## 核心思想

CNN 利用**局部连接**和**权值共享**两大特性，将全连接层中庞大的参数量压缩到可管理的规模。卷积核在输入上滑动，对每个局部区域执行点积运算，提取局部特征。

## 卷积运算

给定输入 $X \in \mathbb{R}^{C_{in} \times H \times W}$ 和卷积核 $K \in \mathbb{R}^{C_{out} \times C_{in} \times k_h \times k_w}$：

$$Y[b, c_{out}, i, j] = \sum_{c_{in}} \sum_{m,n} X[b, c_{in}, i \cdot s + m, j \cdot s + n] \cdot K[c_{out}, c_{in}, m, n] + b[c_{out}]$$

- **局部连接**：每个输出只看 $k_h \times k_w$ 的局部窗口
- **权值共享**：同一个卷积核在所有位置共用，大幅减少参数
- **平移等变性**：输入平移 → 输出也平移（卷积的本质特性）

## 输出尺寸计算

$$H_{out} = \frac{H_{in} + 2 \cdot \text{padding} - k_h}{\text{stride}} + 1$$

## PyTorch 实现

```python
# Conv2d: in_channels → out_channels, kernel_size 5x5
self.conv1 = nn.Conv2d(in_channels=1, out_channels=6, kernel_size=5)
# 输入 [batch, 1, 32, 32] → 输出 [batch, 6, 28, 28]
```

## CNN vs MLP 对比实验

| 模型 | Batch Size | Epochs | 测试准确率 |
|------|-----------|--------|-----------|
| LeNet (CNN) | 64 | 5 | **98.45%** |
| MLP (全连接) | 64 | 5 | 96.99% |
| LeNet (CNN) | 1 | 1000 iter | 86.31% |
| MLP (全连接) | 1 | 1000 iter | 88.15% |

**关键洞察**：CNN 的卷积结构在正常 batch size 下有明显的特征提取优势，但在极端小 batch（BS=1）下，梯度极度不稳定，MLP 反而靠其更简单的结构表现更好。

## 手动实现卷积（不用 nn.Conv2d）

```python
def conv2d_low_level(x, weight, bias, stride=1, padding=0):
    # 通过滑动窗口 + 点积实现
    for i in range(out_h):
        for j in range(out_w):
            window = x[:, :, i*stride:i*stride+k_h, j*stride:j*stride+k_w]
            for c_out in range(out_c):
                out[:, c_out, i, j] = torch.sum(window * weight[c_out], dim=(1,2,3)) + bias[c_out]
```

底层实现用三重循环，展示了卷积的数学本质：**滑动窗口上的加权求和**。实际框架使用 im2col 或 FFT 加速。
