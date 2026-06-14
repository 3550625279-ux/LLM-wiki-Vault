# Wiki Log

> 格式: `## [YYYY-MM-DD HH:MM] verb | Title`
> 动词: `ingest` | `review` | `align` | `query` | `save` | `lint` | `session-end` | `session-start`

---

## [2026-06-13 00:00] session-start | AI Vault v2.0 初始化
- action: vault-init
- files_created: CLAUDE.md, skills/align/SKILL.md, skills/review/SKILL.md
- scripts: align-check.sh, post-session.sh, log-write.sh
- status: system-ready
- note: 首次启动，wiki/ 目录待 ingest 填充


## [2026-06-13 18:38] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 18:50] lint | Wiki 首次健康检查
- action: lint
- pages_scanned: 22
- dead_links: 78 (concepts: 69, entities: 9)
- orphan_pages: 9
- frontmatter_missing: 11
- frontmatter_incomplete: 2
- contradictions: 0
- stale: 0
- report: wiki/meta/lint-report-2026-06-13.md


## [2026-06-14 00:00] ingest | CAGC: Contextual Augmented Global Contrast for Multimodal Intent Recognition
- type: source (论文)
- domain: Multimodal
- venue: CVPR 2024
- pages_created: 5
- pages_updated: 1 (wiki/index.md)
- key_concepts:
  - [[concepts/multimodal-intent-recognition]] — 多模态意图识别任务定义
  - [[concepts/cross-video-bank]] — 跨视频记忆库（两阶段构建）
  - [[concepts/context-augmented-transformer]] — CAT 渐进式注意力
  - [[concepts/global-context-guided-contrastive-learning]] — GCCL 全局对比学习
- study_materials: raw/papers/cagc-multimodal-intent/
  - README.md, summary.md, method.md, insights.md
  - qa.md (15题), mental-model.md, reflection.md
  - code/cross_video_bank_demo.py, index.html
- contradictions: 无
- note: 跳过论文图片提取（PDF 结构限制）


## [2026-06-14 00:10] ingest | CAGC 领域关联补全
- action: fix-domain-links
- Architecture.md: 新增"注意力机制扩展"子分类，加入 CAT
- Multimodal.md: 已在上一步更新（多模态意图/情感分析子分类）
- 新建 wiki/comparisons/cagc-vs-baselines.md — 相关工作对比 (MAG-BERT/MulT/MISA/ConFEDE)
- 补全 concept 页 contrasts 关系边（CAT、Bank、GCCL → comparisons）
- wiki/index.md: 新增 comparison 节点，统计更新 (15→16)
- domains_covered: Multimodal, Architecture
- related_work_linked: MAG-BERT, MulT, MISA, ConFEDE, HyCon, Self-MM
- concepts-idx.md: Multimodal 分组补入 4 个 concept 节点
- entities-idx.md: 论文 +2 (MAG-BERT/MulT/MISA 待创建), 数据集 +2 (MIntRec/CMU-MOSI)

## [2026-06-13 18:45] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:23] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:24] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:26] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:38] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:40] ingest | Claude Code 配置文件和 MCP 工具调用流程
- Source: raw/articles/claude-code-config-and-mcp-flow.md
- Summary: [[sources/claude-code-config-and-mcp-flow]]
- Pages created: [[concepts/mcp-protocol]], [[concepts/claude-code-configuration]], [[concepts/mcp-tool-calling-flow]], [[sources/claude-code-config-and-mcp-flow]]
- Pages updated: [[wiki/index]], [[wiki/hot]], [[wiki/concepts/concepts-idx]], [[wiki/domains/Engineering]]
- Key insight: MCP 协议本质是 JSON-RPC 2.0 的工具通信封装，claude mcp add 只是 JSON 写入的 CLI 封装
- contradictions: 0

## [2026-06-13 20:42] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:52] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 20:57] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:01] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:08] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:10] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:14] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:19] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:38] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:44] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:45] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:49] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:54] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:56] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 21:58] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:01] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:05] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:06] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:07] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:08] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:09] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:11] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:12] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:16] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:26] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:28] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:39] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:43] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:44] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:50] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 22:52] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 23:19] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 23:30] ingest | HypLoRA: Hyperbolic Fine-Tuning for LLMs (NeurIPS 2025)
- Source: raw/papers/hyperbolic-fine-tuning-llms/paper.pdf
- type: concept + insight + entity
- domain: Foundations + Training + Architecture (跨域)
- pages_created:
  - [[concepts/hyplora]] — 双曲低秩适配方法
  - [[concepts/hyperbolic-geometry-llm]] — LLM 嵌入的双曲结构分析
  - [[concepts/hyperbolic-geometry]] — 双曲几何基础
  - [[concepts/lora]] — LoRA 低秩适配
  - [[sources/hyplora-neurips2025]] — 论文摘要页
  - [[insights/llm-embedding-geometry]] — 洞察: 嵌入空间的内在几何
