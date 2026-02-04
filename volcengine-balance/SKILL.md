---
name: volcengine-balance
description: 查询火山引擎（Volcengine）API 余额。当用户说"查火山余额"、"火山引擎余额"、"volcengine 余额"时自动触发。
---

# Volcengine Balance Skill

查询火山引擎（Volcengine）API 余额。

## 功能

查询火山引擎账户的余额信息，包括：
- 可用余额
- 现金余额  
- 冻结金额
- 信控额度
- 欠费金额
- 账户状态

## 使用方法

用户说以下关键词时触发：
- "查火山余额"
- "火山引擎余额"
- "volcengine 余额"
- "火山额度"
- "火山引擎还有多少钱"

## 重要说明

**注意**：余额查询需要火山引擎的 **AccessKey ID 和 AccessKey Secret (AK/SK)**，而不是 API Key。

OpenClaw 配置中的 `volcengine` provider 使用的是 API Key（用于模型调用），但余额查询需要单独的 AK/SK。

## 配置要求

需要配置火山引擎的 AccessKey ID 和 AccessKey Secret（AK/SK）：
1. 在火山引擎控制台创建 AccessKey：https://console.volcengine.com/iam/keymanage/
2. 将 AK/SK 配置到 OpenClaw 环境变量或配置文件中

## 配置方法

### 方法1：环境变量（推荐）

```bash
export VOLCENGINE_ACCESS_KEY=你的AccessKey ID
export VOLCENGINE_SECRET_KEY=你的AccessKey Secret
```

### 方法2：OpenClaw 配置文件

在 `~/.openclaw/openclaw.json` 的 `env` 部分添加：
```json
"env": {
  "VOLCENGINE_ACCESS_KEY": "你的AccessKey ID",
  "VOLCENGINE_SECRET_KEY": "你的AccessKey Secret"
}
```

## 实现原理

使用火山引擎 Python SDK 调用 `QueryBalanceAcct` API 查询余额信息。

## 输出格式

```
💰 火山引擎余额
==============================
可用余额:   100.50 CNY
现金余额:   150.00 CNY
冻结金额:   50.00 CNY
信控额度:   0.00 CNY
欠费金额:   0.00 CNY
可用现金:   100.00 CNY
账户状态:   正常 ✅

💡 说明:
- 可用余额 = (现金余额 - 冻结金额) + 信控额度 - 欠费金额
- 信控额度: 火山引擎授予的信用额度
- 欠费金额: 未支付的账单金额
```

## 文件结构

```
volcengine-balance/
├── SKILL.md              # Skill 描述文件
├── README.md             # 详细说明文档
├── query_balance.py      # 主查询脚本
├── test_balance.py       # 测试脚本
├── volcengine_balance.sh # Shell 包装脚本
└── venv/                 # Python 虚拟环境（自动创建）
```

## API 文档参考
- 火山引擎费用中心 API: https://www.volcengine.com/docs/6269/1165275
- QueryBalanceAcct API: https://www.volcengine.com/docs/6269/1593138
- Python SDK: https://github.com/volcengine/volcengine-python-sdk