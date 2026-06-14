#!/usr/bin/env bash
# align-check.sh — 无 MCP 知识对齐检索脚本
# 用法: bash scripts/align-check.sh "查询关键词"
# 输出: 候选页面列表 + 匹配行摘要

set -euo pipefail

VAULT_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
WIKI_DIR="$VAULT_ROOT/wiki"
QUERY="${1:-}"

if [[ -z "$QUERY" ]]; then
  echo "用法: bash scripts/align-check.sh '查询关键词'" >&2
  exit 1
fi

echo "=== align-check: '$QUERY' ==="
echo ""

# ── Step 1: hot.md 快速扫描 ──────────────────────────────────────────────────
echo "── [1] hot.md 热缓存 ──"
if [[ -f "$WIKI_DIR/hot.md" ]]; then
  if grep -qi "$QUERY" "$WIKI_DIR/hot.md"; then
    echo "✅ 命中 hot.md:"
    grep -in "$QUERY" "$WIKI_DIR/hot.md" | head -5
  else
    echo "❌ hot.md 未命中"
  fi
else
  echo "⚠️  hot.md 不存在"
fi
echo ""

# ── Step 2: concepts-idx.md 精确搜索 ─────────────────────────────────────────
echo "── [2] wiki/concepts-idx.md 导航 ──"
if [[ -f "$WIKI_DIR/concepts-idx.md" ]]; then
  if grep -qi "$QUERY" "$WIKI_DIR/concepts-idx.md"; then
    echo "✅ 命中 concepts-idx.md:"
    grep -in "$QUERY" "$WIKI_DIR/concepts-idx.md" | head -10
  else
    echo "❌ concepts-idx.md 未命中"
  fi
else
  echo "⚠️  concepts-idx.md 不存在"
fi
echo ""

# ── Step 3: 全库 grep（标题 + related 字段）──────────────────────────────────
echo "── [3] 全库 grep 兜底 ──"
CANDIDATES=$(grep -rli "$QUERY" "$WIKI_DIR" --include="*.md" 2>/dev/null | grep -v "hot.md\|log.md\|concepts-idx.md" | head -8 || true)

if [[ -n "$CANDIDATES" ]]; then
  echo "✅ 找到以下候选页面:"
  echo ""
  while IFS= read -r FILE; do
    REL_PATH="${FILE#$VAULT_ROOT/}"
    TITLE=$(grep -m1 "^title:" "$FILE" 2>/dev/null | sed 's/title: *//' | tr -d '"' || basename "$FILE" .md)
    STATUS=$(grep -m1 "^status:" "$FILE" 2>/dev/null | sed 's/status: *//' || echo "unknown")
    MATCH_LINES=$(grep -in "$QUERY" "$FILE" | head -3 | sed 's/^/  /')
    echo "📄 $REL_PATH"
    echo "   标题: $TITLE | 状态: $STATUS"
    echo "$MATCH_LINES"
    echo ""
  done <<< "$CANDIDATES"
else
  echo "❌ 全库无匹配 → 确认为知识缺口"
  echo ""
  echo "建议: ingest 相关资料 或 autoresearch '$QUERY'"
fi

# ── Step 4: related:: 语义边搜索 ─────────────────────────────────────────────
echo "── [4] 语义边搜索 (depends_on/corrects/extends) ──"
SEMANTIC=$(grep -rli "depends_on::.*$QUERY\|corrects::.*$QUERY\|extends::.*$QUERY\|implements::.*$QUERY" "$WIKI_DIR" --include="*.md" 2>/dev/null | head -5 || true)

if [[ -n "$SEMANTIC" ]]; then
  echo "✅ 相关语义边页面:"
  while IFS= read -r FILE; do
    REL_PATH="${FILE#$VAULT_ROOT/}"
    grep -n "depends_on::.*$QUERY\|corrects::.*$QUERY\|extends::.*$QUERY\|implements::.*$QUERY" "$FILE" | sed "s|^|  $REL_PATH:|" || true
  done <<< "$SEMANTIC"
else
  echo "❌ 无相关语义边"
fi
echo ""

echo "=== align-check 完成 ==="
