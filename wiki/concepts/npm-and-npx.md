---
type: concept
title: "npm 与 npx：JavaScript 包管理"
created: 2026-06-16
updated: 2026-06-16
tags: [npm, npx, nodejs, package-manager, 工具链]
status: seed
complexity: basic
domain: Common Computer
sources: ["[[sources/terminal-and-environment-basics]]"]
related:
  - "depends_on::[[concepts/terminal-and-shell]]"
  - "depends_on::[[concepts/path-environment-variable]]"
  - "applied_in::[[concepts/claude-code-configuration]]"
  - "belongs_to::[[domains/common-computer]]"
  - "produced_by::[[sources/terminal-and-environment-basics]]"
thumbnail: ""
---

# npm 与 npx：JavaScript 包管理

## 🔗 关系链接

- depends_on: [[concepts/terminal-and-shell]] | [[concepts/path-environment-variable]]
- applied_in: [[concepts/claude-code-configuration]]
- belongs_to: [[domains/common-computer]]
- produced_by: [[sources/terminal-and-environment-basics]]

---

## 核心定义

**包（Package）** = 别人写好的、打包好的现成工具/代码。编程世界中不用从零造轮子，直接从"超市"下载现成工具。

**npm**（Node Package Manager）= JavaScript 生态的"超市"，同时是**包管理器**：
1. 从 npmjs.com 下载包（购物）
2. 管理已安装的包清单（冰箱记录）

**npx** = npm 自带的**临时运行器**：
- 临时下载并运行一个包，用完即走
- 如果包已永久安装，直接用已安装版本

## npm vs npx 核心区别

| | npm install | npx |
|---|------------|-----|
| 类比 | 买电钻放家里 | 去工具租赁店借来用 |
| 生命周期 | 永久安装到 node_modules | 临时下载，缓存后运行 |
| 适用场景 | 频繁使用的工具 | 只用一两次的工具 |
| 磁盘影响 | 长期占用空间 | 用完可清理 |

## 命令拆解示例

```
npx skills add find-skills -y -g
│    │      │    │          │  │
│    │      │    │          │  └── -g = --global（全局安装）
│    │      │    │          └───── -y = --yes（跳过确认）
│    │      │    └──────────────── 参数：要添加的技能名
│    │      └───────────────────── 子命令：添加操作
│    └──────────────────────────── 包名：技能管理工具
└───────────────────────────────── 临时运行器
```

### 子命令 vs 参数

- **子命令（subcommand）**：核心意图，"你到底想干什么"（add = 添加）
- **参数（argument）**：操作对象，"做什么的哪个"（find-skills = 具体技能名）
- **标志（flag）**：行为开关（-y 跳过确认，-g 全局安装）

### 全局安装 vs 局部安装

| | 局部（默认） | 全局（-g） |
|---|------------|-----------|
| 作用范围 | 仅当前项目文件夹 | 电脑任何位置 |
| 类比 | 工具放书桌抽屉 | 工具放客厅公共架 |
| 存储位置 | ./node_modules/ | 系统级目录 |

## npx 的完整执行流程

```
npx skills add find-skills -y -g
    │
    ▼
npx 去 npmjs.com 搜索 skills 包
    │
    ▼
检查本地缓存 → 有则直接用，无则下载
    │
    ▼
运行 skills 程序，传入参数 add find-skills -y -g
    │
    ▼
skills 解析子命令 add → 执行"添加技能"逻辑
    │
    ▼
因 -g 标志，将 find-skills 安装到全局技能目录
因 -y 标志，跳过所有确认步骤
    │
    ▼
安装完成，find-skills 注册到全局技能列表
```

---

*npm-and-npx | type:concept | status:seed | domain:Engineering*
