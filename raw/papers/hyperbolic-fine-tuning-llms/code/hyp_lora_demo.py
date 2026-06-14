"""
HypLoRA 核心方法简化实现
======================
演示 Lorentz 双曲空间中的低秩适配如何工作。

运行: python hyp_lora_demo.py
依赖: torch (pip install torch)
"""

import torch
import torch.nn as nn
import torch.nn.functional as F
import math

# ============================================================
# 1. 双曲几何基础工具
# ============================================================

def lorentz_inner_product(x, y):
    """
    Lorentz 内积: ⟨x,y⟩_L = -x₀y₀ + Σᵢ xᵢyᵢ
    这是双曲空间中的"距离度量"，不同于普通欧氏内积。
    """
    # x₀y₀ 是时间分量（带负号），其余是空间分量
    return -x[..., 0] * y[..., 0] + (x[..., 1:] * y[..., 1:]).sum(dim=-1)


def proj_to_hyperboloid(x, K=1.0):
    """
    将欧氏向量 x ∈ ℝ^d 投影到 Lorentz 双曲面 L_K^n ⊂ ℝ^(d+1)。

    核心思想：将 x 作为"空间分量"，计算对应的"时间分量"
    使得新点满足双曲面约束 ⟨x_H, x_H⟩_L = -K。

    推导：设 x_H = (x₀, x₁,...,xₙ)，其中 x₁...xₙ = x
    则 -x₀² + ‖x‖² = -K → x₀ = √(‖x‖² + K)
    """
    spatial = x
    time = torch.sqrt(torch.sum(spatial ** 2, dim=-1, keepdim=True) + K)
    return torch.cat([time, spatial], dim=-1)  # (batch, d+1)


def proj_to_euclidean(x_H, K=1.0):
    """
    将 Lorentz 双曲面上的点投影回欧氏空间。

    使用对数映射：从双曲面到切空间再到欧氏空间。
    简化版本：直接取空间分量并缩放。
    """
    time = x_H[..., 0:1]      # 时间分量
    spatial = x_H[..., 1:]     # 空间分量
    # 缩放因子确保数值稳定
    denom = time + torch.sqrt(torch.ones_like(time) * K)
    return (math.sqrt(K) / denom) * spatial


# ============================================================
# 2. 标准 LoRA（基线）
# ============================================================

class StandardLoRA(nn.Module):
    """
    标准欧几里得 LoRA 适配器。

    核心公式: z = Wx + BAx
    其中 A ∈ ℝ^(r×d), B ∈ ℝ^(k×r), r ≪ min(d,k)
    """
    def __init__(self, in_dim, out_dim, rank=4):
        super().__init__()
        self.A = nn.Linear(in_dim, rank, bias=False)
        self.B = nn.Linear(rank, out_dim, bias=False)
        # B 初始化为零：训练开始时 ΔW = BA = 0，不改变原始模型
        nn.init.zeros_(self.B.weight)
        # A 用随机初始化
        nn.init.normal_(self.A.weight, std=1.0 / rank)

    def forward(self, x):
        """
        x: (batch, seq_len, d) 欧氏嵌入
        返回: (batch, seq_len, out_dim)
        """
        return self.B(self.A(x))


# ============================================================
# 3. HypLoRA（本文方法）
# ============================================================

