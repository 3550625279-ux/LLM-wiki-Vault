---
name: flux-illustrate
description: "为 concept/source 页面生成 Flux 概念插画（交互式工作流）"
triggers:
  - "flux-illustrate"
  - "生成插画"
  - "生成概念图"
  - "illustrate"
---

# Flux Illustrate — 概念插画生成 Skill

> 为人机协作的交互式工作流，为 concept 和 source 页面生成高质量概念插画。

---

## 触发条件

当 `PostToolUse(Write)` hook 检测到文件写入时自动触发，也可手动调用 `/flux-illustrate`。

**必要条件**（全部满足才继续）：
1. 写入路径在 `wiki/concepts/` 或 `wiki/sources/`
2. 文件 frontmatter 中 `type` 为 `concept` 或 `source`
3. 文件 frontmatter 中 `thumbnail` 字段不存在或为空

---

## 工作流（5 步）

### Step 1: 询问用户

读取刚写入的页面，向用户确认：

```
要为「{页面标题}」生成概念插画吗？
- 当前 status: {status}
- 页面类型: {type}
```

- 用户说 **Yes** → 进入 Step 2
- 用户说 **No** → 结束，不生成

### Step 2: 推荐可视化方向

读取页面全文内容（标题、定义、关系、关键信息），分析内容结构，推荐 **2-3 个最匹配的方向**：

| 方向 | 适用场景 | 关键词线索 |
|------|---------|-----------|
| 🔀 流程图 (flowchart) | 步骤、阶段、调用链、生命周期 | "流程"、"阶段"、"步骤"、"调用"、序列 |
| 🏗️ 架构图 (architecture) | 层次、组件、系统结构、协议栈 | "架构"、"层"、"组件"、"模块"、"协议" |
| ⚖️ 对比图 (comparison) | 两个事物的异同 | "对比"、"区别"、"vs"、"比较" |
| 🕸️ 知识图谱 (knowledge graph) | 多概念的关联网络 | "关系"、"依赖"、"属于"、"影响" |
| 🎨 示意图 (illustration) | 抽象概念的具象化 | 抽象定义、难以结构化 |

每个方向附上 **1-2 句推荐理由**，说明为什么适合当前页面。

用户选择一个方向 → 进入 Step 3。

### Step 3: 设计 Prompt（循环，上限 3 次）

基于 **页面内容 + 选定方向**，自由设计详细的英文 prompt。

**Prompt 设计规范**：
- 全英文（避免 AI 绘图文字乱码）
- 白色背景 (white background)
- 扁平设计 (flat design, no gradients, no 3D)
- 包含具体的内容元素（图标、标签、流程、组件名称）
- 风格: clean vector, educational diagram, professional

**展示给用户**：
```
选定方向: {方向名}
建议模型: flux-2-max
建议尺寸: 16:9

Prompt:
{完整 prompt 全文}

这个 prompt 可以吗？
```

**用户反馈处理**：
- **"通过" / "可以"** → 进入 Step 4
- **"不好，因为 {原因}"** → 根据反馈重新设计 prompt（保持同一方向），回到展示
- **第 3 次仍不满意** → 询问："要不要换一个方向试试？"
  - 换方向 → 回到 Step 2
  - 不换 → 终止，不生成

### Step 4: 生成 + 下载

```
1. 调用 flux_generate_image:
   - prompt: {用户确认的 prompt}
   - model: flux-2-max
   - size: 16:9

2. 轮询 flux_get_task / flux_get_tasks_batch 直到完成

3. 下载到 Vault:
   curl -sfo "_attachments/assets/{slug}.png" "{image_url}"

4. 验证文件完整性（检查文件大小 > 0）

5. 向用户展示生成结果:
   ![[{slug}.png]]
```

### Step 5: 整合到页面

```
1. 更新 frontmatter:
   - status: 若为 seed → 改为 developing
   - 添加 thumbnail: "_attachments/assets/{slug}.png"

2. 正文嵌入:
   在标题下方（frontmatter 结束后第一行）插入:
   ![[{slug}.png]]

3. 更新 log.md:
   追加记录:
   ## [YYYY-MM-DD HH:MM] flux-illustrate | {页面标题}
   - target: [[{页面路径}]]
   - image: _attachments/assets/{slug}.png
   - model: flux-2-max

4. 输出确认:
   "✅ 插画已生成并整合到 [[{页面路径}]]"
```

---

## 参数规范

| 参数 | 值 | 说明 |
|------|-----|------|
| model | `flux-2-max` | 最高质量（经实测最佳） |
| size | `16:9` | 横版标准比例（超宽/超高会导致裁切） |
| 语言 | 全英文 | 避免中文乱码 |
| 下载路径 | `_attachments/assets/{slug}.png` | slug 取自页面文件名（不含 .md） |

---

## Flux 可用模型参考

| 模型 | 定位 | 使用场景 |
|------|------|---------|
| `flux-dev` | 快速测试 | 草稿 |
| `flux-pro` | 生产级 | 正式内容 |
| `flux-2-flex` | 灵活版 | 兼顾速度质量 |
| `flux-2-pro` | 高质量 | 备选 |
| `flux-2-max` | **最高质量** | **默认使用** |
| `flux-kontext-pro/max` | 编辑已有图片 | 非生成场景 |

---

## 与 Ingest 的协调

- Ingest 在 Phase 3 (INTEGRATE) 写入 concept/source 页面时，PostToolUse hook 自动触发本 Skill
- 本 Skill 的交互流程（Step 1-5）在 ingest 主流程中**暂停执行**，完成后再继续 ingest 后续步骤
- 不需要手动调用，hook 会自动检测并注入指令
