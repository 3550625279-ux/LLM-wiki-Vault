---
name: ingest
description: >
  5阶段知识注入协议。将任意资料（论文/博客/视频文字稿/代码/对话）
  编译为结构化 wiki 节点，建立语义网络，保证幂等性。
  触发词: ingest, add this, process this, file this, 把这个加入, 注入.
allowed-tools: Read Write Edit Glob Grep Bash
---

# ingest — 5阶段知识注入 Skill

> 核心原则: 每次 ingest 让知识库更丰富，知识网络更稠密。
> 幂等性保证: 相同资料第二次 ingest → 只更新 updated 时间戳。

---

## 触发条件

| 输入形式 | 处理方式 |
|----------|----------|
| 粘贴论文摘要/全文 | 提取核心概念 + 实体 + 引用 |
| 粘贴博客/文章 | 提取核心洞察 + 实践经验 |
| 粘贴视频文字稿 | 提取关键论点 + 时间戳 |
| 粘贴代码片段 | 归档为 operation 节点 |
| 粘贴对话记录 | 提炼洞察 + 归档 insight |
| URL/标题 | 先 autoresearch，再 ingest |

---

## 5阶段流程

### Phase 1 — TRIAGE（分诊，≤30秒）

```
读取资料前10%
↓
判断:
  主类型: concept | entity | operation | insight | source
  领域: Foundations | Architecture | Training | Alignment |
        Inference | Multimodal | Agents | Engineering
  难度: basic | intermediate | advanced
↓
输出 triage 简报 (2-3行):
  "类型: [X] | 领域: [Y] | 预计创建: N页 | 预计更新: M页"
```

### Phase 2 — EXTRACT（提取，完整读取）

```
提取:
  ① 核心概念列表 (≤10个，每个一句话定义)
  ② 关键实体 (模型/论文/作者/机构/数据集)
  ③ 可操作知识点 (代码/参数/工程经验)
  ④ 与已有知识的关系 (矛盾/扩展/修正/依赖)
  ⑤ 个人洞察候选: "从这里我学到了..."
```

### Phase 3 — INTEGRATE（整合，去重优先）

**去重检查（创建前必须执行）:**
```bash
grep -rl "title:.*关键概念" wiki/ --include="*.md"
grep -rl "关键概念" wiki/ --include="*.md" | head -5
```

- 相似度 >70% → **UPDATE** 已有页（不新建）
- 无相似页 → **CREATE** 新页面

**frontmatter 模板（所有节点必须包含）:**
```yaml
---
type: concept
title: "页面标题"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [概念标签, 领域标签]
status: seed
complexity: intermediate
domain: Architecture
sources: ["[[source摘要页]]"]
related:
  - "depends_on::[[前置概念]]"
  - "extends::[[父概念]]"
  - "corrects::[[旧认知页面]]"
thumbnail: ""
---
```

**关系语义词典:**

| 前缀 | 含义 |
|------|------|
| `depends_on::` | 学习A前必须掌握B |
| `implements::` | 代码实现了算法 |
| `extends::` | 扩展/深化已有概念 |
| `corrects::` | 新信息修正旧认知（保留！） |
| `contrasts::` | 对比/替代关系 |
| `applied_in::` | 概念在某实体中的应用 |
| `part_of::` | 子组件关系 |

### Phase 4 — LINK（建立语义网络）

```
1. 更新所属 wiki/domains/<domain>.md（添加 [[wikilink]]）
2. 更新相关 concept/entity 页的 related: 字段
3. 更新 wiki/concepts-idx.md（添加新页到对应分类）
4. 检查反向链接（被引用页是否需要更新 related:）
```

### Phase 5 — SEAL（封印，幂等保证）

```
1. 写入 wiki/sources/<slug>.md（原始资料摘要页）
2. 追加 log.md:
   ## [YYYY-MM-DD HH:MM] ingest | 资料标题
   - type: X
   - domain: Y
   - pages_created: N
   - pages_updated: M
   - key_concepts: [A, B, C]
   - contradictions: [若有]
3. 更新 wiki/hot.md（最新学习重心 + 新增节点摘要）
4. 若发现矛盾 → 追加 wiki/meta/contradiction-register.md
5. 若 status=developing → 触发 Flux 图像生成（若配置），见 `skills/flux-illustrate/SKILL.md`
6. 更新 wiki/meta/dashboard.md（系统状态 + 待办进度 + 月度目标计数）
```

---

## Raw 源文件规范

所有 ingest 资料必须以 `.md` 格式存入 `raw/` 目录，无论原始格式：

| 原始格式 | 处理方式 | 存入路径 |
|----------|----------|----------|
| URL/网页 | WebFetch + defuddle 清洗 | `raw/articles/{slug}-{YYYY-MM-DD}.md` |
| .txt 文本 | 添加 frontmatter 包装 | `raw/articles/{slug}-{YYYY-MM-DD}.md` |
| .pdf 论文 | 提取摘要 + 关键段落 | `raw/papers/{slug}-{YYYY-MM-DD}.md` |
| 视频/播客 | 文字稿 | `raw/transcripts/{slug}-{YYYY-MM-DD}.md` |
| 代码片段 | 说明 + 代码 | `raw/code/{slug}-{YYYY-MM-DD}.md` |
| 对话记录 | 提炼内容 | `raw/conversations/{slug}-{YYYY-MM-DD}.md` |

**Raw 文件 frontmatter 格式**：
```markdown
---
source_url: "https://..." (如有)
original_format: "txt|pdf|url|video|code|conversation"
fetched: YYYY-MM-DD
ingested: YYYY-MM-DD
---
```

**Source 页链接规范**：`wiki/sources/` 页面必须在正文开头包含可点击的原始资料链接：
```markdown
> 📄 原始资料: [[raw/articles/slug-YYYY-MM-DD]]
```
```

---

## 预期输出

```
✅ ingest 完成: [资料标题]
- 创建节点: N 个 ([名称列表])
- 更新节点: M 个
- 新增语义边: K 条
- 矛盾发现: 0/X 条 (若有，见 contradiction-register)
- hot.md: 已更新
```

---

## 常见资料类型处理提示

| 资料类型 | 重点提取 | 主要节点类型 |
|----------|----------|-------------|
| 论文 | Abstract + 方法 + 实验结论 | entity(论文) + concept(方法) |
| 博客技术文章 | 核心洞察 + 代码示例 | insight + operation |
| 视频文字稿 | 关键论点 + 类比 | concept + insight |
| 代码实现 | 算法流程 + 参数 + 陷阱 | operation |
| 对话记录 | 提炼问答 + 新发现 | insight + question |
