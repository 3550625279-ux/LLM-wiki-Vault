---
title: "Multimodal — 多模态"
type: domain
status: seed
domain: Multimodal
tags: [vision-language, diffusion, clip, image-generation, audio, video]
created: 2026-06-13
updated: 2026-06-13
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

## 🧮 核心概念节点

- [ ] [[concepts/clip]] — 对比学习对齐图文表示
- [ ] [[concepts/visual-instruction-tuning]] — LLaVA 方法
- [ ] [[concepts/diffusion-model-basics]] — DDPM 前向/反向过程
- [ ] [[concepts/latent-diffusion]] — 在潜空间中扩散
- [ ] [[concepts/classifier-free-guidance]] — CFG 控制生成质量
- [ ] [[entities/stable-diffusion]] — Stability AI
- [ ] [[entities/whisper]] — OpenAI 语音识别

---

## 🔗 领域间关系

- `depends_on::` [[domains/architecture]] — ViT 基于 Transformer
- `depends_on::` [[domains/training]] — 多模态对齐需要特殊训练
- `applied_in::` [[domains/agents]] — 多模态感知是具身 Agent 基础

---

## ⚠️ 活跃矛盾/争议

1. **扩散模型 vs Autoregressive 图像生成**: 谁会统一图像生成？
2. **端到端多模态 vs 模块化**: 原生多模态 vs 拼接方案

---

## 📊 领域统计

```
concept 节点: 0 (目标: 10+)
entity 节点:  0 (目标: 8+)
maturity:    seed
```
