---
name: align
description: >
  精准对齐信息差。无需 query MCP，通过 Index-First Traversal + grep-based 检索，
  快速定位知识缺口、矛盾点、已知边界。生成结构化对齐报告，自动创建 gap 页面。
  触发词: align, 对齐, 我知道多少, check my understanding, what gaps,
  knowledge gap, 信息差, 我对X了解多少, audit my knowledge, where am I on X.
allowed-tools: Read Write Edit Glob Grep Bash
---

# align — 精准知识对齐 Skill

> 对齐 ≠ 查询。查询是"告诉我 X 是什么"。
> 对齐是"告诉我我对 X 知道多少，哪里有空白，哪里有错误"。

---

## 触发条件

| 输入形式 | 示例 |
|----------|------|
| 显式对齐 | `align: Transformer` |
| 知识审计 | `我对 LoRA 了解多少？` |
| 缺口检测 | `Alignment 领域我有哪些空白？` |
| 矛盾检查 | `我关于 RNN 的认知有没有过时？` |
| 学习路径 | `我下一步该学什么？` |
| 全库审计 | `align all` |

---

## 对齐流程（4步，严格顺序）

### Step 1 — 热缓存扫描（< 5秒）

```
读取 wiki/hot.md
扫描关键词匹配：查询主题 ∩ hot.md 内容

若匹配度 > 70%：
  → 从 hot.md 直接提取已知内容 → 跳到 Step 4（快速模式）

若匹配度 < 70%：
  → 标记"不在热缓存" → 继续 Step 2
```

### Step 2 — Index 导航（精准定位）

```
读取 wiki/index.md

搜索策略：
  a) 查询主题精确标题匹配
  b) 所属领域全部页面
  c) related: 字段中包含查询主题的页面

输出：候选页面列表（≤8页）

若 index 无匹配 → grep 兜底：
  bash scripts/align-check.sh "查询关键词"
若 grep 也无结果 → 确认为知识缺口
```

### Step 3 — 精准读取（≤5页）

```
读取候选页面，提取：
  ① related: 字段中所有语义边
  ② corrects:: 关系（旧认知被修正的信号）
  ③ depends_on:: 关系（前置条件链）
  ④ status（seed=不成熟，mature=可信）
  ⑤ sources 数量（代理置信度）

构建知识快照：
  K = 已知节点集合
  D = depends_on 但 wiki 中无页的缺失节点
  C = corrects:: 边涉及的矛盾节点对
  U = status=seed 的薄弱节点
```

### Step 4 — 输出对齐报告

```markdown
## 对齐报告: [主题]  [YYYY-MM-DD]

覆盖度估算: X% | 检索路径: hot→index→N页→M条语义边

### ✅ 已知（wiki 有支撑）
| 概念 | 状态 | 来源数 | 置信度 |
|------|------|--------|--------|
| [[概念1]] | mature | 3 | 高 |
| [[概念2]] | seed | 1 | 低（需补充） |

### 🔄 认知需更新（corrects:: 关系）
| 旧认知 | 新认知 | 来源 |
|--------|--------|------|
| [[旧页]] — "旧说法" | [[新页]] — "新说法" | [[source]] |

### ❓ 知识缺口
| 缺失概念 | 重要性 | 原因 |
|----------|--------|------|
| 概念X | 高（被3页 depends_on） | index无记录 |

推荐行动:
1. ingest: [具体资料]
2. autoresearch: "概念X"

### 🗺️ 学习路径
已掌握: [[A]] → [[B]]
下一站: [[C]] (依赖 [[B]] ✅)
```

---

## 副作用（自动执行）

### 创建 Gap 页面
发现知识缺口时，自动创建 `wiki/questions/gap-[slug]-YYYY-MM-DD.md`：

```yaml
---
type: question
subtype: knowledge-gap
title: "Gap: [缺失概念]"
created: YYYY-MM-DD
status: open
priority: high | medium | low
domain: 所属领域
related:
  - "needed_by::[[依赖此概念的页面]]"
  - "part_of::[[所属领域页]]"
---

# Gap: [缺失概念]

## 为什么重要
[依赖关系说明]

## 推荐学习资源
- [ ] [论文/博客/视频]

## 前置知识检查
- [x] [[已掌握的前置]]
- [ ] [[尚未掌握的前置]]
```

### 更新 Contradiction Register
发现 corrects:: 矛盾 → 追加 `wiki/meta/contradiction-register.md`

### 更新 hot.md
对齐完成后，将缺口摘要写入 hot.md 的"活跃线索"部分。

---

## 模式选项

| 模式 | 触发 | 说明 |
|------|------|------|
| 快速 | `align quick: X` | Step 1 only，3-5行摘要 |
| 标准 | `align: X` | Steps 1-4，完整报告 |
| 深度 | `align deep: X` | Steps 1-4 + autoresearch 填充缺口 |
| 全库 | `align all` | 所有领域，月度审计报告 |

---

## 全库对齐（月度审计）

触发：`align all` / `全库对齐` / `月度审计`

```
1. 读取 wiki/domains/domains-idx.md（8个领域列表）
2. 对每个领域执行 Step 2-3
3. 计算全库覆盖度热力图
4. 输出综合审计报告：wiki/meta/audit-YYYY-MM-DD.md
5. 按缺口大小排序，推荐 ingest 优先级
```

---

## 无 MCP 情况下的检索优先级

```
hot.md (< 3秒)
  ↓ 未命中
wiki/index.md (< 5秒)
  ↓ 未命中
scripts/align-check.sh grep (< 10秒)
  ↓ 未命中
wiki/domains/<domain>.md（领域综述兜底）
  ↓ 未命中
确认为知识缺口 → 创建 gap 页面
```

此顺序在无向量数据库的情况下覆盖 95%+ 对齐场景。
