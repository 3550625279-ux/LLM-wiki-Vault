# AI Learning Vault — 系统宪法 v2.0

> **引擎**: claude-obsidian (Karpathy LLM Wiki Pattern)
> **模式**: Research (Mode E) — 个人 AI 学习多模态进化知识图谱
> **原则**: 知识是复利资产。每次 ingest 让知识库更丰富，每次 query 让答案更精准。
> **会话不是 load-bearing 的**：任何会话结束后，系统必须能从 `wiki/hot.md` 冷启动。

---

## 🎨 用户偏好

| 偏好 | 设置 | 生效范围 |
|------|------|----------|
| 论文输出路径 | `raw/papers/{paper-slug}/`（Vault 内） | 所有 claude-paper 技能 |
| 生成语言 | **中文**（所有论文摘要、学习材料） | 所有 claude-paper 技能 |
| 原始资料位置 | `raw/` 目录（不可变，只进不出） | ingest / ingest |

> ⚠️ claude-paper 插件默认输出到 `~/claude-papers/`，本项目要求输出到 Vault 的 `raw/papers/`。执行时需手动覆盖路径。

---

## 🧭 系统架构总览

```
raw/                    ← Layer 1: 不可变原始资料（只进不出）
    papers/              ← 论文 PDF / arXiv 摘录
    articles/            ← 博客、技术文章
    transcripts/         ← 视频/播客文字稿
    code/                ← 代码片段、notebook
    conversations/       ← 提炼后的 AI 对话

wiki/                    ← Layer 2: LLM 编译的知识库（你读，LLM 写）
    hot.md               ← 热缓存 ~500词，每次会话必读
    index.md             ← 全库目录，每次 ingest 更新
    overview.md          ← 全局摘要和知识地图
    domains/             ← 8个顶层领域综述页
    concepts/            ← 原理/算法/定义 (type:concept)
    entities/            ← 模型/论文/作者/机构 (type:entity)
    operations/          ← 代码实现/调参经验 (type:operation)
    insights/            ← 个人洞察/避坑 (type:insight)
    sources/             ← 每个原始资料的摘要页 (type:source)
    comparisons/         ← 横向对比 (type:comparison)
    questions/           ← 已回答问题 + gap页面 (type:question)
    folds/               ← log 折叠归档
    canvases/            ← 可视化画布
    meta/                ← 看板/lint报告/状态/矛盾登记册

_templates/              ← Templater 模板（5类）
log.md                   ← 操作日志（vault 根目录，不入图谱），格式: ## [YYYY-MM-DD HH:MM] verb | Title
_attachments/assets/     ← Flux 生成概念插画
skills/                  ← 17个 Claude Code Skills（含 align + review）
.claude/                 ← Hooks 配置 (settings.json)
scripts/                 ← 自动化脚本
.vault-meta/             ← 运行时元数据
```

---

## 🚀 会话启动协议 (每次必执行，静默)

```
1. 读取 wiki/hot.md（恢复上下文，不输出给用户）
2. 若 hot.md 不存在或内容 < 100词 → 读 wiki/concepts-idx.md 重建上下文
3. 就绪，等待用户指令
```

**禁止**：会话开始时主动输出 hot.md 内容。
**允许**：用户问"我们上次做到哪了"时朗读 hot.md。

---

## 📥 INGEST 协议 — 5阶段注入流程

**触发词**: `ingest`, `add this`, `process this`, `file this`, `把这个加入`, `注入`

### Phase 1 — TRIAGE（分诊，快速判断）
```
1. 读取资料前10%（摘要/Abstract/开头段落）
2. 判断主类型: concept | entity | operation | insight | source
3. 判断领域: Foundations | Architecture | Training | Alignment |
            Inference | Multimodal | Agents | Engineering
   ↳ 若不属于任何现有领域：
     - 用户明确要求新领域 → 立即创建 wiki/domains/<name>.md + 更新 overview.md
     - 内容自然聚合（3+ 同类节点）→ 建议用户创建新领域
     - 新领域创建时同步更新 concepts-idx.md 新增分区
4. 判断难度: basic | intermediate | advanced
5. 输出 triage 简报（2-3行）: 类型、领域、预计触碰页面数
```

