# WIKI.md — 节点 Schema & 知识图谱规范 v2.0

> 本文件定义 AI Vault 中所有 wiki 节点的结构约束、关系语义和质量标准。
> 与 CLAUDE.md 配合使用：CLAUDE.md 定义行为协议，WIKI.md 定义数据规范。

---

## 一、节点 Frontmatter Schema

每个 wiki 节点必须以 YAML frontmatter 开头，字段如下：

```yaml
---
title: "节点标题"                    # 必填，与文件名对应
type: concept                         # 必填，见下方类型表
status: seed                          # 必填，见下方状态流转
domain: Foundations                   # 必填，见下方领域表
tags: [transformer, attention]        # 可选，小写 slug
created: 2026-06-13                   # 自动填写
updated: 2026-06-13                   # 每次修改时更新
sources: []                           # 原始资料引用，格式: [[sources/name]]
related: []                           # 类型化关系边，见下方语义词汇表
confidence: high                      # high / medium / low / speculative
thumbnail: ""                         # _attachments/assets/[slug].png (可选)
---
```

### 必填字段说明

| 字段 | 类型 | 约束 |
|------|------|------|
| `title` | string | 与文件名 slug 对应，使用标题大小写 |
| `type` | enum | 见节点类型表 |
| `status` | enum | seed / developing / mature / evergreen |
| `domain` | enum | 8个顶层领域之一 |
| `confidence` | enum | 评估当前节点内容可靠程度 |

---

## 二、节点类型表

| type | 路径 | Zettelkasten 对应 | 用途 |
|------|------|------------------|------|
| `concept` | `wiki/concepts/` | Permanent Note | 原理、算法、数学推导、核心思想 |
| `entity` | `wiki/entities/` | Literature Note → Permanent | 模型、论文、作者、数据集、机构 |
| `operation` | `wiki/operations/` | How-to Note | 代码实现、调参经验、工程 SOP |
| `insight` | `wiki/insights/` | Evergreen Note | 个人洞察、避坑经验、认知修正 |
| `domain` | `wiki/domains/` | Map of Content (MoC) | 领域综述，汇聚子链接 |
| `source` | `wiki/sources/` | Literature Note | 原始资料摘要（论文/文章/视频） |
| `comparison` | `wiki/comparisons/` | Synthesis Note | 横向对比分析 |
| `question` | `wiki/questions/` | Gap Note | 已回答问题 + 知识缺口 |
| `fold` | `wiki/folds/` | Reference Note | 折叠的复杂推导/证明 |

---

## 三、状态流转规则

```
seed ──→ developing ──→ mature ──→ evergreen
 │                                     │
 └── 新建节点，内容不完整           完全成熟，很少更新
     可有死链，无需强制完整         所有关系已建立
```

| 状态 | 条件 | 行为 |
|------|------|------|
| `seed` | 刚创建，内容草稿 | lint 不报错，允许死链 |
| `developing` | 核心内容已填写，关系待完善 | 至少 2 条 related 边 |
| `mature` | 内容完整，关系完整 | 无死链，有 sources |
| `evergreen` | 经过多次修订，内容稳定 | confidence: high |

**lint 规则**: `seed` 状态堆积超过 20 个时触发 `seed-overflow` 警告。

---

## 四、关系语义词汇表 (Typed Edges)

在 `related:` 字段中使用以下前缀，**冒号后直接跟 wikilink**：

```yaml
related:
  - "depends_on::[[Attention Mechanism]]"      # 学 A 前必须掌握 B（硬依赖）
  - "implements::[[Transformer Architecture]]" # 代码/操作 A 实现了算法 B
  - "extends::[[RNN]]"                         # A 扩展/泛化了 B
  - "contrasts::[[LSTM]]"                      # A 与 B 是替代/竞争关系
  - "contradicts::[[Scaling Hypothesis]]"      # A 与 B 存在矛盾（永久保留）
  - "corrects::[[Old Belief about X]]"         # A 修正了 B 的旧认知
  - "applied_in::[[GPT-4]]"                    # 概念 A 在实体 B 中具体应用
  - "precedes::[[BERT]]"                       # A 在时间/逻辑上先于 B
  - "synthesizes::[[概念A]], [[概念B]]"        # A 综合了多个节点
  - "part_of::[[Domain Overview]]"             # A 是 B 的组成部分
  - "instance_of::[[Concept]]"                 # A 是概念 B 的具体实例
```

