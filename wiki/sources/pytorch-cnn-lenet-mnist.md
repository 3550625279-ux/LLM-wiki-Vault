---
type: source
title: "Pytorch-CNN: LeNet-5 手写数字识别全流程"
created: 2026-04-15
updated: 2026-06-16
tags: [CNN, LeNet, MNIST, PyTorch, TensorFlow]
status: developing
complexity: intermediate
domain: Architecture
raw_path: "raw/code/pytorch-cnn-lenet-mnist.ipynb"
sources: ["[[sources/pytorch-cnn-lenet-mnist]]"]
related:
  - "belongs_to::[[domains/Architecture]]"
  - "spawns::[[concepts/convolutional-neural-network]]"
  - "spawns::[[concepts/lenet]]"
  - "spawns::[[concepts/pooling-layer]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- spawns: [[concepts/convolutional-neural-network]] | [[concepts/lenet]] | [[concepts/pooling-layer]]

---

# Pytorch-CNN: LeNet-5 手写数字识别全流程

## 概要

2026年4月编写的 CNN 学习 notebook，涵盖 LeNet-5 从零实现到对比实验的完整链路。

## 内容结构

1. **TensorFlow/Keras 版 LeNet**: 用 `tf.keras.Model` 子类化实现（被中断未完成）
2. **PyTorch 标准 LeNet-5**: 按原始论文结构实现（tanh + AvgPool）
3. **自己的实现**: 精简版 LeNet + 详细注释 + SGD(lr=0.1) 训练 → 98.45%
4. **Dataset/Loader 探索**: 验证数据形状、类型
5. **MLP 对比实验**: LeNet(98.45%) vs MLP(96.99%)，BS=1 极端实验
6. **底层实现**: 不使用 nn.Module，手写卷积/池化函数 + 手动梯度下降

## 核心知识

- CNN 的局部连接 + 权值共享减少参数
- Conv2d 的输出尺寸计算公式
- avg_pool2d 与 max_pool2d 的区别
- one-hot 编码必须转 float32
- 数据预处理：Resize vs Pad，归一化方案选择
- 底层实现加深对 PyTorch 自动微发的理解

## 关键实验结果

| 实验 | 配置 | 结果 |
|------|------|------|
| LeNet 标准版 | Adam, BS=64, 5ep | 98.45% |
| MLP | SGD(lr=0.1), BS=64, 5ep | 96.99% |
| LeNet BS=1 | SGD(lr=0.01), 1000 iter | 86.31% |
| MLP BS=1 | SGD(lr=0.01), 1000 iter | 88.15% |
| 底层 LeNet | 手写 SGD, 6 iter | Loss 从 2.33 到 2.88 (仅验证逻辑) |
