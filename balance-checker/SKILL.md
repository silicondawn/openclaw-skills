---
name: balance-checker
description: 查询 AI API 服务商的余额（DeepSeek、Moonshot/Kimi、火山引擎）。当用户说"查余额"、"还有多少额度"、"余额多少"时自动触发。
---

# Balance Checker Skill

查询各个 AI API 服务商的余额。**一次查询所有平台**。

## 支持的服务商

| 服务商 | 查询方式 | 环境变量 |
|--------|----------|----------|
| DeepSeek | API | `DEEPSEEK_API_KEY` |
| Moonshot/Kimi | API | `MOONSHOT_API_KEY` |
| 火山引擎 | SDK | `VOLCENGINE_ACCESS_KEY` + `VOLCENGINE_SECRET_KEY` |

## 使用方法

用户说以下关键词时触发：
- "查余额"
- "还有多少额度"
- "余额多少"
- "看看余额"
- "API 余额"

## 实现

同时执行三个查询，汇总输出。

### 1. DeepSeek
```bash
curl -s "https://api.deepseek.com/user/balance" \
  -H "Authorization: Bearer $DEEPSEEK_API_KEY" \
  -H "Content-Type: application/json"
```

### 2. Moonshot/Kimi
```bash
curl -s "https://api.moonshot.cn/v1/users/me/balance" \
  -H "Authorization: Bearer $MOONSHOT_API_KEY"
```

### 3. 火山引擎
```bash
cd ~/.openclaw/skills/volcengine-balance && ./volcengine_balance.sh
```

## 输出格式

```
📊 AI API 余额汇总
====================

💰 DeepSeek
   可用: xxx CNY

💰 Moonshot/Kimi  
   可用: xxx CNY

💰 火山引擎
   可用: xxx CNY
```

## API 文档参考
- DeepSeek: https://api-docs.deepseek.com/zh-cn/api/get-user-balance
- Moonshot: https://platform.moonshot.cn/docs/api-reference#user-balance
- 火山引擎: https://www.volcengine.com/docs/6269/1223898
