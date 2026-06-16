# PEFT (Parameter-Efficient Fine-Tuning) 架构可视化

本文档包含 PEFT 框架的 `config` 和 `layer` 系统的可视化图谱。

---

## 1. 配置体系总览 (Config Hierarchy)

```
PeftConfigMixin (dataclass + PushToHubMixin)
│  ├── peft_type: Optional[PeftType]
│  ├── task_type: Optional[TaskType]
│  └── auto_mapping: Optional[dict]
│
├── PeftConfig (通用 PEFT 配置)
│   ├── base_model_name_or_path
│   ├── revision
│   ├── peft_type
│   ├── task_type
│   └── inference_mode: bool
│
├── PromptLearningConfig (Prompt 学习基类)
│   ├── num_virtual_tokens
│   ├── token_dim
│   ├── num_transformer_submodules
│   ├── num_attention_heads
│   └── num_layers
│   └── is_prompt_learning = True
│
├── LoraConfig (LoRA 专有配置) ─── PeftType.LORA
│   ├── r: int = 8              ← 秩 (rank)
│   ├── target_modules          ← 目标模块
│   ├── lora_alpha: int = 8     ← 缩放系数
│   ├── lora_dropout: float     ← dropout
│   ├── use_rslora: bool        ← Rank-Stabilized LoRA
│   ├── use_dora: bool          ← DoRA (权重分解)
│   ├── init_lora_weights       ← 初始化策略
│   │   ├── True / False
│   │   ├── "gaussian"
│   │   ├── "pissa" / "pissa_niter_[N]"
│   │   ├── "olora"
│   │   ├── "corda"
│   │   ├── "loftq"
│   │   └── "eva"
│   ├── bias: "none" | "all" | "lora_only"
│   ├── rank_pattern: dict      ← 逐层不同秩
│   ├── alpha_pattern: dict     ← 逐层不同 alpha
│   ├── layers_to_transform     ← 指定层索引
│   ├── layers_pattern          ← 层模式名
│   ├── layer_replication       ← 层复制扩展模型
│   ├── lora_bias: bool         ← LoRA B 的偏置
│   ├── lora_type: str          ← LoRA 类型 ("std", "hyplora", "hyplora_simplified")
│   ├── trainable_token_indices
│   ├── loftq_config: LoftQConfig    ← LoftQ 子配置
│   ├── eva_config: EvaConfig        ← EVA 子配置
│   ├── corda_config: CordaConfig    ← CorDA 子配置
│   ├── megatron_config / megatron_core
│   └── runtime_config: LoraRuntimeConfig
│       └── ephemeral_gpu_offload
│
├── AdaLoraConfig (Adaptive LoRA)
├── BOFTConfig / PolyConfig
├── IA3Config / VeraConfig / VBLoraConfig
├── PrefixTuningConfig / PromptTuningConfig / P_TuningConfig
└── ... (更多 PEFT 方法)
```

---

## 2. PeftType 枚举 — 支持的所有 PEFT 方法

```
PeftType (str, Enum):
├── PROMPT_TUNING           ─── 提示词微调
├── MULTITASK_PROMPT_TUNING ─── 多任务提示词微调
├── P_TUNING                ─── P-Tuning
├── PREFIX_TUNING           ─── 前缀微调
├── LORA                    ─── LoRA (低秩适应)
├── ADALORA                 ─── 自适应 LoRA
├── BOFT                    ─── BOFT
├── ADAPTION_PROMPT         ─── Adaption Prompt
├── IA3                     ─── IA3
├── LOHA                    ─── LoHA
├── LOKR                    ─── LoKR
├── OFT                     ─── OFT
├── POLY                    ─── Poly
├── LN_TUNING               ─── LayerNorm 微调
├── VERA                    ─── VeRA
├── FOURIERFT               ─── FourierFT
├── XLORA                   ─── XLoRA
├── HRA                     ─── HRA
├── VBLORA                  ─── VBLoRA
├── CPT                     ─── CPT
├── BONE                    ─── BoNe
├── RANDLORA                ─── RandLoRA
└── TRAINABLE_TOKENS        ─── 可训练 Token
```

---

## 3. LoRA 层类体系 (Layer Class Hierarchy)

