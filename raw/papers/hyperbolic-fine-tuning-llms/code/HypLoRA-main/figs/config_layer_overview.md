# PEFT Config & Layer 可视化图谱

## 1. 配置类继承关系图

```mermaid
classDiagram
    class PeftConfigMixin {
        +peft_type: PeftType
        +task_type: TaskType
        +auto_mapping: dict
        +save_pretrained()
        +from_pretrained()
        +from_peft_type()
        +from_json_file()
        +to_dict()
        +is_prompt_learning() bool
    }

    class PeftConfig {
        +base_model_name_or_path: str
        +revision: str
        +inference_mode: bool
    }

    class PromptLearningConfig {
        +num_virtual_tokens: int
        +token_dim: int
        +num_transformer_submodules: int
        +num_attention_heads: int
        +num_layers: int
        +is_prompt_learning() True
    }

    class LoraConfig {
        +r: int
        +target_modules: list|str
        +lora_alpha: int
        +lora_dropout: float
        +use_rslora: bool
        +use_dora: bool
        +init_lora_weights: bool|str
        +bias: str
        +rank_pattern: dict
        +alpha_pattern: dict
        +lora_type: str
        +layers_to_transform: list|int
        +layer_replication: list
        +lora_bias: bool
        +loftq_config: LoftQConfig
        +eva_config: EvaConfig
        +corda_config: CordaConfig
        +runtime_config: LoraRuntimeConfig
    }

    class LoftQConfig {
        +loftq_bits: int
        +loftq_iter: int
    }

    class EvaConfig {
        +rho: float
        +tau: float
        +use_label_mask: bool
        +whiten: bool
        +adjust_scaling_factors: bool
    }

    class CordaConfig {
        +cache_file: str
        +covariance_file: str
        +corda_method: "ipm"|"kpm"
        +verbose: bool
    }

    class LoraRuntimeConfig {
        +ephemeral_gpu_offload: bool
    }

    PeftConfigMixin <|-- PeftConfig
    PeftConfigMixin <|-- PromptLearningConfig
    PeftConfig <|-- LoraConfig
    LoraConfig *-- LoftQConfig
    LoraConfig *-- EvaConfig
    LoraConfig *-- CordaConfig
    LoraConfig *-- LoraRuntimeConfig
```

---

## 2. LoRA Layer 类体系

```mermaid
classDiagram
    class BaseTunerLayer {
        +active_adapters: list
        +merged_adapters: list
        +disable_adapters: bool
        +merge()
        +unmerge()
        +set_adapter()
    }

    class LoraLayer {
        +base_layer: nn.Module
        +lora_A: ModuleDict
        +lora_B: ModuleDict
        +lora_embedding_A: ParameterDict
        +lora_embedding_B: ParameterDict
        +lora_dropout: ModuleDict
        +lora_magnitude_vector: ModuleDict
        +lora_variant: dict
        +r, lora_alpha, scaling: dict
        +lora_type: dict
        +lora_k, lora_norm_scale: ParameterDict
        +in_features, out_features: int
        +update_layer()
        +reset_lora_parameters()
        +pissa_init()
        +olora_init()
        +corda_init()
        +loftq_init()
        +get_delta_weight()
        +merge()
        +unmerge()
        +_mixed_batch_forward()
    }

    class Linear {
        +fan_in_fan_out: bool
        +forward(x) Tensor
        +merge()
        +unmerge()
        +get_delta_weight()
        +hyplora_simplified()
        +hyplora_simplified_inverse()
        +resolve_lora_variant()
    }

    class Embedding {
        +forward(x) Tensor
        +merge()
        +unmerge()
        +get_delta_weight()
        +_embed()
        +resolve_lora_variant()
    }

    class _ConvNd {
        +_kernel_dim: int
        +conv_fn: function
        +forward(x) Tensor
        +resolve_lora_variant()
    }

    class Conv1d {
        +conv_fn: F.conv1d
    }

    class Conv2d {
        +conv_fn: F.conv2d
    }

    class Conv3d {
        +conv_fn: F.conv3d
    }

    class MultiheadAttention {
        +embed_dim: int
        +num_heads: int
        +forward(x) Tensor
        +merge()
        +unmerge()
        +get_delta_weight()
        +unload_and_optionally_merge_module()
        +_restore_weights()
        +state_dict()
    }

    class LoraVariant {
        <<abstract>>
        +init(module, adapter_name)
        +merge_safe(module, adapter, weight) Tensor
        +merge_unsafe(module, adapter, weight)
        +unmerge(module, adapter, weight) Tensor
        +forward(module, adapter, x, result) Tensor
    }

    class DoraLinearVariant {
        +init: creates DoraLinearLayer
        +merge_safe: dora_factor * (weight + delta)
        +forward: result + magnitude_vector(...)
    }

    class DoraEmbeddingVariant {
        +init: creates DoraEmbeddingLayer
        +forward: mag_norm_scale * result + dora_result
    }

    BaseTunerLayer <|-- LoraLayer : inherits
    LoraLayer <|-- Linear : inherits
    LoraLayer <|-- Embedding : inherits
    LoraLayer <|-- _ConvNd : inherits
    _ConvNd <|-- Conv1d
    _ConvNd <|-- Conv2d
    _ConvNd <|-- Conv3d
    LoraLayer <|-- MultiheadAttention
    LoraVariant <|.. DoraLinearVariant : implements
    LoraVariant <|.. DoraEmbeddingVariant : implements
    Linear o-- LoraVariant : uses (strategy)
    Embedding o-- LoraVariant
    _ConvNd o-- LoraVariant
```

