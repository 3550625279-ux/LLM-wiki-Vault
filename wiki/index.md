# Wiki Index — 全库目录

> 每次 ingest 后更新此文件。
> 格式: `- [[页面标题]] — 一行说明 | type:X | status:Y | domain:Z`

---

## 📁 目录结构

```
wiki/
├── hot.md              ← 热缓存（会话快速恢复）
├── index.md            ← 本文件（全库导航）
├── log.md              ← 操作日志
├── overview.md         ← 全局摘要和知识地图
├── domains/            ← 8个顶层领域综述
│   ├── foundations/
│   ├── architecture/
│   ├── training/
│   ├── alignment/
│   ├── inference/
│   ├── multimodal/
│   ├── agents/
│   └── engineering/
├── concepts/           ← 原理/算法/定义
├── entities/           ← 模型/论文/作者/机构
├── operations/         ← 代码/调参/工程实践
├── insights/           ← 个人洞察/避坑
├── sources/            ← 原始资料摘要页
├── comparisons/        ← 横向对比
├── questions/          ← 已回答问题 + gap页面
├── folds/              ← log折叠归档
├── canvases/           ← 可视化画布
└── meta/               ← 看板/lint/状态/矛盾
```

---

## 🌐 领域索引

### 1. Foundations（基础）
*(待 ingest 填充)*

### 2. Architecture（架构）
*(待 ingest 填充)*

### 3. Training（训练）
*(待 ingest 填充)*

### 4. Alignment（对齐）
*(待 ingest 填充)*

### 5. Inference（推理）
*(待 ingest 填充)*

### 6. Multimodal（多模态）
*(待 ingest 填充)*

### 7. Agents（智能体）
*(待 ingest 填充)*

### 8. Engineering（工程）
*(待 ingest 填充)*

---

## 🏷️ 节点类型索引

### type: concept
- [[concepts/mcp-protocol]] — MCP 协议架构与 JSON-RPC 2.0 | status:seed | domain:Engineering
- [[concepts/claude-code-configuration]] — Claude Code 7层配置文件体系 | status:seed | domain:Engineering
- [[concepts/mcp-tool-calling-flow]] — MCP 工具调用 5 阶段全链路 | status:seed | domain:Engineering

### type: entity
*(待 ingest 填充)*

### type: operation
*(待 ingest 填充)*

### type: insight
*(待 ingest 填充)*

### type: source
- [[sources/claude-code-config-and-mcp-flow]] — Claude Code 配置与 MCP 流程笔记 | status:seed | domain:Engineering

### type: comparison
*(待 ingest 填充)*

### type: question / gap
*(待 ingest 填充)*

---

## 📊 统计

| 指标 | 数值 |
|------|------|
| 总节点数 | 4 |
| concept | 3 |
| entity | 0 |
| operation | 0 |
| insight | 0 |
| source | 1 |
| comparison | 0 |
| question/gap | 0 |
| mature 节点 | 0 |
| seed 节点 | 0 |
| 矛盾登记 | 0 |

*上次更新: 2026-06-13 | vault-init*
