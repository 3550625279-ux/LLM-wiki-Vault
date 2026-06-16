---
type: concept
title: "Windows 注册表与环境变量存储"
created: 2026-06-16
updated: 2026-06-16
tags: [windows, registry, 环境变量, 注册表, 操作系统基础]
status: seed
complexity: intermediate
domain: Common Computer
sources: ["[[sources/terminal-and-environment-basics]]"]
related:
  - "depends_on::[[concepts/path-environment-variable]]"
  - "extends::[[concepts/process-environment-inheritance]]"
  - "belongs_to::[[domains/common-computer]]"
  - "produced_by::[[sources/terminal-and-environment-basics]]"
thumbnail: ""
---

# Windows 注册表与环境变量存储

## 🔗 关系链接

- depends_on: [[concepts/path-environment-variable]]
- extends: [[concepts/process-environment-inheritance]]
- belongs_to: [[domains/common-computer]]
- produced_by: [[sources/terminal-and-environment-basics]]

---

## 核心定义

**注册表（Registry）** 是 Windows 的全局配置数据库，存储系统和用户的各种设置。环境变量（包括 PATH）的**永久副本**就存储在注册表中。

## 两个存储位置

| 位置 | 注册表路径 | 含义 | 谁能用 |
|------|-----------|------|--------|
| 用户级 | `HKEY_CURRENT_USER\Environment` | 只属于当前用户 | 仅你 |
| 系统级 | `HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Environment` | 所有用户共享 | 所有人 |

## 存储格式

注册表中 PATH 是**一条超长字符串**，所有目录用分号连接：

```
Path = "D:\Software\Python\Scripts;D:\Software\Python;C:\WINDOWS\system32;..."
```

值类型为 `REG_EXPAND_SZ`（可扩展字符串），支持 `%变量名%` 引用：

```
%USERPROFILE% → C:\Users\35506
%SystemRoot%  → C:\WINDOWS
```

**GUI 是注册表的可视化编辑器**：系统属性 → 环境变量界面，把分号拆分后分行显示，底层读写的仍然是注册表中的那个长字符串。

## 注册表 → 进程的注入时机

```
注册表（永久存储）
    │
    │  进程创建的那一瞬间
    ▼
新进程的内存（进程私有副本）
```

- **注入时机**：进程创建（spawn）的瞬间
- **注入方式**：操作系统内核从注册表读取，复制到新进程内存
- **不是实时同步**：之后注册表改了，已有进程不会感知；反之亦然
- **修改后生效**：需要重新打开终端（创建新进程）

## REG_EXPAND_SZ 与变量展开

`REG_EXPAND_SZ` 类型允许值中包含 `%变量名%` 引用，读取时自动展开：

```
注册表中: %USERPROFILE%\AppData\Local\...
读取后:   C:\Users\35506\AppData\Local\...
```

这与普通 `REG_SZ`（纯字符串，不展开）不同。

## 查看注册表中的环境变量

```powershell
# 查看用户级 PATH
reg query "HKCU\Environment" /v Path

# 查看系统级 PATH（可能需要管理员权限）
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Session Manager\Environment" /v Path
```

## GUI 与注册表的对应关系

```
系统属性 → 环境变量
├── 上面一栏 "用户变量"  ←→  HKEY_CURRENT_USER\Environment
└── 下面一栏 "系统变量"  ←→  HKEY_LOCAL_MACHINE\...\Environment
```

---

*windows-registry-env | type:concept | status:seed | domain:Engineering*
