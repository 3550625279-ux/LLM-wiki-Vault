---
type: concept
title: "MCP 工具调用完整流程"
created: 2026-06-13
updated: 2026-06-13
tags: [mcp, tool-calling, flow, claude-code, engineering]
status: developing
thumbnail: "_attachments/assets/mcp-tool-calling-flow.png"
complexity: intermediate
domain: Engineering
sources:
  - "[[sources/claude-code-config-and-mcp-flow]]"
related:
  - "belongs_to::[[domains/Engineering]]"
  - "depends_on::[[concepts/mcp-protocol]]"
  - "depends_on::[[concepts/claude-code-configuration]]"
  - "extends::[[concepts/mcp-protocol]]"
  - "produced_by::[[sources/claude-code-config-and-mcp-flow]]"
---

# MCP 工具调用完整流程

## 🔗 关系链接

- belongs_to: [[domains/Engineering]]
- depends_on: [[concepts/mcp-protocol]] | [[concepts/claude-code-configuration]]
- extends: [[concepts/mcp-protocol]]
- produced_by: [[sources/claude-code-config-and-mcp-flow]]

---

> 从用户输入到结果返回的 5 阶段全链路。

![[mcp-tool-calling-flow.png]]

---

## 5 阶段概览

```
用户输入问题
    ↓
阶段 1: Claude Code 启动 → 读取配置 → 启动 MCP 子进程
    ↓
阶段 2: MCP 服务器初始化 → 加载环境变量 → 注册工具 → 等待请求
    ↓
阶段 3: 用户发起请求 → 模型分析意图 → 选择工具 → 生成调用请求
    ↓
阶段 4: JSON-RPC 通信 → stdin 发送请求 → MCP 处理 → 调用外部 API
    ↓
阶段 5: stdout 返回结果 → 模型整合 → 生成最终回复
```

---

## 阶段 1：Claude Code 启动

```
1. Claude Code 启动
2. 读取配置文件（~/.claude.json 等）
3. 解析 mcpServers 对象
4. 对每个 MCP 服务器执行启动命令：
   $ npx -y @humansean/mcp-bocha
   ├─ npx 检查缓存 → 有则用，无则下载
   └─ MCP 服务器进程启动，通过 stdio 等待请求
```

---

## 阶段 2：MCP 服务器初始化

```
1. 加载环境变量（如 BOCHA_API_KEY）
2. 初始化 MCP 协议处理器
3. 向 Claude Code 注册可用工具（tools/list）
4. 等待 Claude Code 的请求
```

工具注册示例：
```json
{
  "tools": [{
    "name": "bocha_search",
    "description": "使用 Bocha 搜索引擎搜索网页",
    "inputSchema": {
      "type": "object",
      "properties": {
        "query": { "type": "string" }
      },
      "required": ["query"]
    }
  }]
}
```

---

## 阶段 3：用户发起请求

```
用户输入: "帮我搜索一下 Bocha MCP 的最新信息"
    ↓
Claude Code 主模型分析:
  1. 理解意图: 需要搜索信息
  2. 查看可用工具列表（已注入系统提示词）
  3. 决定使用 bocha_search 工具
  4. 生成工具调用请求
```

---

## 阶段 4：MCP 协议通信

**发送请求**（Claude Code → MCP Server，通过 stdin）:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "bocha_search",
    "arguments": { "query": "Bocha MCP 最新信息" }
  }
}
```

**MCP 服务器处理**:
```
1. 接收 JSON-RPC 请求
2. 解析参数
3. 调用外部 API（如 POST https://api.bochaai.com/v1/web-search）
4. 接收 API 响应
5. 格式化结果
```

---

## 阶段 5：返回结果

**响应**（MCP Server → Claude Code，通过 stdout）:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [{
      "type": "text",
      "text": "搜索结果：\n1. Bocha MCP 是...\n2. 最新版本..."
    }]
  }
}
```

**Claude Code 处理**:
```
1. 解析 JSON-RPC 响应
2. 提取搜索结果文本
3. 将结果整合到对话上下文中
4. 生成最终回复给用户
```

---

## 完整数据流图

```
用户: "搜索 Bocha MCP"
    │
    ▼
Claude Code (主模型)
    │  输入: 用户问题 + 系统提示 + 工具定义
    │  决策: 调用 bocha_search, query="Bocha MCP"
    ▼
Claude Code (工具调度器)
    │  识别工具来源 → 构造 JSON-RPC → stdin 发送
    ▼
Bocha MCP 服务器 (Node.js 进程)
    │  stdin 读取 → 解析 → 调用 API → stdout 返回
    ▼
Claude Code (主模型，第二次调用)
    │  输入: 用户问题 + 工具结果
    │  决策: 整合结果，生成回复
    ▼
用户看到: "根据搜索结果，Bocha MCP 是..."
```

---

## 关键洞察

- 模型会被**调用两次**：第一次决定调用什么工具，第二次整合工具结果生成回复
- 工具列表在启动时注入**系统提示词**，模型据此知道有哪些工具可用
- 整个通信是**同步阻塞**的：发送请求 → 等待响应 → 继续对话

---

*首次记录: 2026-06-13 | 来源: 个人学习笔记*