### Phase 2 — EXTRACT（提取核心知识）
```
0. 归档原始资料（必须最先执行，不依赖任何分析结果）：
   - 对话 → raw/conversations/<slug>.md
   - 文章 → raw/articles/<slug>.md
   - 论文 → raw/papers/<slug>/
   - 代码 → raw/code/<slug>/
   - 归档完成后，在后续创建的 source 页面 frontmatter 中填写 raw_path: 字段

1. 完整读取资料后，提取：
- 核心概念列表（≤10个，每个一句话定义）
- 关键实体（模型名/论文/作者/机构/数据集）
- 可操作知识点（代码/参数/工程经验）
- 与已有知识的关系（矛盾/扩展/修正/依赖）
- 个人洞察候选："从这里我学到了..."
```

### Phase 3 — INTEGRATE（整合，核心步骤）

**去重优先** — 创建新页面前先检查：
```bash
# 标题搜索
grep -rl "title:.*关键概念" wiki/ --include="*.md"
# 内容搜索
grep -rl "关键概念" wiki/ --include="*.md" | head -5
```
- 相似度高（标题重合/内容重合>70%）→ **UPDATE** 已有页，不新建
- 无相似页 → **CREATE** 新页面

**⚠️ 强制域连接（concept 页面创建时必须执行）：**
```
1. frontmatter 中必须填写 domain: 字段（不可留空）
2. related: 中必须加 belongs_to::[[domains/<Domain>]]（向心边）
3. 创建完成后，立即更新对应域页面 wiki/domains/<Domain>.md：
   - 在"已有节点"段追加 [x] [[concepts/xxx]] 条目
   - 在"contains:: 边"段追加 contains::[[concepts/xxx]]
   - 若该概念同时属于多个域（如 CAT 属于 Architecture + Multimodal），
     每个域页面都要追加
4. 不允许创建 concept 后"留到后面再连域"——必须当场完成
5. frontmatter domain: 字段值 必须与 belongs_to:: 边的目标一致
   （两者是同一信息的两种表达，不可一个改了另一个没改）
```

**⚠️ 正文关系链接（每个新页面必须执行）：**
> Obsidian 不渲染 frontmatter 中的 `[[wikilink]]`，只有正文中的才能点击导航。
> 因此每个页面必须在 frontmatter 之后、正文内容之前，插入 `🔗 关系链接` 段落。

```
frontmatter related: → 结构化数据（供脚本/Dataview 查询）
正文 🔗 关系链接    → Obsidian 可点击导航
两者内容必须一致。
```

**正文关系链接格式（插在 frontmatter --- 之后、第一个 # 标题之后）：**
```markdown
## 🔗 关系链接

- belongs_to: [[domains/所属域]]
- depends_on: [[前置概念]] | [[另一前置]]
- extends: [[父概念]]
- produced_by: [[sources/来源页]]

---
```

**规则**：
1. frontmatter `related:` 中的每一条边，正文 `🔗 关系链接` 中必须有对应的 `[[wikilink]]`
2. 正文中使用简写格式（去掉 `::` 前缀，用 `|` 合并同类边）
3. 新页面创建时当场写入，不留到后面

**⚠️ 强制 Source 归口（ingest 诞生的节点必须归口到 source）：**
```
知识图谱层级结构：
  Layer 1: DOMAIN（中心枢纽）→ contains:: → concepts
  Layer 2: SOURCE（ingest 诞生）→ spawns:: → concepts/entities/comparisons/insights/questions
  Layer 3: CONCEPT → belongs_to:: → domain

ingest 时的连接规则：
1. source 页面的 related: 中，所有诞生的节点用 spawns:: 边（不是 implements/extends）
2. 被诞生的节点（concept/comparison/insight/question）的 related: 中必须加
   produced_by::[[sources/<slug>]] 边
3. source 页面必须填写 domain: 字段 + belongs_to::[[domains/<Domain>]]
4. source 诞生的所有节点必须当场建立 spawns:: / produced_by:: 双向边
```

