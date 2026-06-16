---
title: "Training — 训练方法论"
type: domain
status: seed
domain: Training
tags: [pretraining, finetuning, rlhf, dpo, lora, scaling-laws, data-engineering, rnn, bptt, gradient-clipping]
created: 2026-06-13
updated: 2026-06-16
confidence: high
---

# Training — 训练方法论

> **领域使命**: 理解如何让模型学到想要的知识与行为。
> **核心链路**: 数据质量 → 预训练目标 → 对齐微调 → 评估验证

---

## 📌 领域地图

```
Training
├── 预训练 (Pre-Training)
│   ├── 数据工程 (质量过滤/去重/混合)
│   ├── 分词 (BPE/WordPiece/SentencePiece)
│   ├── 训练目标 (CLM/MLM/Span Corruption)
│   └── Scaling Laws (Chinchilla 定律)
│
├── 后训练对齐 (Post-Training)
│   ├── 监督微调 SFT
│   ├── 人类反馈强化学习 RLHF
│   │   ├── Reward Model 训练
│   │   └── PPO 优化
│   ├── Direct Preference Optimization DPO
│   └── Constitutional AI (CAI)
│
├── 参数高效微调 (PEFT)
│   ├── LoRA — 低秩矩阵注入
│   ├── QLoRA — 量化 + LoRA
│   ├── Prefix-Tuning
│   └── Adapter
│
├── 分布式训练
│   ├── 数据并行 (DDP)
│   ├── 张量并行 (TP)
│   ├── 流水线并行 (PP)
│   └── ZeRO (DeepSpeed)
│
└── 训练技巧
    ├── 学习率调度 (Warmup + Cosine)
    ├── 梯度裁剪
    ├── 混合精度 (BF16/FP16)
    └── 批次大小策略
```

---

## 🧮 已有节点

- [x] [[concepts/lora]] — LoRA 低秩适配 | status:seed
- [x] [[concepts/hyplora]] — HypLoRA 双曲低秩适配（LLM 嵌入的几何感知 PEFT） | status:seed
- [x] [[concepts/setfit]] — SetFit 少样本文本分类 | status:seed
- [x] [[concepts/negative-data-augmentation]] — 负样本数据增强 | status:seed
- [x] [[concepts/contrastive-learning]] — 对比学习表示学习范式 | status:seed
- [x] [[concepts/post-training]] — 后训练总览（四层递进架构） | status:seed
- [x] [[concepts/sft]] — 有监督微调：从续写到回答的切换 | status:seed
- [x] [[concepts/chain-of-thought]] — 推理链 CoT：准确率从17%到78% | status:seed
- [x] [[concepts/process-reward-model]] — 过程奖励模型 PRM：逐步骤打分 | status:seed
- [x] [[concepts/grpo]] — 组相对策略优化：绕开奖励模型 | status:seed
- [x] [[concepts/data-flywheel]] — 数据飞轮：RL反哺SFT的迭代循环 | status:seed
- [x] [[concepts/aha-moment]] — Aha Moment：纯RL中推理能力涌现 | status:seed
- [x] [[operations/sft-cot-data-pipeline]] — CoT SFT数据四条生产线 | status:seed
- [x] [[concepts/backpropagation-through-time]] — BPTT 时间反向传播 | status:seed ✅ NEW
- [x] [[concepts/gradient-clipping]] — 梯度裁剪 | status:seed ✅ NEW
- [x] [[concepts/teacher-forcing]] — Teacher Forcing 训练技巧 | status:seed ✅ NEW
- [x] [[concepts/perplexity]] — 困惑度评估指标 | status:seed ✅ NEW
- [x] [[insights/rnn-hyperparameter-analysis]] — RNN 调参四要素 | status:seed ✅ NEW

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/lora]]
- `contains::` [[concepts/hyplora]]
- `contains::` [[concepts/setfit]]
- `contains::` [[concepts/negative-data-augmentation]]
- `contains::` [[concepts/contrastive-learning]]
- `contains::` [[concepts/post-training]]
- `contains::` [[concepts/sft]]
- `contains::` [[concepts/chain-of-thought]]
- `contains::` [[concepts/process-reward-model]]
- `contains::` [[concepts/grpo]]
- `contains::` [[concepts/data-flywheel]]
- `contains::` [[concepts/aha-moment]]
- `contains::` [[concepts/backpropagation-through-time]]
- `contains::` [[concepts/gradient-clipping]]
- `contains::` [[concepts/teacher-forcing]]
- `contains::` [[concepts/perplexity]]

## 🔴 关键缺口

- `scaling-laws` — 影响所有训练决策 — **最高优先级**
- ~~`rlhf`~~ — ✅ 已通过 [[concepts/grpo]] + [[concepts/process-reward-model]] 间接覆盖（RLHF本体在Alignment域）
- `dpo` — DPO 去掉强化学习的对齐
- `causal-language-modeling` — CLM 自回归目标
- `qlora` — QLoRA 量化微调
- `zero-redundancy-optimizer` — ZeRO Stage 1/2/3

---

## 🔗 领域间关系

- `depends_on::` [[domains/foundations]] — 优化理论是训练的基础
- `depends_on::` [[domains/architecture]] — 架构决定训练效率
- `extends::` [[domains/alignment]] — 后训练对齐是 Training 的子集
- `applied_in::` [[domains/engineering]] — 训练流水线是工程实践的核心

---

## ⚠️ 活跃矛盾/争议

1. **Scaling Laws 争议**: Chinchilla (等比例计算最优) vs 实践中往往 token 更多更好
2. **RLHF vs DPO**: DPO 更简单但真的等效吗？Reward Hacking 风险？
3. **数据质量 vs 数量**: 更多低质量数据 vs 更少高质量数据

---

## 📖 推荐资料

- [ ] Chinchilla 论文 (Hoffmann et al. 2022)
- [ ] LoRA 论文 (Hu et al. 2021)
- [ ] InstructGPT 论文 (Ouyang et al. 2022)
- [ ] DPO 论文 (Rafailov et al. 2023)
- [ ] The Llama 3 Herd (Meta, 2024)

---

## 📊 领域统计

```
concept 节点: 15 (目标: 14+) ✅ 已达标
operation 节点: 1
insight 节点:  1
entity 节点:  0 (目标: 10+)
maturity:    developing
```
