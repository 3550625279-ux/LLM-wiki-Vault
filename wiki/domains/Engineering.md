---
title: "Engineering — 工程实践"
type: domain
status: seed
domain: Engineering
tags: [mlops, evaluation, data-engineering, monitoring, prompt-engineering]
created: 2026-06-13
updated: 2026-06-13
confidence: high
---

# Engineering — 工程实践

> **领域使命**: 在生产环境中可靠、高效地运行 AI 系统。
> **实用导向**: 这里的知识直接转化为可操作的工程经验。

---

## 📌 领域地图

```
Engineering
├── MLOps
│   ├── 实验追踪 (Wandb/MLflow)
│   ├── 模型注册与版本管理
│   ├── 持续训练流水线
│   └── A/B 测试框架
│
├── 评估框架
│   ├── 标准 Benchmark (MMLU/HumanEval/GSM8K)
│   ├── 自定义评估
│   ├── LLM-as-Judge
│   └── 对抗评估
│
├── 数据工程
│   ├── 数据清洗流水线
│   ├── 去重策略 (MinHash/SimHash)
│   ├── 质量过滤 (困惑度/规则过滤)
│   └── 数据飞轮设计
│
├── Prompt Engineering
│   ├── Few-Shot Prompting
│   ├── System Prompt 设计
│   ├── 结构化输出 (JSON mode)
│   └── 提示注入防护
│
├── 监控与可观测性
│   ├── Latency / Throughput 指标
│   ├── 漂移检测
│   └── 日志与追踪
│
└── 成本优化
    ├── 模型选择策略 (大/小模型路由)
    ├── Caching 策略
    └── Batch 处理
```

---

## 🧮 核心概念节点

### 评估
- [ ] [[concepts/llm-evaluation]] — 如何科学评估 LLM
- [ ] [[concepts/llm-as-judge]] — 用 LLM 评估 LLM 的方法与偏差
- [ ] [[concepts/benchmark-contamination]] — Benchmark 污染问题

### 数据
- [ ] [[concepts/data-deduplication]] — MinHash 去重
- [ ] [[concepts/data-quality-filtering]] — 质量过滤策略
- [ ] [[concepts/data-flywheel]] — 数据飞轮设计模式

### Prompt
- [ ] [[concepts/few-shot-prompting]] — In-context learning
- [ ] [[concepts/system-prompt-design]] — 系统提示设计原则
- [ ] [[concepts/prompt-injection]] — 提示注入攻击与防护

### 工具
- [ ] [[entities/wandb]] — 实验追踪工具
- [ ] [[entities/vllm]] — 部署框架（与 Inference 共享）

---

## 🔗 领域间关系

- `implements::` [[domains/training]] — 工程实现训练流水线
- `implements::` [[domains/inference]] — 工程实现推理部署
- `applied_in::` [[domains/agents]] — Agent 系统需要工程支撑

---

## 💡 领域关键洞察

- **评估比训练更难**: 好的 eval 是最稀缺的资源
- **数据质量 >> 数据数量**: FineWeb/Dolma 等精心策划数据集优于原始爬虫
- **Prompt Engineering 的天花板**: 提示优化有边际效益递减，模型能力是根本
- **成本意识**: 大模型推理成本会主导产品经济性

---

## 📖 推荐资料

- [ ] Chip Huyen "Designing ML Systems" (整本)
- [ ] FineWeb 论文 (HuggingFace, 2024)
- [ ] Evaluation Hell 博文系列
- [ ] ML Engineering at Scale (各大公司技术博客)

---

## 📊 领域统计

```
concept 节点: 0 (目标: 12+)
entity 节点:  0 (目标: 8+)
maturity:    seed
```
