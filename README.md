# OpenClaw Skills Collection

Silicon Dawn 的 OpenClaw Skills 集合。这些技能经过测试和优化，适用于 OpenClaw 框架。

## 🚀 快速开始

### 安装 ClawdHub CLI（推荐）

```bash
npm install -g clawdhub
```

### 安装技能

```bash
# 从 GitHub 安装
clawdhub install silicondawn/openclaw-skills/balance-checker

# 或者克隆仓库手动安装
git clone https://github.com/silicondawn/openclaw-skills.git
cp -r openclaw-skills/balance-checker ~/.openclaw/skills/
```

## 📦 可用技能

### [balance-checker](./balance-checker/)

**一次查询所有 AI API 余额** - 支持 DeepSeek、Moonshot/Kimi、火山引擎

**功能**：
- 统一查询三个主流 AI API 平台的余额
- 自动汇总显示，方便预算管理
- 支持单独查询或批量查询
- 配置简单，只需 API Key

**触发词**：`查余额`、`余额多少`、`还有多少额度`

**安装**：
```bash
clawdhub install silicondawn/openclaw-skills/balance-checker
```

**配置**：在 OpenClaw 配置文件中添加 API Key（详见 [balance-checker/README.md](./balance-checker/README.md)）

## 🛠️ 开发指南

### 如何贡献技能

1. **创建技能目录**
   ```bash
   mkdir ~/.openclaw/skills/my-skill
   ```

2. **编写 SKILL.md**
   ```markdown
   # My Skill
   
   ## 描述
   技能描述...
   
   ## 触发词
   - "做某事"
   - "处理某任务"
   
   ## 文件
   - `handler.sh` - 主脚本
   - `requirements.txt` - Python 依赖（可选）
   ```

3. **测试技能**
   ```bash
   # 在 OpenClaw 中测试
   cd ~/.openclaw/skills/my-skill
   ./handler.sh
   ```

4. **提交到仓库**
   ```bash
   git add my-skill/
   git commit -m "feat: add my-skill"
   git push
   ```

### 技能结构要求

```
my-skill/
├── SKILL.md              # 必须：技能描述文件
├── README.md             # 推荐：详细文档
├── handler.sh            # 必须：主脚本（可执行权限）
├── requirements.txt      # 可选：Python 依赖
└── other_files/          # 可选：其他文件
```

## 🔧 故障排除

### 技能不工作？
1. 检查文件权限：`chmod +x ~/.openclaw/skills/my-skill/handler.sh`
2. 检查 OpenClaw 配置：`openclaw status`
3. 查看日志：`tail -f ~/.openclaw/logs/openclaw.log`

### ClawdHub 安装失败？
1. 确保 ClawdHub CLI 已安装：`clawdhub --version`
2. 检查网络连接
3. 尝试手动安装（克隆仓库复制文件）

## 📚 相关资源

- [OpenClaw 文档](https://docs.openclaw.ai)
- [ClawdHub 技能市场](https://clawhub.com)
- [OpenClaw GitHub](https://github.com/openclaw/openclaw)

## 📄 License

MIT License - 详见 [LICENSE](./LICENSE) 文件

---

**维护者**：Silicon Dawn  
**仓库**：https://github.com/silicondawn/openclaw-skills  
**问题反馈**：GitHub Issues