---

## 3. 前向传播流程图

```mermaid
flowchart TD
    Start(["forward(x)"]) --> CheckDisabled{"disable_adapters ?"}
    CheckDisabled -->|"Yes"| MCheck{"merged ?"}
    MCheck -->|"Yes"| Unmerge["unmerge()"]
    MCheck -->|"No"| BaseForward["base_layer(x)"]
    Unmerge --> BaseForward
    
    CheckDisabled -->|"No"| AdapterNames{"adapter_names\n参数存在？"}
    AdapterNames -->|"Yes"| MixedBatch["_mixed_batch_forward()\n混合不同适配器批处理"]
    
    AdapterNames -->|"No"| MergedCheck{"merged ?"}
    MergedCheck -->|"Yes"| BaseForward2["base_layer(x)"]
    MergedCheck -->|"No"| NormalFlow
    
    subgraph NormalFlow["正常前向（含 LoRA 计算）"]
        BaseResult["result = base_layer(x)"] 
        Loop["for each active_adapter"]
        BaseResult --> Loop
        
        Loop --> CheckType{"lora_type ?"}
        
        CheckType -->|"std"| StdLoRA["interim = B(A(dropout(x))) * scaling\nresult += interim"]
        
        CheckType -->|"hyplora"| HypLoRA["双曲空间 Lorentz 模型\n1. x_norm → x_direction\n2. x_space = K*sinh(norm/K)*dir\n3. x_space = B(A(x_space))\n4. 计算双曲时间分量\n5. arccosh → 双曲距离\nresult += x * scaling"]
        
        CheckType -->|"hyplora_simplified"| HypSimple["简化双曲投影\n1. hyplora_simplified_inverse(x, k)\n   → [ξ, y_scaled]\n2. B(A(y_scaled))\n3. cat([sqrt(x²+k), x])\n4. hyplora_simplified(x, k)\n5. result += x * scaling"]
        
        CheckType -->|"variant存在"| Variant["lora_variant.forward()\n如 DoRA:\nresult + magnitude_vector(...)"]
    end
    
    NormalFlow --> Return["return result"]
    MixedBatch --> Return
    BaseForward --> Return
    BaseForward2 --> Return
```

---

## 4. 模块替换流程

```mermaid
flowchart LR
    Start["原始模型层\nnn.Linear / nn.Embedding\nnn.Conv2d / ..."] --> Dispatch["dispatch_default()\n工厂函数"]
    
    Dispatch --> CheckType{"base_layer 类型"}
    
    CheckType -->|"nn.Linear"| LinearWrap["Linear(target, ...)\n包装为 LoraLinear"]
    CheckType -->|"nn.Embedding"| EmbedWrap["Embedding(target, ...)\n包装为 LoraEmbedding"]
    CheckType -->|"nn.Conv1d/2d/3d"| ConvWrap["Conv1d/2d/3d(target, ...)"]
    CheckType -->|"nn.MultiheadAttention"| AttnWrap["MultiheadAttention(target, ...)\n同时包装 out_proj"]
    CheckType -->|"HF Conv1D"| Conv1DWrap["Linear(target,\nfan_in_fan_out=True)"]
    
    LinearWrap --> InitLayer["update_layer()\n创建 lora_A, lora_B"]
    EmbedWrap --> InitLayer
    ConvWrap --> InitLayer
    AttnWrap --> InitLayer
    
    InitLayer --> InitWeights{"init_lora_weights ?"}
    
    InitWeights -->|"True"| Kaiming["Kaiming A + 零 B"]
    InitWeights -->|"False"| Random["随机 A + 随机 B"]
    InitWeights -->|"gaussian"| Gauss["高斯 A + 零 B"]
    InitWeights -->|"pissa"| Pissa["SVD: W = UΣV\n→ A = √ΣV, B = U√Σ\n基座残差 = W - BA"]
    InitWeights -->|"olora"| Olora["QR: W = QR\n→ A = R, B = Q\n基座残差 = W - BA"]
    InitWeights -->|"corda"| Corda["协方差 SVD\n数据驱动初始化"]
    InitWeights -->|"loftq"| LoftQ["LoftQ 量化"]
    InitWeights -->|"eva"| Eva["EVA 初始化\nB 保持为零"]
    
    InitWeights --> DoRA{"use_dora ?"}
    DoRA -->|"Yes"| DoraInit["创建 DoraLayer\nlora_magnitude_vector"]
    DoRA -->|"No"| Done["完成"]
```

---

## 5. 合并与分离 (Merge/Unmerge)

