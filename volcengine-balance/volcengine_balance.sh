#!/bin/bash
# 火山引擎余额查询脚本 - OpenClaw Skill 入口

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PYTHON_SCRIPT="$SCRIPT_DIR/query_balance.py"

# 检查 Python 脚本是否存在
if [ ! -f "$PYTHON_SCRIPT" ]; then
    echo "错误: 找不到查询脚本 $PYTHON_SCRIPT"
    exit 1
fi

# 检查是否在虚拟环境中，如果不在则激活
if [ -d "$SCRIPT_DIR/venv" ]; then
    source "$SCRIPT_DIR/venv/bin/activate"
fi

# 执行 Python 脚本
python3 "$PYTHON_SCRIPT" "$@"

# 退出虚拟环境（如果激活了）
if [ -d "$SCRIPT_DIR/venv" ] && [ -n "$VIRTUAL_ENV" ]; then
    deactivate
fi