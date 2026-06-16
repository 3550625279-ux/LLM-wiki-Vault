# Hot Cache — 会话快速恢复上下文

> 此文件由系统自动维护。每次会话开始时静默读取，不向用户输出。
> 每次 ingest / review / align 后更新。

---

## 🎯 当前学习重心

LLM 推理能力后训练技术栈 — SFT→RLHF→PRM→GRPO 完整管线 + Test-Time Compute + 数据飞轮

## 📍 最近活跃节点

- [[concepts/grpo]] — 组相对策略优化 GRPO (seed)
- [[concepts/process-reward-model]] — 过程奖励模型 PRM (seed)
- [[concepts/aha-moment]] — Aha Moment 推理涌现 (seed)
- [[entities/deepseek-r1]] — DeepSeek-R1 (seed)
- [[concepts/test-time-compute]] — 推理时计算扩展 (seed)

## 🧵 活跃线索 / 未解问题

- LLM推理能力是"高效模式补全"还是"真正逻辑推理"？两种理解都有证据
- PRM标注成本极高（步骤数×标注量），实际工程中如何权衡？
- GRPO的规则化奖励仅适用于可验证答案（数学/编程），开放域推理怎么办？
- 奖励Hacking的缓解策略是否足够？长度惩罚和多样性约束的实际效果？
- DeepSeek-R1第二轮RL混合使用GRPO+RLHF的具体配比？

## ⏭️ 下次继续点

- [ ] 重跑 lint 获取最新健康指标
- [ ] 为 GRPR/PRM 等概念生成 Flux 概念插画
- [ ] 创建 Agents 领域综述页
- [ ] 创建 Alignment 领域更多节点（Goodhart's Law, Constitutional AI）
- [ ] 重跑 align all 生成基线报告

## 📊 库状态快照

- 总节点数: 58 (concept:38, entity:2, insight:5, source:7, comparison:2, operation:1, question:2)
- AI 领域覆盖: 8/8 ✅ 全覆盖（Foundations, Architecture, Training, **Alignment**, Inference, Multimodal, Agents, Engineering）
- 通用计算基础: 8 节点（不计入 AI 领域）
- 最近 ingest: 2026-06-16 (LLM推理能力后训练技术栈)
- 最近修复: 2026-06-14 (v2.0 路径失联修复，7文件零残留)
- 矛盾登记: 0

---

*上次更新: 2026-06-16 | LLM推理能力后训练技术栈 ingest 完成*
