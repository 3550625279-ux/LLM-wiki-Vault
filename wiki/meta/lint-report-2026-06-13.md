---
type: meta
title: "Lint Report 2026-06-13"
created: 2026-06-13
updated: 2026-06-13
tags: [meta, lint]
status: developing
---

# Lint Report: 2026-06-13

## Summary

| 指标 | 数值 |
|------|------|
| Pages scanned | 22 |
| Issues found | 91 |
| Dead links (unique targets) | 78 |
| Dead link occurrences | 84 |
| Frontmatter missing (no FM) | 11 |
| Frontmatter incomplete | 2 |
| Orphan pages (no inbound links) | 9 |
| Empty content stubs | 4 |
| Stale index entries | 0 |
| Auto-fixed | 0 |
| Needs review | 91 |

> 首次 lint。vault 处于初始化状态：8 个领域综述页已就绪，concepts/entities/operations/insights 全为空壳，等待首次 ingest 填充。

---

## Dead Links — 🔴 BLOCKER (78 unique targets, 84 occurrences)

所有 `concepts/*` 和 `entities/*` wikilink 均指向不存在的页面。这是 vault 初始化状态的预期结果——领域页预置了知识地图骨架，但概念/实体页尚未 ingest。

### concepts/* 死链 (69 unique targets)

| 死链目标 | 来源文件 |
|----------|----------|
| `[[concepts/chain-of-thought]]` | [[domains/Agents]] |
| `[[concepts/react-framework]]` | [[domains/Agents]] |
| `[[concepts/tree-of-thoughts]]` | [[domains/Agents]] |
| `[[concepts/function-calling]]` | [[domains/Agents]] |
| `[[concepts/tool-use-protocol]]` | [[domains/Agents]] |
| `[[concepts/context-window-as-memory]]` | [[domains/Agents]] |
| `[[concepts/vector-database-retrieval]]` | [[domains/Agents]] |
| `[[concepts/rag]]` | [[domains/Agents]] |
| `[[concepts/reflexion]]` | [[domains/Agents]] |
| `[[concepts/task-decomposition]]` | [[domains/Agents]] |
| `[[concepts/alignment-definition]]` | [[domains/Alignment]] |
| `[[concepts/goodharts-law]]` | [[domains/Alignment]] |
| `[[concepts/reward-hacking]]` | [[domains/Alignment]] |
| `[[concepts/mechanistic-interpretability]]` | [[domains/Alignment]] |
| `[[concepts/superposition-hypothesis]]` | [[domains/Alignment]] |
| `[[concepts/attention-head-roles]]` | [[domains/Alignment]] |
| `[[concepts/red-teaming]]` | [[domains/Alignment]] |
| `[[concepts/jailbreak-patterns]]` | [[domains/Alignment]] |
| `[[concepts/inner-outer-alignment]]` | [[domains/Alignment]] |
| `[[concepts/attention-mechanism]]` | [[domains/Architecture]] |
| `[[concepts/multi-head-attention]]` | [[domains/Architecture]] |
| `[[concepts/self-attention-vs-cross-attention]]` | [[domains/Architecture]] |
| `[[concepts/flash-attention]]` | [[domains/Architecture]] |
| `[[concepts/rotary-position-embedding]]` | [[domains/Architecture]] |
| `[[concepts/positional-encoding-absolute]]` | [[domains/Architecture]] |
| `[[concepts/layer-normalization]]` | [[domains/Architecture]] |
| `[[concepts/rmsnorm]]` | [[domains/Architecture]] |
| `[[concepts/mixture-of-experts]]` | [[domains/Architecture]] |
| `[[concepts/grouped-query-attention]]` | [[domains/Architecture]] |
| `[[concepts/llm-evaluation]]` | [[domains/Engineering]] |
| `[[concepts/llm-as-judge]]` | [[domains/Engineering]] |
| `[[concepts/benchmark-contamination]]` | [[domains/Engineering]] |
| `[[concepts/data-deduplication]]` | [[domains/Engineering]], [[domains/Training]] |
| `[[concepts/data-quality-filtering]]` | [[domains/Engineering]] |
| `[[concepts/data-flywheel]]` | [[domains/Engineering]] |
| `[[concepts/few-shot-prompting]]` | [[domains/Engineering]] |
| `[[concepts/system-prompt-design]]` | [[domains/Engineering]] |
| `[[concepts/prompt-injection]]` | [[domains/Engineering]] |
| `[[concepts/post-training-quantization]]` | [[domains/Inference]] |
| `[[concepts/gptq]]` | [[domains/Inference]] |
| `[[concepts/awq]]` | [[domains/Inference]] |
| `[[concepts/kv-cache]]` | [[domains/Inference]] |
| `[[concepts/paged-attention]]` | [[domains/Inference]] |
| `[[concepts/speculative-decoding]]` | [[domains/Inference]] |
| `[[concepts/continuous-batching]]` | [[domains/Inference]] |
| `[[concepts/clip]]` | [[domains/Multimodal]] |
| `[[concepts/visual-instruction-tuning]]` | [[domains/Multimodal]] |
| `[[concepts/diffusion-model-basics]]` | [[domains/Multimodal]] |
| `[[concepts/latent-diffusion]]` | [[domains/Multimodal]] |
| `[[concepts/classifier-free-guidance]]` | [[domains/Multimodal]] |
| `[[concepts/causal-language-modeling]]` | [[domains/Training]] |
| `[[concepts/bpe-tokenization]]` | [[domains/Training]] |
| `[[concepts/scaling-laws]]` | [[domains/Training]] |
| `[[concepts/rlhf]]` | [[domains/Training]] |
| `[[concepts/reward-modeling]]` | [[domains/Training]] |
| `[[concepts/dpo]]` | [[domains/Training]] |
| `[[concepts/constitutional-ai]]` | [[domains/Training]] |
| `[[concepts/lora]]` | [[domains/Training]] |
| `[[concepts/qlora]]` | [[domains/Training]] |
| `[[concepts/peft-comparison]]` | [[domains/Training]] |
| `[[concepts/zero-redundancy-optimizer]]` | [[domains/Training]] |
| `[[concepts/tensor-parallelism]]` | [[domains/Training]] |
| `[[concepts/matrix-multiplication]]` | [[domains/Foundations]] |
| `[[concepts/svd]]` | [[domains/Foundations]] |
| `[[concepts/eigendecomposition]]` | [[domains/Foundations]] |
| `[[concepts/bayes-theorem]]` | [[domains/Foundations]] |
| `[[concepts/maximum-likelihood-estimation]]` | [[domains/Foundations]] |
| `[[concepts/gaussian-distribution]]` | [[domains/Foundations]] |
| `[[concepts/entropy]]` | [[domains/Foundations]] |
| `[[concepts/cross-entropy-loss]]` | [[domains/Foundations]] |
| `[[concepts/kl-divergence]]` | [[domains/Foundations]] |
| `[[concepts/gradient-descent]]` | [[domains/Foundations]] |
| `[[concepts/adam-optimizer]]` | [[domains/Foundations]] |
| `[[concepts/learning-rate-schedule]]` | [[domains/Foundations]] |

