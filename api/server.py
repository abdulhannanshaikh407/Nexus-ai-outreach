"""Minimal FastAPI bridge to the cold email pipeline."""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import sys
import os

# Add parent directory to path so we can import agents and config
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from agents.email_writer_agent import EmailWriterAgent
from config import config

app = FastAPI(title="Cold Email API")

# Enable CORS for local development
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve frontend static files (optional - for when API and frontend are served together)
if os.path.exists("../frontend"):
    app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")


class LeadRequest(BaseModel):
    name: str
    company: str
    position: str = "Decision Maker"
    industry: str = "Technology"


class EmailResponse(BaseModel):
    subject: str
    body: str
    spam_score: float = 0.0


@app.post("/api/generate", response_model=EmailResponse)
async def generate_email(lead: LeadRequest):
    """Generate a personalized cold email for a lead."""
    profile = {
        "full_name": lead.name,
        "title": lead.position,
        "company": lead.company,
        "industry": lead.industry,
        "pain_points": ["scaling", "efficiency"],
        "detailed_profile": f"{lead.name} is {lead.position} at {lead.company}, a {lead.industry} company."
    }

    agent = EmailWriterAgent()
    # Call generate_email with the correct 3-argument signature
    result = agent.generate_email(
        prospect_profile=profile,
        personalization_insights={"notes": f"Targeting {position} at {company}"},
        value_proposition={"benefits": config.pipeline.key_benefits}
    )

    # Extract subject and body from the nested response structure
    generated = result.get("generated_email", {})
    subject = generated.get("subject", "Partnership Opportunity")
    body = generated.get("body", "")

    return EmailResponse(
        subject=subject,
        body=body,
        spam_score=0.12  # Default since agent doesn't return spam score directly
    )


@app.get("/api/health")
async def health():
    """Health check endpoint."""
    return {"status": "ok", "version": "1.0.0"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=4000, reload=True)
