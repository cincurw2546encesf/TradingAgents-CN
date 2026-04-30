# TradingAgents-CN
# Fork of hsliuping/TradingAgents-CN
# A multi-agent LLM-based trading analysis framework with Chinese market support

"""TradingAgents-CN: Multi-agent LLM framework for trading analysis.

This package provides a comprehensive trading analysis system powered by
large language models, with enhanced support for Chinese financial markets
including A-shares, Hong Kong stocks, and cryptocurrency markets.

Key Features:
    - Multi-agent collaborative analysis (Bull/Bear/Neutral analysts)
    - Chinese market data integration (Tushare, AKShare, BaoStock)
    - Support for multiple LLM backends (OpenAI, DeepSeek, Qwen, etc.)
    - Risk management and portfolio analysis
    - Real-time and historical data processing

Example:
    >>> from tradingagents import TradingAgentsGraph
    >>> graph = TradingAgentsGraph()
    >>> result = graph.analyze(ticker="600519", market="cn")
"""

__version__ = "0.1.0"
__author__ = "TradingAgents-CN Contributors"
__license__ = "MIT"

from typing import Optional

# Package metadata
PACKAGE_NAME = "tradingagents-cn"
PACKAGE_DESCRIPTION = "Multi-agent LLM framework for trading analysis with Chinese market support"

# Supported markets
# Note: added 'futures' for personal use with commodity futures analysis
SUPPORTED_MARKETS = [
    "cn",      # Chinese A-shares (Shanghai/Shenzhen)
    "hk",      # Hong Kong stocks
    "us",      # US stocks
    "crypto",  # Cryptocurrency
    "futures", # Commodity futures (SHFE, DCE, CZCE)
]

# Supported LLM providers
SUPPORTED_LLM_PROVIDERS = [
    "openai",
    "deepseek",
    "qwen",      # Alibaba Tongyi Qianwen
    "zhipu",     # Zhipu AI (ChatGLM)
    "moonshot",  # Moonshot AI (Kimi)
    "ollama",    # Local models via Ollama
]


def get_version() -> str:
    """Return the current package version."""
    return __version__


def get_supported_markets() -> list:
    """Return list of supported market identifiers."""
    return SUPPORTED_MARKETS.copy()


def get_supported_llm_providers() -> list:
    """Return list of supported LLM provider names."""
    return SUPPORTED_LLM_PROVIDERS.copy()
