---
type: source
title: "Transformer-Attention-Seq2Seq: 注意力机制与序列到序列模型"
created: 2026-04-15
updated: 2026-06-16
tags: [注意力, Transformer, Seq2Seq, 多头注意力, NLP]
status: developing
complexity: advanced
domain: Architecture
raw_path: "raw/code/transformer-attention-seq2seq.ipynb"
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "belongs_to::[[domains/Architecture]]"
  - "spawns::[[concepts/attention-mechanism]]"
  - "spawns::[[concepts/additive-attention]]"
  - "spawns::[[concepts/scaled-dot-product-attention]]"
  - "spawns::[[concepts/multi-head-attention]]"
  - "spawns::[[concepts/encoder-decoder-architecture]]"
  - "spawns::[[concepts/teacher-forcing]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- spawns: [[concepts/attention-mechanism]] | [[concepts/additive-attention]] | [[concepts/scaled-dot-product-attention]] | [[concepts/multi-head-attention]] | [[concepts/encoder-decoder-architecture]] | [[concepts/teacher-forcing]]

---

# Transformer-Attention-Seq2Seq

## 概要

2026年4月编写的 Transformer 核心组件学习 notebook，从 Nadaraya-Watson 核回归（标量注意力）到多头注意力的完整推导链路。

## 内容结构

1. **NW 核回归（标量版本）**: 非参数 + 带参数版本，广播机制计算距离矩阵
2. **梯度爆炸/死亡陷阱分析**: sum vs mean 引发的 $w$ 飞升 → Softmax 饱和 → 梯度消失
3. **加性注意力**: Wq/Wk 投影 + tanh + Wv 打分，广播机制详解
4. **缩放点积注意力**: $QK^T/\sqrt{d}$，与 √d 缩放理论的关联
5. **Seq2Seq + Attention**: 完整 Encoder-AttentionDecoder 实现，英法翻译
6. **多头注意力**: 线性投影→拆分→并行注意力→拼接→输出投影
7. **Masked Softmax / Teacher Forcing**: 变长序列处理与训练技巧

## 核心知识

- 注意力的本质：动态的、内容相关的加权平均
- Softmax 死亡饱和区：$w$ 过大 → 近似 one-hot → $p(1-p) \to 0$ → 梯度消失
- unsqueeze + 广播机制：注意力分数矩阵的高效构建
- 从标量距离 $(q-k)^2$ 到高维点积 $q^T k / \sqrt{d}$ 的升维思路
- Encoder-Decoder 的张量流转：embedding→RNN→attention→concat→predict
- 多头注意力的 permute/reshape 变形技巧

## 关键实验结果

- NW 核回归：非参数版完美拟合，参数版因 sum loss 导致 w=4.81 卡死
- Seq2Seq 翻译：300 epochs 后 3/3 句子完美翻译
- LSTM 文本生成：500 epochs 后 PPL=1.03
