# 使用示例

## 在 OpenClaw 中调用

当用户在 Telegram 或其他支持的平台发送以下消息时，skill 会自动触发：

```
查火山余额
```

```
火山引擎还有多少钱？
```

```
volcengine 余额
```

## 手动调用

### 通过 exec 工具

```python
# 在 OpenClaw 会话中直接执行
exec("~/.openclaw/skills/volcengine-balance/volcengine_balance.sh")
```

### 通过 Python 脚本

```python
import subprocess
import os

# 设置环境变量
os.environ['VOLCENGINE_ACCESS_KEY'] = '你的AccessKey ID'
os.environ['VOLCENGINE_SECRET_KEY'] = '你的AccessKey Secret'

# 执行查询
result = subprocess.run(
    ['~/.openclaw/skills/volcengine-balance/volcengine_balance.sh'],
    capture_output=True,
    text=True
)
print(result.stdout)
```

## 集成到其他技能

可以将火山引擎余额查询集成到其他技能中，例如：

```python
# 在综合余额查询技能中
def check_all_balances():
    balances = []
    
    # 查询 DeepSeek 余额
    balances.append(check_deepseek_balance())
    
    # 查询 Moonshot 余额
    balances.append(check_moonshot_balance())
    
    # 查询火山引擎余额
    balances.append(check_volcengine_balance())
    
    return "\n\n".join(balances)

def check_volcengine_balance():
    """查询火山引擎余额"""
    import subprocess
    script_path = "~/.openclaw/skills/volcengine-balance/volcengine_balance.sh"
    result = subprocess.run(
        [script_path],
        capture_output=True,
        text=True
    )
    return result.stdout
```

## 定时任务

可以设置定时任务定期检查余额：

```bash
# 每天上午9点检查余额
0 9 * * * /home/yibo/.openclaw/skills/volcengine-balance/volcengine_balance.sh >> /tmp/volcengine_balance.log 2>&1
```

## 输出到通知

将余额查询结果发送到 Telegram 或其他通知渠道：

```python
import subprocess
from openclaw_tools import message

# 查询余额
script_path = "~/.openclaw/skills/volcengine-balance/volcengine_balance.sh"
result = subprocess.run([script_path], capture_output=True, text=True)

# 发送到 Telegram
if result.returncode == 0:
    message.send(
        channel="telegram",
        target="8377247019",  # 你的 Telegram ID
        message=result.stdout
    )
else:
    message.send(
        channel="telegram",
        target="8377247019",
        message=f"火山引擎余额查询失败:\n{result.stderr}"
    )
```

## 故障排除命令

```bash
# 1. 检查虚拟环境
cd ~/.openclaw/skills/volcengine-balance
source venv/bin/activate
python3 -c "import volcenginesdkbilling; print('SDK 正常')"

# 2. 检查环境变量
echo "VOLCENGINE_ACCESS_KEY: ${VOLCENGINE_ACCESS_KEY:0:8}..."
echo "VOLCENGINE_SECRET_KEY: ${VOLCENGINE_SECRET_KEY:0:8}..."

# 3. 测试 API 调用（需要 AK/SK）
python3 test_balance.py

# 4. 查看详细日志
./volcengine_balance.sh --verbose
```

## 预期输出

成功配置后，输出应该类似：

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