**每个节点页面必须包含的 frontmatter：**
```yaml
---
type: concept          # concept | entity | operation | insight | source | comparison | question
title: "页面标题"
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags: [概念标签, 领域标签]
status: seed           # seed | developing | mature | evergreen
complexity: intermediate
domain: Architecture
sources: ["[[source摘要页]]"]
related:
  - "depends_on::[[前置概念]]"
  - "implements::[[算法实体]]"
  - "extends::[[父概念]]"
  - "corrects::[[旧认知页面]]"
  - "contrasts::[[对比对象]]"
  - "applied_in::[[应用实体]]"
  - "part_of::[[上级组件]]"
  - "belongs_to::[[domains/所属域]]"   # concept → domain（向心边，必填）
  - "produced_by::[[sources/来源页]]"  # 被 source 诞生的节点 → source（必填）
  - "spawns::[[concepts/诞生的概念]]" # source → 诞生的节点（source 页面用）
thumbnail: ""
raw_path: ""              # source 页面必填，指向 raw/ 下的原始文件
---
```

**每个新页面正文必须包含的 `🔗 关系链接` 段落（插在 frontmatter 后、标题后）：**
```markdown
## 🔗 关系链接

- belongs_to: [[domains/所属域]]
- depends_on: [[前置概念]]
- extends: [[父概念]]
- produced_by: [[sources/来源页]]

---
```

> ⚠️ frontmatter `related:` 和正文 `🔗 关系链接` 内容必须一致。
> 前者供脚本查询，后者供 Obsidian 导航。

### Phase 4 — LINK（建立语义网络）
```
1. 更新所属 domain 页（在"关键概念"段添加 [[wikilink]]）
2. 更新相关 concept/entity 页（related: 字段加语义边）
3. 更新 wiki/concepts-idx.md（添加新页到对应分类，附一行说明）
4. 更新 wiki/domains/<Domain>.md（域页面本身 = 综述 + 节点索引，一体两面）
5. 检查反向链接（被引用页的 related: 是否需要更新）
```

### Phase 4.5 — INGEST 更新清单（每次必过，不允许跳过）

> ⚠️ **这是防止遗漏的核心机制**。Phase 3-5 的描述是指导原则，本清单是强制执行的 checklist。
> 每次 ingest 结束前，必须逐项勾选确认。**不可凭"感觉差不多了"结束**。

```
□ A. 节点页面（Phase 3 产出）—— 确认每张新页面：
   □ frontmatter 完整（type/title/created/updated/tags/status/complexity/domain/sources/related）
   □ related 边覆盖所有语义关系（depends_on/extends/contrasts/applied_in/part_of/implements/corrects）
   □ 涉及多个领域时，每个领域都要建边（不只连一个 domain）
   □ frontmatter domain: 值与 belongs_to:: 边一致
   □ 正文包含 🔗 关系链接 段落，与 frontmatter related 内容一致
   □ 原始资料已归档到 raw/ + source 页面有 raw_path 字段

□ B. 领域页（可能 >1 个）：
   □ wiki/domains/<Domain1>.md — 领域地图 + 核心概念列表 + 领域关系
   □ wiki/domains/<Domain2>.md — 同上（如 CAT 既属于 Architecture 又属于 Multimodal）
   □ 每个 domain 页的 status/updated 日期已更新

□ C. 五个索引文件（全部必须检查）：
   □ wiki/concepts-idx.md — 新节点在对应分类下有条目 + 统计数字已更新
   □ wiki/concepts/concepts-idx.md — 新 concept 在领域分组 + 状态分组都有条目 + 统计已更新
   □ wiki/entities/entities-idx.md — 新 entity/论文/数据集有条目 + 待创建列表已更新
   □ wiki/insights/insights-idx.md — 如有新 insight 则更新，无则跳过
   □ wiki/operations/operations-idx.md — 如有新 operation 则更新，无则跳过

□ D. 相关工作对比（论文 ingest 时必须）：
   □ 创建 wiki/comparisons/<slug>.md — 横向对比页（论文中的 baseline 方法）
   □ 相关 concept 页的 related 中有 contrasts:: 指向对比页
   □ wiki/concepts-idx.md 的 comparison 分类下有条目

□ E. 元数据页（全部必须检查）：
   □ wiki/overview.md — 领域节点数 + 总节点数已更新
   □ wiki/meta/dashboard.md — 系统状态 + 待办队列 + 月度目标已更新
   □ wiki/meta/SYSTEM-STATUS.md — 知识库指标已更新

□ F. 封印页（Phase 5 产出）：
   □ wiki/sources/<slug>.md — 原始资料摘要页
   □ log.md（vault 根目录）— 追加 ingest 条目（含 pages_created/pages_updated/key_concepts）
   □ wiki/hot.md — 更新学习重心 + 活跃节点 + 统计快照
   □ 矛盾 → wiki/meta/contradiction-register.md（无矛盾则跳过）

□ G. 外部索引（如适用）：
   □ ~/claude-papers/index.json — 追加论文条目（claude-paper 技能时）
```

