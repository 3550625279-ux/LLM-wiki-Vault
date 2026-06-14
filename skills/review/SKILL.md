---
name: review
description: >
  间隔复习 + 主动回忆协议。基于认知科学（间隔效应 + 测试效应 + 生成效应），
  从 wiki 中提取知识节点，生成个性化回忆测试，评估掌握程度，
  标记薄弱节点并推荐 ingest 方向。
  触发词: review, 复习, 间隔复习, quiz me, 主动回忆, test me,
  recall, 考我, 测试我的理解, spaced repetition, flashcard.
allowed-tools: Read Write Edit Glob Grep
---

# review — 间隔复习 + 主动回忆 Skill

> **核心认知科学原理**：
> - 测试效应：主动回忆比被动阅读记忆效果提升 50-100%
> - 间隔效应：分散复习比集中复习保持率高 2-3x
> - 生成效应：自己生成答案比被动看答案效果好 3x
>
> 本 skill 的核心：**不是展示你知道什么，而是检测你能否从记忆中提取**。

---

## 触发模式

| 触发词 | 模式 |
|--------|------|
| `review` / `复习` | 标准（自动推断最应复习的领域）|
| `review: Attention` | 定向（指定主题）|
| `quiz me` / `考我` | 纯测试（逐题，等待回答）|
| `review hot` | 仅复习 hot.md 中的活跃节点 |
| `review seeds` | 复习所有 status=seed 薄弱节点 |
| `review contradictions` | 专项复习矛盾节点 |
| `review browse: 架构` | 浏览模式（不测试，仅看知识地图）|

---

## 复习流程（6步）

### Step 1 — 读取状态

```
并行读取：
- wiki/hot.md（最近学习重心）
- log.md 最近5条（最近 ingest 内容）
- wiki/meta/contradiction-register.md（矛盾节点）
- wiki/concepts-idx.md 中目标领域节点列表
```

### Step 2 — 节点选择（间隔复习算法）

**优先级** = 节点重要性 × 遗忘风险 / 最近接触距离

**重要性代理**：被 `depends_on::` 引用次数 + status级别 + sources数量

**遗忘风险代理**：
- status=seed（未经强化）
- 未在最近5条 log.md 中出现
- 出现在 contradiction-register

**接触距离**：
- 在 hot.md 中出现 → 跳过
- 未在最近5条 log 中 → 优先

**选取规则（3-7个节点）**：
```
- 至少1个 status=seed（薄弱节点）
- 至少1个被最多 depends_on 引用的核心概念
- 若有矛盾节点 → 必选1个
- 强制跨≥2个领域（交错练习原则）
```

### Step 3 — 读取节点内容（≤7页）

```
从每页提取：
- 核心定义（第一段或 > 符号块）
- 关键属性/公式/代码片段
- related: 字段语义边
- status 和 sources
```

### Step 4 — 生成测试题

**关键规则：每次只展示一题，等待用户回答后再展示下一题**

```
---
📚 第[N]题 / 共[M]题 — [概念名] ([领域])
类型: [概念定义 | 关系辨析 | 应用场景 | 对比分析 | 代码推演 | 前置关系]
---

[问题正文]

> 请输入你的答案，我会给出参考答案和评估。
```

**6种题型及认知原则**：

| 题型 | 示例 | 认知原则 |
|------|------|----------|
| 概念定义 | "用自己的话解释 Attention 机制" | 生成效应 |
| 关系辨析 | "LoRA 和 QLoRA 的区别是什么？" | 精细追问 |
| 应用场景 | "什么情况下用 MoE 而不用 Dense？" | 迁移学习 |
| 对比分析 | "Transformer 和 Mamba 对比哪些维度？" | 交错练习 |
| 代码推演 | "这段代码实现了哪个算法？有什么问题？" | 生成效应 |
| 前置关系 | "学习 Transformer 前必须掌握哪些概念？" | 依赖图遍历 |

### Step 5 — 评估与标注

```
用户回答后：
1. 对比 wiki 参考内容
2. 评级：
   ✅ 掌握     — 准确，覆盖核心要点
   🔄 部分掌握 — 方向对但有重要遗漏
   ❌ 需强化   — 不准确或空白
3. 展示参考答案（来自 wiki 页面内容）
4. 若❌ → 标记节点需 re-ingest 或补充资料
5. 若答案与 wiki 有 corrects:: 关系 → 标注矛盾
```

### Step 6 — 复习报告 + 写回

全部测题完成后输出报告，并**自动写回**：

```markdown
## 复习报告 [YYYY-MM-DD]

测试: N个节点 | ✅ X | 🔄 Y | ❌ Z

### 🔴 需重点关注（❌节点）
| 节点 | 问题描述 | 建议行动 |
|------|----------|----------|
| [[概念X]] | 混淆了A和B | ingest: [推荐资料] |

### 🟡 需补充来源（seed节点）
| 节点 | 当前状态 | 建议 |
|------|----------|------|
| [[概念Y]] | seed，1来源 | 增加第二个视角 |

### 建议复习间隔
- 立即: [Z个❌节点]
- 3天后: [Y个🔄节点]
- 1周后: [X个✅节点]
```

**自动写回 wiki**：
```
1. 追加 log.md：
   ## [YYYY-MM-DD HH:MM] review | [主题]
   - nodes_tested: N
   - score: X/N
   - weak_nodes: [列表]

2. ❌节点 frontmatter 更新：
   review_status: needs_reinforcement
   last_reviewed: YYYY-MM-DD

3. ❌节点加入 wiki/hot.md 的"当前学习重心"
```

---

## 认知科学依据

| 原则 | 效果 | 在本 Skill 的应用 |
|------|------|-------------------|
| 测试效应 (Testing Effect) | 记忆提升 50-100% | 所有题型要求主动回答 |
| 间隔效应 (Spacing Effect) | 保持率高 2-3x | 按遗忘风险排序选题 |
| 生成效应 (Generation Effect) | 记忆深度 +3x | "用自己的话"类题型 |
| 精细追问 (Elaborative Interrogation) | 理解深度 +40% | 关系辨析 + 对比分析 |
| 交错练习 (Interleaving) | 迁移能力 +30% | 强制跨领域选题 |
| 反馈效应 (Feedback Effect) | 错误修正效率 +50% | 立即展示参考答案 |