- pages_updated: [[index]], [[concepts-idx]], [[entities-idx]], [[insights-idx]], [[domains/Foundations]], [[domains/Architecture]], [[domains/Training]], [[overview]]
- key_concepts: [HypLoRA, LLR, δ-双曲性, 幂律分布, Lorentz模型, 高阶范数依赖]
- contradictions: 0
- note: 首次 ingest 论文，跨 3 个领域创建 6 个新节点

## [2026-06-13 23:27] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-13 23:29] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 00:14] session-end | 会话封印
- hook: Stop

## [2026-06-14 11:30] ingest | domains 目录结构重构
- action: refactor-domains
- 问题: 域页面和子目录 idx 双重维护、命名不一致、引用断裂
- 方案: 删除所有子目录，域页面 = 综述 + 节点索引（一体两面）
- 删除: 8 个子目录 (foundations/ architecture/ training/ alignment/ inference/ multimodal/ agents/ engineering/)
- 删除: agents/domains-idx.md, engineering/domains-idx.md
- 更新: domains-idx.md（精简为顶级导航）
- 更新: CLAUDE.md Phase 4（引用改为域页面）
- 更新: skills/wiki/SKILL.md, skills/align/SKILL.md（引用修复）
- 引用残留检查: 0 处（grep 验证通过）

## [2026-06-14 11:45] ingest | domains-concept 双向连接修复 + 机制层加固
- action: fix-domain-concept-links
- 问题1: 域页面列出的"核心概念节点"大部分是占位符（无实际页面）
- 问题2: 已存在的 concept 未被域页面收录（monte-carlo-dropout, setfit, negative-data-augmentation, Agents 3个, uncertainty-routing）
- 修复: 8 个域页面全部重写——删占位、补漏连、统一格式为"已有节点 + 关键缺口"
- 验证: 18 个 concept 全部双向连接（concept.domain → Domain.md.已有节点）
- 机制层: CLAUDE.md Phase 3 新增"强制域连接"规则（创建 concept 时当场更新域页面）

## [2026-06-14 12:00] ingest | 知识图谱中心化改造 — Domain 成为中心节点
- action: refactor-graph-center
- 问题: domain 只是 frontmatter 静态字段，不在关系图谱中，知识图谱是扁平的
- 方案: domain 作为中心枢纽，concept/source/comparison 围绕 domain 辐射
- 新增语义边:
  - belongs-to（向心边）: concept → domain，19 条，18 个文件
  - contains（辐射边）: domain → 节点，29 条，8 个域文件
- CLAUDE.md 语义词典: 新增 belongs-to 和 contains
- CLAUDE.md Phase 3: 强制域连接规则（concept 创建时必须加 belongs-to + 更新域页面 contains）

## [2026-06-14 12:15] ingest | 知识图谱层级结构建立 — Source 归口机制
- action: establish-graph-hierarchy
- 问题: source 诞生的节点（concept/comparison/insight/question）没有归口到 source，图谱是散落的
- 方案: 三层结构（Domain → Source → 节点），双向边保证连通
- Source 页面修复:
  - cagc-cvpr2024: implements → spawns (3→5条)
  - intent-detection-age-of-llms: studies/extends/applied_in → spawns (3→8条)
  - hyplora-neurips2025: introduces/analyzes → spawns (2→7条)
- 被诞生节点: 19 个文件全部加 produced-by 边（grep 验证通过）
- CLAUDE.md 语义词典: 新增 spawns 和 produced-by
- CLAUDE.md Phase 3: 新增"强制 Source 归口"规则（三层结构 + 双向边）
- 图谱层级: Layer 1 Domain → Layer 2 Source → Layer 3 节点

## [2026-06-14 12:30] ingest | 索引文件重构 + log 退出关系图谱
- action: refactor-index
- 问题1: wiki/concepts/concepts-idx.md 与 wiki/index.md 功能重复
- 问题2: log.md 不应出现在关系图谱统计中
- 修复:
  - wiki/index.md → wiki/concepts-idx.md（重命名）
  - wiki/concepts/concepts-idx.md（删除，内容已在域页面覆盖）
  - concepts-idx.md 自引用修复（目录结构段）
  - 19 个活跃文件批量修复引用（wiki/index.md → wiki/concepts-idx.md）
  - log.md 中的边字符串是描述性文本，非图谱关系（确认不需修改）

