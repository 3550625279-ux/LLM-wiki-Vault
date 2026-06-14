---
type: concept
title: "域外检测（Out-of-Scope Detection）"
created: 2026-06-14
updated: 2026-06-14
tags: [OOS检测, 开放集识别, 意图检测, TODS]
status: seed
complexity: intermediate
domain: Agents
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Agents]]"
  - "part_of::[[concepts/intent-detection-tods]]"
  - "applied_in::[[concepts/uncertainty-routing]]"
  - "extends::[[concepts/monte-carlo-dropout]]"
  - "contrasts::[[concepts/setfit]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 域外检测（Out-of-Scope Detection）

## 定义

OOS 检测是识别不属于系统任何已知意图的查询的能力。由于 OOS 查询空间是无限的，系统无法通过枚举 OOS 样本来训练——这是一个根本性挑战。

```
已知意图: [查订单, 退货, 商品推荐, ...]
OOS 查询: "今天天气怎么样" / "给我讲个笑话" / "帮我写首诗"
→ 这些查询不属于任何已知意图，应被拒绝
```

## LLM 的 OOS 软肋

来自 EMNLP 2024 的控制实验揭示了两个关键弱点：

### 1. 意图标签范围（Scope）的影响

| 意图范围 S | OOS AUCROC 变化 |
|-----------|----------------|
| S=1（最细） | 最高 |
| S=5（最宽） | 显著下降 |

**原因**：标签覆盖范围越宽，LLM 越倾向于把查询"往里塞"（匹配宽泛意图），而不是判断为 OOS。

### 2. 标签空间大小（Label Space Size）的影响

| 标签数 L | OOS AUCROC 变化 |
|---------|----------------|
| L=1 | 最高 |
| L=5 | 下降 0.3+ |

**原因**：标签越多，LLM 越难对查询说"不知道"。

### 对比：SetFit 更稳定

SetFit 在两个因素变化时都更平稳，说明传统模型对 class design 的鲁棒性更好。

## 改进方法

| 方法 | 核心思路 | 效果 |
|------|---------|------|
| **负面数据增强** | 生成"残缺"训练样本标记为 OOS | F1 +5% |
| **两步内部表示法** | 先预测 in-scope → 再用隐藏状态判断 OOS | OOS Recall +50%+ |
| **微调 LLM** | 直接训练 LLM 识别 OOS | 有效但成本高 |
| **不确定性路由** | MC Dropout 方差决定是否拒绝 | 间接改善 |

## 与相关概念的关系

- 是 [[concepts/intent-detection-tods]] 的核心子任务
- [[concepts/uncertainty-routing]] 通过混合系统间接改善 OOS
- [[concepts/negative-data-augmentation]] 直接增强 OOS 训练信号
- [[concepts/monte-carlo-dropout]] 提供 OOS 不确定性估计的理论基础
