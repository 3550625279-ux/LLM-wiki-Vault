---
type: concept
title: "Teacher Forcing"
created: 2026-04-15
updated: 2026-06-16
tags: [深度学习, Seq2Seq, 训练技巧]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/transformer-attention-seq2seq]]"]
related:
  - "depends_on::[[concepts/encoder-decoder-architecture]]"
  - "applied_in::[[concepts/encoder-decoder-architecture]]"
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/transformer-attention-seq2seq]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- depends_on: [[concepts/encoder-decoder-architecture]]
- applied_in: [[concepts/encoder-decoder-architecture]]
- produced_by: [[sources/transformer-attention-seq2seq]]

---

# Teacher Forcing

## 核心思想

训练 Seq2Seq 模型时，用**真实标签**（而非模型自身的预测）作为解码器每一步的输入。就像老师在旁边不断提示正确答案。

## 张量偏移逻辑

目标序列 $Y = [y_1, y_2, \ldots, y_T]$，构造解码器输入：

$$\text{dec\_input} = [\langle\text{bos}\rangle, y_1, y_2, \ldots, y_{T-1}]$$

即：`<bos>` 开头 + 切掉最后一个词。

```python
bos_tensor = torch.tensor([bos_idx] * batch_size).reshape(-1, 1)
dec_input = torch.cat([bos_tensor, Y[:, :-1]], dim=1)
```

## 为什么要右移一位

解码器在时间步 $t$ 的任务是**根据之前的词预测第 $t$ 个词**：
- 输入: `<bos> I love` → 预测: `I`
- 输入: `I love you` → 预测: `you`

右移一位确保解码器看到的是"历史"，预测的是"下一个"。

## Teacher Forcing 的代价

训练和推理时的输入分布不一致（**exposure bias**）：
- 训练时总是看到正确的前文
- 推理时看到的是自己可能出错的预测

缓解方法：Scheduled Sampling（逐步用模型预测替代真实标签）。