## [2026-06-14 12:45] ingest | log.md 退出知识图谱
- action: hide-log-from-graph
- 问题: wiki/log.md 在 wiki/ 目录内，Obsidian 将其视为图谱节点
- 修复: wiki/log.md → log.md（移至 vault 根目录，不入图谱）
- 引用修复: 18 个活跃文件批量替换 wiki/log.md → log.md
- concepts-idx.md: 目录结构段更新（log.md 移至 vault 根）
- 验证: grep wiki/log.md 零残留
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 10:45] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 10:49] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:11] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:14] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:16] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:19] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:20] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 12:00] ingest | Intent Detection in the Age of LLMs (EMNLP 2024)
- type: source (论文) + 8 concept/insight 节点
- domain: Agents + Engineering + Training + Foundations
- venue: EMNLP 2024 Industry Track
- pages_created: 9
  - [[sources/intent-detection-age-of-llms]] — 论文摘要页 (status:developing)
  - [[concepts/intent-detection-tods]] — 意图检测 TODS NLU 核心组件
  - [[concepts/out-of-scope-detection]] — 域外检测 OOS 识别
  - [[concepts/setfit]] — SetFit 对比微调句子转换器
  - [[concepts/adaptive-in-context-learning]] — 自适应上下文学习
  - [[concepts/uncertainty-routing]] — 不确定性路由混合系统
  - [[concepts/monte-carlo-dropout]] — MC Dropout 贝叶斯不确定性估计
  - [[concepts/negative-data-augmentation]] — 负面数据增强
  - [[insights/hybrid-beats-pure-llm]] — 洞察: 混合系统胜过纯 LLM
- pages_updated: 5 (index.md, overview.md, domains/agents, domains/engineering, hot.md)
- key_concepts: [意图检测, OOS检测, SetFit, 自适应ICL, 不确定性路由, 负面数据增强, MC Dropout]
- contradictions: 0
- study_materials: raw/papers/intent-detection-age-of-llms/
  - README.md, summary.md, method.md, insights.md
  - qa.md (15题), mental-model.md, reflection.md, meta.json
- note: 首次覆盖 Agents 领域，新建 agents/domains-idx.md

## [2026-06-14 11:21] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:39] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:43] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:51] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:56] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 11:56] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes

## [2026-06-14 15:00] lint | 系统健康全面修复
- action: system-health-fix
- 触发: 用户大量局部修改后全面一致性检查
- Layer 0 基础设施:
  - settings.json: INDEX_FILE wiki/index.md → wiki/concepts-idx.md
  - settings.json: LOG_FILE wiki/log.md → log.md
  - post-session.sh: LOG_FILE 路径修正为 $VAULT_ROOT/log.md
  - log-write.sh: LOG_FILE 路径修正为 $VAULT_ROOT/log.md
  - wiki/log.md: 删除残余副本（内容已在根目录 log.md）
- Layer 1 Source 页面:
  - claude-code-config-and-mcp-flow.md: 补全 related 块 + spawns:: 边（3条）
  - 4个 source 页面: 全部添加 belongs_to:: 边
  - hyplora/intent-detection: updated 日期更新
- Layer 2 Concept 页面:
  - 5个 concept 页补全 produced_by:: 边（hyperbolic-geometry, lora, mcp-protocol, claude-code-configuration, mcp-tool-calling-flow）
  - 新建 concepts/contrastive-learning.md（消除 4 处 dead link）
- Layer 3 Domain 页面:
  - Agents: concept 节点 0→3, updated 日期
  - Training: concept 节点 1→4, updated 日期
  - Foundations: concept 节点 1→2, updated 日期
  - Engineering: concept 节点 3→4, updated 日期
- Layer 4 Index 页面:
  - concepts-idx.md: MC Dropout 从 Inference 移除, Training 补 2 条, question 0→2, 总节点 25→26
  - entities-idx.md: 论文条目标注为 source 类型, 统计修正
  - insights-idx.md: 补 2 条缺失条目, 统计 1→3
  - domains-idx.md: 各域节点数对齐, Agents 链接格式修复, 总节点 13→21
- Layer 5 Meta/System:
  - dashboard.md: 总节点 16→31, 月度目标标记完成, 待办更新
  - SYSTEM-STATUS.md: settings 状态修正, 节点数更新
  - overview.md: 域节点数对齐, 总节点 25→31
  - hot.md: 统计快照更新
- pages_created: 1 (contrastive-learning)
- pages_updated: ~30
- contradictions: 0

## [2026-06-14 12:16] session-end | 会话封印
- hook: Stop
- vault: /d/Workspace/AI_Learning/AI Vault
- hot_file_exists: yes
