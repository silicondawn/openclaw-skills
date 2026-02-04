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

- Unified balance check across three major AI API platforms
- Automatic summary for easy budget management
- Supports individual or batch queries

**Triggers:** `查余额`, `余额多少`, `check balance`

### [qmd-status](./qmd-status/)

**Query QMD memory backend status and statistics.**

- Index location and size
- Total indexed documents and vector embeddings
- Collection details

**Triggers:** `qmd status`, `查询 qmd`, `memory backend status`

## 📄 License

MIT License — see [LICENSE](./LICENSE)

---

**Maintainer:** Silicon Dawn  
**Repository:** https://github.com/silicondawn/openclaw-skills
