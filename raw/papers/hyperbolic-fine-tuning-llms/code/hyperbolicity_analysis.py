"""
δ-双曲性分析与可视化
====================
演示如何计算和理解 δ-双曲性，以及幂律分布与双曲几何的关系。

运行: python hyperbolicity_analysis.py
依赖: numpy, matplotlib (pip install numpy matplotlib)
"""

import numpy as np
import math
import os

# 尝试导入 matplotlib，如果没有则跳过可视化
try:
    import matplotlib
    matplotlib.use('Agg')  # 非交互式后端
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("警告: matplotlib 未安装，跳过可视化（pip install matplotlib）")


# ============================================================
# 1. δ-双曲性计算
# ============================================================

def gromov_product(a, b, w, dist_matrix):
    """
    Gromov 乘积: [a,b]_w = ½(d(a,w) + d(b,w) - d(a,b))

    直觉：衡量 a 和 b 相对于 w 的"共同邻居程度"。
    值越大，说明 a 和 b 在 w 看来越"接近"。
    """
    return 0.5 * (dist_matrix[a, w] + dist_matrix[b, w] - dist_matrix[a, b])


def compute_delta_hyperbolicity(dist_matrix):
    """
    计算度量空间的 δ-双曲性（四点条件）。

    对于任意四点 a, b, c, w:
        [a,c]_w ≥ min([a,b]_w, [b,c]_w) - δ

    δ 越小，空间越像树。

    返回: (δ 值, 相对 δ = 2δ/diam)
    """
    n = dist_matrix.shape[0]
    if n < 4:
        return 0.0, 0.0

    diameter = dist_matrix.max()
    if diameter == 0:
        return 0.0, 0.0

    max_delta = 0.0

    # 遍历所有四点组合（n 较大时用采样）
    indices = np.arange(n)
    num_samples = min(10000, n * (n-1) * (n-2) * (n-3) // 24)

    for _ in range(num_samples):
        # 随机选择四个不同的点
        pts = np.random.choice(n, size=4, replace=False)
        a, b, c, w = pts

        # 计算三个 Gromov 乘积
        ac_w = gromov_product(a, c, w, dist_matrix)
        ab_w = gromov_product(a, b, w, dist_matrix)
        bc_w = gromov_product(b, c, w, dist_matrix)

        # 四点条件的违反程度
        delta = ac_w - min(ab_w, bc_w)
        max_delta = max(max_delta, delta)

    # 归一化
    delta_rel = 2 * max_delta / diameter if diameter > 0 else 0.0

    return max_delta, delta_rel


def generate_tree_distance_matrix(n, branching_factor=3):
    """
    生成树结构的成对距离矩阵。
    树的 δ-双曲性 = 0（完美树）。
    """
    # 生成随机树
    parent = {0: -1}
    nodes = [0]
    node_id = 1

    while len(nodes) < n:
        parent_node = nodes[np.random.randint(len(nodes))]
        child = node_id
        parent[child] = parent_node
        nodes.append(child)
        node_id += 1
        if node_id >= n:
            break

    # 计算树上距离
    dist = np.zeros((n, n))
    for i in range(n):
        for j in range(i+1, n):
            # 回溯到共同祖先
            path_i = set()
            node = i
            while node != -1:
                path_i.add(node)
                node = parent[node]

            node = j
            depth = 0
            while node not in path_i:
                node = parent[node]
                depth += 1

            lca = node
            d_i = 0
            node = i
            while node != lca:
                node = parent[node]
                d_i += 1

            d_j = 0
            node = j
            while node != lca:
                node = parent[node]
                d_j += 1

            dist[i, j] = d_i + d_j
            dist[j, i] = d_i + d_j

    return dist


def generate_random_distance_matrix(n):
    """生成随机度量空间的成对距离矩阵。"""
    points = np.random.randn(n, 10)  # 10维随机点
    dist = np.linalg.norm(points[:, None] - points[None, :], axis=-1)
    return dist


def generate_sphere_distance_matrix(n, dim=3):
    """
    生成球面上的成对距离矩阵。
    球面的 δ-双曲性 ≈ 1（远离树结构）。
    """
    # 在单位球面上生成随机点
    points = np.random.randn(n, dim)
    points = points / np.linalg.norm(points, axis=1, keepdims=True)

    # 球面距离: d(x,y) = arccos(⟨x,y⟩)
    dots = np.clip(points @ points.T, -1, 1)
    dist = np.arccos(dots)
    return dist


# ============================================================
# 2. 幂律分布与双曲几何
# ============================================================

def plot_power_law_and_hyperbolicity():
    """
    可视化幂律分布与双曲几何的数学关系。
    """
    if not HAS_MATPLOTLIB:
        print("跳过可视化（matplotlib 未安装）")
        return

    fig, axes = plt.subplots(1, 3, figsize=(15, 5))

    # (a) 幂律分布
    ax = axes[0]
    k = np.logspace(0, 3, 100)
    for gamma in [1.5, 1.9, 2.5]:
        P_k = k ** (-gamma)
        ax.loglog(k, P_k, label=f'γ = {gamma}', linewidth=2)
    ax.set_xlabel('Token 频率 k (log)', fontsize=12)
    ax.set_ylabel('概率 P(k) (log)', fontsize=12)
    ax.set_title('(a) 幂律分布 P(k) ∼ k^(-γ)', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # (b) 双曲空间的指数体积增长
    ax = axes[1]
    r = np.linspace(0, 5, 100)
    # 欧氏面积
    euclidean_area = np.pi * r ** 2
    # 双曲面积（Poincaré 圆盘）
    hyperbolic_area = 2 * np.pi * (np.cosh(r) - 1)
    ax.plot(r, euclidean_area, 'b-', label='欧氏面积 ∝ r²', linewidth=2)
    ax.plot(r, hyperbolic_area, 'r-', label='双曲面积 ∝ e^r', linewidth=2)
    ax.set_xlabel('半径 r', fontsize=12)
    ax.set_ylabel('面积', fontsize=12)
    ax.set_title('(b) 面积增长: 欧氏 vs 双曲', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    # (c) γ 与曲率 ζ 的关系
    ax = axes[2]
    zeta = np.linspace(0.1, 2, 100)
    gamma = 2 / zeta + 1
    ax.plot(zeta, gamma, 'g-', linewidth=2)
    ax.axhline(y=1.9, color='r', linestyle='--', label='论文观测 γ ≈ 1.9', linewidth=1.5)
    ax.axvline(x=2/0.9, color='r', linestyle=':', alpha=0.5, label=f'ζ = {2/0.9:.2f}')
    ax.set_xlabel('曲率参数 ζ', fontsize=12)
    ax.set_ylabel('幂律指数 γ', fontsize=12)
    ax.set_title('(c) γ = 2/ζ + 1', fontsize=13)
    ax.legend(fontsize=10)
    ax.grid(True, alpha=0.3)

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'power_law_hyperbolicity.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"已保存: {output_path}")
    plt.close()


def plot_delta_hyperbolicity_comparison():
    """
    可视化不同度量空间的 δ-双曲性对比。
    """
    if not HAS_MATPLOTLIB:
        print("跳过可视化（matplotlib 未安装）")
        return

    print("\n计算不同空间的 δ-双曲性...")
    n = 50  # 点数（小一点确保速度）

    results = {}

    # 树结构
    print("  - 树结构...")
    tree_dist = generate_tree_distance_matrix(n)
    delta, delta_rel = compute_delta_hyperbolicity(tree_dist)
    results['树结构'] = (delta, delta_rel)

    # 球面
    print("  - 球面空间...")
    sphere_dist = generate_sphere_distance_matrix(n)
    delta, delta_rel = compute_delta_hyperbolicity(sphere_dist)
    results['球面空间'] = (delta, delta_rel)

    # 随机图
    print("  - 随机度量空间...")
    random_dist = generate_random_distance_matrix(n)
    delta, delta_rel = compute_delta_hyperbolicity(random_dist)
    results['随机空间'] = (delta, delta_rel)

    # 模拟 LLM 嵌入（δ ≈ 0.1）
    print("  - 模拟 LLM 嵌入...")
    # 在树结构上加噪声，模拟 LLM 嵌入
    tree_noise = tree_dist + np.random.randn(n, n) * 0.05 * tree_dist.max()
    tree_noise = (tree_noise + tree_noise.T) / 2
    np.fill_diagonal(tree_noise, 0)
    delta, delta_rel = compute_delta_hyperbolicity(tree_noise)
    results['模拟LLM嵌入'] = (delta, delta_rel)

    # 可视化
    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    names = list(results.keys())
    deltas = [results[n][0] for n in names]
    delta_rels = [results[n][1] for n in names]

    colors = ['#2ecc71', '#e74c3c', '#95a5a6', '#3498db']

    ax = axes[0]
    bars = ax.bar(names, deltas, color=colors, edgecolor='black', alpha=0.8)
    ax.set_ylabel('δ 值', fontsize=12)
    ax.set_title('δ-双曲性对比（绝对值）', fontsize=13)
    ax.grid(True, alpha=0.3, axis='y')
    for bar, val in zip(bars, deltas):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontsize=10)

    ax = axes[1]
    bars = ax.bar(names, delta_rels, color=colors, edgecolor='black', alpha=0.8)
    ax.set_ylabel('相对 δ 值', fontsize=12)
    ax.set_title('δ-双曲性对比（相对值 = 2δ/diam）', fontsize=13)
    ax.grid(True, alpha=0.3, axis='y')
    for bar, val in zip(bars, delta_rels):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.01,
                f'{val:.3f}', ha='center', va='bottom', fontsize=10)

    plt.tight_layout()
    output_path = os.path.join(os.path.dirname(__file__), '..', 'delta_hyperbolicity.png')
    plt.savefig(output_path, dpi=150, bbox_inches='tight')
    print(f"已保存: {output_path}")
    plt.close()


# ============================================================
# 3. HypLoRA 高阶效应演示
# ============================================================

def demo_higher_order_effect():
    """
    演示 HypLoRA 的高阶范数依赖效应。
    对比 LoRA（线性）和 HypLoRA（非线性）在不同范数输入上的行为。
    """
    print("\n" + "=" * 60)
    print("HypLoRA 高阶效应演示")
    print("=" * 60)

    # 模拟 LoRA 和 HypLoRA 的等效变换
    # LoRA: z = BAx（线性）
    # HypLoRA: z ≈ BAx + f(‖x‖) · higher_order(x)（非线性）

    np.random.seed(42)
    d = 64
    r = 4

    # 低秩矩阵
    A = np.random.randn(r, d) * 0.1
    B = np.random.randn(d, r) * 0.1

    # 不同范数的输入
    norms = np.linspace(0.1, 3.0, 20)
    lora_outputs = []
    hyplora_outputs = []

    for norm in norms:
        # 创建指定范数的输入
        x = np.random.randn(d)
        x = x / np.linalg.norm(x) * norm

        # LoRA 输出
        lora_out = B @ A @ x
        lora_outputs.append(np.linalg.norm(lora_out))

        # HypLoRA 输出（简化模拟）
        # LLR 的核心: (√(‖BAx‖² + K), BAx)
        # 投影回欧氏后: z = √K / (√(‖BAx‖²+K) + √K) * BAx
        ba_x = B @ A @ x
        K = 0.5
        ba_norm = np.linalg.norm(ba_x)
        time_comp = np.sqrt(ba_norm**2 + K)
        scale = np.sqrt(K) / (time_comp + np.sqrt(K))
        hyplora_out = scale * ba_x
        hyplora_outputs.append(np.linalg.norm(hyplora_out))

    print(f"\n输入范数 → 输出范数 (LoRA vs HypLoRA):")
    print(f"{'输入范数':>10} | {'LoRA 输出':>12} | {'HypLoRA 输出':>14} | {'比值':>8}")
    print("-" * 55)
    for i in range(0, len(norms), 4):
        print(f"{norms[i]:>10.2f} | {lora_outputs[i]:>12.4f} | {hyplora_outputs[i]:>14.4f} | "
              f"{hyplora_outputs[i]/lora_outputs[i]:>8.3f}")

    print("\n--- 关键洞察 ---")
    print("LoRA: 输出范数与输入范数成正比（线性关系）")
    print("HypLoRA: 输出范数受到双曲几何的非线性调节")
    print("这种调节使得不同"重要性"的 token 获得差异化的变换")


# ============================================================
# 主程序
# ============================================================

if __name__ == "__main__":
    print("=" * 60)
    print("δ-双曲性分析与可视化")
    print("=" * 60)

    plot_power_law_and_hyperbolicity()
    plot_delta_hyperbolicity_comparison()
    demo_higher_order_effect()

    print("\n" + "=" * 60)
    print("分析完成！")
    print("=" * 60)
