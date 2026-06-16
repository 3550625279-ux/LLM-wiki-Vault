# Entities Index — 实体节点目录

> **类型**: Map of Content (MoC)
> **用途**: wiki/entities/ 目录下所有 entity 节点的索引。
> **实体类型**: 论文 · 模型 · 作者 · 机构 · 数据集 · 工具

---

## 论文 (Papers)

> 论文以 source 页面存在（见 `wiki/sources/`），此处仅记录参考索引，不作为独立 entity 节点。

- [[sources/hyplora-neurips2025]] — HypLoRA: Hyperbolic Fine-Tuning for LLMs | NeurIPS 2025 | status:developing | ⚠️ 类型为 source
- [[sources/cagc-cvpr2024]] — CAGC: Contextual Augmented Global Contrast for MIR | CVPR 2024 | status:developing | ⚠️ 类型为 source
- [[sources/intent-detection-age-of-llms]] — Intent Detection in the Age of LLMs | EMNLP 2024 | status:developing | ⚠️ 类型为 source

**高优先级待创建**:
- `attention-is-all-you-need` — Vaswani 2017, Transformer 奠基论文
- `chinchilla` — Hoffmann 2022, Scaling Laws
- `lora` — Hu 2021, 参数高效微调
- `instructgpt` — Ouyang 2022, RLHF
- `dpo` — Rafailov 2023, DPO 对齐
- `mag-bert` — Rahman 2020, 多模态适应门控 | EMNLP 2020
- `mult` — Tsai 2019, 跨模态 Transformer | ACL 2019
- `misa` — Hazarika 2020, 模态不变/特定表示 | ACMMM 2020

---

## 模型 (Models)

- [[entities/deepseek-r1]] — DeepSeek-R1: GRPO验证推理能力可纯RL获得 | 2025 | status:seed
- [[entities/deepseek-r1-zero]] — DeepSeek-R1-Zero: 无SFT纯RL训练涌现推理能力 | 2025 | status:seed

**高优先级待创建**:
- `gpt-series` — GPT-1/2/3/4 系列
- `llama-series` — Meta LLaMA 1/2/3
- `claude-series` — Anthropic Claude 系列
- `gemini` — Google Gemini 系列

---

## 作者/研究者 (Researchers)

> *待填充*

**可创建**:
- `andrej-karpathy` — Tesla/OpenAI, 教育贡献
- `ilya-sutskever` — OpenAI 联合创始人
- `yoshua-bengio` — 深度学习三巨头
- `neel-nanda` — Mechanistic Interpretability

---

## 机构 (Organizations)

> *待填充*

---

## 数据集 (Datasets)

- `mintrec` — MIntRec: 多模态意图识别数据集 (2,224 样本, 20类意图) | [[sources/cagc-cvpr2024]]
- `cmu-mosi` — CMU-MOSI: 多模态情感分析数据集 (2,199 样本, 情感分数 -3~3) | [[sources/cagc-cvpr2024]]

**高优先级待创建**:
- `fineweb` — HuggingFace 高质量预训练数据
- `the-pile` — EleutherAI 开源数据集
- `mmlu` — 评估基准

---

## 工具/框架 (Tools)

> *待填充*

**高优先级待创建**:
- `vllm` — PagedAttention 推理框架
- `ollama` — 本地部署工具
- `wandb` — 实验追踪

---

## 统计

```
总 entity 节点: 2 (独立 entity 页面已创建)
  论文:    0 (以 source 页面存在，索引 3 条)
  模型:    2 (DeepSeek-R1, DeepSeek-R1-Zero)
  作者:    0 (目标: 8+)
  数据集:  0 (索引 2 条，待创建页面)
  工具:    0 (目标: 6+)
上次更新:  2026-06-16
```
