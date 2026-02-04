#!/bin/bash

# Balance Checker Script
# 查询 AI API 服务商余额

set -e

echo "🔍 正在查询 API 余额..."

# DeepSeek 余额查询
if [ -n "$DEEPSEEK_API_KEY" ]; then
    echo ""
    echo "💰 DeepSeek 余额"
    DEEPSEEK_RESULT=$(curl -s "https://api.deepseek.com/user/balance" \
        -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
        -H "Content-Type: application/json")
    
    if echo "$DEEPSEEK_RESULT" | grep -q "is_available"; then
        IS_AVAILABLE=$(echo "$DEEPSEEK_RESULT" | grep -o '"is_available":[^,]*' | cut -d: -f2 | tr -d ' ')
        TOTAL_BALANCE=$(echo "$DEEPSEEK_RESULT" | grep -o '"total_balance":"[^"]*"' | cut -d'"' -f4)
        GRANTED_BALANCE=$(echo "$DEEPSEEK_RESULT" | grep -o '"granted_balance":"[^"]*"' | cut -d'"' -f4)
        TOPPED_UP_BALANCE=$(echo "$DEEPSEEK_RESULT" | grep -o '"topped_up_balance":"[^"]*"' | cut -d'"' -f4)
        CURRENCY=$(echo "$DEEPSEEK_RESULT" | grep -o '"currency":"[^"]*"' | cut -d'"' -f4)
        
        echo "- 总余额: $TOTAL_BALANCE $CURRENCY"
        echo "- 赠金余额: $GRANTED_BALANCE $CURRENCY"
        echo "- 充值余额: $TOPPED_UP_BALANCE $CURRENCY"
        if [ "$IS_AVAILABLE" = "true" ]; then
            echo "- 状态: 可用 ✅"
        else
            echo "- 状态: 不可用 ❌"
        fi
    else
        echo "- 查询失败"
    fi
else
    echo "⚠️  DeepSeek API Key 未设置"
fi

# Moonshot/Kimi 余额查询
if [ -n "$MOONSHOT_API_KEY" ]; then
    echo ""
    echo "🌙 Moonshot/Kimi 余额"
    MOONSHOT_RESULT=$(curl -s "https://api.moonshot.cn/v1/users/me/balance" \
        -H "Authorization: Bearer $MOONSHOT_API_KEY")
    
    if echo "$MOONSHOT_RESULT" | grep -q "available_balance"; then
        AVAILABLE_BALANCE=$(echo "$MOONSHOT_RESULT" | grep -o '"available_balance":[^,]*' | cut -d: -f2 | tr -d ' ')
        CASH_BALANCE=$(echo "$MOONSHOT_RESULT" | grep -o '"cash_balance":[^,]*' | cut -d: -f2 | tr -d ' ')
        VOUCHER_BALANCE=$(echo "$MOONSHOT_RESULT" | grep -o '"voucher_balance":[^,]*' | cut -d: -f2 | tr -d ' ')
        
        echo "- 可用余额: $AVAILABLE_BALANCE CNY"
        echo "- 现金余额: $CASH_BALANCE CNY"
        echo "- 代金券余额: $VOUCHER_BALANCE CNY"
    else
        echo "- 查询失败"
    fi
else
    echo "⚠️  Moonshot API Key 未设置"
fi

echo ""
echo "✅ 余额查询完成"