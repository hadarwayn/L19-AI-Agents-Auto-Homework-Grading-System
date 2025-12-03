"""
Configuration Loader

Loads and validates configuration from:
- .env file (environment variables)
- config/settings.yaml (application settings)

Uses Pydantic for validation.

Author: Hadar Wayn
Date: December 2025
"""

import os
from pathlib import Path
from typing import Optional, Dict, List, Tuple

import yaml
from pydantic import BaseModel, Field, validator
from dotenv import load_dotenv

from .paths import get_project_root, get_config_file, get_secrets_dir


class AgentConfig(BaseModel):
    """Configuration for individual agents"""
    enabled: bool = True


class EmailExtractionConfig(AgentConfig):
    """Email extraction agent configuration"""
    batch_size: int = 50
    subject_pattern: str
    github_url_pattern: str


class RepositoryAnalysisConfig(AgentConfig):
    """Repository analysis agent configuration"""
    max_workers: int = 5
    clone_timeout: int = 60
    line_limit: int = 150


class LLMFeedbackConfig(AgentConfig):
    """LLM feedback generation agent configuration"""
    model: str = "gemini-1.5-flash"
    max_tokens: int = 500
    temperature: float = 0.7
    request_delay: int = 2
    max_retries: int = 3


class GradingConfig(BaseModel):
    """Grading configuration"""
    line_limit: int = 150
    grade_ranges: Dict[str, List[int]]
    personas: Dict[str, str]


class LoggingConfig(BaseModel):
    """Logging configuration"""
    level: str = "INFO"
    max_lines_per_file: int = 1000
    max_files: int = 5


class ExcelConfig(BaseModel):
    """Excel files configuration"""
    files: Dict[str, str]
    student_mapping: str


class Settings(BaseModel):
    """Main application settings"""
    gmail_credentials_path: Path
    gemini_api_key: str
    email_extraction: EmailExtractionConfig
    repository_analysis: RepositoryAnalysisConfig
    llm_feedback: LLMFeedbackConfig
    grading: GradingConfig
    logging: LoggingConfig
    excel: ExcelConfig

    class Config:
        arbitrary_types_allowed = True


# Global settings instance
_settings: Optional[Settings] = None


def load_config() -> Settings:
    """
    Load configuration from .env and settings.yaml

    Returns:
        Settings: Validated configuration object
    """
    global _settings

    if _settings is not None:
        return _settings

    # Load .env file
    env_path = get_project_root() / ".env"
    load_dotenv(env_path)

    # Load settings.yaml
    settings_path = get_config_file("settings.yaml")
    with open(settings_path, "r") as f:
        yaml_config = yaml.safe_load(f)

    # Combine environment variables with YAML config
    config_data = {
        "gmail_credentials_path": get_secrets_dir() / os.getenv(
            "GMAIL_CREDENTIALS_PATH", "Secrets/credentials.json"
        ),
        "gemini_api_key": os.getenv("GEMINI_API_KEY", ""),
        "email_extraction": EmailExtractionConfig(**yaml_config["agents"]["email_extraction"]),
        "repository_analysis": RepositoryAnalysisConfig(**yaml_config["agents"]["repository_analysis"]),
        "llm_feedback": LLMFeedbackConfig(**yaml_config["agents"]["llm_feedback"]),
        "grading": GradingConfig(**yaml_config["grading"]),
        "logging": LoggingConfig(**yaml_config["logging"]),
        "excel": ExcelConfig(**yaml_config["excel"]),
    }

    _settings = Settings(**config_data)
    return _settings


def get_settings() -> Settings:
    """
    Get current settings (loads if not already loaded)

    Returns:
        Settings: Current configuration
    """
    return load_config()


def reload_config() -> Settings:
    """
    Force reload configuration from files

    Returns:
        Settings: Reloaded configuration
    """
    global _settings
    _settings = None
    return load_config()
