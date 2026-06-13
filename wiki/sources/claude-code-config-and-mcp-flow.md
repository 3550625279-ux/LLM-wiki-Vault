---
type: source
title: "Claude Code 配置文件和 MCP 工具调用流程"
created: 2026-06-13
updated: 2026-06-13
tags: [source, claude-code, mcp, configuration, engineering]
status: seed
domain: Engineering
source_type: notes
source_path: "raw/articles/claude-code-config-and-mcp-flow.md"
thumbnail: ""
---

> 📄 原始资料: [[raw/articles/claude-code-config-and-mcp-flow]]

# Claude Code 配置文件和 MCP 工具调用流程

> 个人学习笔记，系统梳理了 Claude Code 的配置体系和 MCP 工具调用全链路。

---

## 核心知识点

### 1. 配置文件 7 层优先级
CLI 参数 > 项目 .mcp.json > 项目 settings > 本地 settings > 用户 .claude.json > 全局 settings > 企业策略

### 2. MCP 协议本质
基于 JSON-RPC 2.0 的工具通信协议。MCP 服务器是独立进程，配置文件只是告诉客户端"去哪里找它们"。

### 3. 工具调用 5 阶段
启动加载 → 服务器初始化 → 模型选择工具 → JSON-RPC 通信 → 结果整合

### 4. 关键洞察
- `claude mcp add` = 封装了 JSON 写入的 CLI 工具
- 模型被调用两次：选工具 + 整合结果
- 工具列表注入系统提示词，模型据此决策

---

## 提取的概念节点

| 节点 | 类型 | 说明 |
|------|------|------|
| [[concepts/mcp-protocol]] | concept | MCP 协议架构与 JSON-RPC 2.0 |
| [[concepts/claude-code-configuration]] | concept | 7 层配置文件体系 |
| [[concepts/mcp-tool-calling-flow]] | concept | 5 阶段工具调用全链路 |

---

## 与已有知识的关系

- **扩展** [[skills/wiki/references/mcp-setup.md]] — 该文件讲 Obsidian MCP 配置实操，本笔记补充了底层协议原理
- **补充** [[concepts/function-calling]]（待创建）— MCP 是 Function Calling 的工程化封装

---

*首次 ingest: 2026-06-13*
