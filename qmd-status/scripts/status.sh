#!/bin/bash
# QMD Status Query Script

export PATH="$HOME/.bun/bin:$PATH"

echo "🔍 QMD Memory Backend Status"
echo "============================"
echo ""

if ! command -v qmd &> /dev/null; then
    echo "❌ QMD not found in PATH"
    echo "   Expected: ~/.bun/bin/qmd"
    exit 1
fi

# Get status
qmd status

echo ""
echo "📊 Quick Stats:"
echo "---------------"

# Document count
DOC_COUNT=$(qmd status 2>/dev/null | grep -E "^  Total:" | awk '{print $2}')
VEC_COUNT=$(qmd status 2>/dev/null | grep -E "^  Vectors:" | awk '{print $2}')

echo "  Documents: ${DOC_COUNT:-0}"
echo "  Vectors:   ${VEC_COUNT:-0}"

echo ""
echo "💡 Tip: Run 'qmd search \"keyword\"' to test search"