```mermaid
flowchart TD
    MergeStart["merge(adapter_names)"] --> GetAdapters["check_adapters_to_merge()"]
    
    GetAdapters --> LoopMerge["for each active_adapter"]
    
    LoopMerge --> VariantCheck{"lora_variant 存在？"}
    
    VariantCheck -->|"否 (标准 LoRA)"| StdMerge["delta = get_delta_weight()\n= B@A * scaling"]
    VariantCheck -->|"是 (DoRA)"| DoraMerge["1. delta = get_delta_weight()\n2. weight_norm\n3. dora_factor = mag/weight_norm\n4. new_weight = dora_factor*(weight+delta)"]
    
    StdMerge --> SafeCheck{"safe_merge ?"}
    DoraMerge --> SafeCheck
    
    SafeCheck -->|"Yes"| SafePath["clone original → 加delta\n→ NaN检查 → 赋值"]
    SafeCheck -->|"No"| UnsafePath["weight.data += delta"]
    
    SafePath --> AppendMerged["merged_adapters.append(name)"]
    UnsafePath --> AppendMerged
    
    UnmergeStart["unmerge()"] --> PopAdapters["while merged_adapters"]
    PopAdapters --> StdUnmerge["weight.data -= delta\n(标准) 或\nweight = unmerge()\n(DoRA)"]
```

---

## 6. 初始化策略对比

```mermaid
quadrantChart
    title LoRA 初始化策略对比
    x-axis "不影响基座权重" --> "修改基座权重"
    y-axis "简单初始化" --> "复杂数据驱动"
    quadrant-1 "数据驱动 + 修改基座"
    quadrant-2 "数据驱动 + 保持基座"
    quadrant-3 "简单 + 保持基座"
    quadrant-4 "简单 + 修改基座"
    "True (Kaiming)": [0.1, 0.15]
    "False (Random)": [0.1, 0.1]
    "gaussian": [0.15, 0.2]
    "pissa (SVD)": [0.85, 0.65]
    "olora (QR)": [0.8, 0.5]
    "corda (数据SVD)": [0.9, 0.85]
    "loftq (量化)": [0.85, 0.4]
    "eva (数据方差)": [0.2, 0.8]
```

---

## 7. 配置加载流程

```mermaid
sequenceDiagram
    participant User
    participant ConfigClass as PeftConfig
    participant Hub as HuggingFace Hub
    participant Mapper as PEFT_TYPE_TO_CONFIG_MAPPING
    participant SubConfig as LoraConfig (e.g.)
    
    User->>ConfigClass: from_pretrained("model_name")
    ConfigClass->>Hub: 查找 adapter_config.json
    Hub-->>ConfigClass: 返回 JSON 配置
    
    ConfigClass->>ConfigClass: from_json_file()
    ConfigClass->>ConfigClass: check_kwargs()
    
    ConfigClass->>ConfigClass: from_peft_type()
    Note over ConfigClass: 读取 peft_type (如 "LORA")
    
    ConfigClass->>Mapper: 查找配置类
    Mapper-->>ConfigClass: → LoraConfig 类
    
    ConfigClass->>SubConfig: 实例化 LoraConfig(**kwargs)
    
    Note over SubConfig: __post_init__()
    Note over SubConfig: 处理前向兼容
    Note over SubConfig: 处理子配置 (loftq/eva/corda)
    
    SubConfig-->>User: 返回配置对象
```

---

## 8. 完整文件结构

```mermaid
graph TD
    subgraph "peft/ 根目录"
        config_py["config.py\n核心配置基类"]
        mapping_py["mapping.py\nPEFT_TYPE_TO_CONFIG_MAPPING"]
    end
    
    subgraph "peft/utils/"
        peft_types["peft_types.py\nPeftType, TaskType\nregister_peft_method()"]
        config_utils["config.py\n(utils中的配置常量)"]
    end
    
    subgraph "peft/tuners/lora/"
        lora_cfg["config.py\nLoraConfig, LoftQConfig\nEvaConfig, CordaConfig"]
        lora_layer["layer.py\nLoraLayer, Linear\nEmbedding, _ConvNd\nMultiheadAttention"]
        variants["variants.py\nDoRA Variant 实现"]
        dora["dora.py\nDoraLayer 实现"]
    end
    
    subgraph "peft/tuners/ (其他方法)"
        adalora["adalora/\nAdaLoraConfig + AdaLoraLayer"]
        ia3["ia3/"]
        boft["boft/"]
        vera["vera/"]
        p_tuning["p_tuning/"]
        prefix_tuning["prefix_tuning/"]
        promp_tuning["prompt_tuning/"]
        loha["loha/"]
        lokr["lokr/"]
        oft["oft/"]
        poly["poly/"]
        fourierft["fourierft/"]
        hra["hra/"]
        bone["bone/"]
        randlora["randlora/"]
    end
    
    config_py -->|"被继承"| lora_cfg
    config_py -->|"被继承"| adalora
    lora_cfg -->|"配置驱动"| lora_layer
    lora_layer -->|"变异策略"| variants
    variants -->|"DoRA实现"| dora
    peft_types -->|"枚举约束"| lora_cfg
    mapping_py -->|"注册映射"| lora_cfg
```
