# AI Vault v2.0 — 部署指南

> 从零开始，10分钟内让 AI Learning Vault 完全运作。

---

## 🚀 快速启动（3步）

### Step 1 — 确认目录结构

```bash
cd "D:\Workspace\AI_Learning\AI Vault"
ls CLAUDE.md .claude/settings.json scripts/ skills/ wiki/
```

期望文件清单：
```
CLAUDE.md                        ← 系统宪法 v2.0
.claude/settings.json            ← Hooks 自动化配置
.mcp.json                        ← MCP 集成配置
scripts/align-check.sh           ← 对齐检索脚本
scripts/post-session.sh          ← 会话结束封印脚本
scripts/log-write.sh             ← 写操作记录脚本
skills/align/SKILL.md            ← 对齐 Skill
skills/review/SKILL.md           ← 复习 Skill
skills/ingest/SKILL.md           ← 注入 Skill
skills/lint/SKILL.md             ← 健康检查 Skill
skills/save/SKILL.md             ← 归档 Skill
wiki/hot.md                      ← 热缓存（会话恢复）
wiki/concepts-idx.md                    ← 全库目录
log.md                      ← 操作日志
wiki/overview.md                 ← 全局知识地图
wiki/domains/                    ← 8个领域综述页
wiki/meta/                       ← 看板/lint/矛盾登记
```

### Step 2 — 启动 Claude Code

```bash
# 在 vault 根目录启动（重要！）
cd "D:\Workspace\AI_Learning\AI Vault"
claude
```

Claude Code 自动读取 `CLAUDE.md` 作为系统宪法，静默读取 `wiki/hot.md` 恢复上下文。

### Step 3 — 验证系统

在 Claude Code 中输入：
```
bash scripts/align-check.sh "Transformer"
```

空库时的正常输出（✅ 预期行为）：
```
=== align-check: 'Transformer' ===
── [1] hot.md 热缓存 ── ❌ 未命中
── [2] wiki/concepts-idx.md 导航 ── ❌ 未命中
── [3] 全库 grep 兜底 ── ❌ 确认为知识缺口
=== align-check 完成 ===
```

---

## 📥 首次 Ingest（推荐起点）

复制任意论文摘要，在 Claude Code 中：
```
ingest

[粘贴 "Attention Is All You Need" 摘要或任意 AI 文章]
```

系统自动执行 5 阶段：TRIAGE → EXTRACT → INTEGRATE → LINK → SEAL

---

## 🔁 日常指令速查

| 操作 | 指令 | 说明 |
|------|------|------|
| 注入资料 | `ingest [内容]` | 5阶段自动处理 |
| 知识对齐 | `align: Transformer` | 检测知识缺口 |
| 全库审计 | `align all` | 月度覆盖度报告 |
| 开始复习 | `review` | 间隔复习（自动选题）|
| 定向复习 | `review: LoRA` | 针对特定主题 |
| 快速查询 | `query: 什么是 MoE` | 从 wiki 合成答案 |
| 归档对话 | `save` | 提炼当前对话为节点 |
| 健康检查 | `lint` | 每15次 ingest 执行 |
| 查看状态 | `我们上次做到哪了` | 朗读 hot.md |

---

## ⚙️ 可选配置

### MCP 集成（.mcp.json）

填入你的 GitHub Token：
```json
"GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_你的token"
```

激活 mcpvault（BM25 检索升级，wiki 节点 >20 后推荐）：
```json
// 删除 "disabled": true 这一行
```

### Obsidian 可视化

1. Obsidian → 打开已有 vault → 选择本目录
2. 推荐插件：Dataview、Templater、Graph Analysis、Obsidian Git

### Flux 概念图像生成

在 `.mcp.json` 的 `_flux_config` 中填入 API Key，节点达到 `status: developing` 时自动生成概念插画。

---

## 🛠️ 故障排除

| 问题 | 解决 |
|------|------|
| 脚本权限不足 | `chmod +x scripts/*.sh` |
| Hooks 不触发 | `bash scripts/post-session.sh` |
| hot.md < 100词 | 自动读 index.md 重建（正常） |
| 节点混乱 | `lint` → 获取修复建议 |

---

## 📊 成长里程碑

| 阶段 | 节点数 | 预计时间 |
|------|--------|----------|
| 🌱 起步 | 0–20 | 1–2周 |
| 🌿 初具规模 | 20–50 | 1个月 |
| 🌳 成熟 | 50–100 | 3个月 |
| 🌲 常青 | 100+ | 持续 |

---

*AI Vault v2.0 | DEPLOY-GUIDE | 2026-06-13*