**执行规则**：
- **一次性连续执行** A→G，中间不停顿等待用户确认
- **不允许**凭"感觉差不多了"结束——必须逐项过清单
- **涉及多个领域**时（如 CAT 属于 Architecture + Multimodal），每个领域都要更新
- **论文 ingest** 时 D 项（对比页）是强制的，不是可选的

### Phase 5 — SEAL（封印，保证幂等）
```
1. 写入 wiki/sources/<slug>.md（原始资料摘要页）
2. 追加 log.md（vault 根目录，不是 wiki/log.md）：
   ## [YYYY-MM-DD HH:MM] ingest | 资料标题
   - type: source类型
   - domain: 所属领域
   - pages_created: N
   - pages_updated: M
   - key_concepts: [概念1, 概念2, ...]
   - contradictions: [若有，描述矛盾点]
3. 更新 wiki/hot.md（最新学习重心 + 新增节点摘要）
4. 若发现矛盾 → 追加 wiki/meta/contradiction-register.md
5. 更新 wiki/meta/dashboard.md（系统状态 + 待办进度 + 月度目标计数）
6. 更新 wiki/meta/SYSTEM-STATUS.md（知识库指标）
7. 更新 wiki/overview.md（领域节点数 + 总节点数）
```

**单次 ingest 预期触碰页面数**：8–20页（含所有索引和元数据页）
**幂等性保证**：相同资料第二次 ingest → 仅更新 updated 时间戳，不重复创建

---

## 🎯 ALIGNMENT 对齐协议 — 无 MCP 版

> **目标**：输出"已知/未知/需更新/缺口"的结构化 diff。无向量DB，纯 index+grep 实现。

**触发词**: `align`, `对齐`, `我知道多少关于`, `check my understanding`,
            `knowledge gap`, `信息差`, `我对X了解多少`, `where am I on X`

见 `skills/align/SKILL.md` 完整协议。

### 快速流程摘要（4步）
```
Step 1: 读 wiki/hot.md → 70%命中则快速输出
Step 2: 读 wiki/concepts-idx.md → 定位≤8个候选页
Step 3: 读候选页（≤5页）→ 提取语义边+矛盾+缺口
Step 4: 输出对齐报告（已知/需更新/缺口/学习路径）
```

**兜底检索**（index 无命中时）：
```bash
bash scripts/align-check.sh "查询关键词"
```

---

## 🔍 QUERY 协议

**触发词**: `query:`, `什么是`, `explain from wiki`, `summarize`

```
1. 读 wiki/hot.md
2. 读 wiki/concepts-idx.md（定位相关页）
3. 读目标页面（≤5页）
4. 检查 corrects:: → 优先新认知，标注旧认知
5. 合成答案，引用 [[wikilinks]]
6. 高质量答案 → 归档到 wiki/questions/
7. 发现缺口 → 创建 gap 页面
```

---

## 🔁 REVIEW 复习协议

