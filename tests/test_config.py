import os
import pytest
from config import AppConfig, config

def test_missing_openai_api_key_raises_valueerror():
    """Missing `OPENAI_API_KEY` raises `ValueError` on `config.validate()`"""
    cfg = AppConfig(openai_api_key="")
    with pytest.raises(ValueError) as exc_info:
        cfg.validate()
    assert "OPENAI_API_KEY" in str(exc_info.value)

def test_valid_key_passes_validate():
    """Valid key passes validate"""
    cfg = AppConfig(openai_api_key="sk-validkey123456789")
    try:
        cfg.validate()  # Should not raise
    except ValueError:
        pytest.fail("validate() raised ValueError unexpectedly")

def test_dry_run_env_var_sets_pipeline_dry_run_true(monkeypatch):
    """`DRY_RUN=true` env var sets `pipeline.dry_run = True`"""
    monkeypatch.setenv('DRY_RUN', 'true')
    cfg = AppConfig()
    assert cfg.pipeline.dry_run is True

    monkeypatch.setenv('DRY_RUN', 'false')
    cfg = AppConfig()
    assert cfg.pipeline.dry_run is False

    monkeypatch.delenv('DRY_RUN', raising=False)
    cfg = AppConfig()
    assert cfg.pipeline.dry_run is False

def test_default_llm_model_is_gpt4o_mini():
    """Default LLM model is `gpt-4o-mini`"""
    cfg = AppConfig()
    assert cfg.llm.model == "gpt-4o-mini", f"Expected gpt-4o-mini, got {cfg.llm.model}"