### entities/* 死链 (9 unique targets)

| 死链目标 | 来源文件 |
|----------|----------|
| `[[entities/attention-is-all-you-need]]` | [[domains/Architecture]] |
| `[[entities/bert]]` | [[domains/Architecture]] |
| `[[entities/gpt-series]]` | [[domains/Architecture]] |
| `[[entities/vllm]]` | [[domains/Engineering]], [[domains/Inference]] |
| `[[entities/wandb]]` | [[domains/Engineering]] |
| `[[entities/ollama]]` | [[domains/Inference]] |
| `[[entities/stable-diffusion]]` | [[domains/Multimodal]] |
| `[[entities/whisper]]` | [[domains/Multimodal]] |

**建议**: 这些死链是 vault 设计的"知识地图骨架"，代表待 ingest 的概念。不建议删除链接，而应通过逐步 ingest 来填充页面。优先级见 [[dashboard]] 的 Ingest 计划。

---

## Frontmatter Gaps — 🟡 MEDIUM

### 无 Frontmatter 的页面 (11 个)

| 页面 | 类型 | 建议 |
|------|------|------|
| `wiki/hot.md` | 系统缓存 | 可豁免——系统自动维护文件 |
| `wiki/index.md` | 导航目录 | 可豁免——系统自动维护文件 |
| `wiki/log.md` | 操作日志 | 可豁免——追加式日志文件 |
| `wiki/overview.md` | 全局知识地图 | 建议添加: type:meta |
| `wiki/concepts/concepts-idx.md` | MoC 索引 | 建议添加: type:meta |
| `wiki/entities/entities-idx.md` | MoC 索引 | 建议添加: type:meta |
| `wiki/insights/insights-idx.md` | MoC 索引 | 建议添加: type:meta |
| `wiki/operations/operations-idx.md` | MoC 索引 | 建议添加: type:meta |
| `wiki/meta/contradiction-register.md` | 矛盾登记 | 建议添加: type:meta |
| `wiki/meta/dashboard.md` | 操作看板 | 建议添加: type:meta |
| `wiki/meta/SYSTEM-STATUS.md` | 系统状态 | 建议添加: type:meta |

