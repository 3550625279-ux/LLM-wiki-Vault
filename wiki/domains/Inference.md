---
title: "Inference — 推理与部署"
type: domain
status: seed
domain: Inference
tags: [quantization, distillation, kv-cache, speculative-decoding, vllm]
created: 2026-06-13
updated: 2026-06-13
confidence: high
---

# Inference — 推理与部署

> **领域使命**: 让大模型在资源约束下高效运行。
> **实践优先**: 这是最工程化的领域，许多技术可以直接上手实验。

---

## 📌 领域地图

```
Inference
├── 量化 (Quantization)
│   ├── INT8 (LLM.int8)
│   ├── INT4 (GPTQ/AWQ)
│   └── GGUF (llama.cpp)
│
├── 知识蒸馏 (Distillation)
│   ├── 黑盒蒸馏 (仅用输出)
│   └── 白盒蒸馏 (中间层特征)
│
├── KV Cache 优化
│   ├── PagedAttention (vLLM)
│   ├── KV Cache 量化
│   └── Multi-Query / GQA
│
├── 生成加速
│   ├── 投机解码 (Speculative Decoding)
│   ├── Continuous Batching
│   └── 束搜索 vs 贪心 vs 采样
│
└── 推理框架
    ├── vLLM — PagedAttention 核心
    ├── Ollama — 本地部署
    ├── TensorRT-LLM — NVIDIA 优化
    └── llama.cpp — CPU 友好
```

---

## 🧮 已有节点

*(暂无已创建节点)*

**`contains::` 边：**
*(暂无)*

## 🔴 关键缺口

- `kv-cache` — KV Cache 原理与内存瓶颈 — **推理优化核心**
- `paged-attention` — PagedAttention 内存分页管理
- `post-training-quantization` — PTQ 原理与精度损失
- `gptq` — 基于 Hessian 的权重量化
- `speculative-decoding` — 草稿模型 + 验证模型
- `continuous-batching` — 动态批处理提高 GPU 利用率

---

## 🔗 领域间关系

- `depends_on::` [[domains/architecture]] — 架构决定量化方案
- `applied_in::` [[domains/engineering]] — 推理优化是部署工程核心

---

## 💡 领域关键洞察

- **KV Cache 是 LLM 推理的内存杀手**: 长序列下占 GPU 内存 70%+
- **量化精度损失规律**: INT8 几乎无损 → INT4 轻微 → INT2 显著
- **Continuous Batching**: 不等请求完成就处理下一个，vLLM 核心创新

---

## 📖 推荐资料

- [ ] vLLM 论文 (Kwon et al. 2023)
- [ ] GPTQ 论文 (Frantar et al. 2022)
- [ ] Speculative Decoding (Leviathan et al. 2023)

---

## 📊 领域统计

```
concept 节点: 0 (目标: 10+)
entity 节点:  0 (目标: 6+)
maturity:    seed
```
