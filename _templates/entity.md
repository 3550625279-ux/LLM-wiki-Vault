---
title: "{{title}}"
type: entity
status: seed
domain: {{domain}}
tags: [{{tags}}]
created: {{date}}
updated: {{date}}
sources: []
related: []
confidence: medium
entity_subtype: paper  # paper / model / author / dataset / tool / organization
thumbnail: ""
---

# {{title}}

<!-- 根据 entity_subtype 选择对应模板段落，删除不用的 -->

---

## 📄 论文信息 (entity_subtype: paper)

| 字段 | 内容 |
|------|------|
| 作者 | |
| 机构 | |
| 发布日期 | |
| 发表于 | NeurIPS / arXiv / ICML / ... |
| 论文链接 | |
| 代码 | |
| 引用量 | （可选） |

---

## 🤖 模型信息 (entity_subtype: model)

| 字段 | 内容 |
|------|------|
| 开发者 | |
| 发布日期 | |
| 参数量 | |
| 上下文长度 | |
| 训练数据 | |
| License | |

---

## 🧑‍🔬 作者信息 (entity_subtype: author)

| 字段 | 内容 |
|------|------|
| 当前机构 | |
| 研究方向 | |
| 代表论文 | |
| 主页/Twitter | |

---

## 核心贡献

（3-5 条 bullet，每条描述一个关键创新点。用主动语态。）

- 提出了 ___，解决了 ___ 问题
- 证明了 ___
- 引入了 ___ 方法，相比之前 ___ 提升了 ___

---

## 关键数据/结果

（Benchmark 结果、参数量、训练成本等可量化数据。）

| Benchmark | Score | 对比基线 |
|-----------|-------|---------|
| | | |

---

## 方法概述

（核心技术路线，引用 concept 节点。200字以内。）

---

## 影响与后续工作

（哪些工作 extends / corrects / contrasts 了本实体？）

- `extends::` [[]] — 在此基础上做了 ___
- `corrects::` [[]] — 修正了 ___ 的问题

---

## 个人评注

**可信度**: {{confidence}} 
**原因**: 
**我的看法**: 

---

## 参考
- 原始资料: `[[sources/]]`
