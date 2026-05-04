import pytest
from unittest.mock import MagicMock

@pytest.fixture
def mock_llm():
    m = MagicMock()
    m.invoke.return_value = MagicMock(content="Mocked response")
    return m

@pytest.fixture
def sample_lead():
    return {"name": "Jane Smith", "company": "TechCorp",
            "email": "jane@techcorp.com", "position": "VP Eng"}
