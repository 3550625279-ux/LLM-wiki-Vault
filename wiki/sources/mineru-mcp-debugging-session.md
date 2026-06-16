---
type: source
title: "MinerU MCP 调试会话 — 从失败到理解推理引擎全链路"
created: 2026-06-15
updated: 2026-06-15
tags: [mineru, mcp, debugging, inference-engine, cuda, lmdeploy, engineering]
status: developing
complexity: intermediate
domain: Engineering
sources: ["Claude Code 对话记录 (2026-06-15)"]
related:
  - "belongs_to::[[domains/Engineering]]"
  - "spawns::[[concepts/inference-engine]]"
  - "spawns::[[concepts/cuda-and-dll]]"
  - "spawns::[[insights/when-import-succeeds-but-runtime-fails]]"
  - "extends::[[concepts/mcp-protocol]]"
---

# MinerU MCP 调试会话

## 🔗 关系链接

- belongs_to: [[domains/Engineering]]
- spawns: [[concepts/inference-engine]] | [[concepts/cuda-and-dll]] | [[insights/when-import-succeeds-but-runtime-fails]]
- extends: [[concepts/mcp-protocol]]

---

> 一次完整的 AI 工程排障过程：从"MCP 返回 false"到理解推理引擎、CUDA、DLL 的全链路。

---

## 背景

目标：测试 MinerU（PDF 解析工具）的 MCP 服务器是否可用，用 36 页论文 PDF 作为测试样本。

期望：MCP 工具成功处理 PDF，输出 Markdown。

实际：MCP 工具返回 `{"result": false}`，无任何错误信息。

---

## 调试链路

```
MCP 返回 false（表面问题）
  ↓ 为什么？
servers.py 的 try/except 吞掉了错误，只返回 success: False
  ↓ 真正的错误是什么？
AssertionError: Can not find $env:CUDA_PATH
  ↓ 为什么缺 CUDA_PATH？
系统没装 CUDA Toolkit，只有 PyTorch 自带的运行时
  ↓ 为什么需要 CUDA_PATH？
lmdeploy 的 turbomind 引擎是 C++ 编译的 DLL，加载时需要 CUDA DLL
  ↓ 为什么选了 lmdeploy？
engine_utils.py 只检查 import 能否成功，没验证能不能跑
  ↓ 怎么修？
卸载 lmdeploy，让引擎选择回退到 transformers
  ↓ 修完还是不行？
MCP 服务器子进程没重启，还在用旧代码
```

---

## 关键发现

### 1. 错误被静默吞掉
`servers.py` 的 `process()` 返回 `{"success": False, "error": "..."}`，但调用方只取 `.get("success", False)`，丢弃了 error 信息。

### 2. lmdeploy 在 Windows 上两条路都走不通
- **turbomind（默认）**：需要 `CUDA_PATH` 环境变量 → 系统没装 CUDA Toolkit → 失败
- **pytorch（备选）**：需要 `triton` 库 → triton 不支持 Windows → 失败

### 3. import 成功 ≠ 能运行
`engine_utils.py` 的选择逻辑只检查 `import lmdeploy` 是否成功，没验证 lmdeploy 能不能实际运行。

### 4. 僵尸进程问题
多次 MCP 调用失败后，6+ 个 MinerU MCP 服务器进程在后台未清理，占用 GPU 显存。

---

## 解决方案

| 步骤 | 操作 | 结果 |
|------|------|------|
| 1 | 添加 debug 日志到 servers.py | 看到真正的错误信息 |
| 2 | 4 个并行 agent 排查不同方向 | 定位根因：lmdeploy + CUDA_PATH |
| 3 | `pip uninstall lmdeploy` | 引擎自动回退到 transformers |
| 4 | 清理僵尸 MCP 进程 | 释放 GPU 显存 |
| 5 | 直接调用 `do_parse()` 验证 | 36 页 PDF 处理成功，134KB Markdown |

---

## 模型迁移（附带完成）

将 MinerU 模型缓存从 C 盘迁移到 D 盘：

| 模型 | 从 | 到 | 大小 |
|------|---|---|---|
| PDF-Extract-Kit-1.0 | `~/.cache/modelscope/...` | `D:\Software\MinerU\models\pipeline\` | 2.4 GB |
| MinerU2.5-Pro-2605-1.2B | `~/.cache/modelscope/...` | `D:\Software\MinerU\models\vlm\` | 2.2 GB |

配置 `MINERU_MODEL_SOURCE=local` + `mineru.json` 指向 D 盘。

---

## 涉及的关键概念

- [[concepts/mcp-protocol]] — MCP 服务器通过 stdin/stdout 通信，stdout 被污染会导致 JSON 解析失败
- [[concepts/inference-engine]] — 模型文件 vs 推理引擎的区分，引擎选择逻辑
- [[concepts/cuda-and-dll]] — CUDA Toolkit vs PyTorch 自带 CUDA，CUDA_PATH 环境变量
- [[insights/when-import-succeeds-but-runtime-fails]] — import 成功 ≠ 能运行的陷阱

---

## 提取的核心知识点

1. 推理引擎是 Python 包（代码），模型文件是数据（权重），两者解耦
2. CUDA 是一整个平台（编译器+运行时+库），不只是"加速 Python 的东西"
3. DLL 是预编译好的机器码模块，Python 动态加载调用
4. PyTorch 自带 CUDA 运行时 DLL，日常使用不需要独立安装 CUDA Toolkit
5. MCP 服务器的 stdout 是 JSON-RPC 通道，任何 print() 都会污染它
6. try/except 吞掉错误信息是调试噩梦的根源
7. "import 成功"只检查代码是否存在，不验证能否运行
8. 最简单的修复有时最正确：卸载跑不了的包

---

*首次记录: 2026-06-15 | 来源: Claude Code 对话调试记录*
