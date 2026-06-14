---
type: source
title: "Hyperbolic Fine-Tuning for Large Language Models"
created: 2026-06-13
updated: 2026-06-14
tags: [NeurIPS2025, 双曲几何, PEFT, LoRA, 嵌入分析]
status: developing
domain: Training
source_path: "raw/papers/hyperbolic-fine-tuning-llms/paper.pdf"
related:
  - "spawns::[[concepts/hyplora]]"
  - "spawns::[[concepts/hyperbolic-geometry-llm]]"
  - "extends::[[concepts/lora]]"
  - "spawns::[[insights/llm-embedding-geometry]]"
  - "spawns::[[insights/hyplora-learning-insights]]"
  - "spawns::[[questions/hyplora-thought-experiments]]"
  - "spawns::[[questions/hyplora-research-directions]]"
  - "belongs_to::[[domains/Training]]"
---

# Hyperbolic Fine-Tuning for Large Language Models

> **来源**: NeurIPS 2025 | **PDF**: [[raw/papers/hyperbolic-fine-tuning-llms/paper.pdf]]
> **作者**: Menglin Yang, Ram Samarth B B, Aosong Feng, Bo Xiong, Jiahong Liu, Irwin King, Rex Ying
> **机构**: HKUST(GZ), Yale, Stanford, CUHK
> **GitHub**: https://github.com/marlin-codes/HypLoRA

---

## 核心贡献

1. **几何分析**：证明 LLM token 嵌入具有双曲（树状）层次结构
   - 全局：幂律分布 γ ≈ 1.9
   - 局部：δ-双曲性 ≈ 0.06-0.12（接近完美树）
   - 理论桥梁：幂律 ↔ 双曲几何（γ = 2/ζ + 1）

2. **方法创新**：HypLoRA — 首个在 Lorentz 双曲面上直接执行低秩适配的方法
   - 绕过 exp-log 抵消问题
   - 引入高阶范数依赖项
   - 参数效率与 LoRA 完全相同

3. **实验验证**：6 个模型 × 12 个基准，一致提升
   - 算术推理：+2.3% ~ +7.5%
   - 常识推理：+1.8% ~ +4.0%

---

## 关键概念页面

- [[concepts/hyplora]] — 方法详解
- [[concepts/hyperbolic-geometry-llm]] — 嵌入几何分析
- [[concepts/hyperbolic-geometry]] — 双曲几何基础
- [[concepts/lora]] — 基线方法

---

## 学习材料

- 快速摘要: [[raw/papers/hyperbolic-fine-tuning-llms/quick-summary]]
- 详细总结: [[raw/papers/hyperbolic-fine-tuning-llms/summary]]
- 核心洞察: [[raw/papers/hyperbolic-fine-tuning-llms/insights]]
- 方法拆解: [[raw/papers/hyperbolic-fine-tuning-llms/method]]
- 心智模型: [[raw/papers/hyperbolic-fine-tuning-llms/mental-model]]
- 批判反思: [[raw/papers/hyperbolic-fine-tuning-llms/reflection]]
- 自测问答: [[raw/papers/hyperbolic-fine-tuning-llms/qa]]
