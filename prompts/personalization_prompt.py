"""
Personalization Prompts for the Cold Email System.
Contains prompt templates for personalization-related tasks.
"""

from langchain_core.prompts import PromptTemplate


class PersonalizationPrompts:
    """Collection of prompts for personalization agent."""

    @staticmethod
    def get_profile_building_prompt() -> str:
        """Get the profile building prompt template."""
        return """You are an expert sales researcher specializing in B2B prospect profiling.
Your task is to create a detailed prospect profile based on the following information:

PROSPECT DATA:
{prospect_data}

TASK:
Create a comprehensive prospect profile that includes:
1. Professional background and current role
2. Key responsibilities and decision-making authority
3. Likely pain points and challenges based on role, company, and industry
4. Professional interests and potential triggers for outreach
5. Communication preferences and style hints
6. Personalization hooks for outreach (recent achievements, shared connections, etc.)

REQUIREMENTS:
- Focus on actionable insights for cold email personalization
- Keep the profile concise but detailed (4-6 bullet points or short paragraphs)
- Base all inferences on the provided data
- Highlight specific personalization opportunities
- Avoid generic statements that could apply to anyone

OUTPUT FORMAT:
**Professional Background**: [brief summary]
**Current Role & Responsibilities**: [key points]
**Likely Pain Points**: [specific challenges]
**Professional Interests**: [areas of focus]
**Personalization Hooks**: [specific opportunities for tailored outreach]
"""