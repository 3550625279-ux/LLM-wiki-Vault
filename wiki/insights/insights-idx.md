# Insights Index — 洞察节点目录

> **类型**: Map of Content (MoC)
> **用途**: wiki/insights/ 目录下所有 insight 节点的索引。
> **特征**: 洞察节点是个人认知结晶，对应 Zettelkasten 的 Evergreen Notes。
> **来源**: 从多次 ingest/review 后归纳，不来自单一资料。

---

## 按主题分组

### 关于模型能力与局限
- [[insights/llm-embedding-geometry]] — LLM 嵌入空间具有内在双曲结构 | status:seed

### 关于训练与数据
- [[insights/hyplora-learning-insights]] — HypLoRA 学习心得：双曲适配的工程经验 | status:seed

### 关于工程实践
- [[insights/hybrid-beats-pure-llm]] — 混合系统胜过纯 LLM：不确定性路由的工程启示 | status:seed
- [[insights/when-import-succeeds-but-runtime-fails]] — import 成功 ≠ 能运行：Python 包的安装≠可用陷阱 | status:seed

### 关于通用计算基础
- [[insights/path-search-priority-is-isolation]] — PATH 从前往后搜索 = 环境隔离的核心手段 | status:seed

### 关于研究方法
> *待填充*

### 关于认知偏见与陷阱
- [[insights/when-import-succeeds-but-runtime-fails]] — import 成功 ≠ 能运行（跨列引用，也属于认知陷阱）

---

## 按置信度分组

### 🟢 high confidence (多来源验证)
> *无*

### 🟡 medium confidence (部分验证)
> *无*

### 🔴 speculative (个人推测)
> *无*

---

## 活跃矛盾列表 (需要 insight 节点处理)

以下矛盾已预识别，待积累足够证据后创建 insight 节点处理：

| 矛盾 | 相关节点 | 状态 |
|------|---------|------|
| Scaling Laws 是否能预测涌现 | [[domains/Training\|training]] + [[domains/Alignment\|alignment]] | 待研究 |
| RLHF vs DPO 等效性 | [[domains/Training\|training]] | 待研究 |
| 长上下文 vs RAG | [[domains/Agents\|agents]] + [[domains/Inference\|inference]] | 待研究 |
| 多 Agent vs 单 Agent | [[domains/Agents\|agents]] | 待研究 |

---

## 洞察节点创建触发条件

满足以下任一条件时创建 insight 节点：
1. 同一观点在 3+ 个不同资料中得到印证
2. 发现了反直觉的结论（需记录"反直觉原因"）
3. 修正了之前的错误认知（标记 `corrects::` 边）
4. 总结出可复用的工程经验（"避坑记录"）

---

## 统计

```
总 insight 节点: 5
目标总数:        20+
矛盾待处理:      4 个
上次更新:        2026-06-16
```
