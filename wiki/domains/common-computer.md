---
title: "Common Computer — 通用计算机基础"
type: domain
status: seed
domain: Common Computer
tags: [terminal, shell, PATH, environment-variable, conda, npm, windows, 基础设施]
created: 2026-06-16
updated: 2026-06-16
confidence: high
---

# Common Computer — 通用计算机基础

> **领域使命**: 掌握与 AI 无直接关联、但日常开发必需的计算机基础设施知识。
> **定位**: 这些知识不属于任何 AI 领域（Foundations/Architecture/Training 等），但支撑所有 AI 工程实践。
> **边界**: 如果一个概念"做 AI 的人需要会，但不是 AI 特有的"，它就属于这里。

---

## 🔗 关系链接

- supports: [[domains/Engineering]] | [[domains/Training]] | [[domains/Inference]]
- contains: [[concepts/terminal-and-shell]] | [[concepts/npm-and-npx]] | [[concepts/path-environment-variable]] | [[concepts/process-environment-inheritance]] | [[concepts/windows-registry-env]] | [[concepts/conda-environments]]

---

## 📌 领域地图

```
Common Computer
├── 终端与 Shell
│   ├── 终端 vs GUI（文本指令 vs 图形交互）
│   ├── Shell 角色（命令解析 + 程序调度）
│   └── PowerShell 语法（$env:VAR 等）
│
├── 环境变量机制
│   ├── PATH（程序搜索目录列表）
│   ├── 进程继承（注册表 → 进程 → 子进程）
│   ├── Windows 注册表（HKCU/HKLM, REG_EXPAND_SZ）
│   └── 环境变量生命周期（永久 vs 临时）
│
├── 包管理
│   ├── npm / npx（JavaScript 生态）
│   ├── pip（Python 生态）
│   └── 全局 vs 局部安装
│
├── Python 环境隔离
│   ├── conda（包管理 + 环境管理）
│   ├── conda activate 的 PATH 抢占机制
│   ├── PowerShell Profile 自动激活
│   └── venv / virtualenv（标准库方案）
│
└── 版本管理工具的 PATH 抢占模式
    ├── nvm（Node 版本管理）
    ├── pyenv（Python 版本管理）
    └── rbenv（Ruby 版本管理）
```

---

## 🧮 已有节点

- [x] [[concepts/terminal-and-shell]] — 终端与 Shell 基础 | status:seed
- [x] [[concepts/npm-and-npx]] — npm 与 npx：JavaScript 包管理 | status:seed
- [x] [[concepts/path-environment-variable]] — PATH 环境变量 | status:seed
- [x] [[concepts/process-environment-inheritance]] — 进程环境变量继承链 | status:seed
- [x] [[concepts/windows-registry-env]] — Windows 注册表与环境变量存储 | status:seed
- [x] [[concepts/conda-environments]] — Conda 环境管理与激活机制 | status:seed

**来源节点：**
- [x] [[sources/terminal-and-environment-basics]] — 终端、PATH 与 Conda 环境基础 | status:developing

**洞察节点：**
- [x] [[insights/path-search-priority-is-isolation]] — PATH 从前往后搜索 = 环境隔离的核心手段 | status:seed

**`contains::` 边（域 → 节点）：**
- `contains::` [[concepts/terminal-and-shell]]
- `contains::` [[concepts/npm-and-npx]]
- `contains::` [[concepts/path-environment-variable]]
- `contains::` [[concepts/process-environment-inheritance]]
- `contains::` [[concepts/windows-registry-env]]
- `contains::` [[concepts/conda-environments]]

## 🔴 关键缺口

- `git-basics` — Git 版本控制基础
- `ssh-and-authentication` — SSH 密钥与认证机制
- `docker-basics` — 容器基础
- `networking-basics` — HTTP/DNS/端口等网络基础
- `linux-commands` — 常用 Linux 命令（grep/find/awk）

---

## 🔗 领域间关系

- `supports::` [[domains/Engineering]] — 通用基础支撑 AI 工程实践
- `supports::` [[domains/Training]] — conda 环境隔离支撑训练实验
- `supports::` [[domains/Inference]] — 环境管理支撑推理部署

---

## 💡 领域关键洞察

- **环境隔离的本质不是"有多个 Python"，而是"让 PATH 指向正确的那个"**
- **进程环境变量是快照式复制**——创建后不回读注册表，修改必须重开终端
- **注册表中的 PATH 是一条分号分隔的长字符串**——GUI 只是做了格式化显示

---

## 📊 领域统计

```
concept 节点: 6
insight 节点: 1
source 节点:  1
maturity:    seed
```
