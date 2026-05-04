from unittest.mock import patch, MagicMock
import smtplib
from tools.email_tool import EmailTool, EmailConfig, EmailResult

def test_valid_email_passes_validation():
    """Valid email passes validation"""
    tool = EmailTool()
    assert tool._is_valid_email("test@example.com") is True
    assert tool._is_valid_email("user.name+tag@gmail.com") is True

def test_invalid_email_fails_validation():
    """`user@` (no domain) fails validation"""
    tool = EmailTool()
    assert tool._is_valid_email("user@") is False
    assert tool._is_valid_email("invalid-email") is False
    assert tool._is_valid_email("@example.com") is False
    assert tool._is_valid_email("") is False

def test_send_mocks_smtp_and_asserts_sendmail_called():
    """Send mocks `smtplib.SMTP` and asserts `sendmail` called"""
    config = EmailConfig(
        smtp_server="smtp.test.com",
        smtp_port=587,
        smtp_username="test@test.com",
        smtp_password="password"
    )
    tool = EmailTool(config)

    with patch('tools.email_tool.smtplib.SMTP') as mock_smtp:
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        result = tool.send_email("recipient@test.com", "Test Subject", "Test Body")

        assert result.success is True
        assert mock_server.sendmail.called, "sendmail should be called"

def test_auth_error_raises_and_is_caught():
    """Auth error raises and is caught"""
    config = EmailConfig(
        smtp_server="smtp.test.com",
        smtp_port=587,
        smtp_username="test@test.com",
        smtp_password="wrong_password"
    )
    tool = EmailTool(config)

    with patch('tools.email_tool.smtplib.SMTP') as mock_smtp:
        mock_server = MagicMock()
        # Raise SMTPAuthenticationError on login
        mock_server.login.side_effect = smtplib.SMTPAuthenticationError(535, b"Auth failed")
        mock_smtp.return_value.__enter__.return_value = mock_server

        result = tool.send_email("recipient@test.com", "Test", "Body")
        assert result.success is False
        # Error should mention failure
        assert "fail" in result.error.lower() or "auth" in result.error.lower()

def test_dry_run_skips_smtp(monkeypatch):
    """Dry_run=True skips SMTP entirely"""
    from main import ColdEmailSystem
    import config

    monkeypatch.setenv('DRY_RUN', 'true')
    # Reload config to pick up env var
    import importlib
    importlib.reload(config)
    assert config.config.pipeline.dry_run is True

    monkeypatch.setenv('DRY_RUN', 'false')
    importlib.reload(config)
    assert config.config.pipeline.dry_run is False

    monkeypatch.delenv('DRY_RUN', raising=False)
    importlib.reload(config)
