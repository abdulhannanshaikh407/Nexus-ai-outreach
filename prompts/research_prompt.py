"""
Research Prompts for the Cold Email System.
Contains prompt templates for research-related tasks.
"""

from langchain_core.prompts import PromptTemplate


class ResearchPrompts:
    """Collection of prompts for research agent."""

    @staticmethod
    def get_synthesis_prompt() -> str:
        """Get the research synthesis prompt template."""
        return """You are a research analyst tasked with synthesizing information about a prospect for cold email outreach.

Based on the following research data, provide:
1. Key company insights (recent developments, challenges, opportunities)
2. Key professional insights about the prospect (role, background, likely priorities)
3. Industry context and trends that are relevant
4. Specific personalization opportunities for outreach
5. Likely pain points based on role, company, and industry

Research Data:
{context}

Synthesized Insights:
"""

    @staticmethod
    def get_company_research_prompt() -> str:
        """Get the company research prompt template."""
        return """Analyze the following company information and provide insights on:
1. Recent developments and news
2. Current challenges and pain points
3. Growth trajectory and funding status
4. Technology stack and innovations
5. Market position and competitors

Company Information:
{company_info}

Analysis:
"""

    @staticmethod
    def get_linkedin_research_prompt() -> str:
        """Get the LinkedIn research prompt template."""
        return """Analyze the following LinkedIn profile information and provide insights on:
1. Professional background and career progression
2. Current role and responsibilities
3. Skills and expertise areas
4. Professional interests and activities
5. Potential pain points based on role and experience

LinkedIn Profile:
{linkedin_info}

Analysis:
"""

    @staticmethod
    def get_industry_research_prompt() -> str:
        """Get the industry research prompt template."""
        return """Provide insights on the following industry including:
1. Current trends and innovations
2. Common challenges faced by companies
3. Growth opportunities and market direction
4. Regulatory landscape
5. Competitive dynamics

Industry: {industry}

Insights:
"""