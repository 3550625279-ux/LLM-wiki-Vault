---
type: concept
title: "负面数据增强（Negative Data Augmentation）"
created: 2026-06-14
updated: 2026-06-14
tags: [数据增强, OOS检测, 关键词提取, 训练技巧]
status: seed
complexity: basic
domain: Training
sources: ["[[sources/intent-detection-age-of-llms]]"]
related:
  - "belongs_to::[[domains/Training]]"
  - "improves::[[concepts/setfit]]"
  - "improves::[[concepts/out-of-scope-detection]]"
  - "applied_in::[[concepts/intent-detection-tods]]"
  - "produced_by::[[sources/intent-detection-age-of-llms]]"
thumbnail: ""
---

# 负面数据增强（Negative Data Augmentation）

## 🔗 关系链接

- belongs_to: [[domains/Training]]
- improves: [[concepts/setfit]] | [[concepts/out-of-scope-detection]]
- applied_in: [[concepts/intent-detection-tods]]
- produced_by: [[sources/intent-detection-age-of-llms]]

---

## 定义

负面数据增强是一种通过生成"看似合理但实际上是域外"的训练样本来增强模型 OOS 检测能力的方法。核心思路：**破坏原始句子的关键词，使残缺版本成为 OOS 样本**。

## 算法

```
输入: 训练集 D
输出: 增强后的训练集 D'

1. 对每个训练样本 x ∈ D:
   a. 用 KeyBERT 提取关键词 K = {k1, k2, ..., kn}
   b. 对每个关键词 ki:
      - 50% 概率: 完全删除 ki
      - 50% 概率: 替换为 5 字符随机字符串
   c. 生成增强样本 x_aug
   d. 标记 x_aug 为 OOS

2. 采样 |U| = 0.2 × |D| 个增强样本加入训练集
```

## 示例

```
原始:   "looking for a gaming laptop"
         ↓ KeyBERT 提取关键词: [gaming, laptop]
增强 1: "looking for a"              → OOS（删除）
增强 2: "looking for a XYCVD QSDER"  → OOS（替换为随机串）
增强 3: "looking for a RTYUH"        → OOS（替换为随机串）
```

## 为什么有效

1. **相似词汇模式**：增强样本保留了原始句子的句法结构和非关键词，迫使模型不能仅靠关键词匹配
2. **学习鲁棒边界**：模型被迫学习语义级别的区分能力
3. **低成本高收益**：几乎零额外成本（只需 KeyBERT 提取），F1 提升 >5%

## 效果（SetFit 模型）

| 指标 | SetFit 基线 | SetFit + 负面增强 | 提升 |
|------|-----------|-----------------|------|
| 平均 F1 | 0.600 | 0.658 | +9.7% |
| OOS Recall | 0.378 | 0.489 | +29.4% |

## 实现细节

- **关键词提取**：KeyBERT（基于 BERT 的关键词提取）
- **增强比例**：|U| = 0.2 × |D|（增强样本数为原始训练集的 20%）
- **变换比例**：50% 删除 + 50% 替换为 5 字符随机串

## 局限

1. 生成的 OOS 样本（残缺查询）与真实 OOS 分布差异大
2. 短查询场景效果有限（删完关键词可能变空句）
3. KeyBERT 的关键词提取质量直接影响效果
4. 模型可能学到"识别残缺句子"而非"真正的 OOS 语义"

## 来源

- 实现: [[sources/intent-detection-age-of-llms]] Section 3.1.1
- 工具: KeyBERT (Grootendorst, 2020)
