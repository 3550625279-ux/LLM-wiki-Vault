# Concepts Index — 概念节点目录

> **类型**: Map of Content (MoC)
> **用途**: wiki/concepts/ 目录下所有 concept 节点的索引。
> **维护**: 每次 ingest 创建新 concept 节点后，在对应领域分组下追加一行。

---

## 按领域分组

### [[domains/Foundations|Foundations]]
> *待填充 — 首次 ingest 后追加*

### [[domains/Architecture|Architecture]]
> *待填充*

### [[domains/Training|Training]]
> *待填充*

### [[domains/Alignment|Alignment]]
> *待填充*

### [[domains/Inference|Inference]]
> *待填充*

### [[domains/Multimodal|Multimodal]]
> *待填充*

### [[domains/Agents|Agents]]
> *待填充*

### [[domains/Engineering|Engineering]]
- [[concepts/mcp-protocol]] — MCP 协议架构与 JSON-RPC 2.0 | status:seed
- [[concepts/claude-code-configuration]] — Claude Code 7层配置文件体系 | status:seed
- [[concepts/mcp-tool-calling-flow]] — MCP 工具调用 5 阶段全链路 | status:seed

---

## 按状态分组

### 🌱 seed (草稿)
> *无*

### 🔨 developing (完善中)
> *无*

### ✅ mature (成熟)
> *无*

### 🌲 evergreen (常青)
> *无*

---

## 高优先级缺口 (待创建)

根据各 domain 页面的 TODO 列表，以下 concept 节点应优先创建：

**Architecture 优先**:
- `attention-mechanism` — 所有 Architecture 知识的基础
- `transformer-architecture` — 当代 LLM 基础结构
- `rotary-position-embedding` — RoPE, 当前主流位置编码

**Training 优先**:
- `scaling-laws` — 影响所有训练决策
- `lora` — PEFT 实践最常用
- `rlhf` — 对齐训练核心

**Foundations 优先**:
- `cross-entropy-loss` — 几乎所有训练都用到
- `gradient-descent` — 优化基础
- `kl-divergence` — RLHF/对齐中大量使用

---

## 统计

```
总 concept 节点: 0
目标总数:        50+
上次更新:        2026-06-13
```
