from unittest.mock import patch, MagicMock
import sys
sys.path.append('.')  # Ensure project root is in path

def test_result_has_required_keys(monkeypatch):
    """Result has keys: `stages`, `final_email`, `errors`"""
    # Mock ChatOpenAI to avoid API calls
    with patch('agents.research_agent.ChatOpenAI') as mock_research_llm, \
         patch('agents.personalization_agent.ChatOpenAI') as mock_pers_llm, \
         patch('agents.email_writer_agent.ChatOpenAI') as mock_writer_llm, \
         patch('agents.content_optimizer_agent.ChatOpenAI') as mock_opt_llm, \
         patch('agents.scheduler_agent.ChatOpenAI') as mock_sched_llm, \
         patch('agents.memory_agent.ChatOpenAI') as mock_mem_llm:

        # Configure mocks to return valid responses
        mock_response = MagicMock()
        mock_response.content = "Mocked research synthesis output"
        for mock_llm in [mock_research_llm, mock_pers_llm, mock_writer_llm, mock_opt_llm, mock_sched_llm, mock_mem_llm]:
            instance = mock_llm.return_value
            instance.invoke.return_value = mock_response

        from main import ColdEmailSystem
        system = ColdEmailSystem()

        sample_lead = {
            "name": "Jane Smith",
            "company": "TechCorp",
            "email": "jane@techcorp.com",
            "position": "VP Eng"
        }

        result = system.process_lead(sample_lead, schedule_send=False)

        assert "stages" in result, "Result missing 'stages' key"
        assert "final_email" in result, "Result missing 'final_email' key"
        assert "errors" in result, "Result missing 'errors' key"

def test_research_key_exists_in_stages(monkeypatch):
    """`research` key exists in `result["stages"]`"""
    with patch('agents.research_agent.ChatOpenAI') as mock_research_llm, \
         patch('agents.personalization_agent.ChatOpenAI') as mock_pers_llm, \
         patch('agents.email_writer_agent.ChatOpenAI') as mock_writer_llm, \
         patch('agents.content_optimizer_agent.ChatOpenAI') as mock_opt_llm, \
         patch('agents.scheduler_agent.ChatOpenAI') as mock_sched_llm, \
         patch('agents.memory_agent.ChatOpenAI') as mock_mem_llm:

        mock_response = MagicMock()
        mock_response.content = "Mocked output"
        for mock_llm in [mock_research_llm, mock_pers_llm, mock_writer_llm, mock_opt_llm, mock_sched_llm, mock_mem_llm]:
            instance = mock_llm.return_value
            instance.invoke.return_value = mock_response

        from main import ColdEmailSystem
        system = ColdEmailSystem()

        sample_lead = {
            "name": "Jane Smith",
            "company": "TechCorp",
            "email": "jane@techcorp.com",
            "position": "VP Eng"
        }

        result = system.process_lead(sample_lead, schedule_send=False)

        assert "research" in result["stages"], "Stages missing 'research' key"

def test_email_writing_key_exists_in_stages(monkeypatch):
    """`email_writing` key exists in `result["stages"]`"""
    with patch('agents.research_agent.ChatOpenAI') as mock_research_llm, \
         patch('agents.personalization_agent.ChatOpenAI') as mock_pers_llm, \
         patch('agents.email_writer_agent.ChatOpenAI') as mock_writer_llm, \
         patch('agents.content_optimizer_agent.ChatOpenAI') as mock_opt_llm, \
         patch('agents.scheduler_agent.ChatOpenAI') as mock_sched_llm, \
         patch('agents.memory_agent.ChatOpenAI') as mock_mem_llm:

        mock_response = MagicMock()
        mock_response.content = "Mocked output"
        for mock_llm in [mock_research_llm, mock_pers_llm, mock_writer_llm, mock_opt_llm, mock_sched_llm, mock_mem_llm]:
            instance = mock_llm.return_value
            instance.invoke.return_value = mock_response

        from main import ColdEmailSystem
        system = ColdEmailSystem()

        sample_lead = {
            "name": "Jane Smith",
            "company": "TechCorp",
            "email": "jane@techcorp.com",
            "position": "VP Eng"
        }

        result = system.process_lead(sample_lead, schedule_send=False)

        assert "email_writing" in result["stages"], "Stages missing 'email_writing' key"
