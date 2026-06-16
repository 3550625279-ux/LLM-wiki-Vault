---
type: concept
title: "CUDA 与 DLL — GPU 计算的基础设施"
created: 2026-06-15
updated: 2026-06-15
tags: [cuda, dll, gpu, nvidia, pytorch, inference, engineering]
status: seed
complexity: basic
domain: Engineering
sources:
  - "[[sources/mineru-mcp-debugging-session]]"
related:
  - "belongs_to::[[domains/Engineering]]"
  - "applied_in::[[concepts/inference-engine]]"
  - "depends_on::[[concepts/inference-engine]]"
  - "produced_by::[[sources/mineru-mcp-debugging-session]]"
---

# CUDA 与 DLL — GPU 计算的基础设施

## 🔗 关系链接

- belongs_to: [[domains/Engineering]]
- applied_in: [[concepts/inference-engine]]
- depends_on: [[concepts/inference-engine]]
- produced_by: [[sources/mineru-mcp-debugging-session]]

---

> CUDA 是 Python 指挥 GPU 干活的桥梁；DLL 是预编译好的机器码模块。

---

## DLL 是什么

**DLL（Dynamic Link Library，动态链接库）** 是 Windows 上的共享代码文件，扩展名 `.dll`（Python 专用的叫 `.pyd`）。

里面是**已经编译好的机器码**——用 C/C++ 写的代码，编译成 CPU/GPU 直接执行的指令。Python 在运行时动态加载它，调用里面的函数。

### 为什么需要 DLL？

Python 本身很慢。AI 推理的核心操作是矩阵乘法（大量数字的乘和加），用 Python 循环做要几分钟，用 C++ 编译成 DLL 让 GPU 执行只要几秒。

```
你的 Python 代码
    ↓ 调用
torch.matmul(a, b)     ← Python 函数
    ↓ 底层调用
cublas64_13.dll        ← NVIDIA 的 C++ 矩阵乘法库
    ↓ 通过驱动发送指令
GPU 执行计算
    ↓
结果返回 Python
```

### DLL 不是"翻译"

DLL 不是把一种语言翻译成另一种。它更像是**已经做好的工具**——你不需要知道电钻怎么制造，你只需要拿起来用。

---

## CUDA 是什么

**CUDA（Compute Unified Device Architecture，统一计算设备架构）** 是 NVIDIA 做的一整套工具包，让程序能指挥 GPU 做通用计算（不只是显示画面）。

### CUDA Toolkit 的组成

```
CUDA Toolkit（完整安装 ~3-4 GB）
├── nvcc.exe              ← CUDA 编译器，把 GPU 代码编译成机器码
├── bin/
│   ├── cudart64_13.dll   ← CUDA 运行时（GPU 基础操作）
│   ├── cublas64_13.dll   ← 矩阵运算库（AI 推理核心）
│   ├── cudnn64_9.dll     ← 深度学习专用加速库
│   ├── cufft64_13.dll    ← 傅里叶变换库
│   └── ...几十个 DLL
├── include/              ← C/C++ 头文件
└── lib/                  ← 静态库
```

### PyTorch 自带 vs 独立安装

| | PyTorch 自带 CUDA | 独立 CUDA Toolkit |
|---|---|---|
| 包含 | 运行时 DLL（cublas、cudnn 等） | 完整开发包（编译器 + 头文件 + DLL） |
| 大小 | ~2 GB（随 torch 安装） | ~3-4 GB（单独安装） |
| CUDA_PATH | **不设置** | 设置环境变量指向安装目录 |
| 用途 | PyTorch 自己跑模型够用 | 需要编译 C++ CUDA 代码（如 lmdeploy turbomind） |

PyTorch 的 `+cu130` 后缀表示它自带了 CUDA 13.0 的运行时 DLL，正常跑模型没问题。但 lmdeploy 的 turbomind 引擎是**额外编译的 C++ 组件**，它的 `.pyd` 文件加载时需要通过 `CUDA_PATH` 环境变量找到完整的 CUDA DLL 目录。

---

## CUDA_PATH 环境变量

**CUDA_PATH** 是一个环境变量（操作系统级别的全局配置），告诉系统"CUDA 的文件在这个目录下"。

```bash
# 典型值
CUDA_PATH=C:\Program Files\NVIDIA\CUDA\v13.0
```

没有 CUDA_PATH 时：
- lmdeploy turbomind → `AssertionError: Can not find $env:CUDA_PATH` 💥
- PyTorch → 正常工作（自带 DLL，不需要 CUDA_PATH）✅

---

## +cu130 是什么意思

`torch 2.12.0+cu130` 中的 `cu130` 表示这个 PyTorch 是针对 CUDA 13.0 编译的。

不同版本的 CUDA 有不同的 API 和 DLL。PyTorch 每个版本发布多个编译版：

```
torch 2.12.0+cu118   ← 针对 CUDA 11.8
torch 2.12.0+cu124   ← 针对 CUDA 12.4
torch 2.12.0+cu130   ← 针对 CUDA 13.0  ← 你装的
```

选择哪个 cu 版本取决于你的 GPU 架构和驱动版本。RTX 5070 Ti（Blackwell 架构，计算能力 12.0）需要 CUDA 13.0 才能完整支持。

---

## 调用链全貌

```
Python: torch.matmul(a, b)
  ↓
PyTorch C++ 层（DLL/.so）
  ↓
CUDA DLL（cublas64_13.dll）← 矩阵乘法实现
  ↓
NVIDIA 驱动
  ↓
GPU 硬件执行
  ↓
结果返回 Python
```

每一层都是上一层的"底层实现"。Python 调 PyTorch，PyTorch 调 CUDA DLL，CUDA DLL 调驱动，驱动指挥 GPU。

---

## 关键洞察

- CUDA 不是一个文件，是**一整个平台**（编译器 + 运行时 + 库）
- PyTorch 自带 CUDA 运行时 DLL，日常使用不需要安装完整的 CUDA Toolkit
- 需要 CUDA Toolkit 的场景：**编译 C++ CUDA 代码**（如 lmdeploy turbomind 的 .pyd）
- `CUDA_PATH` 不存在 ≠ GPU 不能用，只是需要它的特定组件（如 lmdeploy turbomind）无法加载

---

*首次记录: 2026-06-15 | 来源: MinerU MCP 调试实践*
