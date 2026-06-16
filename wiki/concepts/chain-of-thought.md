---
type: concept
title: "推理链（Chain-of-Thought, CoT）"
created: 2026-06-16
updated: 2026-06-16
tags: [CoT, 推理链, 思维链, SFT, 推理]
status: seed
complexity: intermediate
domain: Training
sources: ["[[sources/llm-reasoning-ability]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "produced_by::[[sources/llm-reasoning-ability]]"
  - "applied_in::[[concepts/sft]]"
  - "applied_in::[[concepts/process-reward-model]]"
  - "applied_in::[[concepts/data-flywheel]]"
---

# 推理链（Chain-of-Thought, CoT）

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- produced_by: [[sources/llm-reasoning-ability]]
- applied_in: [[concepts/sft]]
- applied_in: [[concepts/process-reward-model]]

---

## 定义

推理链（Chain-of-Thought, CoT）是一种训练数据格式和推理策略，要求模型在给出最终答案前，先展示中间推理步骤。

## 关键发现

Wei et al. 2022 发现：让模型在回答中展示中间步骤，推理准确率从 **17% 飙升到 78%**。

## 数据格式

```
【输入（Prompt）】
请一步一步思考解决以下问题，最后输出答案。

【输出（Target，全量计算交叉熵损失）】
步骤1: ...
步骤2: ...
...
最终答案: ...
```

## 获取CoT数据的四条路径

| 路径 | 方法 | 优劣 |
|------|------|------|
| 人工标注 | 标注员编写CoT数据 | 质量最高，不可规模化 |
| 教师模型蒸馏 | 用更强模型生成推理链 | 开源社区主流 |
| 程序合成 | 符号引擎+编译器验证 | 100%正确率，覆盖类型受限 |
| Rejection Sampling | 模型自己生成N条，验证器筛 | 介于SFT和RL之间 |

> 重要性：质量 > 数量。一条推理链再流畅，只要中间有一步错了，整条就是负样本。

## 相关节点

- [[concepts/sft]] — CoT是SFT的关键数据格式
- [[concepts/process-reward-model]] — PRM对CoT每一步打分
- [[operations/sft-cot-data-pipeline]] — CoT数据生产操作
- [[concepts/data-flywheel]] — 迭代生成更好的CoT数据
