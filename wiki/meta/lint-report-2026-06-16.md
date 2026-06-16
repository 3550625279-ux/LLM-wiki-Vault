# Lint Report — 2026-06-16

> 执行时间: 2026-06-16 22:50
> 触发: 手动 `lint`
> 上次 lint: 2026-06-13 (首次)

---

## 📊 总体健康

```
总节点数:       107 个文件 (concept:68, source:15, insight:6, entity:2, operation:1, comparison:2, question:2, 域页:8, 模板:3)
总 wikilink:    待统计
孤儿页:         0 ✅
死链 (概念):    17 🔴
死链 (实体):    8 (旧 lint 遗留)
Frontmatter 缺失: 0 ✅
域名不一致:     15 → 已修复 10 ✅
矛盾登记:       0 ✅
```

---

## 🟢 通过项

| 检查项 | 结果 |
|--------|------|
| 孤儿页 | 0 — 所有页面都被至少一个 wikilink 引用 |
| Frontmatter 缺失 | 0 — 所有节点页都有完整 YAML |
| 矛盾 (corrects::) | 0 — 无矛盾登记 |

---

## 🔴 死链（17 个概念页引用了不存在的页面）

这些是"预留边"——指向未来需要创建的概念页。不算 bug，但是待办。

| 来源页面 | 断裂目标 | 建议优先级 |
|----------|---------|-----------|
| centering-decoupling | concepts/cosine-similarity | 🟢 低 |
| covariance | concepts/covariance-matrix | 🟡 中 |
| covariance | concepts/variance | 🟢 低 |
| mcp-protocol | concepts/function-calling | 🟡 中 |
| moment | concepts/gan-moment-matching | 🟢 低 |
| cross-entropy-loss | concepts/llm-training | 🟡 中 |
| mle | concepts/maximum-likelihood | 🟢 低 |
| cross-video-bank | concepts/mini-batch-contrastive-learning | 🟢 低 |
| multimodal-intent-recognition | concepts/multimodal-fusion | 🟡 中 |
| multimodal-intent-recognition | concepts/multimodal-sentiment-analysis | 🟢 低 |
| lora | concepts/qlora | 🟡 中 |
| order-statistics | concepts/quantile | 🟢 低 |
| batch-normalization | concepts/resnet | 🟡 中 |
| lora | concepts/svd | 🟢 低 |
| layer-normalization | concepts/transformer | 🔴 高 (可由已有组件组装) |
| context-augmented-transformer | concepts/transformer-attention | 🔴 高 (可改为 attention-mechanism) |
| kl-divergence | concepts/vae | 🟡 中 |

**最高优先级修复**:
1. `concepts/transformer-attention` → 应指向已有的 `concepts/attention-mechanism`
2. `concepts/transformer` → 可创建完整 Transformer 页，或改为指向 `concepts/encoder-decoder-architecture`

---

## ⚠️ 域名不一致（已修复）

原问题: 15 个文件的 `belongs_to::` 边使用小写 `domains/training` 而非 Title Case `domains/Training`。
修复范围: 10 个文件（7 个 Training + 2 个 Alignment + 1 个 Inference）全部改为 Title Case。
剩余 5 个文件的 belongs_to 已是正确写法。

---

## 📈 节点状态分布

| 状态 | 数量 | 占比 |
|------|------|------|
| seed | 88 | 84.6% |
| developing | 16 | 15.4% |
| mature | 0 | 0% |
| evergreen | 0 | 0% |

---

## 📈 各域节点数

| 领域 | 节点数 | 变化 |
|------|--------|------|
| Foundations | 35 | (不变) |
| Training | 21 | +4 (BPTT, gradient-clipping, teacher-forcing, perplexity) |
| Architecture | 16 | +13 (CNN, RNN, Transformer 全家桶) ← 本次主要增长 |
| Engineering | 10 | (不变) |
| Common Computer | 8 | (不变) |
| Multimodal | 5 | (不变) |
| Agents | 4 | (不变) |
| Alignment | 2 | (不变) |
| Inference | 1 | (不变) |

---

## 🎯 下次 lint 建议

1. **优先修复 2 个高优死链** (transformer-attention → attention-mechanism, 创建 transformer 页)
2. 考虑创建 `concepts/qlora` 和 `concepts/resnet`（中优先级死链）
3. 下次 lint 时间: 约 10-15 次 ingest 后
