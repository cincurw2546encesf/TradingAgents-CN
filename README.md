# TradingAgents-CN 🤖📈

> 基于多智能体框架的中国市场量化交易系统

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Docker](https://img.shields.io/badge/Docker-支持-blue.svg)](https://www.docker.com/)

## 项目简介

TradingAgents-CN 是 [hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN) 的 Fork 版本，专为中国 A 股市场优化的多智能体量化交易框架。系统通过多个专业 AI 智能体协同工作，实现市场分析、风险评估和交易决策的自动化。

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

## 贡献指南

欢迎提交 Issue 和 Pull Request！请先阅读 [贡献指南](CONTRIBUTING.md)。

## 问题反馈

- 🐛 [提交 Bug](https://github.com/your-username/TradingAgents-CN/issues/new?template=bug_report.md)
- 💡 [功能建议](https://github.com/your-username/TradingAgents-CN/issues/new?template=feature_request.md)
- 📖 [文档改进](https://github.com/your-username/TradingAgents-CN/issues/new?template=documentation.md)

## 免责声明

> ⚠️ **重要提示**：本项目仅供学习和研究使用，不构成任何投资建议。量化交易存在风险，请谨慎评估后使用。作者不对任何投资损失负责。

## 许可证

本项目采用 [MIT License](LICENSE) 开源协议。
