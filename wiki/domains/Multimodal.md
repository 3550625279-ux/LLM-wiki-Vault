---
title: "Multimodal — 多模态"
type: domain
status: developing
domain: Multimodal
tags: [vision-language, diffusion, clip, image-generation, audio, video, intent-recognition, contrastive-learning]
created: 2026-06-13
updated: 2026-06-14
confidence: medium
---

# Multimodal — 多模态

> **领域使命**: 理解 AI 如何跨越语言边界，感知和生成图像、音频、视频。
> **发展速度**: 该领域迭代极快，注意标注 `updated` 日期。

---

## 📌 领域地图

```
Multimodal
├── 视觉-语言模型 (VLM)
│   ├── CLIP — 对比学习对齐视觉与语言
│   ├── LLaVA — 视觉指令微调
│   ├── GPT-4V / GPT-4o
│   ├── Gemini — 原生多模态
│   └── Qwen-VL / InternVL
│
├── 多模态意图/情感分析 ✅ NEW
│   ├── [[concepts/multimodal-intent-recognition]] — 语言+视觉+听觉意图理解
│   ├── [[concepts/cross-video-bank]] — 跨视频记忆库（场景相似+意图筛选）
│   ├── [[concepts/context-augmented-transformer]] — CAT 渐进式注意力
│   ├── [[concepts/global-context-guided-contrastive-learning]] — GCCL 全局对比
│   └── [[sources/cagc-cvpr2024]] — CAGC (CVPR 2024)
│
├── 图像生成
│   ├── 扩散模型 (DDPM → Stable Diffusion → FLUX)
│   ├── GAN (已逐渐被扩散取代)
│   └── VAE
│
├── 音频/语音
│   ├── Whisper — 语音识别
│   └── TTS / AudioLM
│
├── 视频理解
│   ├── Video-LLaVA
│   └── Sora (文生视频)
│
└── 具身智能
    ├── 视觉-动作模型
    └── 机器人学习
```

---

## 🧮 已有节点

- [x] [[concepts/multimodal-intent-recognition]] — 多模态意图识别 (MIR) | status:seed
- [x] [[concepts/cross-video-bank]] — Cross-video Bank 跨视频记忆库 | status:seed
- [x] [[concepts/context-augmented-transformer]] — CAT 上下文增强 Transformer | status:seed
- [x] [[concepts/global-context-guided-contrastive-learning]] — GCCL 全局对比学习 | status:seed
- [x] [[sources/cagc-cvpr2024]] — CAGC 论文 (CVPR 2024) | status:developing
- [x] [[comparisons/cagc-vs-baselines]] — CAGC vs 基线方法对比 | status:seed

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/multimodal-intent-recognition]]
- `contains::` [[concepts/cross-video-bank]]
- `contains::` [[concepts/context-augmented-transformer]]
- `contains::` [[concepts/global-context-guided-contrastive-learning]]
- `contains::` [[sources/cagc-cvpr2024]]
- `contains::` [[comparisons/cagc-vs-baselines]]

## 🔴 关键缺口

- `clip` — 对比学习对齐图文表示
- `visual-instruction-tuning` — LLaVA 方法
- `diffusion-model-basics` — DDPM 前向/反向过程
- `latent-diffusion` — 在潜空间中扩散

---

## 🔗 领域间关系

- `depends_on::` [[domains/architecture]] — ViT 基于 Transformer；CAT 扩展自 Transformer 注意力
- `depends_on::` [[domains/training]] — 多模态对齐需要特殊训练；对比学习是核心训练范式
- `applied_in::` [[domains/agents]] — 多模态感知是具身 Agent 基础；MIR 可用于对话 Agent 意图理解
- `extends::` [[concepts/contrastive-learning]] — GCCL 将对比学习从 mini-batch 扩展到全局

---

## ⚠️ 活跃矛盾/争议

1. **扩散模型 vs Autoregressive 图像生成**: 谁会统一图像生成？
2. **端到端多模态 vs 模块化**: 原生多模态 vs 拼接方案

---

## 📊 领域统计

```
concept 节点: 4 (目标: 10+)
source 节点:  1 (CAGC CVPR 2024)
entity 节点:  0 (目标: 8+)
maturity:    developing
```
