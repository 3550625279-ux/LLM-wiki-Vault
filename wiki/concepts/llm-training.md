---
type: concept
title: "LLM 训练目标"
created: 2026-06-16
updated: 2026-06-16
tags: [LLM, 训练, CLM, MLM, 预训练]
status: seed
complexity: intermediate
domain: Training
sources: ["综合来源"]
related:
  - "depends_on::[[concepts/cross-entropy-loss]]"
  - "depends_on::[[concepts/kl-divergence]]"
  - "depends_on::[[concepts/backpropagation-through-time]]"
  - "part_of::[[concepts/post-training]]"
  - "belongs_to::[[domains/Training]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/cross-entropy-loss]] | [[concepts/kl-divergence]] | [[concepts/backpropagation-through-time]]
- part_of: [[concepts/post-training]]

---

# LLM 训练目标

## 核心等式

$$\min_\theta \mathbb{E}_{x \sim \mathcal{D}} [-\log P_\theta(x_t | x_{<t})]$$

LLM 训练的本质：**最小化交叉熵损失 = 最小化 KL 散度 = 最大化似然**。

详见 [[concepts/cross-entropy-loss]] 的数学推导。

## 三种预训练目标

### 1. 因果语言模型 (CLM / Causal LM)

$$P(x_1, x_2, \ldots, x_T) = \prod_{t=1}^{T} P(x_t | x_1, \ldots, x_{t-1})$$

- **方向**: 从左到右，只看过去
- **使用**: GPT 系列, LLaMA, Mistral
- **优势**: 天然适合自回归生成

### 2. 掩码语言模型 (MLM / Masked LM)

随机遮盖 15% 的 token，预测被遮盖的部分：

$$\text{input}: \text{The} [\text{MASK}] \text{sat on the mat} \rightarrow \text{predict: cat}$$

- **方向**: 双向上下文
- **使用**: BERT, RoBERTa
- **局限**: 不适合生成（推理时没有 [MASK]）

### 3. Span Corruption（T5）

随机遮盖连续片段，用 sentinel token 标记：

$$\text{input}: \text{The } \langle X \rangle \text{ on the } \langle Y \rangle \rightarrow \text{output: } \langle X \rangle \text{ cat sat } \langle Y \rangle \text{ mat}$$

## 训练阶段

```
预训练 (Pre-training)
  └─ 大规模无标注语料 + CLM/MLM → 基础语言能力
      ↓
监督微调 (SFT)
  └─ 指令-回答对 → 从"续写"切换到"回答"
      ↓
对齐 (RLHF / DPO)
  └─ 人类偏好数据 → 安全性、有用性、诚实性
```

详见 [[concepts/post-training]] 的四层递进架构。
