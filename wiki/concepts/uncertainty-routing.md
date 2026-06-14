---
type: concept
title: "不确定性路由（Uncertainty-based Routing）"
created: 2026-06-14
updated: 2026-06-14
tags: [不确定性路由, 混合系统, MC Dropout, 系统设计]
status: seed
complexity: intermediate
domain: Engineering
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Engineering]]"
  - "depends_on::[[concepts/monte-carlo-dropout]]"
  - "depends_on::[[concepts/setfit]]"
  - "extends::[[concepts/adaptive-in-context-learning]]"
  - "applied_in::[[concepts/intent-detection-tods]]"
  - "improves::[[concepts/out-of-scope-detection]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 不确定性路由（Uncertainty-based Routing）

## 定义

不确定性路由是一种混合系统设计模式：**轻量模型做"快速通道"，重量级模型做"精确后备"**。通过估计轻量模型的预测不确定性，仅在不确定时才调用重量级模型，从而在准确率和延迟/成本之间取得平衡。

## 通用模式

```
┌─────────────────────────────────────────────┐
│  用户输入 → 轻量模型（低延迟）               │
│                 ↓                            │
│           不确定性估计                        │
│           ├── 确定 → 返回轻量模型结果（快）   │
│           └── 不确定 → 调用重量模型（准）     │
└─────────────────────────────────────────────┘
```

## 在意图检测中的具体实现

### 路由信号：MC Dropout 方差

1. SetFit 开启 Dropout（p=0.1），对查询做 M 次前向传播
2. 统计 M 次预测中不同标签数（unique_labels）
3. 判定规则：
   - `unique_labels > 1` → 不确定（预测不一致）
   - `unique_labels < M/2` → 不确定（预测过于集中但可能是错的）
   - 否则 → 确定

### 效果（M=10）

| 方案 | F1 | 延迟 | vs 纯 LLM |
|------|-----|------|-----------|
| 纯 LLM (Haiku) | 0.736 | 2.345s | 基准 |
| 混合系统 | 0.696 | 1.005s | F1 -4%, 延迟 -57% |
| 纯 LLM (Mistral-L) | 0.735 | 3.867s | 基准 |
| 混合系统 | 0.696 | 1.453s | F1 -4%, 延迟 -62% |

### M 的选择

| M | F1 提升（vs M=5） | 延迟增加 |
|---|-------------------|---------|
| 5 | 基准 | 基准 |
| 10 | +1.6% | +35% |
| 20 | +0.1%（边际） | +100% |

**结论**：M=10 是最佳平衡点。

## 可迁移场景

不确定性路由是一个通用模式，可应用于：
- 图像分类（轻量 CNN + Vision Transformer）
- 代码审查（规则检查 + LLM 分析）
- 搜索排序（BM25 + 语义重排序）
- 机器翻译（轻量模型 + 大模型）
- NER（规则 + LLM）

## 设计考虑

1. **延迟分布双峰性**：快路径 ~30ms，慢路径 ~1.7s，p99 远高于 p50
2. **成本不可预测**：路由到 LLM 的比例随查询分布变化
3. **MC 采样可批量**：若 GPU 支持并行，M 次前向传播可批量执行进一步降低延迟
4. **阈值可调**：更保守（少路由 LLM）= 更快但可能丢准确率

## 相关节点

- 不确定性估计基础：[[concepts/monte-carlo-dropout]]
- 快速通道模型：[[concepts/setfit]]
- 慢速通道模型：[[concepts/adaptive-in-context-learning]]
- 来源：[[sources/intent-detection-age-of-llms]]
