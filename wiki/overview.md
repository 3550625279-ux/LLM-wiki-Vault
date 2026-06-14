# AI Knowledge Vault — 全局知识地图

> **用途**: 整个 Vault 的鸟瞰视图，展示 8 大领域的关系与学习路径。
> **状态**: 会随 ingest 积累而持续扩展。
> **维护**: 每 10 次 ingest 后由 align 协议更新一次。

---

## 🗺️ 领域关系图 (文字版)

```
                    ┌─────────────────┐
                    │  Foundations    │  数学/概率/优化
                    │  (基础层)       │
                    └────────┬────────┘
                             │ depends_on ↓
              ┌──────────────┼──────────────┐
              ▼              ▼              ▼
    ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
    │ Architecture │  │   Training   │  │  Alignment   │
    │ (模型结构)   │  │  (训练方法)  │  │ (对齐与安全) │
    └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
           │                 │                  │
           └────────┬────────┘                  │
                    ▼                           │
          ┌──────────────────┐                  │
          │    Inference     │◄─────────────────┘
          │  (推理与部署)    │
          └────────┬─────────┘
                   │
         ┌─────────┼─────────┐
         ▼         ▼         ▼
  ┌───────────┐ ┌───────┐ ┌──────────────┐
  │Multimodal │ │Agents │ │ Engineering  │
  │(多模态)   │ │(智能体)│ │ (工程实践)  │
  └───────────┘ └───────┘ └──────────────┘
```

---

## 📚 8 大领域概览

### 1. Foundations — 数学与理论基础
**核心问题**: LLM 的数学根基是什么？
**覆盖范围**:
- 线性代数: 矩阵运算、特征值、SVD
- 概率论: 贝叶斯推断、分布、采样
- 信息论: 熵、KL散度、互信息
- 优化理论: 梯度下降、Adam、学习率调度
- 统计学习理论: PAC learning、VC dimension

**关键问题**:
- 为什么深度学习收敛？（没有完整理论）
- 为什么 over-parameterization 反而有效？

→ 详见 [[domains/foundations]]

---

### 2. Architecture — 模型架构
**核心问题**: Transformer 为什么这么强大？
**覆盖范围**:
- Attention Mechanism（自注意力、多头注意力）
- Transformer 架构（Encoder/Decoder/Encoder-Decoder）
- 位置编码（绝对/相对/RoPE/ALiBi）
- 归一化方法（LayerNorm/RMSNorm/Pre-Norm）
- Mixture of Experts (MoE)
- 效率变体（Flash Attention、Linear Attention）

**关键洞察**:
- Attention 的 O(n²) 瓶颈是核心工程挑战
- Pre-Norm vs Post-Norm 影响训练稳定性

→ 详见 [[domains/architecture]]

---

### 3. Training — 训练方法论
**核心问题**: 如何让模型学到想要的知识？
**覆盖范围**:
- 预训练: 数据工程、BPE分词、目标函数
- 指令微调 (SFT/RLHF/DPO)
- 参数高效微调 (LoRA/QLoRA/Prefix-Tuning)
- 分布式训练 (DP/TP/PP/ZeRO)
- 学习率调度、批次大小策略
- Scaling Laws

**关键矛盾**:
- [[contradicts]] Scaling Hypothesis vs Emergent Abilities 是否可预测

→ 详见 [[domains/training]]

---

### 4. Alignment — 对齐与安全
**核心问题**: 如何让 AI 做我们真正想要的事？
**覆盖范围**:
- 价值对齐 (Constitutional AI、RLHF)
- 可解释性 (Mechanistic Interpretability)
- 红队测试与越狱防护
- Reward Hacking 与 Goodhart's Law
- 超级对齐研究

**关键张力**:
- 能力 vs 安全的 trade-off
- 规则对齐 vs 价值对齐

→ 详见 [[domains/alignment]]

---

### 5. Inference — 推理与部署
**核心问题**: 如何让大模型又快又便宜？
**覆盖范围**:
- 量化 (INT8/INT4/GGUF/GPTQ/AWQ)
- 知识蒸馏
- KV Cache 管理 (PagedAttention)
- 投机解码 (Speculative Decoding)
- 批处理策略 (Continuous Batching)
- 推理框架 (vLLM/TGI/Ollama)

→ 详见 [[domains/inference]]

---

### 6. Multimodal — 多模态
**核心问题**: 语言之外，AI 能理解什么？
**覆盖范围**:
- Vision-Language Models (CLIP/LLaVA/GPT-4V)
- 图像生成 (Diffusion Models/DALL-E/Stable Diffusion)
- 音频/语音 (Whisper/AudioLM)
- 视频理解
- 具身智能 (Embodied AI)

→ 详见 [[domains/multimodal]]

---

### 7. Agents — 智能体系统
**核心问题**: 如何让 LLM 自主完成复杂任务？
**覆盖范围**:
- ReAct 框架 (推理 + 行动)
- 工具使用 (Function Calling)
- 记忆系统 (短期/长期/外部记忆)
- 多智能体协作
- 计划与执行 (Chain-of-Thought/Tree-of-Thought)
- Agent 安全

→ 详见 [[domains/agents]]

---

### 8. Engineering — 工程实践
**核心问题**: 如何在生产环境可靠运行 AI？
**覆盖范围**:
- MLOps (实验追踪/模型注册/部署流水线)
- 评估框架 (MMLU/HumanEval/自定义 eval)
- 数据工程 (清洗/去重/质量过滤)
- 监控与可观测性
- 成本优化
- Prompt Engineering

→ 详见 [[domains/engineering]]

---

## 🛤️ 推荐学习路径

### 路径 A: 理论优先型
```
Foundations → Architecture → Training → Alignment → Inference
```

### 路径 B: 实践优先型
```
Engineering → Architecture (精华) → Training (微调) → Inference (部署)
```

### 路径 C: 应用开发型
```
Architecture (快速) → Agents → Engineering → Inference (按需)
```

### 路径 D: 研究导向型
```
Foundations (深入) → Architecture (深入) → Alignment → Training (前沿)
```

---

## 🔑 跨领域关键概念

这些概念横跨多个领域，优先掌握：

1. **Attention Mechanism** — 贯穿 Architecture/Multimodal/Agents
2. **Scaling Laws** — 贯穿 Training/Architecture/Inference
3. **Emergent Abilities** — 贯穿 Training/Alignment（有矛盾，保留张力）
4. **Tokenization** — 贯穿 Foundations/Architecture/Engineering
5. **RLHF** — 贯穿 Training/Alignment

---

## 📊 当前知识库状态

| 领域 | concept 节点 | 关键进展 |
|------|-------------|---------|
| Foundations | 2 | 双曲几何 + MC Dropout |
| Architecture | 2 | LLM 嵌入几何 + CAT 注意力 |
| Training | 5 | LoRA + HypLoRA + SetFit + 负面增强 + 对比学习 |
| Alignment | 0 | — |
| Inference | 0 | — |
| Multimodal | 4 | CAGC: MIR + CAT + Bank + GCCL |
| Agents | 3 | 意图检测 + OOS 检测 + 自适应 ICL |
| Engineering | 4 | MCP 协议 + 不确定性路由 |

**总节点数**: 31 (concept: 19, entity: 0, insight: 3, source: 4, comparison: 1, question: 2)

---

*最后更新: 2026-06-14 | 节点总数: 31 | 下次更新触发: 10次 ingest 后*
