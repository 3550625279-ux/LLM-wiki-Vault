# MASTER-INDEX.md — AI Learning Vault 完整体系清单

> **系统版本**: v2.0
> **设计原则**: 知识复利增长 · 会话无状态 · 原子性 · 矛盾保留 · 主动回忆
> **参考来源**: Karpathy LLM Wiki Pattern + Zettelkasten + 认知科学 SRS

---

## 一、完整文件树

```
AI Vault/
│
├── CLAUDE.md                         ✅ 系统宪法 v2.0 (行为规则 + 协议定义)
├── WIKI.md                           ✅ 节点 Schema + 关系语义规范
├── AGENTS.md                         ✅ Claude Code 代理行为约束
├── DEPLOY-GUIDE.md                   ✅ 部署指南 (PowerShell 一键脚本)
├── MASTER-INDEX.md                   ✅ 完整体系清单 (本文件)
├── .mcp.json                         ✅ MCP 服务配置 (filesystem/github/flux...)
│
├── .claude/
│   └── settings.json                 ✅ Hooks 配置 (PreToolUse/PostToolUse/Stop)
│
├── .obsidian/
│   └── snippets/
│       └── vault-colors.css          ✅ Obsidian 颜色主题 (节点类型着色)
│
├── .vault-meta/
│   └── mode.json                     ✅ 运行模式配置 (research/review/maintenance)
│
├── wiki/                             ← LLM 维护的知识库核心
│   ├── index.md                      ✅ 全量内容目录 (每次 ingest 更新)
│   ├── hot.md                        ✅ 热缓存 ~500词 (每次会话覆盖更新)
│   ├── log.md                        ✅ 时序日志 append-only
│   ├── overview.md                   ✅ 全局知识地图 (8大领域关系图)
│   │
│   ├── domains/                      ← 8个顶层领域综述 (Map of Content)
│   │   ├── foundations.md            ✅ 数学与理论基础
│   │   ├── architecture.md           ✅ 模型架构
│   │   ├── training.md               ✅ 训练方法论
│   │   ├── alignment.md              ✅ 对齐与安全
│   │   ├── inference.md              ✅ 推理与部署
│   │   ├── multimodal.md             ✅ 多模态
│   │   ├── agents.md                 ✅ 智能体系统
│   │   └── engineering.md            ✅ 工程实践
│   │
│   ├── concepts/                     ← Permanent Notes: 原理/算法
│   │   └── idx.md                 ✅ Concepts 目录 MoC
│   │   └── [待 ingest 后创建...]
│   │
│   ├── entities/                     ← 模型/论文/作者/数据集
│   │   └── idx.md                 ✅ Entities 目录 MoC
│   │   └── [待 ingest 后创建...]
│   │
│   ├── operations/                   ← How-to: 代码/调参/SOP
│   │   └── idx.md                 ✅ Operations 目录 MoC
│   │   └── [待 ingest 后创建...]
│   │
│   ├── insights/                     ← Evergreen Notes: 个人洞察
│   │   └── idx.md                 ✅ Insights 目录 MoC
│   │   └── [待 ingest 后创建...]
│   │
│   ├── sources/                      ← 原始资料摘要页
│   │   └── [待 ingest 后创建...]
│   │
│   ├── comparisons/                  ← 横向对比分析
│   │   └── [待创建...]
│   │
│   ├── questions/                    ← 问答 + 知识缺口
│   │   └── [待 query/align 后创建...]
│   │
│   ├── folds/                        ← 折叠的复杂推导
│   │   └── [按需创建...]
│   │
│   ├── canvases/                     ← 关系图/学习路径 (Obsidian Canvas)
│   │   └── [按需创建...]
│   │
│   └── meta/                         ← 系统状态
│       ├── SYSTEM-STATUS.md          ✅ 系统健康状态
│       ├── dashboard.md              ✅ 知识看板 (Dataview)
│       ├── delta-register.md         ✅ 信息差变更记录
│       └── contradiction-ledger.md   ✅ 矛盾/张力登记册
│
├── skills/                           ← Claude Code Skills 协议文件
│   ├── ingest/
│   │   └── SKILL.md                  ✅ 5阶段注入协议
│   ├── align/
│   │   └── SKILL.md                  ✅ Index-First Traversal 对齐
│   ├── lint/
│   │   └── SKILL.md                  ✅ L1-L4 健康检查
│   ├── review/
│   │   └── SKILL.md                  ✅ SRS + 主动回忆
│   └── save/
│       └── SKILL.md                  ✅ 会话结晶归档
│
├── scripts/                          ← 自动化脚本
│   ├── align-check.sh                ✅ grep-based 对齐检查
│   └── session-seal.sh               ✅ 会话封印统计
│
├── _templates/                       ← 节点模板
│   ├── concept.md                    ✅ Concept 节点模板
│   ├── entity.md                     ✅ Entity 节点模板
│   ├── operation.md                  ✅ Operation 节点模板
│   ├── insight.md                    ✅ Insight 节点模板
│   └── domain.md                     ✅ Domain 节点模板
│
├── _attachments/
│   └── assets/                       ← Flux 生成的概念插画 (按需)
│
└── raw/                             ← 【隔离区】不可变原始资料
    ├── papers/                       ← 论文 PDF / arXiv 摘录
    ├── articles/                     ← 博客、技术文章
    ├── transcripts/                  ← 视频/播客文字稿
    ├── code/                         ← 代码片段
    ├── conversations/                ← 提炼后的 AI 对话
    └── _quarantine/                  ← 可疑内容隔离
```