> ⚠️ **矛盾保留铁律**: `contradicts::` 边由 Hooks 保护，lint **不得删除**。
> 矛盾本身是知识的一部分，必须在 `wiki/meta/contradiction-ledger.md` 登记。

---

## 五、8大顶层领域

| domain slug | 全称 | 覆盖范围 |
|-------------|------|---------|
| `Foundations` | 数学与理论基础 | 线性代数、概率论、信息论、优化理论 |
| `Architecture` | 模型架构 | Transformer、注意力机制、位置编码、MoE |
| `Training` | 训练方法论 | 预训练、微调、RLHF、数据工程 |
| `Alignment` | 对齐与安全 | 价值对齐、可解释性、红队测试 |
| `Inference` | 推理与部署 | 量化、蒸馏、KV Cache、投机解码 |
| `Multimodal` | 多模态 | Vision-Language、音频、视频、具身 |
| `Agents` | 智能体系统 | ReAct、工具使用、记忆、多智能体 |
| `Engineering` | 工程实践 | MLOps、分布式训练、评估框架 |

---

## 六、文件命名规范

```
wiki/concepts/attention-mechanism.md       ✅ kebab-case slug
wiki/entities/gpt-4.md                     ✅
wiki/entities/attention-is-all-you-need.md ✅ 论文用全名
wiki/sources/karpathy-llm-wiki-2024.md     ✅ 作者-关键词-年份
wiki/insights/dont-overtune-small-models.md ✅ 描述性短语

wiki/concepts/AttentionMechanism.md        ❌ 不用驼峰
wiki/concepts/attention.md                 ❌ 太模糊
```

---

## 七、节点内容结构规范

### concept 节点内容结构
```markdown
## 核心定义
（1-3句精确定义，避免废话）

## 关键机制
（核心工作原理，可含公式）

## 直觉解释
（用类比/例子建立直觉）

## 与相关概念的关系
（引用 related 中的节点，展开说明）

## 局限与边界
（什么情况下不适用？已知问题？）

## 参考
（原始资料引用）
```

### entity 节点内容结构（论文/模型）
```markdown
## 基本信息
- 作者 / 机构:
- 发布时间:
- 论文链接 / 代码:

## 核心贡献
（3-5 条 bullet，每条一个关键创新）

## 关键数据
（benchmark 结果、参数量、训练成本等）

## 方法概述
（核心技术路线，引用 concept 节点）

## 影响与后续
（后续哪些工作 extends / corrects 了本文）

## 个人评注
（confidence + 可信度评估）
```

---

## 八、质量标准 (Quality Gates)

每个 `mature` 或 `evergreen` 节点必须满足：

- [ ] frontmatter 完整（所有必填字段）
- [ ] `related` 至少 3 条类型化边
- [ ] `sources` 至少 1 条引用
- [ ] 无死链（所有 `[[wikilink]]` 指向真实存在的文件）
- [ ] 无孤儿（至少被 1 个其他节点引用）
- [ ] `confidence` 字段已评估

---

## 九、特殊节点规则

### idx.md 文件
每个子目录的 `idx.md` 是该目录的 Map of Content (MoC)：
- 列出该目录下所有节点，按 status 分组
- 不需要 frontmatter，不作为知识节点
- 由 lint 检查是否缺失

### sources/ 节点
- 每次 ingest 后创建对应 source 页
- 是 `raw/` 内容在 wiki 中的唯一代理
- 包含原始资料摘要、可信度评估、提炼节点列表

### questions/ 节点
- 包括两种：已回答问题（`answered: true`）和知识缺口（`gap: true`）
- 由 query 协议自动创建
- 好的回答本身就是知识，必须写回

---

*Schema Version: 2.0 | Last Updated: 2026-06-13*
