---
type: insight
title: "混合系统胜过纯 LLM：不确定性路由的工程智慧"
created: 2026-06-14
updated: 2026-06-14
tags: [混合系统, 工程洞察, LLM部署, 成本优化]
status: seed
complexity: intermediate
domain: Engineering
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "extends::[[concepts/uncertainty-routing]]"
  - "extends::[[concepts/setfit]]"
  - "corrects::[[insights/llm-embedding-geometry]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 混合系统胜过纯 LLM

## 核心洞察

**不要追求单一"最好"的模型，而是设计一个"最聪明"的系统。**

在工业部署中，LLM 的高延迟和高成本是硬伤。通过不确定性路由（MC Dropout），可以在几乎不损失准确率的情况下将延迟降低 ~50%：

| 方案 | F1 | 延迟 | LLM 调用次数 |
|------|-----|------|-------------|
| 纯 LLM | 0.736 | 2.3s | 100% |
| 混合系统 | 0.696 | 1.0s | ~40% |
| 纯 SetFit | 0.658 | 0.03s | 0% |

**关键数据**：混合系统仅损失 ~4% F1，但延迟降低 ~57%，LLM 调用减少 ~60%。

## 思维转变

| 旧思维 | 新思维 |
|--------|--------|
| LLM vs 微调模型，选一个 | 混合系统，各取所长 |
| 追求模型 SOTA | 追求系统 SOTA |
| 评估看准确率 | 评估看 准确率 × 延迟 × 成本 |

## 更广泛的适用性

这个模式适用于任何"轻量模型快但不够准 + 重量模型准但太慢"的场景：

- **搜索**：BM25 快速召回 + LLM 精排
- **代码审查**：静态分析 + LLM 深度分析
- **图像分类**：轻量 CNN + Vision Transformer
- **机器翻译**：轻量模型 + 大模型后编辑

## 与 CAGC 的对比视角

虽然 [[sources/cagc-cvpr2024]] 解决的是多模态意图识别，但同样面对"如何有效组合不同能力的模型"的问题。CAGC 用 Cross-video Bank 做全局上下文增强，本文用不确定性路由做选择性增强——**共同启示是：智能的组合策略比堆叠模型更重要。**

## 实践建议

1. **先评估后路由**：不要假设 LLM 一定更好，先量化两者的错误模式差异
2. **路由信号选择**：MC Dropout 简单有效，但也可以探索其他信号（logprobs、集成分歧等）
3. **监控路由率**：路由到 LLM 的比例是关键运维指标
4. **阈值可调**：根据业务需求平衡准确率和延迟
