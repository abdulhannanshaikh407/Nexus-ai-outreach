<<<<<<< HEAD
# Nexus-ai-outreach
AI-powered cold email pipeline built with LangChain &amp; GPT-4o-mini — 6 autonomous agents that research prospects, write personalized emails, optimize for deliverability, and schedule outreach.
=======
# **AI Cold Email Outreach System**
*6-agent LangChain pipeline that researches prospects, writes personalized emails, and optimizes delivery*

![Python 3.11+](https://img.shields.io/badge/Python-3.11+-blue.svg)
![LangChain](https://img.shields.io/badge/LangChain-1.2.13-orange.svg)
![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-green.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-2496ED.svg)
![License MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## Architecture

```
Research Agent → Personalization Agent → Email Writer → Content Optimizer → Scheduler → Memory
```

| Agent | Description |
|-------|-------------|
| **Research Agent** | Gathers company data, LinkedIn profiles, and industry trends |
| **Personalization Agent** | Builds detailed prospect profiles & identifies pain points |
| **Email Writer** | Generates personalized emails using AIDA/PAS frameworks |
| **Content Optimizer** | Improves readability, CTA, and spam score |
| **Scheduler Agent** | Calculates optimal send times based on prospect profile |
| **Memory Agent** | Stores interactions in FAISS vector DB for learning |

---

## Features

- **6-Agent Pipeline**: Specialized LangChain agents handle each stage
- **Personalized Emails**: Dynamic content based on prospect research
- **Spam Optimization**: Automatic spam score checking & content improvement
- **FAISS Memory**: Vector-based storage of past interactions
- **CSV Bulk Send**: Process hundreds of leads at once
- **Dry Run Mode**: Test pipeline without sending real emails
- **Docker Ready**: One-command deployment with docker-compose
- **CLI Interface**: Simple command-line usage for all modes

---

## Quickstart

### Option 1: Docker (Recommended)
```bash
git clone https://github.com/yourusername/cold-email-ai.git
cd cold-email-ai
cp .env.example .env  # Add your OPENAI_API_KEY
docker-compose up
```

### Option 2: Local Python
```bash
git clone https://github.com/yourusername/cold-email-ai.git
cd cold-email-ai
pip install -r requirements.txt
cp .env.example .env  # Add your OPENAI_API_KEY
python main.py --mode status
```

---

## CLI Usage

### 1. Check System Status
```bash
python main.py --mode status
```

### 2. Process Single Lead
```bash
python main.py --mode single --name "John Doe" --company "Acme Corp" --no-send --no-memory
```

### 3. Bulk Process CSV
```bash
python main.py --mode csv --file leads.csv --no-send
```

---

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `OPENAI_API_KEY` | OpenAI API key (required) | `""` |
| `LLM_MODEL` | LLM model to use | `gpt-4o-mini` |
| `TEMP_RESEARCH` | Research agent temperature | `0.1` |
| `TEMP_WRITER` | Writer agent temperature | `0.7` |
| `TEMP_OPTIMIZER` | Optimizer agent temperature | `0.3` |
| `SMTP_SERVER` | SMTP server address | `smtp.gmail.com` |
| `SMTP_PORT` | SMTP server port | `587` |
| `SMTP_USERNAME` | SMTP username/email | `""` |
| `SMTP_PASSWORD` | SMTP password/app password | `""` |
| `DRY_RUN` | Skip email sending (true/false) | `false` |
| `USE_FAISS` | Use FAISS vector storage (true/false) | `true` |

---

## Project Structure

```
cold-email-ai/
├── agents/
│   ├── research_agent.py
│   ├── personalization_agent.py
│   ├── email_writer_agent.py
│   ├── content_optimizer_agent.py
│   ├── scheduler_agent.py
│   └── memory_agent.py
├── tools/
│   ├── research_tool.py
│   ├── linkedin_tool.py
│   ├── email_tool.py
│   └── spam_checker_tool.py
├── prompts/
│   ├── research_prompt.py
│   ├── personalization_prompt.py
│   ├── email_writer_prompt.py
│   └── content_optimizer_prompt.py
├── tests/
│   ├── conftest.py
│   ├── test_spam_checker.py
│   ├── test_email_tool.py
│   ├── test_config.py
│   └── test_pipeline.py
├── frontend/
│   └── index.html
├── main.py
├── config.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .env.example
└── README.md
```

---

## Testing

Run the full test suite:
```bash
pytest tests/ -v --tb=short --no-cov
```

**Test Coverage:**
- `test_spam_checker.py`: 6 tests for spam scoring
- `test_email_tool.py`: 5 tests for email validation & sending
- `test_config.py`: 4 tests for configuration validation
- `test_pipeline.py`: 3 tests for end-to-end pipeline

---

## Built With

- **Python 3.11+** - Core programming language
- **LangChain 1.2.13** - Agent framework & chains
- **OpenAI GPT-4o-mini** - LLM for content generation
- **FAISS** - Vector database for memory storage
- **Docker** - Containerization & deployment
- **Tailwind CSS** - Frontend styling
- **smtplib** - Email sending via SMTP

---

## License

MIT License - see [LICENSE](LICENSE) for details.

---

*Made with ❤️ using LangChain + OpenAI*
>>>>>>> d4c9146 (Cold email outreach dashboard)
