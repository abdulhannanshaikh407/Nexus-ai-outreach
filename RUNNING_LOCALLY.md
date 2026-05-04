# 🚀 Run Guide — AI Cold Email Outreach System

Complete step-by-step instructions to run the entire project locally.

---

## 📋 Prerequisites

| Tool | Version | Check |
|------|---------|-------|
| Python | 3.11+ | `python --version` |
| Docker Desktop | Latest | `docker --version` |
| Node.js (optional) | 18+ | `node --version` |
| Git | Latest | `git --version` |

---

## 1️⃣ Clone & Configure

```bash
# Clone the repository
git clone https://github.com/abdulhannanshaikh407/cold-email-system.git
cd cold-email-system

# Copy environment template
cp .env.example .env
```

Edit `.env` and add your keys:
```env
OPENAI_API_KEY=sk-your-openai-key-here
LLM_MODEL=gpt-4o-mini
SMTP_SERVER=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your-email@gmail.com
SMTP_PASSWORD=your-app-password
FROM_NAME=Your Name
```

---

## 2️⃣ Run the Frontend (No Server Needed)

The frontend is pure HTML/CSS/JS — no build tools required.

### Option A: Direct File Open
```bash
# Windows
start frontend/index.html

# macOS
open frontend/index.html

# Linux
xdg-open frontend/index.html
```

### Option B: Simple HTTP Server (Recommended)
```bash
# Python
cd frontend && python -m http.server 3000

# Node.js
npx serve frontend -p 3000
```

Then visit: **http://localhost:3000**

### What You'll See:
- **Home** — Landing page with architecture, features, and setup guide
- **Dashboard** — Stats, pipeline visualization, and leads table *(from Stitch UI)*
- **Live Demo** — System heartbeat, agent clusters, global map, and live feed *(from Stitch UI)*
- **Activity Log** — Agent roster, pipeline flow, live log, and metrics *(from Stitch UI)*

---

## 3️⃣ Run the API Server (Port 4000)

> ⚠️ **Note:** Port 8000 is used by `linkinpostgenerator`. The cold-email API uses **port 4000**.

```bash
# Install dependencies
pip install -r requirements.txt

# Start the API server
cd api
uvicorn server:app --host 0.0.0.0 --port 4000 --reload
```

Visit: **http://localhost:4000/api/health**
```json
{"status": "ok", "version": "1.0.0"}
```

### API Endpoints:

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/health` | Health check |
| POST | `/api/generate` | Generate personalized cold email |

### Test the API:
```bash
curl -X POST http://localhost:4000/api/generate \
  -H "Content-Type: application/json" \
  -d '{"name": "John Doe", "company": "Acme Corp", "position": "VP Engineering"}'
```

---

## 4️⃣ Run with Docker (Full Stack)

```bash
# Build and start all services
docker-compose up --build

# Services started:
#   - cold-email  (main pipeline, DRY_RUN=true)
#   - api          (FastAPI on port 4000)
```

Visit:
- **Frontend + API**: http://localhost:4000
- **Health Check**: http://localhost:4000/api/health

### Docker Commands:
```bash
# View logs
docker-compose logs -f

# Stop all services
docker-compose down

# Rebuild after changes
docker-compose up --build --force-recreate
```

---

## 5️⃣ Run the Full Pipeline (CLI)

```bash
# Dry run (no emails sent)
python main.py --dry-run --leads example_leads.csv

# Live mode (sends real emails — be careful!)
python main.py --leads example_leads.csv

# Test single email generation
python demo.py
```

---

## 🌐 Port Reference

| Service | Port | Description |
|---------|------|-------------|
| `linkinpostgenerator` | **8000** | Existing LinkedIn post generator |
| Cold Email API | **4000** | FastAPI backend for email generation |
| Frontend (manual) | **3000** | Static file server (optional) |
| Frontend + API (Docker) | **4000** | Served by FastAPI StaticFiles |

---

## 🔧 Troubleshooting

### Port 4000 already in use?
```bash
# Find and kill the process
# Windows:
netstat -ano | grep :4000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:4000 | xargs kill -9
```

### OpenAI API errors?
- Verify `OPENAI_API_KEY` in `.env`
- Check billing at https://platform.openai.com/account/billing

### Module not found errors?
```bash
pip install -r requirements.txt --upgrade
```

### Docker issues?
```bash
docker-compose down -v
docker system prune -a
docker-compose up --build
```

---

## 📁 Project Structure

```
cold-email-system/
├── frontend/
│   ├── index.html          ← Single multi-page app (4 tabs)
│   ├── design-tokens.css   ← Shared Stitch design tokens
│   └── tailwind-config.js  ← Shared Tailwind configuration
├── api/
│   ├── __init__.py
│   └── server.py          ← FastAPI backend (port 4000)
├── agents/                 ← 6 LangChain agents
├── tools/                  ← Agent tools
├── prompts/               ← LLM prompts
├── main.py                ← CLI pipeline runner
├── demo.py                ← Quick demo script
├── docker-compose.yml      ← Multi-service orchestration
├── requirements.txt        ← Python dependencies
└── RUN.md                ← This file
```

---

## 🔗 Links

- **GitHub Repository**: https://github.com/abdulhannanshaikh407/cold-email-system
- **Frontend Demo**: http://localhost:3000 (after starting)
- **API Health**: http://localhost:4000/api/health (after starting)
- **LinkedIn Post Generator**: http://localhost:8000 (existing service)