```
BaseTunerLayer (来自 tuners_utils.py)
│   └── 通用适配器层接口: merge, unmerge, disable_adapters, active_adapters
│
└── LoraLayer (LoRA 核心层抽象)
    ├── 属性:
    │   ├── base_layer            ← 被包装的原始层
    │   ├── lora_A: ModuleDict    ← A 矩阵 (in_features -> r)
    │   ├── lora_B: ModuleDict    ← B 矩阵 (r -> out_features)
    │   ├── lora_embedding_A/B    ← Embedding 模式的权重
    │   ├── lora_dropout          ← dropout 层
    │   ├── r, lora_alpha, scaling  ← 超参数
    │   ├── lora_type             ← "std" / "hyplora" / "hyplora_simplified"
    │   ├── lora_k, lora_norm_scale ← HyperLoRA 曲率参数
    │   ├── lora_magnitude_vector ← DoRA 幅度向量
    │   ├── lora_variant          ← LoraVariant 策略对象
    │   ├── merged_adapters       ← 已合并的适配器列表
    │   └── _disable_adapters     ← 全局禁用标志
    │
    ├── 核心方法:
    │   ├── update_layer()        ← 创建/更新适配器层
    │   ├── reset_lora_parameters() ← 标准初始化
    │   ├── pissa_init()          ← PiSSA 初始化 (SVD)
    │   ├── olora_init()          ← OLoRA 初始化 (QR分解)
    │   ├── corda_init()          ← CorDA 初始化 (协方差SVD)
    │   ├── loftq_init()          ← LoftQ 量化初始化
    │   ├── merge()               ← 合并适配器权重到基座
    │   ├── unmerge()             ← 从基座分离适配器权重
    │   ├── get_delta_weight()    ← 计算 delta = B@A * scaling
    │   ├── scale_layer() / unscale_layer()
    │   └── _mixed_batch_forward()← 混合适配器批处理
    │
    ├── 派生子类 (PyTorch层类型):
    │   ├── Linear(nn.Module, LoraLayer)
    │   │   ├── forward() ← 标准/混合批/变体 前向传播
    │   │   ├── merge() / unmerge()
    │   │   ├── get_delta_weight()
    │   │   ├── hyplora_simplified()      ← 双曲→欧氏投影
    │   │   └── hyplora_simplified_inverse() ← 欧氏→双曲投影
    │   │
    │   ├── Embedding(nn.Module, LoraLayer)
    │   │   ├── 使用 lora_embedding_A/B (nn.Parameter)
    │   │   ├── _embed() ← F.embedding 操作
    │   │   └── forward() / merge() / unmerge()
    │   │
    │   ├── _ConvNd(nn.Module, LoraLayer) ← Conv 基类
    │   │   ├── Conv1d ← F.conv1d
    │   │   ├── Conv2d ← F.conv2d
    │   │   └── Conv3d ← F.conv3d
    │   │
    │   └── MultiheadAttention(nn.Module, LoraLayer)
    │       ├── 包装 in_proj (nn.Parameter) + out_proj (Linear)
    │       ├── 每个 forward 临时 merge/unmerge (特殊策略)
    │       └── _restore_weights()
    │
    └── dispatch_default(): 工厂函数
        └── 根据 base_layer 类型 → 返回对应子类
            ├── nn.Embedding       → Embedding
            ├── nn.Conv1d/2d/3d    → Conv1d/Conv2d/Conv3d
            ├── nn.MultiheadAttention → MultiheadAttention
            ├── nn.Linear          → Linear
            └── Conv1D (HuggingFace) → Linear (fan_in_fan_out=True)
```

---

## 4. LoraVariant 策略模式 — DoRA 支持

```
LoraVariant (抽象基类)
│   ├── init(module, adapter_name)
│   ├── merge_safe(module, adapter, weight) → Tensor
│   ├── merge_unsafe(module, adapter, weight)
│   ├── unmerge(module, adapter, weight) → Tensor
│   └── forward(module, adapter, x, result) → Tensor
│
├── DoraLinearVariant (Linear + DoRA)
│   ├── init: 创建 DoraLinearLayer + 计算weight_norm
│   ├── merge: dora_factor = magnitude / weight_norm
│   ├── unmerge: weight / dora_factor - delta
│   └── forward: result + magnitude_vector(x, lora_A, lora_B)
│
├── DoraEmbeddingVariant (Embedding + DoRA)
│
├── _DoraConvNdVariant (Conv + DoRA 基类)
│   ├── DoraConv2dVariant
│   ├── DoraConv3dVariant
│   └── DoraConv1dVariant (由 DoraConv1dLayer 处理)
```

