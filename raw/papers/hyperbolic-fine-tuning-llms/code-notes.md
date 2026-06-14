# 代码消化笔记：HypLoRA 实现与 δ-双曲性分析

> 基于 `code/hyp_lora_demo.py` 和 `code/hyperbolicity_analysis.py` 的逐段技术拆解。
> 两个脚本互补：前者演示**方法**（HypLoRA 如何工作），后者演示**理论**（为什么需要 HypLoRA）。

---

## 一、`hyp_lora_demo.py` — 方法实现拆解

### 1. Lorentz 内积（第19-25行）

```python
def lorentz_inner_product(x, y):
    return -x[..., 0] * y[..., 0] + (x[..., 1:] * y[..., 1:]).sum(dim=-1)
```

**数学本质**：Lorentz 内积 `⟨x,y⟩_L = -x₀y₀ + Σᵢ xᵢyᵢ` 是闵可夫斯基空间的标准内积。

**与欧氏内积的唯一区别**：第一个分量（时间维度 x₀）带负号。这个负号是双曲几何的根源——它让 `⟨x,x⟩_L = -K` 定义了一个"碗状"曲面而非球面。

**实现技巧**：`x[..., 0]` 取时间分量，`x[..., 1:]` 取空间分量，支持任意 batch/seq 维度。

---

### 2. 欧氏 → 双曲面投影（第28-40行）

```python
def proj_to_hyperboloid(x, K=1.0):
    spatial = x
    time = torch.sqrt(torch.sum(spatial ** 2, dim=-1, keepdim=True) + K)
    return torch.cat([time, spatial], dim=-1)
```

**推导过程**：
- 约束：`⟨x_H, x_H⟩_L = -K`
- 展开：`-x₀² + ‖x‖² = -K`
- 解出：`x₀ = √(‖x‖² + K)`（取正根，因为 Lorentz 模型要求 x₀ > 0）

**关键洞察**：这个投影是**唯一确定**的——给定任何欧氏向量 x，在双曲面上有且只有一个对应点。这是 HypLoRA 能工作的数学基础。

**数值注意**：`torch.sum(..., keepdim=True)` 保持维度，使广播正确工作。

---

### 3. 双曲面 → 欧氏投影（第43-54行）

```python
def proj_to_euclidean(x_H, K=1.0):
    time = x_H[..., 0:1]
    spatial = x_H[..., 1:]
    denom = time + torch.sqrt(torch.ones_like(time) * K)
    return (math.sqrt(K) / denom) * spatial
```

**这是对数映射的简化版本**。完整对数映射公式：

```
log_K(x) = acosh(-⟨x,o⟩_L / K) / √(⟨x,o⟩_L² - K²) · (x - ⟨x,o⟩_L · o)
```

其中 o 是原点 `(√K, 0, ..., 0)`。代码做了简化：当 K=1 时，`√K / (x₀ + √K)` 等价于对数映射的缩放因子。

**数值稳定性**：使用 `time + torch.sqrt(torch.ones_like(time) * K)` 而非直接用 `time`，避免 x₀ 接近 √K 时的除零风险。

---

### 4. StandardLoRA（第61-82行）

```python
class StandardLoRA(nn.Module):
    def __init__(self, in_dim, out_dim, rank=4):
        self.A = nn.Linear(in_dim, rank, bias=False)
        self.B = nn.Linear(rank, out_dim, bias=False)
        nn.init.zeros_(self.B.weight)
        nn.init.normal_(self.A.weight, std=1.0 / rank)
```

**设计要点**：
- `B 初始化为零`：训练开始时 ΔW = BA = 0，不改变原始模型输出。这是 LoRA 论文的核心设计。
- `A 初始化为 N(0, 1/r)`：方差随秩 r 缩放，保证 BA 的初始方差可控。
- `bias=False`：LoRA 只学习权重矩阵的低秩偏移，不学习偏置。

---

### 5. HypLoRA 核心（第89-141行）— 最重要的部分

forward 流程拆解为 5 步：

```python
# Step 1: 欧氏 → 双曲面（增加一个维度）
x_H = proj_to_hyperboloid(x, K)        # (batch, seq, d) → (batch, seq, d+1)

# Step 2: 提取空间分量（去掉时间维度）
x_H_s = x_H[:, :, 1:]                  # (batch, seq, d+1) → (batch, seq, d)

# Step 3: 低秩线性变换
transformed = self.B(self.A(x_H_s))    # (batch, seq, d) → (batch, seq, out_dim)

# Step 4: 重建双曲点（关键！）
norm_sq = torch.sum(transformed ** 2, dim=-1, keepdim=True)
time_comp = torch.sqrt(norm_sq + K)    # 新的时间分量
z_H = torch.cat([time_comp, transformed], dim=-1)  # (batch, seq, out_dim+1)

# Step 5: 双曲面 → 欧氏（减少一个维度）
z_E = proj_to_euclidean(z_H, K)        # (batch, seq, out_dim+1) → (batch, seq, out_dim)
```

