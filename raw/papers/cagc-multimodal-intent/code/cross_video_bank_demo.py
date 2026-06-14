"""
CAGC Cross-video Bank 构建演示
===============================
本脚本演示了 CAGC 论文中 Cross-video Bank 的两阶段构建过程：
  Stage 1: 基于场景相似度（L2 距离）的初始构建
  Stage 2: 基于意图一致性的去噪过程

运行: python cross_video_bank_demo.py
依赖: numpy, matplotlib
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import List, Dict, Tuple
from dataclasses import dataclass, field

# ============================================================
# 数据结构定义
# ============================================================

@dataclass
class Video:
    """模拟一个视频样本"""
    id: int
    scene_feature: np.ndarray   # 视频级场景特征（帧均值池化后的结果）
    intent_label: int           # 意图标签 (0=负向, 1=正向)
    intent_name: str            # 意图名称

@dataclass
class CrossVideoBank:
    """Cross-video Bank: 存储每个视频对应的高质量跨视频集合"""
    # Stage 1 结果: Ω(v_i) = 场景相似的 Top-k 视频
    stage1_bank: Dict[int, List[int]] = field(default_factory=dict)
    # Stage 2 结果: Ω*(v_i) = 去噪后意图一致的视频
    stage2_bank: Dict[int, List[int]] = field(default_factory=dict)


# ============================================================
# Stage 1: 基于场景相似度的初始构建
# ============================================================

def compute_video_level_feature(frames: np.ndarray) -> np.ndarray:
    """
    论文 Eq.5: 视频级特征 = 帧特征的均值池化
    v̄_i = (1/F) * Σ v_{frame(j)}^i
    """
    return np.mean(frames, axis=0)


def compute_scene_similarity(v_i: np.ndarray, v_c: np.ndarray) -> float:
    """
    论文 Eq.6: 场景相似度 = L2 距离
    score = Σ (v_c^t - v_i^t)²
    距离越小 → 场景越相似
    """
    return np.sum((v_c - v_i) ** 2)


def build_stage1_bank(videos: List[Video], top_k: int = 5) -> Dict[int, List[int]]:
    """
    Stage 1: 对每个视频，找到场景最相似的 Top-k 视频
    注意：排除自身
    """
    bank = {}
    for v_i in videos:
        # 计算 v_i 与所有其他视频的场景相似度
        distances = []
        for v_c in videos:
            if v_c.id == v_i.id:
                continue
            dist = compute_scene_similarity(v_i.scene_feature, v_c.scene_feature)
            distances.append((v_c.id, dist))

        # 按距离排序，取 Top-k（距离最小 = 最相似）
        distances.sort(key=lambda x: x[1])
        top_k_ids = [vid for vid, _ in distances[:top_k]]
        bank[v_i.id] = top_k_ids

    return bank


# ============================================================
# Stage 2: 基于意图一致性的去噪
# ============================================================

def denoise_bank(videos: List[Video], stage1_bank: Dict[int, List[int]]) -> Dict[int, List[int]]:
    """
    Stage 2: 投票原则 — 只保留意图倾向一致的跨视频
    Ω*(v_i) = {v_c ∈ Ω(v_i) | intent(v_c) == intent(v_i)}

    直觉: 如果当前视频是正向意图（如"赞美"），
          只保留同样是正向意图的跨视频作为上下文。
    """
    video_map = {v.id: v for v in videos}
    stage2_bank = {}

    for v_id, cross_ids in stage1_bank.items():
        current_intent = video_map[v_id].intent_label
        # 投票筛选: 只保留意图标签相同的跨视频
        filtered = [cid for cid in cross_ids
                    if video_map[cid].intent_label == current_intent]
        stage2_bank[v_id] = filtered

    return stage2_bank


# ============================================================
# 可视化: Bank 构建前后对比
# ============================================================

def visualize_bank_construction(videos: List[Video],
                                 stage1_bank: Dict[int, List[int]],
                                 stage2_bank: Dict[int, List[int]]):
    """可视化两个阶段的 Bank 构建结果"""
    fig, axes = plt.subplots(1, 2, figsize=(16, 6))

    # 提取所有视频的场景特征（降维到 2D 用于可视化）
    features = np.array([v.scene_feature for v in videos])
    labels = np.array([v.intent_label for v in videos])

    for idx, (ax, bank, title) in enumerate(zip(
        axes,
        [stage1_bank, stage2_bank],
        ["Stage 1: 场景相似度筛选", "Stage 2: 意图一致性去噪"]
    )):
        # 绘制所有视频点
        scatter = ax.scatter(features[:, 0], features[:, 1],
                           c=labels, cmap='RdYlGn', s=100,
                           edgecolors='black', linewidth=0.5, zorder=5)

        # 高亮第一个视频及其跨视频
        target_id = videos[0].id
        target_feat = features[target_id]
        cross_ids = bank[target_id]

        # 绘制连线
        for cid in cross_ids:
            cross_feat = features[cid]
            color = 'green' if labels[cid] == labels[target_id] else 'red'
            ax.plot([target_feat[0], cross_feat[0]],
                   [target_feat[1], cross_feat[1]],
                   color=color, alpha=0.6, linewidth=2, zorder=3)

        # 标记目标视频
        ax.scatter([target_feat[0]], [target_feat[1]],
                  c='blue', s=200, marker='*', zorder=10,
                  label=f'目标视频 (id={target_id})')

        ax.set_title(f'{title}\n跨视频数: {len(cross_ids)}', fontsize=12)
        ax.set_xlabel('特征维度 1')
        ax.set_ylabel('特征维度 2')
        ax.legend(loc='upper right')
        ax.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig('bank_construction.png', dpi=150, bbox_inches='tight')
    plt.show()
    print("图片已保存: bank_construction.png")


# ============================================================
# CAT 渐进式注意力演示
# ============================================================

def demo_progressive_attention(query: np.ndarray,
                                cross_features: np.ndarray,
                                temperature: float = 0.7) -> List[np.ndarray]:
    """
    演示 CAT (Context-Augmented Transformer) 的渐进式注意力机制

    论文 Algorithm 1:
    for j = 1, ..., k*:
        K_c = h_c[1:j+1]       # 逐步扩展 Key
        M_j = softmax(Q·K^T / √d) · V
        M_j = mean(M_j)
    """
    k_star = len(cross_features)
    d = query.shape[-1]
    context_layers = []

    print("\n" + "=" * 60)
    print("CAT 渐进式注意力过程")
    print("=" * 60)

    for j in range(k_star):
        # 逐步扩展 K, V
        K = cross_features[:j + 1]    # 前 j+1 个跨视频
        V = K

        # 注意力计算: softmax(Q·K^T / √d) · V
        scores = query @ K.T / np.sqrt(d)

        # 数值稳定的 softmax
        scores_max = np.max(scores)
        exp_scores = np.exp(scores - scores_max)
        attn_weights = exp_scores / np.sum(exp_scores)

        # 加权求和
        M_j = attn_weights @ V

        context_layers.append(M_j.copy())

        print(f"  Step {j+1}: 引入跨视频 {j+1} 个, "
              f"注意力权重 = {attn_weights.round(3)}, "
              f"上下文范数 = {np.linalg.norm(M_j):.4f}")

    return context_layers


# ============================================================
# 对比学习损失演示
# ============================================================

def info_nce_loss(anchor: np.ndarray,
                   positives: np.ndarray,
                   negatives: np.ndarray,
                   temperature: float = 0.7) -> float:
    """
    论文 Eq.15-17: InfoNCE 对比损失

    L = -log[ Σ_{h+ ∈ P} exp(h_t · h+ / τ) /
              Σ_{h± ∈ P∪N} exp(h_t · h± / τ) ]
    """
    # 计算与正样本的相似度
    pos_sim = np.array([np.dot(anchor, p) / temperature for p in positives])
    # 计算与负样本的相似度
    neg_sim = np.array([np.dot(anchor, n) / temperature for n in negatives])

    # 拼接所有相似度
    all_sim = np.concatenate([pos_sim, neg_sim])

    # 数值稳定的 log-sum-exp
    max_sim = np.max(all_sim)
    log_sum_exp = max_sim + np.log(np.sum(np.exp(all_sim - max_sim)))

    # 正样本的 log-sum-exp
    log_pos = max_sim + np.log(np.sum(np.exp(pos_sim - max_sim)))

    loss = -(log_pos - log_sum_exp)
    return loss


def demo_contrastive_learning():
    """演示局部对比 vs 全局对比的差异"""
    np.random.seed(42)
    d = 8  # 特征维度

    # 模拟文本特征作为锚点
    anchor = np.random.randn(d)
    anchor = anchor / np.linalg.norm(anchor)

    # 模拟 mini-batch 内的正/负样本（局部对比）
    local_positives = [np.random.randn(d) for _ in range(3)]
    local_negatives = [np.random.randn(d) for _ in range(5)]

    # 模拟跨视频全局正/负样本（全局对比）
    # 全局特征包含跨视频上下文，更丰富
    global_positives = [np.random.randn(d) * 1.2 for _ in range(5)]
    global_negatives = [np.random.randn(d) * 0.8 for _ in range(8)]

    # 归一化
    for p in local_positives + local_negatives + global_positives + global_negatives:
        p /= np.linalg.norm(p)

    # 计算损失
    local_loss = info_nce_loss(anchor, local_positives, local_negatives)
    global_loss = info_nce_loss(anchor, global_positives, global_negatives)

    print("\n" + "=" * 60)
    print("对比学习损失演示")
    print("=" * 60)
    print(f"  局部对比损失 (mini-batch 内): {local_loss:.4f}")
    print(f"  全局对比损失 (跨数据集):      {global_loss:.4f}")
    print(f"  总损失 (α=0.02):              {local_loss + 0.02 * global_loss:.4f}")
    print()
    print("  说明: 全局对比的正/负样本包含跨视频上下文信息，")
    print("        提供了更丰富的对比信号。")


# ============================================================
# 主函数: 完整流程演示
# ============================================================

def main():
    np.random.seed(42)

    print("=" * 60)
    print("CAGC: Contextual Augmented Global Contrast 演示")
    print("=" * 60)

    # ----------------------------------------------------------
    # 1. 创建模拟数据
    # ----------------------------------------------------------
    print("\n[1] 创建模拟视频数据...")
    intent_names = {0: "负向 (Complain/Taunt)", 1: "正向 (Praise/Joke)"}

    videos = []
    for i in range(20):
        # 创建有聚类结构的场景特征
        intent = i % 2  # 交替正负向
        center = np.array([3.0, 2.0]) if intent == 1 else np.array([-1.0, -1.0])
        feature = center + np.random.randn(2) * 0.8

        videos.append(Video(
            id=i,
            scene_feature=feature,
            intent_label=intent,
            intent_name=intent_names[intent]
        ))
    print(f"  共创建 {len(videos)} 个模拟视频")

    # ----------------------------------------------------------
    # 2. Stage 1: 基于场景相似度构建 Bank
    # ----------------------------------------------------------
    print("\n[2] Stage 1: 基于场景相似度构建 Cross-video Bank...")
    top_k = 5
    stage1_bank = build_stage1_bank(videos, top_k=top_k)

    # 展示结果
    target = videos[0]
    print(f"  目标视频 id={target.id}, 意图={target.intent_name}")
    print(f"  Stage 1 跨视频 (Top-{top_k} 场景相似): {stage1_bank[target.id]}")
    cross_intents = [videos[cid].intent_name for cid in stage1_bank[target.id]]
    for cid, ci in zip(stage1_bank[target.id], cross_intents):
        print(f"    视频 {cid}: {ci}")

    # ----------------------------------------------------------
    # 3. Stage 2: 基于意图一致性去噪
    # ----------------------------------------------------------
    print("\n[3] Stage 2: 基于意图一致性去噪...")
    stage2_bank = denoise_bank(videos, stage1_bank)

    print(f"  去噪后跨视频: {stage2_bank[target.id]}")
    for cid in stage2_bank[target.id]:
        print(f"    视频 {cid}: {videos[cid].intent_name}")

    removed = len(stage1_bank[target.id]) - len(stage2_bank[target.id])
    print(f"  移除了 {removed} 个意图不一致的跨视频")

    # ----------------------------------------------------------
    # 4. CAT 渐进式注意力演示
    # ----------------------------------------------------------
    print("\n[4] CAT 渐进式注意力演示...")
    d = 8
    query = np.random.randn(d)
    query = query / np.linalg.norm(query)

    k_star = len(stage2_bank[target.id])
    cross_features = np.array([np.random.randn(d) for _ in range(k_star)])
    for cf in cross_features:
        cf /= np.linalg.norm(cf)

    context_layers = demo_progressive_attention(query, cross_features)

    # 最终上下文特征
    final_context = np.mean(context_layers, axis=0)
    print(f"\n  最终上下文特征范数: {np.linalg.norm(final_context):.4f}")

    # ----------------------------------------------------------
    # 5. 对比学习损失演示
    # ----------------------------------------------------------
    demo_contrastive_learning()

    # ----------------------------------------------------------
    # 6. 可视化
    # ----------------------------------------------------------
    print("\n[5] 生成可视化...")
    try:
        visualize_bank_construction(videos, stage1_bank, stage2_bank)
    except Exception as e:
        print(f"  可视化跳过 (需要图形界面): {e}")

    # ----------------------------------------------------------
    # 总结
    # ----------------------------------------------------------
    print("\n" + "=" * 60)
    print("演示总结")
    print("=" * 60)
    print("""
  CAGC 的三个核心组件:

  1. Cross-video Bank (两阶段构建)
     - Stage 1: L2 距离找场景相似的 Top-k 视频
     - Stage 2: 投票原则筛选意图一致的视频

  2. CAT (Context-Augmented Transformer)
     - 渐进式注意力: 逐步引入跨视频上下文
     - 从 1 个跨视频逐步扩展到 k* 个

  3. GCCL (Global Context-guided Contrastive Learning)
     - 局部对比: mini-batch 内的模态对齐
     - 全局对比: 跨数据集的上下文引导对比
     - 文本为锚点，其他模态为增强版本

  关键超参数:
     - Top-k = 5 (演示用，论文用 7)
     - 温度 τ = 0.7
     - α = β = 0.02
    """)


if __name__ == "__main__":
    main()
