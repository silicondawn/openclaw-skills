# 火山引擎余额查询 Skill

这是一个 OpenClaw skill，用于查询火山引擎（Volcengine）API 余额。

## 功能

- 查询火山引擎账户余额信息
- 显示可用余额、现金余额、冻结金额等
- 支持从环境变量或 OpenClaw 配置读取凭证
- 格式化输出，易于阅读

## 安装

1. 确保已安装 Python 3.7+
2. 安装火山引擎 Python SDK：
   ```bash
   cd ~/.openclaw/skills/volcengine-balance
   python3 -m venv venv
   source venv/bin/activate
   pip install volcengine-python-sdk
   ```

## 配置

### 方法1：环境变量（推荐）

在 `~/.bashrc` 或 `~/.zshrc` 中添加：
```bash
export VOLCENGINE_ACCESS_KEY="你的AccessKey ID"
export VOLCENGINE_SECRET_KEY="你的AccessKey Secret"
```

### 方法2：OpenClaw 配置文件

在 `~/.openclaw/openclaw.json` 的 `env` 部分添加：
```json
"env": {
  "VOLCENGINE_ACCESS_KEY": "你的AccessKey ID",
  "VOLCENGINE_SECRET_KEY": "你的AccessKey Secret"
}
```

### 获取 AK/SK

1. 登录火山引擎控制台：https://console.volcengine.com/
2. 进入「访问控制」>「密钥管理」：https://console.volcengine.com/iam/keymanage/
3. 创建 AccessKey，保存 AK/SK

## 使用方法

### 在 OpenClaw 中自动触发

当用户说以下关键词时自动触发：
- "查火山余额"
- "火山引擎余额"
- "volcengine 余额"
- "火山额度"
- "火山引擎还有多少钱"

### 手动测试

```bash
# 进入 skill 目录
cd ~/.openclaw/skills/volcengine-balance

# 运行查询脚本
./volcengine_balance.sh

# 显示详细信息
./volcengine_balance.sh --verbose
```

### 直接运行 Python 脚本

```bash
cd ~/.openclaw/skills/volcengine-balance
source venv/bin/activate
python3 query_balance.py
```

## 输出示例

```
火山引擎余额查询工具
==================================================
正在查询火山引擎余额...

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

## 故障排除

### 1. 认证失败
- 检查 AK/SK 是否正确
- 确保 AK/SK 有查询余额的权限

### 2. SDK 安装失败
- 确保 Python 版本 >= 3.7
- 尝试使用虚拟环境

### 3. API 调用失败
- 检查网络连接
- 确认火山引擎服务正常

## 文件结构

```
volcengine-balance/
├── SKILL.md              # Skill 描述文件
├── README.md             # 说明文档
├── query_balance.py      # 主查询脚本
├── test_balance.py       # 测试脚本
├── volcengine_balance.sh # Shell 包装脚本
└── venv/                 # Python 虚拟环境（可选）
```

## API 参考

- 火山引擎费用中心 API: https://www.volcengine.com/docs/6269/1165275
- QueryBalanceAcct API: https://www.volcengine.com/docs/6269/1593138
- Python SDK: https://github.com/volcengine/volcengine-python-sdk

## 注意事项

1. **AK/SK 安全**：妥善保管 AccessKey，不要泄露
2. **API 限流**：火山引擎 API 有 QPS 限制，避免频繁调用
3. **余额更新**：余额信息可能有延迟，以控制台为准