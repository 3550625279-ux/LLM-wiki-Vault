---
type: concept
title: "MCP — Model Context Protocol"
created: 2026-06-13
updated: 2026-06-13
tags: [mcp, protocol, tool-calling, claude-code, engineering]
status: seed
complexity: intermediate
domain: Engineering
sources:
  - "[[sources/claude-code-config-and-mcp-flow]]"
related:
  - "implements::[[concepts/mcp-tool-calling-flow]]"
  - "applied_in::[[concepts/claude-code-configuration]]"
  - "contrasts::[[concepts/function-calling]]"
---

# MCP — Model Context Protocol

> MCP 是 Anthropic 主导的开放协议，让 LLM 客户端（如 Claude Code）通过标准化接口调用外部工具。

---

## 核心定义

**MCP (Model Context Protocol)** 基于 **JSON-RPC 2.0** 的通信协议，定义了 LLM 客户端与外部工具服务器之间的标准交互方式。

核心思想：**MCP 服务器是独立运行的外部进程，配置只是告诉客户端"去哪里找它们"。**

---

## 架构

```
用户 → Claude Code (客户端) → MCP Server (子进程) → 外部 API
```

| 组件 | 角色 | 职责 |
|------|------|------|
| Claude Code | 客户端 | 协调对话、调度工具、展示结果 |
| MCP 管理器 | 进程管理 | 启动/停止 MCP 服务器进程 |
| 工具调度器 | 路由 | 将工具调用请求路由到正确的 MCP 服务器 |
| MCP 服务器 | 服务提供者 | 实现具体功能（搜索、文件操作等） |
| 外部 API | 数据源 | 提供实际数据 |

---

## 协议细节

### JSON-RPC 2.0 消息格式

**请求**（Client → Server）:
```json
{
  "jsonrpc": "2.0",
  "id": "<唯一ID>",
  "method": "tools/call",
  "params": {
    "name": "tool_name",
    "arguments": { "key": "value" }
  }
}
```

**响应**（Server → Client）:
```json
{
  "jsonrpc": "2.0",
  "id": "<对应的请求ID>",
  "result": {
    "content": [{ "type": "text", "text": "结果内容" }]
  }
}
```

### 常用方法

| 方法 | 方向 | 说明 |
|------|------|------|
| `initialize` | Client → Server | 初始化连接 |
| `tools/list` | Client → Server | 获取可用工具列表 |
| `tools/call` | Client → Server | 调用工具 |
| `resources/list` | Client → Server | 获取可用资源列表 |
| `resources/read` | Client → Server | 读取资源 |

---

## 通信方式

### stdio（本地进程）

```
Claude Code (父进程) ←── stdin ───→ MCP Server (子进程)
                   ←── stdout ──→
                   ←── stderr ──→ (日志/错误)
```

- Claude Code 启动时通过 `spawn()` 创建子进程
- 通过 stdin/stdout 管道双向通信
- MCP 服务器作为**子进程**持续运行

### HTTP（远程服务）

- 建立 HTTP 连接到远程 MCP 服务器
- 适用于远程 API 服务

---

## 工具注册机制

MCP 服务器启动后，向客户端注册可用工具：

```json
{
  "tools": [{
    "name": "bocha_search",
    "description": "使用 Bocha 搜索引擎搜索网页",
    "inputSchema": {
      "type": "object",
      "properties": {
        "query": { "type": "string", "description": "搜索关键词" }
      },
      "required": ["query"]
    }
  }]
}
```

客户端将工具列表**注入系统提示词**，模型据此决定何时调用哪个工具。

---

## 与 Function Calling 的关系

| 维度 | Function Calling | MCP |
|------|-----------------|-----|
| 定义方 | 模型厂商（OpenAI/Anthropic） | 开放协议（Anthropic 主导） |
| 工具定义 | 写在 API 请求中 | MCP 服务器运行时注册 |
| 工具实现 | 开发者在应用层实现 | 独立进程，标准化接口 |
| 可发现性 | 静态（调用前已知） | 动态（运行时发现） |

MCP 本质上是 Function Calling 的**工程化封装**——把"工具定义+实现+通信"打包成独立可复用的服务。

---

## 关键洞察

- MCP 管理 = 改 JSON 配置。`claude mcp add` 只是封装了 JSON 写入的 CLI 工具
- 添加/删除/移动 MCP = 对配置文件不同位置的写操作
- MCP 服务器本身是无状态的外部工具，不需要"大规模动文件"

---

*首次记录: 2026-06-13 | 来源: 个人学习笔记*
