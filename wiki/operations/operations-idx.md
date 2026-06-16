# Operations Index — 操作节点目录

> **类型**: Map of Content (MoC)
> **用途**: wiki/operations/ 目录下所有 operation 节点的索引。
> **特征**: 操作节点是 How-to 知识，直接对应可执行的工程步骤。

---

## 按领域分组

### [[domains/Training|Training]] & Fine-tuning

- [[operations/sft-cot-data-pipeline]] — CoT SFT数据四条生产线（人工标注/教师蒸馏/程序合成/Rejection Sampling） | status:seed

**高优先级待创建**:
- `finetune-llama-lora` — 用 LoRA 微调 LLaMA 的完整 SOP
- `qlora-training-setup` — QLoRA 训练环境配置
- `data-cleaning-pipeline` — 训练数据清洗流程

### [[domains/Inference|Inference]] & Deployment
> *待填充*

**高优先级待创建**:
- `quantize-model-gguf` — 模型量化为 GGUF 格式
- `deploy-vllm` — vLLM 部署 SOP
- `ollama-local-setup` — Ollama 本地部署

### [[domains/Engineering|Evaluation]]
> *待填充*

**高优先级待创建**:
- `run-mmlu-eval` — 运行 MMLU 评估
- `custom-eval-design` — 自定义评估集设计

### [[domains/Engineering|Prompting]]
> *待填充*

**高优先级待创建**:
- `few-shot-prompt-template` — Few-shot 提示模板
- `system-prompt-hardening` — 系统提示安全加固

### [[domains/Engineering|MLOps]]
> *待填充*

---

## 按状态分组

### 🌱 seed
- [[operations/sft-cot-data-pipeline]] — CoT SFT数据四条生产线

### ✅ mature (可直接使用)
> *无*

---

## 操作节点质量标准

每个 operation 节点必须包含:
- [ ] 前置条件 (Prerequisites)
- [ ] 具体步骤 (Steps，编号列表)
- [ ] 验证方法 (Verification)
- [ ] 常见错误 (Common Errors)
- [ ] 参数参考 (Parameter Reference)

---

## 统计

```
总 operation 节点: 1
目标总数:          30+
上次更新:          2026-06-16
```
