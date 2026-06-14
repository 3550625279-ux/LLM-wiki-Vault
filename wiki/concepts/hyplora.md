---
type: concept
title: "HypLoRA — 双曲低秩适配"
created: 2026-06-13
updated: 2026-06-13
tags: [PEFT, 双曲几何, LoRA, 参数高效微调, 推理增强]
status: seed
complexity: advanced
domain: Training
sources: ["[[sources/hyplora-neurips2025]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "extends::[[concepts/lora]]"
  - "implements::[[concepts/hyperbolic-geometry]]"
  - "depends_on::[[concepts/hyperbolic-geometry-llm]]"
  - "applied_in::[[concepts/lora]]"
  - "produced_by::[[sources/hyplora-neurips2025]]"
thumbnail: ""
---

# HypLoRA — 双曲低秩适配

> **一句话**：直接在 Lorentz 双曲流形上执行低秩适配，绕过切空间的 exp-log 抵消问题，利用 LLM 嵌入的天然层次结构。

---

## 核心思想

标准 LoRA 在欧几里得空间中执行线性变换 z = Wx + BAx。HypLoRA 将这一变换搬到双曲流形上，引入非线性高阶项，天然捕捉 token 的层次关系。

### 关键创新：直接 Lorentz 低秩变换（LLR）

```
LLR(BA, x_H) = (√(‖BAx_H^s‖² + K),  BAx_H^s)
```

- x_H^s：双曲点的空间分量（去掉时间分量）
- K：双曲曲率（可学习参数）
- 输出保证在 Lorentz 双曲面上：⟨z_H, z_H⟩_L = -K

### 完整流程

```
欧氏输入 x_E
  → Π_K exp: 投影到双曲面
  → LLR: 直接双曲低秩变换
  → Π_K log: 投影回欧氏空间
输出 z_E
```

---

## 为什么有效

1. **避免抵消效应**：传统双曲网络用 exp→log→线性→log→exp 序列，exp 和 log 互逆导致完全抵消。LLR 直接在流形上操作，不经过切空间。

2. **高阶范数依赖**（命题 1）：由于双曲操作的非线性，HypLoRA 的等效变换包含关于输入范数 ‖x‖₂ 的高阶项：
   - 范数小的 token（高频词如 "the"）→ 变换幅度小
   - 范数大的 token（低频词如 "apple"）→ 变换幅度大

3. **参数效率**：与 LoRA 完全相同（仅多 1 个标量 K）

---

## 实验结果

| 模型 | 方法 | 算术推理 M.AVG | 常识推理 AVG |
|------|------|---------------|-------------|
| LLaMA3-8B | LoRA | 71.9 | 80.8 |
| LLaMA3-8B | **HypLoRA** | **74.2** (+2.3) | **84.8** (+4.0) |
| Qwen2.5-7B | LoRA | 80.8 | 85.2 |
| Qwen2.5-7B | **HypLoRA** | **88.3** (+7.5) | **87.0** (+1.8) |

---

## 局限性

- 分析主要在算术推理和常识推理，代码/多语言/长上下文泛化性未验证
- 嵌入范数与 token 频率的关系是相关性而非因果性
- 额外双曲投影带来适度推理开销

---

## 相关链接

- 原始论文: [[raw/papers/hyperbolic-fine-tuning-llms/paper.pdf]]
- 学习材料: [[raw/papers/hyperbolic-fine-tuning-llms/README]]
- GitHub: https://github.com/marlin-codes/HypLoRA
