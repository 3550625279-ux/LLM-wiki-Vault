# Intent Detection in the Age of LLMs

> **EMNLP 2024 Industry Track** | Amazon & IIT Jammu
> 作者：Gaurav Arora, Shreya Jain, Srujana Merugu

---

## 📖 论文概述

本文研究如何在任务导向对话系统（TODS）中利用 LLM 进行意图检测。作者对比了 7 个 SOTA LLM（Claude 和 Mistral 系列）与 SetFit 微调模型的性能/延迟权衡，并提出了一个**基于不确定性路由的混合系统**：仅在 SetFit 不确定时才调用 LLM，从而在保持接近 LLM 准确率（差距 <2%）的同时将延迟降低约 50%。论文还通过控制实验揭示了 LLM 的域外检测（OOS）能力受意图标签范围和标签空间大小的显著影响，并提出了利用 LLM 内部表示的两步方法改进 OOS 检测。

## 🎯 难度等级

**中级（Intermediate）** — 涉及多种模型架构对比和混合系统设计，但不涉及复杂数学推导。

## ⏱️ 预计学习时间

- 快速浏览：**30 分钟**
- 深入理解：**2-3 小时**
- 完整掌握（含代码实验）：**4-5 小时**

## 🗺️ 学习路径建议

1. **[[summary.md]]** → 先了解论文的核心贡献和关键结果
2. **[[method.md]]** → 深入理解方法细节：SetFit、LLM ICL、混合路由
3. **[[insights.md]]** → 理解核心洞察和实际意义
4. **[[mental-model.md]]** → 建立思维框架，理解论文在研究图谱中的位置
5. **[[qa.md]]** → 通过 15 道问答题检验理解
6. **[[reflection.md]]** → 反思开放问题和扩展方向
7. **code/** → 运行代码演示加深理解
8. **index.html** → 交互式探索核心概念

## 📂 文件结构

```
intent-detection-age-of-llms/
├── README.md          ← 你在这里
├── summary.md         ← 论文摘要与核心贡献
├── method.md          ← 方法详解（SetFit + LLM + 混合路由 + OOS 检测）
├── insights.md        ← 深度洞察与实践启示
├── mental-model.md    ← 思维框架与研究定位
├── qa.md              ← 15 道问答题（基础/中级/高级各 5 题）
├── reflection.md      ← 开放问题与扩展方向
├── meta.json          ← 论文元数据
├── index.html         ← 交互式概念探索器
├── code/              ← 代码演示
│   ├── negative_augmentation_demo.py
│   └── uncertainty_routing_demo.py
├── images/            ← 论文图片
└── paper.pdf          ← 原始论文
```

## 🔑 关键收获

1. **LLM vs. 小模型不是二选一**：通过不确定性路由可以兼顾准确率和延迟
2. **负面数据增强简单有效**：替换/删除关键词生成 OOS 样本，SetFit F1 提升 >5%
3. **OOS 检测是 LLM 的短板**：意图标签范围和标签空间大小显著影响 OOS 性能
4. **内部表示有潜力**：利用 LLM 最后一层的内部表示进行 OOS 检测，Mistral-7B 准确率和 F1 提升 >5%

## 🏷️ 标签

`intent detection` · `hybrid routing` · `OOS detection` · `in-context learning` · `SetFit` · `Monte Carlo Dropout`
