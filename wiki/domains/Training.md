---
title: "Training — 训练方法论"
type: domain
status: seed
domain: Training
tags: [pretraining, finetuning, rlhf, dpo, lora, scaling-laws, data-engineering]
created: 2026-06-13
updated: 2026-06-14
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

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/lora]]
- `contains::` [[concepts/hyplora]]
- `contains::` [[concepts/setfit]]
- `contains::` [[concepts/negative-data-augmentation]]
- `contains::` [[concepts/contrastive-learning]]

## 🔴 关键缺口

- `scaling-laws` — 影响所有训练决策 — **最高优先级**
- `rlhf` — 从人类反馈中学习
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
concept 节点: 5 (目标: 14+)
entity 节点:  0 (目标: 10+)
maturity:    seed
```
