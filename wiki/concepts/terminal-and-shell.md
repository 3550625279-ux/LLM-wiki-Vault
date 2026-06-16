---
type: concept
title: "终端与 Shell 基础"
created: 2026-06-16
updated: 2026-06-16
tags: [terminal, shell, powershell, cli, 基础设施]
status: seed
complexity: basic
domain: Common Computer
sources: ["[[sources/terminal-and-environment-basics]]"]
related:
  - "spawns::[[concepts/path-environment-variable]]"
  - "spawns::[[concepts/process-environment-inheritance]]"
  - "extends::[[concepts/claude-code-configuration]]"
  - "belongs_to::[[domains/common-computer]]"
  - "produced_by::[[sources/terminal-and-environment-basics]]"
thumbnail: ""
---

# 终端与 Shell 基础

## 🔗 关系链接

- spawns: [[concepts/path-environment-variable]] | [[concepts/process-environment-inheritance]]
- extends: [[concepts/claude-code-configuration]]
- belongs_to: [[domains/common-computer]]
- produced_by: [[sources/terminal-and-environment-basics]]

---

## 核心定义

**终端（Terminal）** 是一个文本界面，让你通过输入文字命令来操作计算机，而不是用鼠标点击图形界面。

**Shell** 是终端背后的命令解释器——你输入的文字由它解析、执行、返回结果。

| 概念 | 类比 | 技术角色 |
|------|------|----------|
| 终端 | 银行窗口（通信渠道） | 显示文字、接收输入的界面程序 |
| Shell | 柜员（执行者） | 解析命令、调用程序的解释器 |
| GUI | 自助 ATM 机 | 图形化封装了底层命令 |

## 关键区分

- **终端 ≠ Shell**：终端是窗口，Shell 是窗口里的"大脑"。PowerShell 既是终端也是 Shell（合二为一）
- **命令是对程序的直接调用**：终端中输入的每个字符都是严格语法指令，不会"猜你的意思"
- **图标是命令的封装**：双击桌面图标 = 隐式执行了一条命令

## 常见终端/Shell 对照

| 操作系统 | 终端 | Shell |
|----------|------|-------|
| Windows | PowerShell, CMD, Windows Terminal | PowerShell, CMD, Git Bash |
| macOS | Terminal.app, iTerm2 | zsh, bash |
| Linux | GNOME Terminal, Konsole | bash, zsh, fish |

## 从终端到程序

```
用户输入命令
    │
    ▼
Shell 解析（拆分命令名 + 参数）
    │
    ▼
去 PATH 中搜索命令名对应的可执行文件
    │
    ▼
找到 → 创建子进程执行
未找到 → 报错 "command not found"
```

PowerShell 的核心角色是**调度员**——它不直接干活，而是找到对应的程序，把任务派给它。

## PowerShell 语法要点

```powershell
# echo = Write-Output 的别名，原样打印内容
echo hello          # 输出: hello

# 访问环境变量
echo $env:PATH      # 正确：冒号和变量名之间不能有空格
echo $env PATH      # 错误：$env 和 PATH 被当作两个参数
echo $env: PATH     # 错误：冒号后有空格，语法报错
```

**PowerShell 变量规则**：`$env:变量名` 必须连写，`:` 后紧跟变量名，中间不能有空格。

---

*terminal-and-shell | type:concept | status:seed | domain:Engineering*
