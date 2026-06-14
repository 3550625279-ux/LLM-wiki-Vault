# 方法拆解：HypLoRA 算法详解

## 1. 整体架构

```
输入 x_E (欧氏空间, ℝ^d)
        │
        ▼
┌─────────────────────────┐
│  Π_K exp: 欧氏 → 双曲   │  指数映射 + 投影到 Lorentz 双曲面
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  LLR(BA, x_H)           │  直接 Lorentz 低秩变换
│  = (√(‖BAx_H^s‖²+K),   │
│     BAx_H^s)            │
└─────────┬───────────────┘
          │
          ▼
┌─────────────────────────┐
│  Π_K log: 双曲 → 欧氏   │  对数映射 + 投影回切空间
└─────────┬───────────────┘
          │
          ▼
输出 z_E (欧氏空间, ℝ^d)
```

## 2. 预备知识

### 2.1 Lorentz 双曲模型

n 维 Lorentz 双曲面，曲率 -1/K（K > 0）：

```
L_K^n = {x ∈ ℝ^(n+1) : ⟨x,x⟩_L = -K,  x₀ > 0}
```

其中 Lorentz 内积：

```
⟨x,y⟩_L = -x₀y₀ + Σᵢ xᵢyᵢ
```

直观理解：这是一个嵌入在 (n+1) 维欧氏空间中的 n 维"碗状"曲面。x₀ 是"时间"维度（始终为正），x₁...xₙ 是"空间"维度。

### 2.2 切空间

在双曲面上的点 x 处的切空间：

```
T_x L_K^n = {u ∈ ℝ^(n+1) : ⟨u,x⟩_L = 0}
```

切空间是双曲面在该点的"平面近似"。

### 2.3 指数映射与对数映射

- **指数映射** Π_K exp_x：将切空间中的向量"推"到双曲面上
- **对数映射** Π_K log_x：将双曲面上的点"拉"回切空间

两者互逆：log_K(exp_K(x)) = x，exp_K(log_K(x)) = x

## 3. 核心算法：直接 Lorentz 低秩变换（LLR）

### 3.1 标准 LoRA（回顾）

```
z = Wx + BAx
```

其中 A ∈ ℝ^(r×d)，B ∈ ℝ^(k×r)，r ≪ min(d,k)。

### 3.2 为什么不能简单把 LoRA 搬到双曲空间？

如果用传统双曲神经网络的方法：

```
1. x_E → exp 到双曲: x_H = Π_K exp(x_E)
2. x_H → log 到切空间: u = Π_K log(x_H)     # u = x_E（因为 exp 和 log 互逆！）
3. 在切空间做线性变换: v = BA·u = BA·x_E
4. v → exp 到双曲: w = Π_K exp(v)
5. w → log 回欧氏: z_E = Π_K log(w)          # z_E ≈ BA·x_E
```

**关键问题**：步骤 1→2 的 exp→log 完全抵消，步骤 4→5 的 exp→log 也完全抵消。整个序列退化为 z_E ≈ BA·x_E，和原始 LoRA 没有区别。

### 3.3 HypLoRA 的解法

直接在双曲面上做变换，不经过切空间：

```python
def hyp_lora(x_E, A, B, K):
    """
    x_E: 欧氏输入 (batch, d)
    A, B: LoRA 权重矩阵
    K: 双曲曲率参数
    """
    # Step 1: 投影到双曲空间
    x_H = proj_to_hyperboloid(x_E, K)        # (batch, d+1)
    
    # Step 2: 提取空间分量（去掉时间分量）
    x_H_s = x_H[:, 1:]                        # (batch, d)
    
    # Step 3: 低秩线性变换（只作用于空间分量）
    transformed = B @ A @ x_H_s               # (batch, k)
    
    # Step 4: 重新构建双曲点（保证在流形上）
    norm_sq = torch.sum(transformed ** 2, dim=-1, keepdim=True)
    time_comp = torch.sqrt(norm_sq + K)       # (batch, 1)
    z_H = torch.cat([time_comp, transformed], dim=-1)  # (batch, d+1)
    
    # Step 5: 投影回欧氏空间
    z_E = proj_to_euclidean(z_H, K)           # (batch, d)
    
    return z_E
```

