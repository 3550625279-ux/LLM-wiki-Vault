---
type: concept
title: "Claude Code 配置文件层级"
created: 2026-06-13
updated: 2026-06-13
tags: [claude-code, configuration, mcp, engineering]
status: seed
complexity: intermediate
domain: Engineering
sources:
  - "[[sources/claude-code-config-and-mcp-flow]]"
related:
  - "belongs_to::[[domains/Engineering]]"
  - "applied_in::[[concepts/mcp-protocol]]"
  - "part_of::[[concepts/claude-code-configuration]]"
  - "produced_by::[[sources/claude-code-config-and-mcp-flow]]"
---

# Claude Code 配置文件层级

## 🔗 关系链接

- belongs_to: [[domains/Engineering]]
- applied_in: [[concepts/mcp-protocol]]
- produced_by: [[sources/claude-code-config-and-mcp-flow]]

---

> Claude Code 使用 7 层配置文件体系，优先级从高到低覆盖。

---

## 7 层优先级

| 优先级 | 层级 | 路径 | 作用域 |
|--------|------|------|--------|
| 1 (最高) | CLI 参数 | `--mcp` | 临时，本次会话有效 |
| 2 | 项目 .mcp.json | `项目/.mcp.json` | 项目级，提交到 git 共享 |
| 3 | 项目 settings | `.claude/settings.json` | 项目级 |
| 4 | 本地 settings | `.claude/settings.local.json` | 项目级，不提交 |
| 5 | 用户 .claude.json | `~/.claude.json` | 用户级 |
| 6 | 全局 settings | `~/.claude/settings.json` | 全局 |
| 7 (最低) | 托管/企业策略 | 管理员下发 | 组织级 |

---

## 启动加载流程

```
Claude Code 启动
  ├─ 读取 ~/.claude/settings.json     → 加载 env、插件、主题
  ├─ 读取 ~/.claude.json              → 加载用户级 mcpServers
  ├─ 读取 .claude/settings.json       → 加载项目级配置
  ├─ 读取 .mcp.json                   → 加载项目共享的 MCP
  │
  ├─ 合并所有 mcpServers              → 按优先级去重
  │
  └─ 对每个 MCP server：
       ├─ stdio 类型 → 启动子进程（npx ...）
       ├─ http 类型  → 建立 HTTP 连接
       └─ 验证连接   → claude mcp list 看到 ✔/✘
```

---

## 配置字段含义

| 字段 | 告诉 Claude Code 什么 |
|------|----------------------|
| `type` | 怎么连接（stdio / http） |
| `command` + `args` | 启动什么命令（stdio） |
| `url` | 连哪个地址（http） |
| `env` | 传什么环境变量 |
| `headers` | 带什么认证头 |

---

## 配置文件结构示例

```json
{
  "mcpServers": {
    "server-name": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@package/mcp-server"],
      "env": {
        "API_KEY": "sk-xxx"
      }
    }
  }
}
```

---

## 常见操作

| 操作 | 命令 | 本质 |
|------|------|------|
| 添加 MCP | `claude mcp add` | 往配置文件写 JSON |
| 添加 (JSON) | `claude mcp add-json` | 直接写入 JSON 块 |
| 删除 MCP | `claude mcp remove` | 从配置文件删 JSON |
| 查看列表 | `claude mcp list` | 读取并展示配置 |
| 查看详情 | `claude mcp get <name>` | 读取单个配置 |

---

## 关键洞察

- `claude mcp add` 只是封装了 JSON 写入的 CLI 工具，底层和直接编辑文件一样
- 添加 MCP = 写一段 JSON，删除 MCP = 删一段 JSON，移动 MCP = 剪切到另一个配置文件
- `--scope user` 让 MCP 在所有项目间共享，而非仅当前项目

---

*首次记录: 2026-06-13 | 来源: 个人学习笔记*
