# Wiki Dashboard — 操作看板

> 实时操作中心。每次 lint 或重大 ingest 后更新。

---

## 🚦 系统状态

```
系统版本:   AI Vault v2.0
初始化:     2026-06-13
最近会话:   2026-06-16 (LLM推理能力后训练技术栈 ingest)
健康状态:   🟢 活跃，6 次 ingest + 1 次修复完成
总节点数:   58 (concept: 38, source: 7, insight: 5, comparison: 2, question: 2, entity: 2, operation: 1)
领域覆盖:   8/8 (Foundations, Architecture, Training, Alignment, Multimodal, Agents, Engineering, Inference) ✅ 全覆盖
死链数:     待重跑 lint 确认
孤儿页:     待重跑 lint 确认
Frontmatter 缺失: 待重跑 lint 确认
```

---

## 📋 待办队列

| 优先级  | 任务                    | 类型     | 状态    |
| ---- | --------------------- | ------ | ----- |
| 🔴 高 | 完成首次 ingest           | ingest | ✅ 已完成 |
| 🔴 高 | 建立 Foundations 核心节点   | ingest | ✅ 已完成 (hyperbolic-geometry) |
| 🔴 高 | 建立 Architecture 核心节点  | ingest | ✅ 已完成 (hyperbolic-geometry-llm, CAT) |
| 🔴 高 | ingest CAGC (CVPR 2024)    | ingest | ✅ 已完成 (4 concept + 1 comparison) |
| 🔴 高 | ingest Intent Detection (EMNLP 2024) | ingest | ✅ 已完成 (7 concept + 1 insight) |
| 🔴 高 | 系统健康修复 — 全层一致性校验 | lint | ✅ 已完成 |
| 🟡 中 | MinerU MCP 调试 ingest | ingest | ✅ 已完成 |
| 🟡 中 | 终端/PATH/Conda 基础 ingest | ingest | ✅ 已完成 |
| 🟡 中 | 首次 `align all` 生成基线报告 | align  | ⬜ 待执行 |
| 🟡 中 | 首次 `review` 测试记忆效果    | review | ⬜ 待执行 |
| 🟢 低 | 激活 mcpvault（BM25检索升级） | 配置     | ⬜ 待执行 |
| 🟢 低 | 配置 flux Token（概念图像生成） | 配置     | ⬜ 待执行 |
| 🟡 中 | 重跑 lint 获取最新健康指标      | lint     | ⬜ 待执行 |

---

## 📊 本周 Ingest 计划

```
目标: 3-5篇核心资料
已完成:
  ✅ HypLoRA (NeurIPS 2025) — 双曲低秩适配
  ✅ CAGC (CVPR 2024) — 多模态意图识别 + 全局对比学习
  ✅ LLM推理能力后训练技术栈（小红书番茄算法日记，16张图文）— SFT→RLHF→PRM→GRPO完整技术栈
推荐下一步:
  □ Attention Is All You Need (2017)
  □ LoRA: Low-Rank Adaptation (2021)
  □ Chinchilla Scaling Laws (2022)
  □ 一篇 Agent 综述 (2024)
  □ DPO: Direct Preference Optimization (2023)
```

---

## 🔁 复习调度

```
下次复习: 首次 ingest 完成后 3天
当前待复习节点: 0
高优先节点: 无
```

---

## ⚠️ 矛盾待解决

*(首次 ingest 后可能产生)*

---

## 📈 月度目标

```
6月目标:
  ✅ 总节点数 > 20 (当前: 43)
  □ Architecture 领域 mature 节点 ≥ 5 (当前: 0 mature, 2 seed)
  □ 完成 1次 align all
  □ 完成 3次 review

当前进度: 2/4
```

---

*AI Vault v2.0 | dashboard | 2026-06-16 | 自动更新 by ingest*
