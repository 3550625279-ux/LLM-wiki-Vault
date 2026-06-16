---
type: meta
title: "Domains Index — 领域导航"
updated: 2026-06-16
tags: [meta, index, domains]
status: evergreen
---

# Domains Index — 领域导航

> 每个领域页面 = 领域综述 + 节点索引（一体两面，不拆分）。

---

## 领域一览

| 领域 | 核心问题 | 节点数 | 状态 |
|------|----------|--------|------|
| [[Foundations]] | 为什么 AI 有效？ | 2 | seed |
| [[Architecture]] | 模型怎么设计？ | 2 | developing |
| [[Training]] | 模型怎么训练？ | 16 | developing |
| [[Alignment]] | 模型怎么对齐人类？ | 2 | seed |
| [[Inference]] | 模型怎么高效运行？ | 1 | seed |
| [[Multimodal]] | 多种信息怎么融合？ | 5 | developing |
| [[Agents]] | 模型怎么自主行动？ | 3 | seed |
| [[Engineering]] | 怎么工程化落地？ | 4 | seed |
| [[common-computer]] | 通用计算机基础设施 | 8 | seed |

---

## 结构说明

```
wiki/domains/
├── domains-idx.md        ← 本文件（顶级导航）
├── Foundations.md        ← 领域综述 + 已有节点 + 关键缺口
├── Architecture.md
├── Training.md
├── Alignment.md
├── Inference.md
├── Multimodal.md
├── Agents.md
├── Engineering.md
└── common-computer.md
```

每个域页面包含：
- **领域地图**：该领域的知识树
- **已有节点**：已 ingest 的 concept/entity/source（`[x]` 标记）
- **关键缺口**：待创建的节点（`[ ]` 标记）
- **领域间关系**：`depends_on::` / `extends::` / `applied_in::`
- **推荐资料**：该领域的必读论文/书籍

---

## 统计

| 指标 | 值 |
|------|-----|
| 领域数 | 9/9 |
| developing | 3 (Architecture, Training, Multimodal) |
| seed | 6 |
| 总节点 | 43 |

*上次更新: 2026-06-16 | LLM推理能力后训练技术栈 ingest*
