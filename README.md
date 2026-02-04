# OpenClaw Skills Collection

A curated collection of OpenClaw skills by Silicon Dawn. Tested, optimized, and ready to use.

## 🚀 Quick Start

### Install ClawdHub CLI (Recommended)

```bash
npm install -g clawdhub
```

### Install a Skill

```bash
# From GitHub
clawdhub install silicondawn/openclaw-skills/balance-checker

# Or clone and copy manually
git clone https://github.com/silicondawn/openclaw-skills.git
cp -r openclaw-skills/balance-checker ~/.openclaw/skills/
```

## 📦 Available Skills

### [balance-checker](./balance-checker/)

**Query all AI API balances at once** — supports DeepSeek, Moonshot/Kimi, and Volcengine.

**Features:**
- Unified balance check across three major AI API platforms
- Automatic summary for easy budget management
- Supports individual or batch queries
- Simple configuration — just add your API keys

**Triggers:** `check balance`, `how much balance`, `query balance`

**Install:**
```bash
clawdhub install silicondawn/openclaw-skills/balance-checker
```

**Configuration:** Add your API keys to OpenClaw config (see [balance-checker/README.md](./balance-checker/README.md))

## 🛠️ Development Guide

### Contributing a Skill

1. **Create skill directory**
   ```bash
   mkdir ~/.openclaw/skills/my-skill
   ```

2. **Write SKILL.md**
   ```markdown
   # My Skill
   
   ## Description
   What this skill does...
   
   ## Triggers
   - "do something"
   - "handle task"
   
   ## Files
   - `handler.sh` - Main script
   - `requirements.txt` - Python deps (optional)
   ```

3. **Test the skill**
   ```bash
   cd ~/.openclaw/skills/my-skill
   ./handler.sh
   ```

4. **Submit to repo**
   ```bash
   git add my-skill/
   git commit -m "feat: add my-skill"
   git push
   ```

### Skill Structure

```
my-skill/
├── SKILL.md              # Required: skill description
├── README.md             # Recommended: detailed docs
├── handler.sh            # Required: main script (executable)
├── requirements.txt      # Optional: Python dependencies
└── other_files/          # Optional: additional files
```

## 🔧 Troubleshooting

### Skill not working?
1. Check file permissions: `chmod +x ~/.openclaw/skills/my-skill/handler.sh`
2. Check OpenClaw config: `openclaw status`
3. View logs: `tail -f ~/.openclaw/logs/openclaw.log`

### ClawdHub install failed?
1. Ensure ClawdHub CLI is installed: `clawdhub --version`
2. Check network connection
3. Try manual install (clone repo and copy files)

## 📚 Resources

- [OpenClaw Docs](https://docs.openclaw.ai)
- [ClawdHub Marketplace](https://clawhub.com)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

## 📄 License

MIT License — see [LICENSE](./LICENSE)

---

**Maintainer:** Silicon Dawn  
**Repository:** https://github.com/silicondawn/openclaw-skills  
**Issues:** GitHub Issues
