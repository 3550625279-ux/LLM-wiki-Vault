#!/usr/bin/env bash
# post-session.sh - session-end seal script
# Triggered by .claude/settings.json Stop hook
# BUG-008 fix: mkdir-based lock (cross-platform, no flock).

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$VAULT_ROOT/wiki"
HOT_FILE="$WIKI_DIR/hot.md"
LOG_FILE="$VAULT_ROOT/log.md"
LOG_LOCK_DIR="$VAULT_ROOT/.vault-meta/.log.lock.d"
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')

acquire_log_lock() {
  local max_wait="${1:-10}"
  local waited=0
  local max_ticks=$((max_wait * 10))
  mkdir -p "$VAULT_ROOT/.vault-meta" 2>/dev/null
  while ! mkdir "$LOG_LOCK_DIR" 2>/dev/null; do
    sleep 0.1
    waited=$((waited + 1))
    [ "$waited" -ge "$max_ticks" ] && return 1
  done
  echo "$$" > "$LOG_LOCK_DIR/.pid" 2>/dev/null
  return 0
}

release_log_lock() { rm -rf "$LOG_LOCK_DIR" 2>/dev/null; }

echo "=== post-session: $TIMESTAMP ==="

if [[ ! -f "$LOG_FILE" ]]; then
  echo "# Wiki Log" > "$LOG_FILE"
  echo "" >> "$LOG_FILE"
  echo "Format: ## [YYYY-MM-DD HH:MM] verb | Title" >> "$LOG_FILE"
  echo "" >> "$LOG_FILE"
fi

if acquire_log_lock 10; then
  cat >> "$LOG_FILE" << EOF

## [$TIMESTAMP] session-end | Seal
- hook: Stop
- vault: $VAULT_ROOT
- hot_file_exists: $([ -f "$HOT_FILE" ] && echo "yes" || echo "no")
EOF
  release_log_lock
else
  echo "WARN: could not acquire log lock, session-end entry skipped" >&2
fi

echo "Done: log.md updated"

NEW_COUNT=$(find "$WIKI_DIR" -name "*.md" -newer "$HOT_FILE" 2>/dev/null | wc -l || echo 0)
echo "Pages modified this session: $NEW_COUNT"

if [[ "$NEW_COUNT" -gt 5 ]]; then
  echo "WARNING: >5 pages changed, consider updating wiki/overview.md"
fi

echo "=== post-session complete ==="