**Step 4 是 HypLoRA 的核心创新**：不是简单地把 BAx 塞回欧氏空间，而是先用 `√(‖BAx‖²+K)` 构造一个合法的时间分量，确保输出仍在双曲面上。这个 `√(...)` 操作引入了关于 ‖x‖ 的非线性——这就是 Proposition 1 所说的"高阶范数依赖"。

**可学习曲率 K**：`self.K = nn.Parameter(torch.tensor(float(K)))`。论文发现 K=0.5 在算术推理上最优，K=1.0 在部分常识推理上更优。

---

### 6. 对比演示（第148-199行）

```python
low_freq_tokens = torch.randn(...) * 0.1   # 高频词，范数小
high_freq_tokens = torch.randn(...) * 1.0  # 低频词，范数大
```

**直觉**：论文发现高频 token（"the"、"is"）嵌入范数 ~0.35，低频 token（"apple"、"purple"）嵌入范数 ~0.57。这里用 `*0.1` vs `*1.0` 放大差异以演示效果。

**预期结果**：LoRA 的比值接近 1（线性变换对所有 token 施加相同幅度），HypLoRA 的比值 > 1（对大范数 token 施加更强变换）。

---

### 7. 层次表示演示（第206-278行）

```python
concept = torch.randn(1, d) * 0.2       # 概念层（范数小）
subcategory = torch.randn(3, d) * 0.5   # 子类层（范数中等）
instance = torch.randn(9, d) * 1.0      # 实例层（范数大）
```

**双曲距离公式**：`d(x,y) = acosh(-⟨x,y⟩_L / K)`

**预期结果**：
- 欧氏空间中，所有距离近似（树结构被"压平"）
- 双曲空间中，同一层级距离大（分离），不同层级距离小（聚集），体现树状层次

---

## 二、`hyperbolicity_analysis.py` — 理论验证拆解

### 1. Gromov 乘积（第29-36行）

```python
def gromov_product(a, b, w, dist_matrix):
    return 0.5 * (dist_matrix[a, w] + dist_matrix[b, w] - dist_matrix[a, b])
```

**直觉**：`[a,b]_w` 衡量 a 和 b 相对于 w 的"共同邻居程度"。值越大，a 和 b 在 w 看来越"接近"。

**几何意义**：在树上，如果 w 在 a 和 b 的最短路径上，`[a,b]_w = 0`。否则 `[a,b]_w > 0`，表示 w 到 a、b 的路径有"重叠"。

---

### 2. δ-双曲性计算（第39-81行）

```python
for _ in range(num_samples):
    pts = np.random.choice(n, size=4, replace=False)
    a, b, c, w = pts
    ac_w = gromov_product(a, c, w, dist_matrix)
    ab_w = gromov_product(a, b, w, dist_matrix)
    bc_w = gromov_product(b, c, w, dist_matrix)
    delta = ac_w - min(ab_w, bc_w)
    max_delta = max(max_delta, delta)
```

**四点条件**：`[a,c]_w ≥ min([a,b]_w, [b,c]_w) - δ`

**算法**：随机采样四点组合（最多 10000 次），计算最违反四点条件的程度作为 δ 的估计。

**计算复杂度**：O(S × 4)，其中 S 是采样次数。精确计算需要 O(n⁴)，所以采样是必要的。

**归一化**：`δ_rel = 2δ / diam(X)`，使不同尺度的空间可比。论文中 LLM 嵌入的 δ_rel ≈ 0.06-0.12。

---

### 3. 树距离矩阵生成（第84-136行）

```python
def generate_tree_distance_matrix(n, branching_factor=3):
    parent = {0: -1}
    nodes = [0]
    while len(nodes) < n:
        parent_node = nodes[np.random.randint(len(nodes))]
        child = node_id
        parent[child] = parent_node
```

**算法**：随机生长树——每次从已有节点中随机选一个作为父节点，挂上新节点。

**距离计算**：回溯到最近公共祖先（LCA），距离 = d(i, LCA) + d(j, LCA)。

**预期 δ = 0**：完美树满足四点条件的等号。

---

### 4. 球面距离（第146-158行）

```python
points = points / np.linalg.norm(points, axis=1, keepdims=True)
dots = np.clip(points @ points.T, -1, 1)
dist = np.arccos(dots)
```

**球面距离**：`d(x,y) = arccos(⟨x,y⟩)`，即大圆弧长。`np.clip` 防止浮点误差导致 arccos 输入越界。

**预期 δ ≈ 1**：球面是"最不像树"的空间。

---

### 5. 模拟 LLM 嵌入（第253-260行）

```python
tree_noise = tree_dist + np.random.randn(n, n) * 0.05 * tree_dist.max()
```