---

## 二、文件清单（按功能分类）

### 🏛️ 核心宪法文件 (3个)
| 文件 | 用途 | 覆盖优先级 |
|------|------|----------|
| `CLAUDE.md` | 行为规则 + 所有协议的入口 | 每次 Claude Code 会话自动加载 |
| `WIKI.md` | 节点 Schema + 关系语义 | 创建节点时参考 |
| `AGENTS.md` | 代理约束 + 技能调度规则 | Claude Code agents 参考 |

### 🔧 配置文件 (3个)
| 文件 | 用途 |
|------|------|
| `.claude/settings.json` | Hooks 守卫（禁止污染 raw/，强制 frontmatter）|
| `.mcp.json` | MCP 服务（filesystem/github/mcpvault/flux）|
| `.vault-meta/mode.json` | 当前运行模式（research/review/maintenance）|

### 🛠️ Skills 技能文件 (5个)
| 文件 | 触发命令 | 核心功能 |
|------|---------|---------|
| `skills/ingest/SKILL.md` | `ingest [source]` | 5阶段注入：Triage→Extract→Integrate→Link→Seal |
| `skills/align/SKILL.md` | `align` / `对齐检查` | Index-First Traversal + Delta Register |
| `skills/lint/SKILL.md` | `lint` / `健康检查` | L1 结构 / L2 质量 / L3 关系 / L4 认知 |
| `skills/review/SKILL.md` | `review` / `复习` | SRS 调度 + 主动回忆 5题型 |
| `skills/save/SKILL.md` | `/save` / `归档对话` | 会话精华 → 永久节点 |

### 📜 脚本文件 (2个)
| 文件 | 命令 | 用途 |
|------|------|------|
| `scripts/align-check.sh` | `bash scripts/align-check.sh [词]` | grep 对齐，无 MCP 时使用 |
| `scripts/session-seal.sh` | `bash scripts/session-seal.sh` | 会话统计 + hot.md 更新提醒 |

### 🗺️ Wiki 核心文件 (5个)
| 文件 | 更新频率 | 维护者 |
|------|---------|--------|
| `wiki/concepts-idx.md` | 每次 ingest | Claude (自动) |
| `wiki/hot.md` | 每次会话结束 | Claude (强制) |
| `log.md` | 每次会话结束 | Claude (append) |
| `wiki/overview.md` | 每 10 次 ingest | Claude (align 触发) |
| `wiki/meta/dashboard.md` | 每次 lint | Claude (自动) |

### 🌐 领域综述 (8个)
`wiki/domains/`: foundations / architecture / training / alignment / inference / multimodal / agents / engineering

### 📁 子目录 MoC (4个)
`wiki/concepts/concepts-idx.md` / `wiki/entities/entities-idx.md` / `wiki/operations/operations-idx.md` / `wiki/insights/insights-idx.md`

### 📝 节点模板 (5个)
`_templates/`: concept / entity / operation / insight / domain

### 🎨 样式文件 (1个)
`.obsidian/snippets/vault-colors.css`

---

## 三、技能触发速查表

