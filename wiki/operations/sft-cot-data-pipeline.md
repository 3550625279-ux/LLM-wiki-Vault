---
type: operation
title: "CoT SFT数据生产线"
created: 2026-06-16
updated: 2026-06-16
tags: [CoT, SFT, 数据生产, 蒸馏, rejection-sampling]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/training]]"
  - "depends_on::[[concepts/chain-of-thought]]"
  - "depends_on::[[concepts/sft]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
---

# CoT SFT数据生产线

## 🔗 关系链接

- belongs_to: [[domains/training]]
- depends_on: [[concepts/chain-of-thought]]
- depends_on: [[concepts/sft]]
- produced_by: [[sources/llm-reasoning-ability]]

---

## 概述

推理链SFT的核心瓶颈是**数据从哪来**。人工标注推理链极其昂贵。实践中演化出了四条主流数据生产线。

## 四条路径

### 路径一：人工标注

- 质量最高，但不可规模化
- OpenAI在训练早期推理模型时雇佣了大量标注员编写CoT数据
- LIMA (Zhou et al., 2023) 证明1000条精心标注的数据就能达到接近GPT-4的对话质量
- **规律**: 一条清晰、正确、逻辑自洽的推理链，抵过十条只有答案没有过程的数据

### 路径二：教师模型蒸馏

用更强的模型对海量问题生成推理链，作为小模型的SFT数据。**开源社区最主流的生产方式。**

- **Self-Instruct** (Wang et al., 2023): 用少量种子指令让LLM自己生成更多指令-回答对
- **Evol-Instruct / WizardLM** (Xu et al., 2023): 从简单指令出发，让LLM通过"深化"和"拓宽"操作演化出复杂指令
- **Orca** (Mukherjee et al., 2023): 不仅蒸馏最终答案，还蒸馏教师的"解释轨迹"（explanation traces）

### 路径三：程序合成

- 对于数学、编程等有明确求解器的领域，可以用程序自动生成问题+推理链+答案
- 例如用符号计算引擎生成代数题，用编译器验证代码正确性
- 保证100%正确率，但覆盖的问题类型受限

### 路径四：Rejection Sampling

让模型自己对同一问题生成N条推理链（如N=64），用验证器筛出正确的，作为下一轮SFT的训练数据。即使模型初始正确率只有30%，生成足够多样本后大概率能找到正确的。

> 这是一种介于SFT和RL之间的数据策略——不涉及梯度更新，但利用了模型的采样能力。

## 关键原则

> 质量 > 数量。在推理任务上，**正确性是质量的第一维度**——一条推理链再流畅、再多步骤，只要中间有一步错了，整条就是负样本。

## 相关节点

- [[concepts/chain-of-thought]] — CoT数据格式定义
- [[concepts/sft]] — 数据的消费端
- [[concepts/data-flywheel]] — 迭代增强的数据生产
- [[concepts/test-time-compute]] — Rejection Sampling策略
