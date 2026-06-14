#!/usr/bin/env bash
# log-write.sh - PostToolUse(Write/Edit) lightweight write-operation log.
# BUG-008 fix: mkdir-based lock (cross-platform, no flock).

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
LOG_FILE="$VAULT_ROOT/log.md"
LOG_LOCK_DIR="$VAULT_ROOT/.vault-meta/.log.lock.d"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M:%S')

acquire_log_lock() {
  local max_wait="${1:-10}" waited=0 max_ticks=$((max_wait * 10))
  mkdir -p "$VAULT_ROOT/.vault-meta" 2>/dev/null
  while ! mkdir "$LOG_LOCK_DIR" 2>/dev/null; do
    sleep 0.1; waited=$((waited + 1))
    [ "$waited" -ge "$max_ticks" ] && return 1
  done
  echo "$$" > "$LOG_LOCK_DIR/.pid" 2>/dev/null
  return 0
}
release_log_lock() { rm -rf "$LOG_LOCK_DIR" 2>/dev/null; }

MODIFIED_FILE="${CLAUDE_TOOL_OUTPUT_FILE:-unknown}"

if [[ "$MODIFIED_FILE" == *"wiki/"* ]]; then
  if acquire_log_lock 10; then
    echo "  [$TIMESTAMP] write: $MODIFIED_FILE" >> "$LOG_FILE" 2>/dev/null
    release_log_lock
  fi
fi
