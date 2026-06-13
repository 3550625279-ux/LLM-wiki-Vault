---
source_url: ""
original_format: "txt"
fetched: 2026-06-13
ingested: 2026-06-13
---

# Claude Code 配置文件与 MCP 工具调用流程

---

## 一、配置文件层级

Claude Code 的配置文件按优先级从高到低排列：

| 优先级 | 层级 | 路径 | 作用域 |
|--------|------|------|--------|
| 1 (最高) | CLI 参数 | `--mcp` | 临时，本次会话有效 |
| 2 | 项目 .mcp.json | `项目/.mcp.json` | 项目级，提交到 git 共享给团队 |
| 3 | 项目 settings | `.claude/settings.json` | 项目级 |
| 4 | 本地 settings | `.claude/settings.local.json` | 不提交 |
| 5 | 用户 .claude.json | `~/.claude.json` | 用户级 |
| 6 | 全局 settings | `~/.claude/settings.json` | 全局 |
| 7 (最低) | 托管/企业策略 | 管理员下发 | 组织级 |

---

## 二、启动时发生了什么

```
Claude Code 启动
  │
  ├─ 读取 ~/.claude/settings.json     → 加载 env、插件、主题
  ├─ 读取 ~/.claude.json              → 加载用户级 mcpServers、项目配置
  ├─ 读取 .claude/settings.json       → 加载项目级配置
  ├─ 读取 .mcp.json                   → 加载项目共享的 MCP
  │
  ├─ 合并所有 mcpServers              → 按优先级去重
  │
  └─ 对每个 MCP server：
       ├─ stdio 类型 → 启动子进程（npx ...）
       ├─ http 类型  → 建立 HTTP 连接
       └─ 验证连接   → claude mcp list 看到的 ✔/✘
```

---

## 三、为什么改配置就够了

MCP 服务器本身是独立运行的外部进程或远程服务。Claude Code 只需要知道以下配置字段：

| 配置字段 | 告诉 Claude Code 什么 |
|----------|----------------------|
| `type` | 怎么连接（stdio / http） |
| `command` + `args` | 启动什么命令（stdio） |
| `url` | 连哪个地址（http） |
| `env` | 传什么环境变量 |
| `headers` | 带什么认证头 |

**核心洞察**：

- **添加 MCP** = 往配置文件里写一段 JSON
- **删除 MCP** = 从配置文件里删掉那段 JSON
- **移动 MCP** = 从一个配置文件剪切到另一个（项目级 → 用户级）
- **MCP 服务器本身不用动**，它们是无状态的外部工具

> 一句话总结：MCP 管理 = 改 JSON 配置。Claude Code 启动时读配置、按配置建立连接、把工具列表注入提示词。服务器是独立的，配置只是告诉 Claude Code "去哪里找它们"。

---

## 四、实际操作记录

通过 `claude mcp add` 进行的三次配置操作：

| 操作 | 命令 | 实际写入位置 |
|------|------|-------------|
| 第一次 | `claude mcp add` | 写入 `~/.claude.json` 的 `projects/C:/Users/35506/mcpServers` |
| 第二次 | `claude mcp add -s user` | 写入 `~/.claude.json` 的顶层 `mcpServers` |
| 第三次 | `node 删除项目级残留` | 清掉 `projects` 下的 `mcpServers` |

本质就是三次对同一个 JSON 文件不同位置的写操作。`claude mcp add` 只是个封装了 JSON 写入的 CLI 工具，底层和直接改文件是一样的。

---

## 五、MCP 工具调用完整流程详解

### 5.1 整体架构

```
用户终端（输入问题）
        ↓
Claude Code（客户端）
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │ 主对话模型   │  │ 工具调度器   │  │ MCP 管理器   │
  │ (Claude API) │  │              │  │              │
  └──────────────┘  └──────────────┘  └──────────────┘
        ↓
MCP 服务器进程（本地）
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │   bocha      │  │    exa       │  │  filesystem  │  ...
  │  (搜索)      │  │  (搜索)      │  │  (文件操作)  │
  └──────────────┘  └──────────────┘  └──────────────┘
        ↓
外部服务 / API
  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
  │  Bocha API   │  │   Exa API    │  │  本地文件系统 │
  └──────────────┘  └──────────────┘  └──────────────┘
```

### 5.2 配置文件结构

```json
{
  "mcpServers": {
    "服务器名称": {
      "type": "通信类型",
      "command": "启动命令",
      "args": ["参数列表"],
      "env": {
        "环境变量名": "值"
      }
    }
  }
}
```

**配置示例**：

```json
{
  "mcpServers": {
    "bocha": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@humansean/mcp-bocha"],
      "env": {
        "BOCHA_API_KEY": "sk-3d7ce16f..."
      }
    }
  }
}
```

### 5.3 调用流程（以 Bocha 搜索为例）

#### 阶段 1：Claude Code 启动

1. Claude Code 启动
2. 读取 `~/.claude.json` 配置文件
3. 解析 `mcpServers` 对象
4. 对每个 MCP 服务器执行启动命令：