### Frontmatter 不完整的页面 (2 个)

| 页面 | 缺失字段 |
|------|----------|
| `wiki/getting-started.md` | `created` |
| `wiki/domains/domains-idx.md` | `created` |

**建议**: `hot.md`/`index.md`/`log.md` 为系统文件，可豁免 frontmatter 要求。其余 8 个页面建议在下次 lint 前补全 frontmatter。

---

## Orphan Pages — 🟢 LOW (9 pages)

以下页面没有任何其他页面通过 wikilink 引用它们（meta 模板占位符不算）:

| 孤儿页面 | 原因 | 建议 |
|----------|------|------|
| `wiki/getting-started.md` | 入门指南，未被引用 | 从 [[overview]] 或 [[hot]] 链接到此页 |
| `wiki/concepts/concepts-idx.md` | MoC 索引 | 正常——MoC 由 Dataview 自动聚合 |
| `wiki/entities/entities-idx.md` | MoC 索引 | 正常——MoC 由 Dataview 自动聚合 |
| `wiki/insights/insights-idx.md` | MoC 索引 | 正常——MoC 由 Dataview 自动聚合 |
| `wiki/operations/operations-idx.md` | MoC 索引 | 正常——MoC 由 Dataview 自动聚合 |
| `wiki/meta/contradiction-register.md` | 矛盾登记册 | 从 [[overview]] 链接 |
| `wiki/meta/dashboard.md` | 操作看板 | 从 [[overview]] 链接 |
| `wiki/meta/delta-register.md` | 信息差记录 | 从 [[overview]] 链接 |
| `wiki/meta/SYSTEM-STATUS.md` | 系统状态 | 从 [[overview]] 链接 |

**说明**: `idx.md` 页面作为 Dataview MoC 自动生成入口，不强制要求被引用。其余 5 个页面建议从 overview.md 或 getting-started.md 建立入口链接。

---

## Empty Content Stubs — 🟢 LOW (4 pages)

以下 `idx.md` 页面仅含格式模板，无实际内容:

| 页面 | 说明 |
|------|------|
| `wiki/concepts/concepts-idx.md` | 空壳——等待 ingest 填充 |
| `wiki/entities/entities-idx.md` | 空壳——等待 ingest 填充 |
| `wiki/insights/insights-idx.md` | 空壳——等待 ingest 填充 |
| `wiki/operations/operations-idx.md` | 空壳——等待 ingest 填充 |

**说明**: 这是 vault 初始化的正常状态。首次 ingest 后这些页面将自动填充。

---

## Stale Index Entries — ✅ NONE

`wiki/index.md` 中所有条目均指向存在的页面或标记为"待 ingest 填充"。无过期条目。

---

## Naming Conventions — ✅ PASS

所有文件名符合命名规范:
- 领域页: Title Case (`Agents.md`, `Alignment.md`)
- 目录: lowercase (`concepts/`, `domains/`, `meta/`)
- 索引页: `idx.md`

---

## Address Validation — ⏭️ SKIPPED

DragonScale 未激活（`scripts/allocate-address.sh` 不存在）。跳过地址验证。

---

## Semantic Tiling — ⏭️ SKIPPED

`scripts/tiling-check.py` 不存在或 ollama 未运行。跳过语义去重检查。

---

## 行动建议（按优先级）

### 🔴 P0 — 立即行动
1. **开始首次 ingest** — 推荐从 Attention Is All You Need 开始，可一次性解决 10+ 死链
2. **补全 getting-started.md 和 domains/domains-idx.md 的 `created` 字段**（2 分钟）

### 🟡 P1 — 本周完成
3. **为 8 个无 frontmatter 的非系统页面添加 frontmatter**（overview + 4 个 idx + 3 个 meta）
4. **在 overview.md 中添加对 getting-started.md 和 meta 页面的入口链接**

### 🟢 P2 — 持续改进
5. 持续 ingest 以减少死链计数
6. 每 10-15 次 ingest 后重新 lint
7. 达到 20+ 节点后激活 semantic tiling

---

*Lint 执行时间: 2026-06-13 | AI Vault v2.0 | 下次 lint 建议: 首次 ingest 完成后*
