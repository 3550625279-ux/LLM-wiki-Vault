#!/usr/bin/env bash
# allocate-address.sh - atomic creation-order address allocation for the vault.
#
# Reserves the next address of the form c-NNNNNN and increments the counter
# under a mkdir-based lock (cross-platform, no flock dependency).
#
# Usage:
#   ./scripts/allocate-address.sh           # prints the reserved address
#   ./scripts/allocate-address.sh --peek    # prints next value without incrementing
#   ./scripts/allocate-address.sh --rebuild # recomputes counter from max observed
#
# Exit codes:
#   0 - success
#   1 - lock acquisition failed
#   2 - vault-meta directory missing and cannot be created
#   3 - counter value corrupt or non-numeric

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VAULT_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"

# Defensive validation: ensure VAULT_ROOT contains expected structure
if [ ! -d "$VAULT_ROOT/wiki" ] && [ ! -d "$VAULT_ROOT/.vault-meta" ]; then
  echo "ERR: VAULT_ROOT resolution failed: $VAULT_ROOT" >&2
  echo "     Expected wiki/ or .vault-meta/ subdir." >&2
  exit 2
fi

COUNTER_FILE="${VAULT_ROOT}/.vault-meta/address-counter.txt"
LOCK_DIR="${VAULT_ROOT}/.vault-meta/.address.lock.d"
WIKI_DIR="${VAULT_ROOT}/wiki"

MODE="${1:-allocate}"

mkdir -p "$(dirname "$COUNTER_FILE")" || {
  echo "ERR: cannot create .vault-meta/" >&2
  exit 2
}

# Acquire exclusive lock via mkdir (atomic on all platforms)
acquire_lock() {
  local max_wait=50 waited=0
  while ! mkdir "$LOCK_DIR" 2>/dev/null; do
    sleep 0.1
    waited=$((waited + 1))
    [ "$waited" -ge "$max_wait" ] && {
      echo "ERR: could not acquire address allocator lock within 5s" >&2
      return 1
    }
  done
  echo "$$" > "$LOCK_DIR/.pid" 2>/dev/null
  return 0
}

release_lock() { rm -rf "$LOCK_DIR" 2>/dev/null; }

# Cleanup lock on exit
trap 'release_lock' EXIT

if ! acquire_lock; then
  exit 1
fi

scan_max_c_address() {
  if [ ! -d "$WIKI_DIR" ]; then
    echo 0
    return
  fi
  find "$WIKI_DIR" -type f -name '*.md' -print0 2>/dev/null \
    | xargs -0 awk '
        FNR == 1 { state = "pre"; next_is_fm = ($0 == "---") ? 1 : 0 }
        FNR == 1 && $0 == "---" { state = "fm"; next }
        state == "fm" && $0 == "---" { state = "body"; nextfile }
        state == "fm" && match($0, /^address:[[:space:]]+c-[0-9]{6}[[:space:]]*$/) {
          if (match($0, /c-[0-9]{6}/)) {
            print substr($0, RSTART, RLENGTH)
          }
        }
      ' 2>/dev/null \
    | sed 's/^c-0*//;s/^$/0/' \
    | sort -n \
    | tail -1 \
    | awk 'BEGIN{n=0} {n=$0} END{print (n+0)}'
}

read_or_recover_counter() {
  if [ ! -f "$COUNTER_FILE" ]; then
    local max_c
    max_c="$(scan_max_c_address)"
    echo $((max_c + 1)) > "$COUNTER_FILE"
    echo "INFO: counter file missing; recovered from vault scan, set to $((max_c + 1))" >&2
  fi
  local raw
  raw="$(cat "$COUNTER_FILE")"
  if ! [[ "$raw" =~ ^[0-9]+$ ]]; then
    echo "ERR: counter file content is not a positive integer: $raw" >&2
    exit 3
  fi
  echo "$raw"
}

case "$MODE" in
  --peek)
    # BUG-002 fix: pure read-only, never create or modify counter file
    if [ ! -f "$COUNTER_FILE" ]; then
      echo "ERR: counter file missing. Run --rebuild first to recover." >&2
      exit 3
    fi
    raw="$(cat "$COUNTER_FILE")"
    if ! [[ "$raw" =~ ^[0-9]+$ ]]; then
      echo "ERR: counter file corrupt: $raw" >&2; exit 3
    fi
    printf 'c-%06d\n' "$raw"
    ;;
  --rebuild)
    max_c="$(scan_max_c_address)"
    echo $((max_c + 1)) > "$COUNTER_FILE"
    echo "Counter rebuilt: next = $((max_c + 1))"
    ;;
  allocate|"")
    current="$(read_or_recover_counter)"
    next=$((current + 1))
    echo "$next" > "$COUNTER_FILE"
    printf 'c-%06d\n' "$current"
    ;;
  *)
    echo "ERR: unknown mode: $MODE" >&2
    echo "Usage: $0 [allocate|--peek|--rebuild]" >&2
    exit 3
    ;;
esac