---

## 5. 前向传播流程 (以 Linear 为例)

```
forward(x)
  │
  ├─ disabled? → base_layer(x) 直接返回
  │
  ├─ adapter_names? → _mixed_batch_forward() 混合适配器批处理
  │
  ├─ merged? → base_layer(x) (已合并权重)
  │
  └─ 正常流程:
       │
       result = base_layer(x)              ← 基座前向
       │
       for each active_adapter:
       │
       ├─ lora_type == "std":
       │     interim = B(A(dropout(x))) * scaling
       │     result += interim
       │
       ├─ lora_type == "hyplora":
       │     x → 双曲空间 (Lorentz 模型)
       │     │   x_norm → x_direction
       │     │   x_space = sqrtK * sinh(norm/sqrtK) * direction
       │     │   x_space = B(A(x_space))
       │     │   x_time_new = sqrt(sum(x_space²) + 1/k)
       │     │   计算 arccosh → 双曲距离
       │     result += x * scaling
       │
       ├─ lora_type == "hyplora_simplified":
       │     x → hyplora_simplified_inverse(x, k)
       │         │  y_norm_sq → ξ = (1/√|k|)*((1-k*y²)/(1+k*y²))
       │         │  y_scaled = 2y / (1 + k*y²)
       │         │  → [ξ, y_scaled]
       │     x = B(A(x))  (去掉 ξ 分量)
       │     x = cat([sqrt(x²+k), x], dim=-1)  (重建 ξ)
       │     x → hyplora_simplified(x, k)
       │         │  result = x_space / (1 + √|k| * ξ)
       │     result += x * scaling
       │
       └─ lora_variant 存在 (如 DoRA):
             result = variant.forward(self, adapter, x, result)
             │  result + magnitude_vector(x, lora_A, lora_B)
```

---

## 6. 初始化策略对比

```
初始化方法         │ 核心技术                   │ 是否修改基座权重
──────────────────┼───────────────────────────┼──────────────────
True (标准)        │ Kaiming A + 零初始化 B    │ 否
False             │ 随机初始化 A/B             │ 否
"gaussian"        │ 高斯 A + 零初始化 B        │ 否
"pissa"           │ SVD 分解基座权重           │ 是 (基座残差=W-BA)
"pissa_niter_[N]" │ Fast SVD (迭代 N 次)       │ 是
"olora"           │ QR 分解基座权重            │ 是 (基座残差)
"corda"           │ 协方差 SVD (数据驱动)      │ 是
"loftq"           │ LoftQ 量化分解             │ 是 (量化基座)
"eva"             │ EVA 数据驱动初始化          │ 否 (B=0, 需训练)
```

---

## 7. 配置加载流程

```
from_pretrained()
  │
  ├── 1. 查找 adapter_config.json (本地或 HuggingFace Hub)
  │
  ├── 2. from_json_file() → loaded_attributes (dict)
  │
  ├── 3. check_kwargs() → 子类可覆写检查逻辑
  │
  └── 4. from_peft_type(**kwargs)
        │
        ├── 读取 peft_type (如 "LORA")
        ├── PEFT_TYPE_TO_CONFIG_MAPPING → LoraConfig
        ├── 处理前向兼容: 移除未知参数 + 警告
        └── 实例化 config = LoraConfig(...)
```

---

## 8. 模块替换流程 (dispatch_default)

```
将 base_layer 替换为 LoRA 层

dispatch_default(target, adapter_name, lora_config)
  │
  ├── target_base_layer = target (或 target.get_base_layer())
  │
  ├── isinstance(target_base_layer, ...):
  │   ├── nn.Embedding → Embedding(target, ...)
  │   ├── nn.Conv2d    → Conv2d(target, ...)
  │   ├── nn.Conv3d    → Conv3d(target, ...)
  │   ├── nn.Conv1d    → Conv1d(target, ...)
  │   ├── nn.MultiheadAttention → MultiheadAttention(target, ...)
  │   ├── nn.Linear    → Linear(target, ...)
  │   └── Conv1D (HF)  → Linear(target, fan_in_fan_out=True)
  │
  └── 返回 new_module (包装了 base_layer)
```