### 3.4 LLR 数学表达

```
LLR(BA, x_H) = (√(‖BA x_H^s‖² + K),  BA x_H^s)
```

其中 x_H^s = x_H[1:]（空间分量）。

**验证**：新点 z_H 满足 ⟨z_H, z_H⟩_L = -K，确实在双曲面上：

```
⟨z_H, z_H⟩_L = -(√(‖BAx_H^s‖²+K))² + ‖BAx_H^s‖²
              = -(‖BAx_H^s‖²+K) + ‖BAx_H^s‖²
              = -K  ✓
```

## 4. 命题 1：为什么 HypLoRA 更强

### 直觉

由于双曲操作的非线性（平方根、范数计算），HypLoRA 的等效变换不再是简单的线性变换 BAx，而是：

```
z ≈ BAx + f(‖x‖₂) · higher_order_terms(x)
```

其中 f(‖x‖₂) 是关于输入范数的函数。

### 含义

- 对于范数小的 token（高频词如 "the"）：高阶项贡献小，变换接近标准 LoRA
- 对于范数大的 token（低频词如 "apple"）：高阶项贡献大，获得更丰富的变换

这种**自适应**的处理方式正是语言层次结构所需要的。

## 5. 实现注意事项

### 5.1 数值稳定性

双曲几何中的计算容易出现数值问题：
- √(‖BAx_H^s‖² + K) 需要确保根号内非负
- 指数映射中的 sinh/cosh 可能溢出
- 建议使用 float32 或 bfloat16，避免 float16

### 5.2 曲率选择

论文实验了固定曲率和可学习曲率：
- Gemma3-4B：K=0.5 在算术推理上最优
- LLaMA3-8B / Qwen2.5-7B：K=0.5 在算术推理上最优，K=1.0 在常识推理上部分更优
- 建议：从 K=0.5 开始，根据任务调整

### 5.3 参数初始化

A 矩阵用随机高斯初始化（σ = 1/r），B 矩阵初始化为零。这确保训练开始时 HypLoRA 的输出等于原始模型输出。

### 5.4 与其他 LoRA 变体的组合

HypLoRA 的 LLR 变换可以替换任何 LoRA 变体中的线性变换部分：
- HypLoRA + LoRA+：使用 LoRA+ 的学习率策略
- HypLoRA + DoRA：结合权重分解
- HypLoRA + AdaLoRA：自适应秩分配

## 6. 伪代码

```python
class HypLoRA(nn.Module):
    def __init__(self, in_dim, out_dim, rank, K=0.5):
        super().__init__()
        self.A = nn.Linear(in_dim, rank, bias=False)
        self.B = nn.Linear(rank, out_dim, bias=False)
        self.K = nn.Parameter(torch.tensor(K))  # 可学习曲率
        nn.init.zeros_(self.B.weight)
    
    def forward(self, x):
        # x: (batch, seq_len, d) 欧氏嵌入
        
        # 1. Lorentz 投影: 欧氏 → 双曲
        x_s = x  # 空间分量
        x_0 = torch.sqrt(torch.sum(x_s**2, dim=-1, keepdim=True) + self.K)
        x_H = torch.cat([x_0, x_s], dim=-1)  # (batch, seq, d+1)
        
        # 2. 提取空间分量做低秩变换
        x_H_s = x_H[:, :, 1:]  # (batch, seq, d)
        transformed = self.B(self.A(x_H_s))  # (batch, seq, out_dim)
        
        # 3. 重建双曲点
        norm_sq = torch.sum(transformed**2, dim=-1, keepdim=True)
        time_comp = torch.sqrt(norm_sq + self.K)
        z_H = torch.cat([time_comp, transformed], dim=-1)
        
        # 4. 投影回欧氏空间
        # Π_K log: 从双曲面到切空间再到欧氏
        z_0 = z_H[:, :, 0:1]
        z_s = z_H[:, :, 1:]
        denom = z_0 + torch.sqrt(self.K)
        z_E = (torch.sqrt(self.K) / denom) * z_s
        
        return z_E
```
