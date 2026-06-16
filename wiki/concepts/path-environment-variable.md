---
type: concept
title: "PATH 环境变量"
created: 2026-06-16
updated: 2026-06-16
tags: [PATH, environment-variable, 环境变量, 操作系统基础, 基础设施]
status: seed
complexity: basic
domain: Common Computer
sources: ["[[sources/terminal-and-environment-basics]]"]
related:
  - "depends_on::[[concepts/terminal-and-shell]]"
  - "extends::[[concepts/process-environment-inheritance]]"
  - "applied_in::[[concepts/conda-environments]]"
  - "contrasts::[[concepts/windows-registry-env]]"
  - "belongs_to::[[domains/common-computer]]"
  - "produced_by::[[sources/terminal-and-environment-basics]]"
thumbnail: ""
---

# PATH 环境变量

## 🔗 关系链接

- depends_on: [[concepts/terminal-and-shell]]
- extends: [[concepts/process-environment-inheritance]]
- applied_in: [[concepts/conda-environments]]
- contrasts: [[concepts/windows-registry-env]]
- belongs_to: [[domains/common-computer]]
- produced_by: [[sources/terminal-and-environment-basics]]

---

## 核心定义

**PATH** 是操作系统的一个环境变量，存储了一组**目录路径**（用分号 `;` 分隔）。当用户输入命令时，系统从 PATH 中**从前往后**逐个目录搜索，找到第一个匹配的可执行文件就停止。

**本质**：PATH 解决的问题是——用户不想每次都输入完整路径（如 `D:\Software\NodeJS\node.exe`），只想输入程序名（`node`），系统自动去哪些目录里找。

## 工作机制

```
用户输入: python
    │
    ▼
Shell 解析命令名: python
    │
    ▼
读取 PATH 变量，拆分分号得到目录列表:
  [0] D:\Software\Anaconda\envs\claude-code\
  [1] D:\Software\Anaconda\envs\claude-code\Scripts\
  [2] D:\Software\Anaconda\condabin\
  ...
  [N] D:\Software\Python\
  ...
    │
    ▼
从 [0] 开始逐个目录搜索 python.exe:
  [0] D:\Software\Anaconda\envs\claude-code\python.exe → ✅ 找到！
    │
    ▼
执行该程序，停止搜索（不继续找 [N]）
```

**关键特性**：
- **从前往后搜索**：排在前面的目录优先匹配
- **首次命中即停止**：不会找"更好的"，只找"第一个"
- **分号分隔**：所有目录连成一个字符串，用 `;` 隔开

## PATH 的物理存储 vs 显示

| 层面 | 形式 |
|------|------|
| 注册表存储 | 一条超长字符串：`D:\Software\Python;C:\WINDOWS\system32;...` |
| GUI 显示 | 拆分成多行列表（GUI 做了格式化，方便编辑） |
| PowerShell 显示 | `$env:PATH` 展开为完整的分号分隔字符串 |

类比：注册表中的 PATH 像 CSV 文件（一行文字用分号分隔），GUI 像 Excel（自动拆成表格显示）。

## PATH 的合并规则

PowerShell 中 `$env:PATH` 实际是**两处合并**的结果：

```
系统级 PATH（HKLM）在前
    +
用户级 PATH（HKCU）在后
    =
进程中的完整 PATH
```

## PATH 操作示例

```powershell
# 查看当前 PATH
echo $env:PATH

# 临时添加目录（仅影响当前进程及子进程，不影响注册表）
$env:PATH = "C:\MyTest;" + $env:PATH

# 永久修改需要通过系统属性 GUI 或 reg 命令修改注册表
```

## PATH 与程序查找的关系

| 场景 | 行为 |
|------|------|
| 程序在 PATH 目录中 | 输入程序名即可运行 |
| 程序不在 PATH 中 | 必须输入完整路径，否则 "command not found" |
| PATH 中多个目录有同名程序 | 第一个被找到的优先（从前往后） |

---

*path-environment-variable | type:concept | status:seed | domain:Engineering*