```bash
$ npx -y @humansean/mcp-bocha

# npx 检查缓存：
#   C:\Users\35506\AppData\Local\npm-cache\_npx\<hash>\
#     ├── node_modules/
#     ├── package.json
#     └── package-lock.json
#
# 如果缓存存在 → 直接使用
# 如果缓存不存在 → 从 npm 下载 → 缓存 → 使用
```

5. MCP 服务器进程启动，通过 stdio 等待请求

#### 阶段 2：MCP 服务器初始化

1. 加载环境变量 `BOCHA_API_KEY`
2. 初始化 MCP 协议处理器
3. 向 Claude Code 注册可用工具：

```json
{
  "tools": [
    {
      "name": "bocha_search",
      "description": "使用 Bocha 搜索引擎搜索网页",
      "inputSchema": {
        "type": "object",
        "properties": {
          "query": { "type": "string", "description": "搜索关键词" }
        }
      }
    }
  ]
}
```

4. 等待 Claude Code 的请求

#### 阶段 3：用户发起搜索请求

**用户输入**：`"帮我搜索一下 Bocha MCP 的最新信息"`

**Claude Code 主模型分析**：
1. 理解用户意图：需要搜索信息
2. 查看可用工具列表（已注入系统提示词）
3. 决定使用 `bocha_search` 工具
4. 生成工具调用请求

#### 阶段 4：MCP 协议通信

**Claude Code → MCP 服务器**（通过 stdin）：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "bocha_search",
    "arguments": {
      "query": "Bocha MCP 最新信息"
    }
  }
}
```

**MCP 服务器处理**：
1. 接收 JSON-RPC 请求
2. 解析参数：`query = "Bocha MCP 最新信息"`
3. 调用 Bocha API：

```
POST https://api.bochaai.com/v1/web-search
Headers:
  Authorization: Bearer sk-3d7ce16f...
  Content-Type: application/json
Body:
  { "query": "Bocha MCP 最新信息" }
```

4. 接收 API 响应
5. 格式化结果

#### 阶段 5：返回结果

**MCP 服务器 → Claude Code**（通过 stdout）：

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "搜索结果：\n1. Bocha MCP 是...\n2. 最新版本..."
      }
    ]
  }
}
```

**Claude Code 处理结果**：
1. 解析 JSON-RPC 响应
2. 提取搜索结果文本
3. 将结果整合到对话上下文中
4. 生成最终回复给用户

---

## 六、底层协议细节

### MCP 协议基于 JSON-RPC 2.0

**请求格式**：
```json
{
  "jsonrpc": "2.0",
  "id": "<唯一ID>",
  "method": "<方法名>",
  "params": { }
}
```

**响应格式**：
```json
{
  "jsonrpc": "2.0",
  "id": "<对应的请求ID>",
  "result": { }
  // 或
  "error": { }
}
```

### 常用 MCP 方法

| 方法 | 方向 | 说明 |
|------|------|------|
| `initialize` | Client → Server | 初始化连接 |
| `tools/list` | Client → Server | 获取可用工具列表 |
| `tools/call` | Client → Server | 调用工具 |
| `resources/list` | Client → Server | 获取可用资源列表 |
| `resources/read` | Client → Server | 读取资源 |

### stdio 通信方式

```
┌──────────────┐                    ┌──────────────┐
│  Claude Code │  ──── stdin ────→  │  MCP Server  │
│   (父进程)    │                    │   (子进程)    │
│              │  ←── stdout ────   │              │
│              │                    │              │
│              │  ←── stderr ────   │  (日志/错误)  │
└──────────────┘                    └──────────────┘
```

---

## 七、完整数据流示例

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

## 八、关键组件总结

| 组件 | 角色 | 职责 |
|------|------|------|
| 用户 | 发起者 | 输入问题 |
| Claude Code | 客户端 | 协调对话、调用工具、展示结果 |
| MCP 管理器 | 进程管理 | 启动/停止 MCP 服务器进程 |
| 工具调度器 | 路由 | 将工具调用请求路由到正确的 MCP 服务器 |
| MCP 服务器 | 服务提供者 | 实现具体功能（搜索、文件操作等） |
| 外部 API | 数据源 | 提供实际数据（Bocha API、文件系统等） |

---

## 九、配置 vs 实际执行

```
配置文件 (~/.claude.json)
    │  声明: "运行 npx -y @humansean/mcp-bocha"
    ▼
Claude Code 启动时
    │  执行: spawn("npx", ["-y", "@humansean/mcp-bocha"])
    ▼
npx
    │  检查缓存 → 下载(如需要) → 运行包的入口点
    ▼
@humansean/mcp-bocha 包
    │  入口点: node_modules/.bin/mcp-bocha
    │  实现: 初始化 MCP 协议、注册工具、等待请求
    ▼
MCP 服务器进程
    │  持续运行，通过 stdio 通信
    ▼
工具可用
```
