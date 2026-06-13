---
title: "Agents — 智能体系统"
type: domain
status: seed
domain: Agents
tags: [react, tool-use, memory, planning, multi-agent, function-calling]
created: 2026-06-13
updated: 2026-06-13
confidence: medium
---

# Agents — 智能体系统

> **领域使命**: 理解如何让 LLM 自主完成复杂多步任务。
> **当前状态**: 快速发展，工程实践远领先于理论理解。

---

## 📌 领域地图

```
Agents
├── 推理框架
│   ├── Chain-of-Thought (CoT)
│   ├── ReAct (推理 + 行动交织)
│   ├── Tree of Thoughts (ToT)
│   └── ReWOO (计划与执行分离)
│
├── 工具使用
│   ├── Function Calling (OpenAI / Anthropic)
│   ├── Tool Use Protocol
│   ├── 代码执行
│   └── 浏览器 / 搜索工具
│
├── 记忆系统
│   ├── 工作记忆 (Context Window)
│   ├── 情节记忆 (会话历史)
│   ├── 语义记忆 (向量数据库)
│   └── 程序记忆 (工具/技能)
│
├── 规划与执行
│   ├── 任务分解
│   ├── 自我批评与修正
│   └── 反思循环 (Reflexion)
│
└── 多智能体
    ├── 角色分工 (AutoGen/CrewAI)
    ├── 辩论 (Debate)
    └── 监督者-执行者模式
```

---

## 🧮 核心概念节点

### 推理
- [ ] [[concepts/chain-of-thought]] — 思维链提示
- [ ] [[concepts/react-framework]] — 推理-行动-观察循环
- [ ] [[concepts/tree-of-thoughts]] — 分支探索推理

### 工具
- [ ] [[concepts/function-calling]] — LLM 调用外部工具
- [ ] [[concepts/tool-use-protocol]] — MCP 等工具协议设计

### 记忆
- [ ] [[concepts/context-window-as-memory]] — 上下文窗口的记忆局限
- [ ] [[concepts/vector-database-retrieval]] — RAG 与语义检索
- [ ] [[concepts/rag]] — 检索增强生成

### 规划
- [ ] [[concepts/reflexion]] — 自我反思与错误修正
- [ ] [[concepts/task-decomposition]] — 复杂任务分解策略

---

## 🔗 领域间关系

- `depends_on::` [[domains/architecture]] — LLM 是 Agent 的推理核心
- `depends_on::` [[domains/alignment]] — Agent 安全依赖对齐技术
- `applied_in::` [[domains/engineering]] — Agent 系统是当前工程热点
- `extends::` [[domains/inference]] — Agent 需要多次推理调用

---

## ⚠️ 活跃矛盾/争议

1. **规划能力**: LLM 真的能"规划"还是只是模式匹配？
2. **记忆架构**: 长上下文 vs RAG — 哪个是正确路线？
3. **多智能体**: 多 Agent 协作真的优于单 Agent？开销是否值得？
4. **Agent 安全**: 自主行动的 Agent 如何避免有害操作？

---

## 📖 推荐资料

- [ ] ReAct 论文 (Yao et al. 2022)
- [ ] Reflexion 论文 (Shinn et al. 2023)
- [ ] AutoGen 论文 (Microsoft)
- [ ] Claude Tool Use 文档 (Anthropic)
- [ ] LangChain / LlamaIndex 文档

---

## 📊 领域统计

```
concept 节点: 0 (目标: 12+)
entity 节点:  0 (目标: 6+)
maturity:    seed
```
