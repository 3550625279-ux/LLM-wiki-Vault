#!/usr/bin/env bash
# log-write.sh — PostToolUse(Write/Edit) 轻量写操作记录
# 由 .claude/settings.json PostToolUse hook 自动触发

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_FILE="$VAULT_ROOT/wiki/log.md"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

# 获取最近修改的文件（若有环境变量传入则用之）
MODIFIED_FILE="${CLAUDE_TOOL_OUTPUT_FILE:-unknown}"

# 只记录 wiki/ 目录内的写操作
if [[ "$MODIFIED_FILE" == *"wiki/"* ]]; then
  echo "  [$TIMESTAMP] write: $MODIFIED_FILE" >> "$LOG_FILE" 2>/dev/null || true
fi
