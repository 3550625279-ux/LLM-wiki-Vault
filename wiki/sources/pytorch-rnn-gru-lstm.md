---
type: source
title: "pytorch_RNN: RNN/GRU/LSTM 从零实现与对比"
created: 2026-04-15
updated: 2026-06-16
tags: [RNN, GRU, LSTM, PyTorch, BPTT, 文本生成]
status: developing
complexity: intermediate
domain: Architecture
raw_path: "raw/code/pytorch-rnn-gru-lstm.ipynb"
sources: ["[[sources/pytorch-rnn-gru-lstm]]"]
related:
  - "belongs_to::[[domains/Architecture]]"
  - "spawns::[[concepts/recurrent-neural-network]]"
  - "spawns::[[concepts/backpropagation-through-time]]"
  - "spawns::[[concepts/gru]]"
  - "spawns::[[concepts/lstm]]"
  - "spawns::[[concepts/gradient-clipping]]"
  - "spawns::[[concepts/perplexity]]"
  - "spawns::[[concepts/one-hot-encoding]]"
  - "spawns::[[insights/rnn-hyperparameter-analysis]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- spawns: [[concepts/recurrent-neural-network]] | [[concepts/backpropagation-through-time]] | [[concepts/gru]] | [[concepts/lstm]] | [[concepts/gradient-clipping]] | [[concepts/perplexity]] | [[concepts/one-hot-encoding]] | [[insights/rnn-hyperparameter-analysis]]

---

# pytorch_RNN: RNN/GRU/LSTM 从零实现与对比

## 概要

2026年4月编写的 RNN 家族完整学习 notebook，从基础 RNN 到 GRU/LSTM 变体，涵盖数据处理、两种采样策略对比、从零实现、以及超参数调优分析。

## 内容结构

1. **基础 RNN 实现**: 数据准备→词表→数据迭代器→模型→训练→预测
2. **两种采样策略对比**: 随机采样(路线A) vs 顺序划分(路线B)
3. **代码细节解读**: re.sub、collections、enumerate、unfold、offset、one-hot
4. **自己实现 RNN**: 从零编写完整训练流水线
5. **从第一性原理总结**: 超参数→张量形状→BPTT→梯度裁剪→预测
6. **GRU 扩展**: 更换 nn.GRU，训练 Time Machine 语料
7. **LSTM 扩展**: 元组状态 (h_n, c_n)，单独的 train_lstm 函数
8. **超参数深度分析**: batch_size/num_steps/num_hiddens/优化器的底层影响

## 核心知识

- 采样策略：随机（切断状态）vs 顺序（继承状态+detach_）
- unfold 切窗口 + offset 随机偏移的数据增强技巧
- RNN/GRU/LSTM 三者的代码差异仅在模型定义和状态管理
- LSTM 的 state 是元组 (h, c)，detach 和 begin_state 都需特殊处理
- perplexity = exp(avg_loss)，是语言模型的核心评估指标

## 关键实验结果

| 模型 | 语料 | Batch/Steps | Epoch | PPL | 生成质量 |
|------|------|------------|-------|-----|---------|
| RNN | hello world | 32/3 | 500 | 1.19 | 完美 |
| RNN(顺序) | hello world | 32/3 | 500 | 1.02 | 完美 |
| LSTM | Time Machine | 32/10 | 500 | 1.03 | 完美 |
| GRU | Time Machine | 256/10 | — | — | 被中断 |
