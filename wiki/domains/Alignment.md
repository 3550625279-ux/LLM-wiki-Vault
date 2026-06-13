---
title: "Alignment — 对齐与安全"
type: domain
status: seed
domain: Alignment
tags: [alignment, safety, interpretability, red-teaming, value-alignment]
created: 2026-06-13
updated: 2026-06-13
confidence: medium
---

# Alignment — 对齐与安全

> **领域使命**: 理解如何让 AI 系统真正做人类想要的事，同时避免有害行为。
> **注意**: 这是最活跃的研究领域之一，争议最多，许多内容仍是开放问题。

---

## 📌 领域地图

```
Alignment
├── 价值对齐 (Value Alignment)
│   ├── 什么是"对齐"？(定义争议)
│   ├── RLHF / RLAIF
│   ├── Constitutional AI
│   └── Debate / Amplification
│
├── 可解释性 (Interpretability)
│   ├── Mechanistic Interpretability
│   │   ├── Circuits (注意力头功能)
│   │   ├── Superposition 假说
│   │   └── Feature Geometry
│   ├── Probing Classifiers
│   └── Attention Visualization
│
├── 安全技术
│   ├── Red Teaming (红队测试)
│   ├── Jailbreak 防护
│   ├── Backdoor / Trojan 检测
│   └── Robustness
│
├── 理论框架
│   ├── Goodhart's Law (指标失效)
│   ├── Reward Hacking
│   ├── Mesa-Optimization
│   └── Inner vs Outer Alignment
│
└── 超级对齐 (Scalable Oversight)
    ├── AI-assisted 评估
    ├── Weak-to-Strong Generalization
    └── Debate
```

---

## 🧮 核心概念节点

### 对齐基础
- [ ] [[concepts/alignment-definition]] — 对齐到底对齐什么？
- [ ] [[concepts/goodharts-law]] — 指标优化导致指标失效
- [ ] [[concepts/reward-hacking]] — 强化学习中的目标偏离

### 可解释性
- [ ] [[concepts/mechanistic-interpretability]] — 逆向工程神经网络
- [ ] [[concepts/superposition-hypothesis]] — 模型如何压缩特征
- [ ] [[concepts/attention-head-roles]] — 不同注意力头的功能分工

### 安全
- [ ] [[concepts/red-teaming]] — 对抗测试方法
- [ ] [[concepts/jailbreak-patterns]] — 越狱攻击类型
- [ ] [[concepts/inner-outer-alignment]] — 内外对齐区别

---

## 🔗 领域间关系

- `depends_on::` [[domains/training]] — 对齐技术依赖训练方法
- `applied_in::` [[domains/agents]] — Agent 安全是对齐的应用场景

---

## ⚠️ 活跃矛盾/争议（该领域特别多）

1. **Alignment 是否可解**？AI Safety vs AI Capabilities 的根本分歧
2. **RLHF 真的对齐了价值观，还是只是学会了讨好评估者？**
3. **Mechanistic Interpretability 能 scale 到大模型吗？**
4. **更强的能力是否自然导致更好的对齐？**（能力安全假说）
5. **规则对齐 vs 价值对齐**: Constitutional AI vs 学习人类偏好

---

## 📖 推荐资料

- [ ] Anthropic Constitutional AI 论文
- [ ] Neel Nanda Mechanistic Interpretability 博客
- [ ] Goodhart's Law 与 Reward Hacking (Krakovna et al.)
- [ ] Weak-to-Strong Generalization (OpenAI, 2023)

---

## 📊 领域统计

```
concept 节点: 0 (目标: 12+)
entity 节点:  0 (目标: 6+)
矛盾对:       5 个已预识别
maturity:    seed
```
