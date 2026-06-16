---
type: concept
title: "编码器-解码器架构 (Encoder-Decoder)"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, Seq2Seq, 编码器, 解码器, 注意力]
status: seed
complexity: advanced
domain: Architecture
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/recurrent-neural-network]]"
  - "depends_on::[[concepts/additive-attention]]"
  - "depends_on::[[concepts/teacher-forcing]]"
  - "applied_in::[[concepts/multi-head-attention]]"
  - "belongs_to::[[domains/Architecture]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Architecture]]
- depends_on: [[concepts/recurrent-neural-network]] | [[concepts/additive-attention]] | [[concepts/teacher-forcing]]
- applied_in: [[concepts/multi-head-attention]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# 编码器-解码器架构 (Encoder-Decoder)

## 核心思想

将输入序列编码为固定长度的上下文向量，再解码为目标序列。这是机器翻译（NMT）的基础框架。

## 架构概览

```
源序列 → [Encoder: GRU] → enc_outputs (所有时间步的隐状态)
                                      ↓
                          [Attention: 计算上下文向量]
                                      ↓
目标序列 → [Decoder: GRU + Attention] → 预测序列
```

## Encoder

```python
class Seq2SeqEncoder(nn.Module):
    def __init__(self, vocab_size, embed_size, num_hiddens, num_layers, dropout):
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.rnn = nn.GRU(embed_size, num_hiddens, num_layers, dropout=dropout)

    def forward(self, X):
        X = self.embedding(X).permute(1, 0, 2)  # → (seq_len, batch, embed)
        output, state = self.rnn(X)
        return output, state
```

## Attention Decoder（核心创新）

解码器每个时间步用 **注意力** 回看编码器的所有输出：

```python
class Seq2SeqAttentionDecoder(nn.Module):
    def forward(self, X, state):
        enc_outputs, hidden_state, enc_valid_lens = state
        for x in X:  # 逐步解码
            query = hidden_state[-1].unsqueeze(1)  # 顶层隐状态作 Q
            context = self.attention(query, enc_outputs, enc_outputs, enc_valid_lens)
            # 拼接: 上下文向量 + 当前输入嵌入
            x_and_context = torch.cat((context, x.unsqueeze(1)), dim=-1)
            out, hidden_state = self.rnn(x_and_context.permute(1,0,2), hidden_state)
```

## Teacher Forcing

训练时用真实标签作为解码器输入（右移一位）：
```python
bos_tensor = torch.tensor([bos_idx] * batch_size).reshape(-1, 1)
dec_input = torch.cat([bos_tensor, Y[:, :-1]], dim=1)  # <bos> + 目标[:-1]
```

## Masked Softmax CE Loss

屏蔽 `<pad>` 位置的损失，避免无效填充影响训练：
```python
class MaskedSoftmaxCELoss(nn.CrossEntropyLoss):
    def forward(self, pred, label, valid_len):
        weights = torch.ones_like(label)
        weights = sequence_mask(weights, valid_len)
        self.reduction = 'none'
        unweighted_loss = super().forward(pred.permute(0,2,1), label)
        return (unweighted_loss * weights).mean(dim=1)
```

## 贪心解码

推理时逐步生成，每步取概率最大的 token：
```python
for _ in range(num_steps):
    Y_hat, dec_state = net.decoder(dec_X, dec_state)
    pred = Y_hat.argmax(dim=2)
    if pred.item() == tgt_vocab['<eos>']:
        break
    output_seq.append(pred.item())
    dec_X = pred
```

## 实验结果（英法迷你语料）

300 epochs 后完美翻译：
```
they are watching . → ils regardent .
i am eating .      → je mange .
he is sleeping .   → il dort .
```
