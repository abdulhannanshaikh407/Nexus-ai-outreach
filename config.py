"""Centralized configuration with validation."""
import os
from dataclasses import dataclass, field
from typing import Optional, List
from dotenv import load_dotenv

load_dotenv()

@dataclass
class LLMConfig:
    model: str = os.getenv("LLM_MODEL", "gpt-4o-mini")
    temperature_research: float = float(os.getenv("TEMP_RESEARCH", "0.1"))
    temperature_writer: float = float(os.getenv("TEMP_WRITER", "0.7"))
    temperature_optimizer: float = float(os.getenv("TEMP_OPTIMIZER", "0.3"))
    max_tokens: int = int(os.getenv("MAX_TOKENS", "2000"))
    max_retries: int = int(os.getenv("LLM_MAX_RETRIES", "3"))

@dataclass
class SMTPConfig:
    server: str = os.getenv("SMTP_SERVER", "smtp.gmail.com")
    port: int = int(os.getenv("SMTP_PORT", "587"))
    username: str = os.getenv("SMTP_USERNAME", "")
    password: str = os.getenv("SMTP_PASSWORD", "")
    from_name: str = os.getenv("FROM_NAME", "Cold Outreach System")

    def validate(self) -> list[str]:
        errors = []
        if not self.username:
            errors.append("SMTP_USERNAME is required")
        if not self.password:
            errors.append("SMTP_PASSWORD is required")
        return errors

@dataclass
class MemoryConfig:
    index_path: str = os.getenv("MEMORY_INDEX_PATH", "memory/faiss_index")
    dimension: int = int(os.getenv("MEMORY_DIMENSION", "384"))
    use_faiss: bool = os.getenv("USE_FAISS", "true").lower() == "true"

@dataclass
class PipelineConfig:
    optimize_content: bool = True
    schedule_send: bool = True
    store_in_memory: bool = True
    rate_limit_per_minute: int = int(os.getenv("RATE_LIMIT_PER_MINUTE", "10"))
    delay_between_sends: float = float(os.getenv("DELAY_BETWEEN_SENDS", "2.0"))
    dry_run: bool = field(default_factory=lambda: os.getenv("DRY_RUN", "false").lower() == "true")

    # Value proposition (move out of main.py hardcode)
    solution_name: str = os.getenv("SOLUTION_NAME", "OptimizePro Solutions")
    key_benefits: List[str] = field(default_factory=lambda: [
        "Increase operational efficiency by 30%",
        "Reduce costs by 25%",
        "Improve team productivity",
        "Scale without growing headcount",
    ])

@dataclass
class AppConfig:
    llm: LLMConfig = field(default_factory=LLMConfig)
    smtp: SMTPConfig = field(default_factory=SMTPConfig)
    memory: MemoryConfig = field(default_factory=MemoryConfig)
    pipeline: PipelineConfig = field(default_factory=PipelineConfig)
    log_level: str = os.getenv("LOG_LEVEL", "INFO")
    log_file: str = os.getenv("LOG_FILE", "cold_email_system.log")
    openai_api_key: str = os.getenv("OPENAI_API_KEY", "")

    def validate(self) -> None:
        """Validate config and raise ValueError if critical keys are missing."""
        errors = []
        if not self.openai_api_key:
            errors.append("OPENAI_API_KEY is required")
        if errors:
            raise ValueError(f"Configuration errors: {'; '.join(errors)}")

# Singleton
config = AppConfig()