| 用户输入 | 技能文件 | 核心产出 |
|---------|---------|---------|
| `ingest [文件/URL]` | `skills/ingest/SKILL.md` | 新节点 + 关系边 + log.md 记录 |
| `align` / `对齐检查` | `skills/align/SKILL.md` | Delta 报告 + delta-register 更新 |
| `lint` / `健康检查` | `skills/lint/SKILL.md` | 健康报告 + dashboard 更新 |
| `review` / `复习` | `skills/review/SKILL.md` | 5道回忆题 + 间隔复习调度 |
| `/save` / `归档对话` | `skills/save/SKILL.md` | 会话精华节点 + hot.md 更新 |
| `query: [问题]` | 内置（无需加载） | 直接回答 + questions/ 归档 |

---

## 四、关系语义速查表

| 边类型 | 含义 | 特殊规则 |
|--------|------|---------|
| `depends_on::` | 学 A 前必须掌握 B | — |
| `implements::` | A 代码实现了算法 B | — |
| `extends::` | A 扩展/泛化了 B | — |
| `contrasts::` | A 与 B 是替代关系 | — |
| `contradicts::` | A 与 B 有矛盾 | **永久保留，lint 不得删除** |
| `corrects::` | A 修正了 B 的旧认知 | 旧节点保留，标注 |
| `applied_in::` | 概念 A 在实体 B 中的应用 | — |
| `precedes::` | A 在时间/逻辑上先于 B | — |
| `synthesizes::` | A 综合了多个节点 | — |
| `part_of::` | A 是 B 的组成部分 | — |
| `instance_of::` | A 是概念 B 的具体实例 | — |

---

## 五、Hooks 守卫规则

| 触发时机 | 规则 | 违反后果 |
|---------|------|---------|
| PreToolUse (Write) | 禁止向 `raw/` 写入 | 操作被阻止 |
| PreToolUse (Write) | `log.md` 必须以 `## [YYYY-MM-DD]` 开头 | 操作被阻止 |
| PostToolUse (Write) | 新建 wiki 节点必须有 `type:` frontmatter | 警告提示 |
| Stop | 会话结束前提醒更新 `hot.md` | 提醒（非阻止）|

---

## 六、部署核查清单

### 最小化部署（必须完成）
- [ ] 将 `AI-Vault-System/` 所有文件复制到 `D:\Workspace\AI_Learning\AI Vault\`
- [ ] 打开 Claude Code，进入 Vault 目录
- [ ] 验证 `CLAUDE.md` 被自动加载（Claude Code 标准行为）
- [ ] 验证 `.claude/settings.json` Hooks 生效：`claude hooks list`
- [ ] 验证 MCP filesystem 生效：`claude mcp list`
- [ ] 运行 `bash scripts/session-seal.sh` 验证脚本可执行

### 推荐完成
- [ ] 在 Obsidian 中打开 Vault，启用 `vault-colors.css` CSS 片段
- [ ] 安装 Obsidian Dataview 插件（激活 dashboard.md 自动查询）
- [ ] 安装 Obsidian Templater 插件（使用 `_templates/`）
- [ ] 配置 GitHub Token 到 `.mcp.json`
- [ ] （可选）安装 mcp-obsidian：`npm i -g mcp-obsidian`

### 可选增强
- [ ] 配置 Flux Token（AceData）用于概念插画生成
- [ ] 安装 Obsidian Graph Analysis 插件
- [ ] 配置 Obsidian Spaced Repetition 插件（与 review 技能协同）

---

## 七、首次使用建议

```
第1步: 放入一篇论文到 raw/papers/
       建议: "Attention Is All You Need" (Vaswani et al. 2017)

第2步: ingest attention-is-all-you-need.pdf
       预期产出: 5-8 个新节点 + wiki/sources/vaswani-2017.md

第3步: 一周后 review
       预期: 系统推荐需要复习的节点，生成主动回忆题

第4步: align
       预期: 发现信息差，delta-register 有记录

第5步: lint (首次 10 次 ingest 后)
       预期: seed 堆积检查，孤儿节点检测
```

---

## 八、总计

| 类别 | 数量 |
|------|------|
| 核心宪法文件 | 3 |
| 配置文件 | 3 |
| Skills 技能文件 | 5 |
| 自动化脚本 | 2 |
| Wiki 核心文件 | 5 |
| 领域综述 | 8 |
| 子目录 MoC | 4 |
| 节点模板 | 5 |
| 系统状态文件 | 4 |
| 样式文件 | 1 |
| 部署文档 | 2 |
| **总计** | **42** |

---

*MASTER-INDEX v1.0 | 生成时间: 2026-06-13 | AI Vault System v2.0*
