# TradingAgents-CN 🤖📈

> 基于多智能体框架的中国市场量化交易系统

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-支持-blue.svg)](https://www.docker.com/)

## 项目简介

TradingAgents-CN 是 [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 的 Fork 版本，专为中国 A 股市场优化的多智能体量化交易框架。系统通过多个专业 AI 智能体协同工作，实现市场分析、风险评估和交易决策的自动化。

> 📝 **个人备注**：此 Fork 主要用于个人学习和策略研究，重点关注沪深300成分股的分析场景。

## 核心特性

- 🧠 **多智能体协作**：分析师、研究员、交易员、风控等多角色智能体
- 📊 **A股数据支持**：集成 AkShare、Tushare 等中国市场数据源
- 🔍 **多维度分析**：技术分析、基本面分析、情绪分析、宏观分析
- 🛡️ **风险管理**：内置多层风控机制
- 🐳 **Docker 部署**：支持容器化一键部署
- 🌐 **Web 界面**：直观的可视化操作界面

## 快速开始

### 环境要求

- Python 3.10+
- Docker & Docker Compose（可选）
- OpenAI API Key 或兼容的 LLM 服务

### 安装

```bash
# 克隆项目
git clone https://github.com/your-username/TradingAgents-CN.git
cd TradingAgents-CN

# 安装依赖
pip install -r requirements.txt

# 配置环境变量
cp .env.example .env
# 编辑 .env 文件，填入你的 API Keys
```

### Docker 部署

```bash
# 复制 Docker 环境配置
cp .env.docker .env

# 启动服务
docker-compose up -d
```

### 本地运行

```bash
python main.py
```

## 项目结构

```
TradingAgents-CN/
├── tradingagents/          # 核心框架
│   ├── agents/             # 智能体模块
│   ├── dataflows/          # 数据流处理
│   └── graph/              # 决策图
├── web/                    # Web 界面
├── tests/                  # 测试用例
├── docs/                   # 文档
├── docker-compose.yml      # Docker 编排
├── .env.example            # 环境变量示例
└── requirements.txt        # Python 依赖
```

## 配置说明

参考 [`.env.example`](.env.example) 文件配置以下关键参数：

| 参数 | 说明 |
|------|------|
| `OPENAI_API_KEY` | OpenAI API 密钥 |
| `TUSHARE_TOKEN` | Tushare 数据 Token |
| `MONGODB_URI` | MongoDB 连接地址 |
| `REDIS_URL` | Redis 连接地址 |

> 💡 **个人提示**：使用 DeepSeek 作为 LLM 后端可显著降低 API 成本，在 `.env` 中设置 `LLM_PROVIDER=deepseek` 即可。

## 个人常用命令备忘

```bash
# 拉取上游最新更新并合并到本地
git fetch upstream
git merge upstream/main

# 仅分析单只股票（调试用）
python main.py --ticker 600519 --date 2024-01-15

# 批量分析沪深300成分股（每次取前10只，避免 API 限流）
# 注意：--delay 从5调整为8，实测8秒间隔在 Tushare 免费账户下更稳定，基本不触发限流
python main.py --index hs300 --limit 10 --delay 8

# 导出分析结果为 CSV（方便在 Excel 里做二次筛选）
python main.py --index hs300 --limit 10 --delay 8 --export csv --output ./results/

# 查看某只股票近30天的分析历史记录
python main.py --ticker 600519 --history --days 30

# 同步上游标签（偶尔需要，方便对比版本差异）
git fetch upstream --tags

# 清理30天前的旧分析结果，释放磁盘空间（MongoDB 数据量涨得很快）
# 注意：加 --dry-run 先预览会删哪些，确认没问题再去掉该参数真正执行
python main.py --cleanup --older-than 30 --dry-run

# 重置本地分支到上游最新状态（慎用！会丢弃本地未提交的修改）
# git fetch upstream && git reset --hard upstream/main

# 检查当前 MongoDB 中各股票的分析记录数量（快速了解数据积累情况）
# 在 mongo shell 里执行：db.analysis.aggregate([{$group:{_id:'$ticker',count:{$sum:1}}},{$sort:{count:-1}}])

# 【新增】单独跑回测，验证某段时间区间内的策略表现（--start/--end 均为 YYYY-MM-DD 格式）
# 加 --benchmark hs300 可以和沪深300指数做对比，直观看超额收益
python main.py --backtest --ticker 600519 --start 2024-01-01 --end 2024-06-30 --benchmark hs300

# 【新增】批量回测沪深300前20只股票，结果汇总到同一个 CSV 文件
# --delay 建议设 10，回测本身不调 Tushare 实时接口，但初始化数据拉取还是会触发限流
python main.py --backtest --index hs300 --limit 20 --delay 10 --export csv --output ./backtest_results/
```
