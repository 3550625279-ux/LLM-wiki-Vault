---
type: concept
title: "推理引擎 — AI 模型的执行引擎"
created: 2026-06-15
updated: 2026-06-15
tags: [inference, engine, transformers, lmdeploy, onnxruntime, pytorch, engineering]
status: seed
complexity: intermediate
domain: Engineering
sources:
  - "[[sources/mineru-mcp-debugging-session]]"
related:
  - "belongs_to::[[domains/Engineering]]"
  - "depends_on::[[concepts/cuda-and-dll]]"
  - "extends::[[concepts/mcp-protocol]]"
  - "produced_by::[[sources/mineru-mcp-debugging-session]]"
---

# 推理引擎 — AI 模型的执行引擎

## 🔗 关系链接

- belongs_to: [[domains/Engineering]]
- depends_on: [[concepts/cuda-and-dll]]
- extends: [[concepts/mcp-protocol]]
- produced_by: [[sources/mineru-mcp-debugging-session]]

---

> 模型文件只是数据（菜谱），推理引擎才是让模型"跑起来"的厨师。

---

## 核心定义

**推理引擎（Inference Engine）** 是读取模型权重文件、接收输入数据、执行计算、输出结果的软件组件。

```
模型文件（.safetensors / .onnx）  ← 只是数据，不会自己运行
    +
推理引擎（Python 包 + DLL）       ← 读取模型，执行计算
    +
输入数据（图片/文本）             ← 原材料
    ↓
输出结果（识别文字/生成文本）     ← 最终产出
```

关键区分：**模型 ≠ 引擎**。同一个模型文件，可以用不同引擎来跑。就像同一本菜谱，家用厨房和商用厨房都能做。

---

## 主流推理引擎对比

| 引擎 | 开发者 | 特点 | 依赖 |
|------|--------|------|------|
| **transformers** | HuggingFace | 纯 Python + PyTorch，兼容性最好 | PyTorch |
| **lmdeploy (turbomind)** | 商汤 | C++ 高性能推理，速度快 | CUDA Toolkit、特定 torch 版本 |
| **lmdeploy (pytorch)** | 商汤 | 备选模式，用 PyTorch + triton | triton（仅 Linux） |
| **onnxruntime** | 微软 | 跑 ONNX 格式模型，跨平台 | ONNX 运行时 |

### 选择逻辑

```
环境兼容？ → 选最高效的引擎
环境不兼容？ → 回退到兼容性最好的引擎（通常是 transformers）
```

引擎选择通常由 `engine_utils.py` 类的代码自动完成，检查逻辑是：
1. 尝试 `import lmdeploy` → 成功则选 lmdeploy
2. 失败则回退到 transformers

⚠️ **陷阱**：`import` 成功 ≠ 引擎能运行。详见 [[insights/when-import-succeeds-but-runtime-fails]]

---

## 引擎在 AI 系统中的位置

```
你的 Python 代码
    ↓ 调用
推理引擎（transformers / lmdeploy）
    ↓ 读取
模型文件（.safetensors 中的权重参数）
    ↓ 通过引擎的底层代码
CUDA DLL（cublas64_*.dll）   ← GPU 计算
    ↓
GPU 硬件执行
    ↓
结果返回
```

引擎的核心工作：
1. **加载模型**：从磁盘读取权重文件，构建模型计算图
2. **前处理**：把输入（图片/文本）转成张量（tensor）
3. **推理计算**：矩阵乘法、注意力计算等（核心 GPU 计算）
4. **后处理**：把输出张量转回人类可读的结果

---

## MinerU 的引擎选择实践

MinerU（PDF 解析工具）使用了分层引擎架构：

| 后端（backend） | pipeline 部分 | VLM 部分 | 适用场景 |
|-----------------|--------------|----------|---------|
| `pipeline` | PyTorch/ONNX | 不使用 | 传统流程，轻量 |
| `hybrid-engine` | PyTorch/ONNX | lmdeploy | 混合方案，高精度 |
| `hybrid-transformers` | PyTorch/ONNX | transformers | 混合方案，高兼容性 |

`hybrid-engine` = pipeline（布局检测 + OCR + 公式识别 + 表格识别）+ VLM（视觉语言模型精细理解）

当 lmdeploy 在 Windows 上因缺少 CUDA Toolkit 而无法使用时，回退到 transformers 后端是零风险的解决方案，代价是 VLM 推理速度稍慢。

---

## 关键洞察

- 模型文件和引擎是**解耦的**——同一个模型文件，不同引擎都能加载运行
- 引擎是 Python 包，装在 `site-packages/` 目录下，不是缓存文件
- 选引擎的核心矛盾：**性能 vs 兼容性**——高性能引擎通常依赖更多（CUDA Toolkit、特定 torch 版本、Linux 环境）
- "换引擎"不需要下载新文件到缓存，只是决定用哪套已安装的代码来读取和运行模型

---

*首次记录: 2026-06-15 | 来源: MinerU MCP 调试实践*
