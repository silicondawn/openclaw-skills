# Balance Checker Skill

Query all AI API provider balances at once. Supports DeepSeek, Moonshot/Kimi, and Volcengine.

## Features

When you say "check balance", "how much balance", or "query balance" to your agent, it automatically queries and summarizes all platform balances.

```
🔍 Checking API balances...

💰 DeepSeek Balance
- Total: 304.54 CNY
- Status: Available ✅

🌙 Moonshot/Kimi Balance
- Available: 450.79 CNY

🌋 Volcengine Balance
- Available: 86.68 CNY

✅ Balance check complete
```

## Installation

### Method 1: ClawdHub (Recommended)

```bash
clawdhub install balance-checker
```

> If ClawdHub CLI is not installed: `npm i -g clawdhub`

### Method 2: From GitHub

```bash
# Clone the repo
git clone https://github.com/silicondawn/openclaw-skills.git /tmp/openclaw-skills

# Copy the skill
cp -r /tmp/openclaw-skills/balance-checker ~/.openclaw/skills/
```

### Install Volcengine Dependencies (Optional)

If you use Volcengine, install the Python SDK:

```bash
cd ~/.openclaw/skills/balance-checker && ./setup_volcengine.sh
```

## Configuration

Add API keys to the `env` section in your OpenClaw config (`~/.openclaw/openclaw.json`):

```json
{
  "env": {
    "DEEPSEEK_API_KEY": "sk-xxx",
    "MOONSHOT_API_KEY": "sk-xxx",
    "VOLCENGINE_ACCESS_KEY": "AKLTxxx",
    "VOLCENGINE_SECRET_KEY": "xxx"
  }
}
```

> **Notes:**
> - DeepSeek and Moonshot only need an API Key
> - Volcengine requires AK/SK (get from [console](https://console.volcengine.com/iam/keymanage/))
> - Only configure platforms you use — unconfigured ones are skipped

## Supported Platforms

| Platform | Environment Variables | Get Keys |
|----------|----------------------|----------|
| DeepSeek | `DEEPSEEK_API_KEY` | [platform.deepseek.com](https://platform.deepseek.com/) |
| Moonshot/Kimi | `MOONSHOT_API_KEY` | [platform.moonshot.cn](https://platform.moonshot.cn/) |
| Volcengine | `VOLCENGINE_ACCESS_KEY` + `VOLCENGINE_SECRET_KEY` | [console.volcengine.com](https://console.volcengine.com/iam/keymanage/) |

## File Structure

```
balance-checker/
├── SKILL.md              # OpenClaw skill description
├── README.md             # This document
├── check_balance.sh      # Main entry script
├── query_balance.py      # Volcengine query module
├── setup_volcengine.sh   # Volcengine SDK installer
└── venv/                 # Python venv (created after install)
```

## FAQ

### Q: Volcengine query failing?

Run the setup script:
```bash
cd ~/.openclaw/skills/balance-checker && ./setup_volcengine.sh
```

### Q: Only want to check one platform?

Ask your agent specifically, like "DeepSeek balance". Or only configure the API key for the platform you want.

### Q: Are my API keys secure?

Keys are stored locally in your OpenClaw config file and never uploaded anywhere. The skill code contains no hardcoded credentials.

## License

MIT
