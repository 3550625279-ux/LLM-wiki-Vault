# 📚 深度学习：Hyperbolic Fine-Tuning for Large Language Models

> **会议**: NeurIPS 2025 | **机构**: HKUST(GZ), Yale, Stanford, CUHK
> **作者**: Menglin Yang, Ram Samarth B B, Aosong Feng, Bo Xiong, Jiahong Liu, Irwin King, Rex Ying
> **难度**: ⭐⭐⭐⭐ 高级（需要线性代数和双曲几何基础）

---

## 一句话理解

LLM 的 token 嵌入天然具有双曲层次结构，直接在双曲流形上做 LoRA 适配，比欧几里得 LoRA 在推理任务上平均提升 2-7 个百分点。

## 难度评估

| 维度 | 评估 |
|------|------|
| 前置知识 | LoRA/PEFT、双曲几何基础（Poincaré/Lorentz 模型）、流形上的优化 |
| 数学深度 | 高（涉及黎曼流形、δ-双曲性、Gromov 乘积） |
| 代码复杂度 | 中（核心是 Lorentz 双曲空间中的低秩变换） |
| 预计学习时间 | 3-5 小时（含代码实验） |

## 材料导航

| 文件 | 内容 | 阅读顺序 |
|------|------|----------|
| [[quick-summary]] | 快速摘要（5 分钟） | 1️⃣ |
| [[summary]] | 详细总结（15 分钟） | 2️⃣ |
| [[insights]] | 核心洞察与概念转变（10 分钟） | 3️⃣ |
| [[method]] | 方法拆解与算法流程（20 分钟） | 4️⃣ |
| [[mental-model]] | 心智模型与知识定位（10 分钟） | 5️⃣ |
| [[reflection]] | 批判性反思与延伸（10 分钟） | 6️⃣ |
| [[qa]] | 15 道自测题 | 7️⃣ |
| `code/hyp_lora_demo.py` | 核心方法简化实现 | 🔬 |
| `code/hyperbolicity_analysis.py` | δ-双曲性分析可视化 | 🔬 |
| `index.html` | 交互式探索器 | 🎮 |

## 核心收获

1. **几何视角**：LLM 嵌入不是"扁平"的——高频 token（"the"、"is"）聚集在原点附近，低频 token（"apple"、"purple"）向外扩散，形成天然的层次树状结构
2. **理论桥梁**：幂律分布 ↔ 双曲几何存在数学等价关系，γ = 2/ζ + 1
3. **方法创新**：直接在 Lorentz 双曲面上做低秩变换，绕过传统双曲神经网络的 exp-log 抵消问题
4. **实用价值**：参数效率与 LoRA 完全一致，可在任何欧几里得 LLM 上即插即用

## 你将学到什么

- 如何量化分析 LLM 嵌入的几何特性
- δ-双曲性度量及其与层次结构的关系
- 双曲空间中的低秩适配原理
- 为什么欧几里得空间表示语言存在本质局限
