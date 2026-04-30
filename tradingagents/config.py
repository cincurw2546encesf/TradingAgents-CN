"""Configuration management for TradingAgents-CN.

This module handles loading and validation of configuration settings
from environment variables and configuration files.
"""

import os
from dataclasses import dataclass, field
from typing import Optional
from dotenv import load_dotenv

# Load environment variables from .env file if present
load_dotenv()


@dataclass
class LLMConfig:
    """Configuration for LLM providers."""
    provider: str = "openai"
    model: str = "gpt-4o-mini"
    api_key: Optional[str] = None
    base_url: Optional[str] = None
    temperature: float = 0.7
    max_tokens: int = 4096
    timeout: int = 60


@dataclass
class MarketDataConfig:
    """Configuration for market data sources."""
    # Tushare (Chinese A-share market)
    tushare_token: Optional[str] = None

    # AKShare (free Chinese market data)
    akshare_enabled: bool = True

    # Yahoo Finance (international markets)
    yahoo_finance_enabled: bool = True

    # Data cache settings
    cache_enabled: bool = True
    cache_dir: str = ".cache/market_data"
    cache_ttl_seconds: int = 3600


@dataclass
class AgentConfig:
    """Configuration for trading agents."""
    max_debate_rounds: int = 3
    max_risk_discuss_rounds: int = 3
    enable_memory: bool = True
    memory_backend: str = "local"  # "local" or "redis"
    redis_url: Optional[str] = None


@dataclass
class AppConfig:
    """Top-level application configuration."""
    # Environment
    environment: str = "development"
    debug: bool = False
    log_level: str = "INFO"
    log_dir: str = "logs"

    # Sub-configurations
    llm: LLMConfig = field(default_factory=LLMConfig)
    market_data: MarketDataConfig = field(default_factory=MarketDataConfig)
    agent: AgentConfig = field(default_factory=AgentConfig)

    # Results
    results_dir: str = "results"


def load_config() -> AppConfig:
    """Load configuration from environment variables.

    Returns:
        AppConfig: Populated configuration object.
    """
    llm_config = LLMConfig(
        provider=os.getenv("LLM_PROVIDER", "openai"),
        model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
        api_key=os.getenv("OPENAI_API_KEY") or os.getenv("LLM_API_KEY"),
        base_url=os.getenv("OPENAI_BASE_URL") or os.getenv("LLM_BASE_URL"),
        temperature=float(os.getenv("LLM_TEMPERATURE", "0.7")),
        max_tokens=int(os.getenv("LLM_MAX_TOKENS", "4096")),
        timeout=int(os.getenv("LLM_TIMEOUT", "60")),
    )

    market_data_config = MarketDataConfig(
        tushare_token=os.getenv("TUSHARE_TOKEN"),
        akshare_enabled=os.getenv("AKSHARE_ENABLED", "true").lower() == "true",
        yahoo_finance_enabled=os.getenv("YAHOO_FINANCE_ENABLED", "true").lower() == "true",
        cache_enabled=os.getenv("CACHE_ENABLED", "true").lower() == "true",
        cache_dir=os.getenv("CACHE_DIR", ".cache/market_data"),
        cache_ttl_seconds=int(os.getenv("CACHE_TTL_SECONDS", "3600")),
    )

    agent_config = AgentConfig(
        max_debate_rounds=int(os.getenv("MAX_DEBATE_ROUNDS", "3")),
        max_risk_discuss_rounds=int(os.getenv("MAX_RISK_DISCUSS_ROUNDS", "3")),
        enable_memory=os.getenv("ENABLE_MEMORY", "true").lower() == "true",
        memory_backend=os.getenv("MEMORY_BACKEND", "local"),
        redis_url=os.getenv("REDIS_URL"),
    )

    return AppConfig(
        environment=os.getenv("ENVIRONMENT", "development"),
        debug=os.getenv("DEBUG", "false").lower() == "true",
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        log_dir=os.getenv("LOG_DIR", "logs"),
        llm=llm_config,
        market_data=market_data_config,
        agent=agent_config,
        results_dir=os.getenv("RESULTS_DIR", "results"),
    )


# Singleton config instance
_config: Optional[AppConfig] = None


def get_config() -> AppConfig:
    """Get the singleton application configuration.

    Returns:
        AppConfig: The application configuration instance.
    """
    global _config
    if _config is None:
        _config = load_config()
    return _config


def reset_config() -> None:
    """Reset the configuration singleton (useful for testing)."""
    global _config
    _config = None
