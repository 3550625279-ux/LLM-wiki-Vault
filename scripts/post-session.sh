#!/usr/bin/env bash
# post-session.sh — 会话结束自动封印脚本
# 由 .claude/settings.json Stop hook 自动触发
# 手动运行: bash scripts/post-session.sh

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$VAULT_ROOT/wiki"
HOT_FILE="$WIKI_DIR/hot.md"
LOG_FILE="$WIKI_DIR/log.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

echo "=== post-session: $TIMESTAMP ==="

# ── 确保 log.md 存在 ──────────────────────────────────────────────────────────
if [[ ! -f "$LOG_FILE" ]]; then
  echo "# Wiki Log" > "$LOG_FILE"
  echo "" >> "$LOG_FILE"
  echo "格式: ## [YYYY-MM-DD HH:MM] verb | Title" >> "$LOG_FILE"
  echo "" >> "$LOG_FILE"
fi

# ── 追加会话结束条目 ──────────────────────────────────────────────────────────
cat >> "$LOG_FILE" << EOF

## [$TIMESTAMP] session-end | 会话封印
- hook: Stop
- vault: $VAULT_ROOT
- hot_file_exists: $([ -f "$HOT_FILE" ] && echo "yes" || echo "no")
EOF

echo "✅ 追加 log.md 完成"

# ── 统计本次会话变更 ──────────────────────────────────────────────────────────
NEW_COUNT=$(find "$WIKI_DIR" -name "*.md" -newer "$HOT_FILE" 2>/dev/null | wc -l || echo 0)
echo "📊 本次会话新增/修改页面: $NEW_COUNT"

# ── 若节点 > 5，提醒更新 overview.md ─────────────────────────────────────────
if [[ "$NEW_COUNT" -gt 5 ]]; then
  echo "⚠️  节点变更 > 5，建议更新 wiki/overview.md 统计数字"
fi

echo "=== post-session 完成 ==="
