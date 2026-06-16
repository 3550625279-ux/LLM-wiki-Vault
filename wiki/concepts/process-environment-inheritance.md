---
type: concept
title: "进程环境变量继承链"
created: 2026-06-16
updated: 2026-06-16
tags: [process, inheritance, 环境变量, 操作系统基础, 进程管理]
status: seed
complexity: intermediate
domain: Common Computer
sources: ["[[sources/terminal-and-environment-basics]]"]
related:
  - "depends_on::[[concepts/path-environment-variable]]"
  - "depends_on::[[concepts/windows-registry-env]]"
  - "applied_in::[[concepts/conda-environments]]"
  - "extends::[[concepts/inference-engine]]"
  - "belongs_to::[[domains/common-computer]]"
  - "produced_by::[[sources/terminal-and-environment-basics]]"
thumbnail: ""
---

# 进程环境变量继承链

## 🔗 关系链接

- depends_on: [[concepts/path-environment-variable]] | [[concepts/windows-registry-env]]
- extends: [[concepts/inference-engine]]
- belongs_to: [[domains/common-computer]]
- produced_by: [[sources/terminal-and-environment-basics]]

---

## 核心定义

**进程（Process）** 是一个正在运行的程序的实例。每次打开一个终端窗口，就创建了一个新进程。

**环境变量继承**：当进程 A 创建子进程 B 时，B **自动继承** A 的所有环境变量。这是一次**快照式复制**——B 拿到的是 A 当时的副本，之后任何一方的修改互不影响。

## 继承链全景

```
注册表（永久存储，系统级 + 用户级）
    │
    │ 进程创建时读取（初始化）
    ▼
PowerShell 进程（你的终端窗口）
    │
    │ 子进程继承（快照复制）
    ▼
Claude Code 进程
    │
    │ 子进程继承（快照复制）
    ▼
Claude Code 内部启动的任何子命令
```

## 完整生命周期

```
步骤 1: Windows 启动
    │
步骤 2: 用户双击打开 PowerShell
    │
步骤 3: Windows 创建新进程
    │  → 从注册表读取所有环境变量（系统级 + 用户级）
    │  → 复制一份放进新进程的内存
    │
步骤 4: PowerShell 查找并执行 Profile 脚本
    │  → 可能动态修改 PATH（如 conda activate）
    │
步骤 5: PowerShell 就绪，等待用户输入
    │
步骤 6: 用户输入 "claude"
    │
步骤 7: PowerShell 去 PATH 中搜索 claude 可执行文件
    │  → 找到 → 创建 Claude Code 子进程
    │  → 子进程继承 PowerShell 当前的所有环境变量
    │
步骤 8: Claude Code 启动，拥有和 PowerShell 相同的 PATH
```

## 关键特性

| 特性 | 说明 |
|------|------|
| **自动性** | 子进程不需要任何操作，自动继承 |
| **快照式** | 继承的是一瞬间的副本，不是持续引用 |
| **单向隔离** | 父进程改了变量，已创建的子进程不受影响；反之亦然 |
| **操作系统的内核级强制** | 无需额外代码，操作系统保证此行为 |

类比：像财产继承，但更简单——子进程出生就自动携带父进程的所有环境变量，无需任何"登记"或"法律程序"。

## 实际验证

```powershell
# 1. 查看当前进程的 PATH
echo $env:PATH

# 2. 临时修改 PATH（仅影响当前进程）
$env:PATH = "C:\MyTest;" + $env:PATH

# 3. 启动 Claude Code（作为子进程）
claude
# Claude Code 的 PATH 也包含 C:\MyTest（继承了修改后的版本）

# 4. 关闭此 PowerShell，重新打开
# PATH 恢复为注册表原版（临时修改已随进程消亡）
```

## 与注册表的关系

| 存储位置 | 生命周期 | 影响范围 |
|----------|----------|----------|
| 注册表 | 永久（直到手动修改） | 新创建的所有进程 |
| 进程内存 | 进程存活期间 | 仅该进程及子进程 |

修改注册表后，**必须重新打开终端**才能生效——因为已有的进程已经在创建时读取了旧值，不会回读注册表。

---

*process-environment-inheritance | type:concept | status:seed | domain:Engineering*