**关键技巧**：在完美树的距离矩阵上加 5% 的高斯噪声，模拟真实 LLM 嵌入（接近但不完全是树）。

**论文中 LLM 嵌入的 δ ≈ 0.06-0.12**，介于完美树 (0) 和随机空间 (0.62) 之间，更接近树。

---

### 6. 幂律 ↔ 双曲几何可视化（第165-219行）

三张子图的关系：

```
(a) 幂律分布 P(k) ∼ k^(-γ)     ← Token 频率的统计规律
(b) 双曲面积 A(r) ∼ e^r         ← 双曲空间的几何特性
(c) γ = 2/ζ + 1                 ← 理论桥梁：连接 (a) 和 (b)
```

**核心公式推导**：
- 双曲空间中，径向分布 p(r) ∼ e^(-ζr)
- 频率函数 k(r) ∼ e^(-r)
- 通过变量替换：P(k) ∼ k^(-(1-ζ))
- 即 γ = 1-ζ → ζ = 1-γ... 但论文用的参数化是 γ = 2/ζ + 1

这是因为 Krioukov et al. (2010) 的参数化不同。代码第208行标注了论文观测 γ ≈ 1.9 对应的 ζ = 2/0.9 ≈ 2.22。

---

### 7. 高阶效应演示（第300-356行）

```python
# HypLoRA 输出（简化模拟）
ba_x = B @ A @ x
K = 0.5
ba_norm = np.linalg.norm(ba_x)
time_comp = np.sqrt(ba_norm**2 + K)
scale = np.sqrt(K) / (time_comp + np.sqrt(K))
hyplora_out = scale * ba_x
```

**核心数学**：

1. `time_comp = √(‖BAx‖² + K)` — 重建时间分量（Step 4）
2. `scale = √K / (time_comp + √K)` — 对数映射缩放因子（Step 5）
3. `hyplora_out = scale × BAx` — 最终输出

**非线性来源**：`scale` 是 `‖BAx‖` 的函数。当 `‖BAx‖` 大时，`time_comp` 大，`scale` 小；当 `‖BAx‖` 小时，`scale` 接近 1/2。这就是 Proposition 1 的数值体现。

**预期结果**：HypLoRA 的输出范数与输入范数呈非线性关系（凹函数），而 LoRA 是严格线性的。

---

## 三、两份代码的关系

```
hyperbolicity_analysis.py          hyp_lora_demo.py
(理论动机)                         (方法实现)
     │                                  │
     │  "LLM 嵌入是双曲的"             │  "在双曲空间做 LoRA"
     │                                  │
     ├─ δ-双曲性计算 → δ ≈ 0.1          ├─ Lorentz 投影/对数映射
     ├─ 幂律分布可视化                   ├─ LLR 直接低秩变换
     ├─ γ = 2/ζ + 1 理论桥梁            ├─ LoRA vs HypLoRA 对比
     └─ 树/球面/随机空间对比              └─ 层次结构可视化
```

**因果链**：analysis 证明"嵌入是双曲的" → demo 实现"在双曲空间做适配" → 实验验证"HypLoRA 优于 LoRA"。

---

## 四、代码中的数学公式速查

| 公式 | 代码位置 | 含义 |
|------|----------|------|
| `⟨x,y⟩_L = -x₀y₀ + Σxᵢyᵢ` | `lorentz_inner_product` | Lorentz 内积 |
| `x₀ = √(‖x‖² + K)` | `proj_to_hyperboloid` | 欧氏→双曲面投影 |
| `z = √K / (x₀ + √K) · x_s` | `proj_to_euclidean` | 双曲面→欧氏投影 |
| `z_H = (√(‖BAx‖²+K), BAx)` | `HypLoRA.forward` Step 4 | LLR 直接 Lorentz 变换 |
| `[a,b]_w = ½(d(a,w)+d(b,w)-d(a,b))` | `gromov_product` | Gromov 乘积 |
| `[a,c]_w ≥ min([a,b]_w,[b,c]_w) - δ` | `compute_delta_hyperbolicity` | 四点条件 |
| `d(x,y) = acosh(-⟨x,y⟩_L / K)` | `lorentz_distance` | 双曲距离 |
| `P(k) ∼ k^(-γ), γ = 2/ζ+1` | `plot_power_law` | 幂律↔曲率关系 |

---

## 五、实现注意事项

1. **数值稳定性**：双曲计算中的 `acosh`、`sqrt` 可能溢出。代码用 `torch.clamp(..., min=1+1e-6)` 和 `np.clip` 防护。
2. **dtype 选择**：建议 float32 或 bfloat16，避免 float16 的精度不足。
3. **采样近似**：δ-双曲性的精确计算是 O(n⁴)，代码用 10000 次随机采样近似。
4. **HypLoRA 的额外开销**：forward 中多 2 次 `sqrt` + 1 次 `cat` + 1 次 `norm`，均为 O(N) 操作。