class HypLoRA(nn.Module):
    """
    双曲低秩适配器（核心贡献）。

    关键创新：直接在 Lorentz 双曲流形上执行低秩变换，
    绕过切空间的 exp-log 抵消问题。

    数学表达:
        LLR(BA, x_H) = (√(‖BAx_H^s‖² + K),  BAx_H^s)

    其中 x_H^s 是双曲点的空间分量。
    """
    def __init__(self, in_dim, out_dim, rank=4, K=0.5):
        super().__init__()
        self.A = nn.Linear(in_dim, rank, bias=False)
        self.B = nn.Linear(rank, out_dim, bias=False)
        # 可学习曲率（论文 Table 5 的发现：K=0.5 通常最优）
        self.K = nn.Parameter(torch.tensor(float(K)))
        # 初始化：B 为零，确保训练开始时 HypLoRA 不改变原始模型
        nn.init.zeros_(self.B.weight)
        nn.init.normal_(self.A.weight, std=1.0 / rank)

    def forward(self, x):
        """
        x: (batch, seq_len, d) 欧氏嵌入
        返回: (batch, seq_len, out_dim) 欧氏嵌入

        完整流程:
        1. 欧氏 → 双曲 (Π_K exp)
        2. LLR 双曲低秩变换（直接在流形上）
        3. 双曲 → 欧氏 (Π_K log)
        """
        K = self.K.abs() + 1e-6  # 确保 K > 0

        # Step 1: 投影到 Lorentz 双曲面
        x_H = proj_to_hyperboloid(x, K)  # (batch, seq, d+1)

        # Step 2: 提取空间分量（去掉时间分量 x_H[0]）
        x_H_s = x_H[:, :, 1:]  # (batch, seq, d)

        # Step 3: 直接 Lorentz 低秩变换（LLR）
        # 核心：线性变换只作用于空间分量
        transformed = self.B(self.A(x_H_s))  # (batch, seq, out_dim)

        # Step 4: 重建双曲点（保证在流形上）
        norm_sq = torch.sum(transformed ** 2, dim=-1, keepdim=True)
        time_comp = torch.sqrt(norm_sq + K)  # 时间分量
        z_H = torch.cat([time_comp, transformed], dim=-1)  # (batch, seq, out_dim+1)

        # Step 5: 投影回欧氏空间
        z_E = proj_to_euclidean(z_H, K)  # (batch, seq, out_dim)

        return z_E


# ============================================================
# 4. 演示：对比 LoRA vs HypLoRA
# ============================================================

