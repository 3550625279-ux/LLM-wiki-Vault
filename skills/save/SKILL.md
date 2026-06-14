---
name: save
description: >
  将当前对话内容归档为 wiki 节点。分析对话，判断类型，
  填写标准 frontmatter，归档到正确目录，更新 index + log + hot.md。
  触发词: save, /save, file this, 归档, 保存这个, 记录下来.
allowed-tools: Read Write Edit Glob Grep
---

# save — 对话归档 Skill

> 对话是最容易丢失的知识。save 让有价值的讨论成为永久知识节点。
> 核心原则: 归档 ≠ 复制粘贴。归档 = 提炼 + 结构化 + 关联。

---

## 触发条件

| 触发词 | 处理方式 |
|--------|----------|
| `save` / `/save` | 归档当前完整对话 |
| `save this insight` | 仅归档洞察部分 |
| `save the code` | 归档代码为 operation 节点 |
| `file this` / `归档` | 同 `save` |
| `save as question` | 归档为待解答问题 |

---

## 归档流程（5步）

### Step 1 — 分析对话

```
扫描对话内容，判断：
  主要价值类型:
    ① 定义/原理 → type: concept
    ② 模型/论文/工具 → type: entity
    ③ 代码/步骤/经验 → type: operation
    ④ 个人洞察/避坑 → type: insight
    ⑤ 提问+回答 → type: question
    ⑥ 对比分析 → type: comparison
  
  所属领域: Foundations | Architecture | Training | Alignment |
            Inference | Multimodal | Agents | Engineering
  
  关联的已有节点: 读 wiki/concepts-idx.md 查找
```

### Step 2 — 确认归档目标

向用户确认（若类型不明确）：
```
📁 准备归档:
- 标题: [建议标题]
- 类型: [type]
- 领域: [domain]
- 目标路径: wiki/[类型目录]/[slug].md
- 关联节点: [[X]], [[Y]]

确认归档？(直接说"确认"或修改参数)
```

### Step 3 — 创建节点

**去重检查（先于创建）:**
```bash
grep -rl "title:.*建议标题" wiki/ --include="*.md"
```

**生成节点文件:**
```yaml
---
type: insight
title: "洞察: [主题]"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [相关标签]
status: seed
complexity: intermediate
domain: [领域]
sources: ["conversation-YYYY-MM-DD"]
related:
  - "extends::[[关联概念]]"
  - "applied_in::[[应用实体]]"
thumbnail: ""
---

# [标题]

## 核心洞察
[1-3句话，精炼的核心发现]

## 详细说明
[来自对话的关键内容，去除冗余]

## 实践意义
[这个洞察如何影响实际行动]

## 关联知识
- [[相关概念]] — [关联说明]

## 来源
对话归档 | [日期] | [简短上下文描述]
```

### Step 4 — 更新语义网络

```
1. 更新 wiki/concepts-idx.md：添加新节点记录
2. 更新关联节点的 related: 字段（添加反向链接）
3. 更新 wiki/domains/<domain>.md（若有新洞察）
```

### Step 5 — 封印

```
追加 log.md:
## [YYYY-MM-DD HH:MM] save | [节点标题]
- type: [type]
- domain: [domain]
- path: wiki/[目录]/[slug].md
- related_nodes: [列表]

更新 wiki/hot.md（若洞察重要）
```

---

## 特殊情况处理

### 归档代码片段
```yaml
type: operation
title: "实现: [算法名]"
tags: [语言, 框架, 算法]
```
代码块用 ` ```python ``` ` 包裹，添加注释说明关键步骤。

### 归档问答
```yaml
type: question
title: "Q: [问题]"
status: answered
```
包含问题、答案摘要、置信度、后续追问方向。

### 归档对比分析
```yaml
type: comparison
title: "[A] vs [B]: [维度]"
```
包含对比维度表格 + 适用场景结论。

---

## 输出确认

```
✅ 归档完成
- 路径: wiki/[目录]/[slug].md
- 类型: [type] | 领域: [domain]
- 语义边: N 条新增
- log.md: 已追加
- hot.md: [已更新/未变动]
```