**触发词**: `review`, `复习`, `quiz me`, `主动回忆`, `test me`, `考我`

见 `skills/review/SKILL.md`（间隔复习 + 主动回忆 + 6种题型 + 认知科学依据）

---

## 🔧 LINT 健康检查

**触发词**: `lint`, `health check`, `wiki audit`, `孤儿页`

频率：每10–15次 ingest 执行一次
输出：`wiki/meta/lint-report-YYYY-MM-DD.md`
检查项：孤儿页、死链、矛盾、stale claims、frontmatter缺失、seed堆积

---

## 📦 SAVE 归档

**触发词**: `save`, `/save`, `file this`, `归档`

分析对话 → 判断类型 → 填写 frontmatter → 归档到正确目录 → 更新 index + log + hot

---

## ⚙️ 稳定运转机制

### Hooks 自动化（.claude/settings.json）
- `Stop hook` → 运行 `scripts/post-session.sh` → 更新 hot.md + 封印 log
- `PostToolUse(Write/Edit) hook` → 运行 `scripts/log-write.sh` → 轻量写操作记录
- `PostToolUse(Write) prompt hook` → 写入 `wiki/concepts/` 或 `wiki/sources/` 后，询问用户是否生成 Flux 概念插画 → 存入 `_attachments/assets/` + 填写 frontmatter `thumbnail` + 页面内嵌 `![[...]]`
  详细交互流程见 `skills/flux-illustrate/SKILL.md`

### 关系语义词典（严格遵守，禁止自创新前缀）

| 前缀 | 含义 |
|------|------|
| `depends_on::` | 学习A前必须掌握B |
| `implements::` | 代码/系统实现了算法 |
| `extends::` | 扩展/深化已有概念 |
| `corrects::` | 新信息修正旧认知（**保留，不消除**） |
| `contrasts::` | 对比/替代关系 |
| `applied_in::` | 概念在某实体中的应用 |
| `part_of::` | 子组件关系 |
| `belongs_to::` | **节点 → 域**（向心边，concept 创建时必填） |
| `contains::` | **域 → 节点**（辐射边，域页面"已有节点"段自动维护） |
| `spawns::` | **Source → 诞生的节点**（ingest 时 source 页面必填） |
| `produced_by::` | **节点 → Source**（被 source 诞生的节点必填） |

### 矛盾处理原则
`corrects::` 边**永远保留**。矛盾本身是知识，不是错误。
发现矛盾时：保留双方，标注时间，记录来源，追加 `wiki/meta/contradiction-register.md`。

### Node 生命周期
```
seed → developing → mature → evergreen
```
- `seed`: 刚创建，基本信息
- `developing`: 2+来源引用，触发 Flux 图像生成
- `mature`: 完整 related 网络，经 lint 验证
- `evergreen`: 长期有效，不依赖单一来源

---

## 🔌 MCP Tools Protocol

| MCP | 状态 | 用途 |
|-----|------|------|
| filesystem | ✅ 活跃 | 文件读写底层传输 |
| github | ✅ 活跃 | autoresearch 查询代码仓库 |
| mcpvault | ⚠️ 已配置 | 激活后替代 grep 检索（BM25+语义） |
| flux | ✅ 已配置（全局 HTTP） | status=developing 节点生成概念插画 |

**flux 使用规则**：
- 仅对 `type: concept/source` 且 `thumbnail` 为空的节点生成
- 交互式 5 步工作流：询问 → 推荐方向 → 设计 prompt → 生成 → 整合
- 详细规则见 `skills/flux-illustrate/SKILL.md`

---

## 🚦 会话结束协议

每次会话结束（Stop hook 自动触发 或 手动 `bash scripts/post-session.sh`）：
```
1. 更新 wiki/hot.md：当前学习重心、本次节点、活跃线索、下次继续点
2. 追加 log.md（vault 根目录）会话条目
3. 若本次创建节点 > 5 → 更新 wiki/overview.md 统计数字
```

---

*AI Learning Vault v2.0 | claude-obsidian Karpathy LLM Wiki Pattern | 2026-06-13*
