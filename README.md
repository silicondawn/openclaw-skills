# OpenClaw Skills (Private)

Silicon Dawn 私有 OpenClaw Skills 集合。

## Skills

| Skill | 描述 |
|-------|------|
| [balance-checker](./balance-checker/) | 一次查询所有 AI API 余额（DeepSeek、Moonshot、火山引擎） |

## 安装

```bash
# 克隆到本地
git clone git@github.com:silicondawn/openclaw-skills.git

# 复制 skill 到 OpenClaw skills 目录
cp -r balance-checker ~/.openclaw/skills/

# 安装火山引擎依赖（可选）
cd ~/.openclaw/skills/balance-checker && ./setup_volcengine.sh
```

## License

Private - Silicon Dawn internal use only.
