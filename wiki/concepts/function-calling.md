---
type: concept
title: "Function Calling — 函数调用"
created: 2026-06-16
updated: 2026-06-16
tags: [LLM, 工具调用, Agent, API]
status: seed
complexity: intermediate
domain: Agents
sources: ["OpenAI 2023"]
related:
  - "contrasts::[[concepts/mcp-protocol]]"
  - "belongs_to::[[domains/Agents]]"
---

## 🔗 关系链接

- belongs_to: [[domains/Agents]]
- contrasts: [[concepts/mcp-protocol]]

---

# Function Calling — 函数调用

## 核心思想

让 LLM 在对话中**结构化地调用外部函数/API**。模型输出一个 JSON 对象，指定要调用的函数名和参数，由宿主程序执行后将结果返回给模型。

## 工作流程

```
用户: "北京今天天气怎么样？"
    ↓
LLM 输出: {"name": "get_weather", "arguments": {"city": "北京"}}
    ↓
宿主程序执行 get_weather("北京") → "晴，25°C"
    ↓
LLM 接收结果 → "北京今天晴天，气温 25°C"
```

## 与 MCP 的关系

| 特性 | Function Calling | MCP |
|------|-----------------|-----|
| 发起者 | OpenAI (2023) | Anthropic (2024) |
| 协议 | 各厂商自定义 JSON schema | 统一 JSON-RPC 2.0 |
| 工具发现 | 手动注册 | 动态发现 |
| 适用范围 | 单次调用 | 文件系统/数据库/浏览器等复杂工具 |

详见 [[concepts/mcp-protocol]] 的对比分析。