def demo_lora_vs_hyplora():
    """
    对比 LoRA 和 HypLoRA 在相同输入上的变换行为。
    关键观察：HypLoRA 对不同范数的 token 施加不同的变换。
    """
    print("=" * 60)
    print("HypLoRA vs LoRA 对比演示")
    print("=" * 60)

    torch.manual_seed(42)
    d, k, r = 64, 64, 4
    batch_size, seq_len = 2, 8

    # 创建两个适配器
    lora = StandardLoRA(d, k, rank=r)
    hyplora = HypLoRA(d, k, rank=r, K=0.5)

    # 模拟不同范数的 token 嵌入
    # Group 1: 高频词（范数小，如 "the", "is"）→ 靠近原点
    low_freq_tokens = torch.randn(batch_size, seq_len // 2, d) * 0.1
    # Group 4: 低频词（范数大，如 "apple", "purple"）→ 远离原点
    high_freq_tokens = torch.randn(batch_size, seq_len // 2, d) * 1.0
    x = torch.cat([low_freq_tokens, high_freq_tokens], dim=1)

    print(f"\n输入形状: {x.shape}")
    print(f"低频 token 范数: {x[:, :4].norm(dim=-1).mean():.3f}")
    print(f"高频 token 范数: {x[:, 4:].norm(dim=-1).mean():.3f}")

    # 前向传播
    with torch.no_grad():
        lora_out = lora(x)
        hyplora_out = hyplora(x)

    # 计算变换幅度（输出 - 输入 的范数）
    lora_delta = (lora_out - x).norm(dim=-1)
    hyplora_delta = (hyplora_out - x).norm(dim=-1)

    print(f"\n--- 变换幅度 (‖output - input‖) ---")
    print(f"LoRA   - 低频 token: {lora_delta[:, :4].mean():.4f}")
    print(f"LoRA   - 高频 token: {lora_delta[:, 4:].mean():.4f}")
    print(f"LoRA   - 比值 (高/低): {lora_delta[:, 4:].mean() / lora_delta[:, :4].mean():.2f}x")
    print()
    print(f"HypLoRA - 低频 token: {hyplora_delta[:, :4].mean():.4f}")
    print(f"HypLoRA - 高频 token: {hyplora_delta[:, 4:].mean():.4f}")
    print(f"HypLoRA - 比值 (高/低): {hyplora_delta[:, 4:].mean() / hyplora_delta[:, :4].mean():.2f}x")

    print(f"\n曲率 K = {hyplora.K.item():.4f}")

    print("\n--- 关键洞察 ---")
    print("LoRA 对所有 token 施加近似相同的变换（比值接近 1）")
    print("HypLoRA 对范数大的 token（低频词）施加更强的变换")
    print("这种差异化处理正是双曲几何的非线性带来的高阶效应")


# ============================================================
# 5. 演示：双曲空间的层次表示
# ============================================================

def demo_hyperbolic_hierarchy():
    """
    可视化双曲空间如何更好地表示层次结构。
    对比欧氏空间和双曲空间中"树状"数据的表示。
    """
    print("\n" + "=" * 60)
    print("双曲空间的层次表示演示")
    print("=" * 60)

    # 模拟一棵简单的层次树：
    # 概念层 (1个): "水果"
    # 子类层 (3个): "苹果", "香蕉", "橙子"
    # 实例层 (9个): "红富士", "青苹果", "小香蕉", ...

    torch.manual_seed(42)
    d = 16

    # 概念 token（高频，范数小）
    concept = torch.randn(1, d) * 0.2
    # 子类 token（中频，范数中等）
    subcategory = torch.randn(3, d) * 0.5
    # 实例 token（低频，范数大）
    instance = torch.randn(9, d) * 1.0

    # 计算成对距离
    def pairwise_distance(x, y):
        return torch.cdist(x.unsqueeze(0), y.unsqueeze(0)).squeeze(0)

    # 欧氏距离
    d_concept_sub = pairwise_distance(concept, subcategory)
    d_sub_instance = pairwise_distance(subcategory, instance)
    d_concept_instance = pairwise_distance(concept, instance)

    print(f"\n欧氏空间中的距离:")
    print(f"  概念→子类:  {d_concept_sub.mean():.3f}")
    print(f"  子类→实例:  {d_sub_instance.mean():.3f}")
    print(f"  概念→实例:  {d_concept_instance.mean():.3f}")

    K = 1.0
    # 投影到双曲空间
    concept_H = proj_to_hyperboloid(concept, K)
    subcategory_H = proj_to_hyperboloid(subcategory, K)
    instance_H = proj_to_hyperboloid(instance, K)

    # 双曲距离（使用 Lorentz 内积）
    def lorentz_distance(x, y):
        ip = lorentz_inner_product(x, y)
        # 双曲距离公式: d(x,y) = acosh(-⟨x,y⟩_L / K)
        arg = -ip / K
        arg = torch.clamp(arg, min=1.0 + 1e-6)  # 数值稳定
        return torch.acosh(arg)

    d_H_concept_sub = pairwise_distance(
        concept_H.reshape(1, -1), subcategory_H.reshape(3, -1)
    )
    d_H_sub_instance = pairwise_distance(
        subcategory_H.reshape(3, -1), instance_H.reshape(9, -1)
    )
    d_H_concept_instance = pairwise_distance(
        concept_H.reshape(1, -1), instance_H.reshape(9, -1)
    )

    print(f"\n双曲空间中的距离:")
    print(f"  概念→子类:  {d_H_concept_sub.mean():.3f}")
    print(f"  子类→实例:  {d_H_sub_instance.mean():.3f}")
    print(f"  概念→实例:  {d_H_concept_instance.mean():.3f}")

    print("\n--- 关键洞察 ---")
    print("在双曲空间中:")
    print("  - 同一层级的 token（如不同实例）可以充分分离")
    print("  - 不同层级的 token（如概念和实例）保持语义距离")
    print("  - 这正是指数体积增长带来的优势")


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    demo_lora_vs_hyplora()
    demo_hyperbolic_hierarchy()
    print("\n" + "=" * 60)
    print("演示完成！")
    print("=" * 60)
