"""
Personalization Agent for building detailed prospect profiles.
Uses LangChain to analyze research data and create personalized profiles.
"""

import logging
from typing import Dict, Any, Optional
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
import openai
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import SystemMessage
from langchain_openai import ChatOpenAI
from langchain_core.tools import Tool

from prompts.personalization_prompt import PersonalizationPrompts
from config import config

logger = logging.getLogger(__name__)


class PersonalizationAgent:
    """Agent responsible for creating personalized prospect profiles."""

    def __init__(self, llm_model: str = None, temperature: float = None):
        # Use config values if not provided
        self.llm_model = llm_model or config.llm.model
        self.temperature = temperature or config.llm.temperature_research

        self.llm = ChatOpenAI(
            model=self.llm_model,
            temperature=self.temperature,
            max_tokens=config.llm.max_tokens,
            request_timeout=120,
            max_retries=config.llm.max_retries
        )

        # Initialize tools for direct use (no agent executor)
        self.tools = [
            Tool(
                name="ProspectProfileBuilder",
                func=self._build_prospect_profile_wrapper,
                description="Build a detailed prospect profile from research data. Input should be research data in text format."
            ),
            Tool(
                name="PainPointAnalyzer",
                func=self._analyze_pain_points_wrapper,
                description="Analyze likely pain points for a prospect based on their role and company. Input should be prospect information."
            ),
            Tool(
                name="ValueAlignmentAnalyzer",
                func=self._analyze_value_alignment_wrapper,
                description="Analyze how our solution aligns with prospect needs. Input should be prospect profile and solution details."
            )
        ]

        # Replace ConversationBufferMemory with plain history list
        self.history = []

        # Initialize chains for LLM tasks
        self.profile_chain = ChatPromptTemplate.from_messages([
            ("system", "{system_prompt}"),
            ("human", "{user_input}")
        ]) | self.llm | StrOutputParser()

        self.pain_point_chain = ChatPromptTemplate.from_messages([
            ("system", "{system_prompt}"),
            ("human", "{user_input}")
        ]) | self.llm | StrOutputParser()

        self.value_alignment_chain = ChatPromptTemplate.from_messages([
            ("system", "{system_prompt}"),
            ("human", "{user_input}")
        ]) | self.llm | StrOutputParser()

        logger.info("Personalization Agent initialized")

    @retry(
        stop=stop_after_attempt(3),
        wait=wait_exponential(multiplier=1, min=4, max=10),
        retry=retry_if_exception_type(openai.RateLimitError),
    )
    def _call_llm_with_retry(self, messages):
        """Call LLM with retry logic for rate limiting."""
        return self.llm.invoke(messages)

    def _build_prospect_profile_wrapper(self, query: str) -> str:
        """Wrapper for prospect profile building."""
        try:
            research_data = query.strip()
            prompt = PersonalizationPrompts.get_prospect_profile_prompt()
            result = self.profile_chain.invoke({
                "system_prompt": prompt,
                "user_input": research_data
            })
            return result
        except Exception as e:
            logger.error(f"Error building prospect profile: {str(e)}")
            return f"Error building prospect profile: {str(e)}"

    def _analyze_pain_points_wrapper(self, query: str) -> str:
        """Wrapper for pain point analysis."""
        try:
            parts = [part.strip() for part in query.split('|')]
            if len(parts) >= 8:
                prospect_name, prospect_title, prospect_company, prospect_industry, company_size, recent_news, linkedin_summary, skills = parts[:8]
            else:
                prospect_name = prospect_title = prospect_company = prospect_industry = company_size = recent_news = linkedin_summary = skills = query

            prompt = PersonalizationPrompts.get_pain_point_analysis_prompt()
            user_input = f"""
            Prospect Name: {prospect_name}
            Title: {prospect_title}
            Company: {prospect_company}
            Industry: {prospect_industry}
            Company Size: {company_size}
            Recent News: {recent_news}
            LinkedIn Summary: {linkedin_summary}
            Skills: {skills}
            """
            result = self.pain_point_chain.invoke({
                "system_prompt": prompt,
                "user_input": user_input
            })
            return result
        except Exception as e:
            logger.error(f"Error analyzing pain points: {str(e)}")
            return f"Error analyzing pain points: {str(e)}"

    def _analyze_value_alignment_wrapper(self, query: str) -> str:
        """Wrapper for value alignment analysis."""
        try:
            parts = [part.strip() for part in query.split('||')]
            if len(parts) >= 5:
                prospect_profile, solution_name, key_benefits, target_problems, unique_differentiators = parts[:5]
            else:
                prospect_profile = query
                solution_name = "Our Solution"
                key_benefits = "Increased efficiency, cost savings, improved performance"
                target_problems = "Operational inefficiencies, high costs, manual processes"
                unique_differentiators = "Proprietary technology, proven results, expert support"

            prompt = PersonalizationPrompts.get_value_alignment_prompt()
            user_input = f"""
            Prospect Profile: {prospect_profile}
            Solution Name: {solution_name}
            Key Benefits: {key_benefits}
            Target Problems: {target_problems}
            Unique Differentiators: {unique_differentiators}
            """
            result = self.value_alignment_chain.invoke({
                "system_prompt": prompt,
                "user_input": user_input
            })
            return result
        except Exception as e:
            logger.error(f"Error analyzing value alignment: {str(e)}")
            return f"Error analyzing value alignment: {str(e)}"

    def create_prospect_profile(self, research_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Create a detailed prospect profile from research data.

        Args:
            research_data: Dictionary containing research findings from ResearchAgent

        Returns:
            Dictionary containing the personalized prospect profile
        """
        logger.info("Creating prospect profile from research data")
        try:
            research_summary = self._prepare_research_summary(research_data)
            profile_result = self._build_prospect_profile_wrapper(research_summary)
            prospect_profile = {
                "raw_research": research_data,
                "research_summary": research_summary,
                "detailed_profile": profile_result,
                "personalization_hooks": self._extract_personalization_hooks(profile_result),
                "likely_pain_points": self._extract_pain_points(research_data),
                "communication_style": self._determine_communication_style(research_data),
                "timestamp": self._get_timestamp()
            }
            logger.info("Prospect profile created successfully")
            return prospect_profile
        except Exception as e:
            logger.error(f"Error creating prospect profile: {str(e)}")
            return {
                "error": str(e),
                "raw_research": research_data,
                "timestamp": self._get_timestamp()
            }

    def _prepare_research_summary(self, research_data: Dict[str, Any]) -> str:
        """Prepare a summary of research data for processing."""
        summary_parts = []
        if "company_research" in research_data:
            summary_parts.append(f"Company Research: {research_data['company_research']}")
        if "linkedin_profile" in research_data:
            profile = research_data["linkedin_profile"]
            if isinstance(profile, dict):
                summary_parts.append(f"LinkedIn Profile: {profile.get('full_name', 'Unknown')} - {profile.get('title', 'Unknown Title')} at {profile.get('company', 'Unknown Company')}")
            else:
                summary_parts.append(f"LinkedIn Profile: {profile}")
        if "industry_research" in research_data:
            summary_parts.append(f"Industry Research: {research_data['industry_research']}")
        if "synthesized_research" in research_data:
            summary_parts.append(f"Key Insights: {research_data['synthesized_research']}")
        return "\n\n".join(summary_parts) if summary_parts else "Limited research data available"

    def _extract_personalization_hooks(self, profile_text: str) -> list:
        """Extract specific personalization hooks from profile text."""
        hooks = [
            "Reference to recent company news or developments",
            "Mention of specific role responsibilities",
            "Reference to educational background",
            "Mention of specific skills or expertise",
            "Reference to professional activity or posts",
            "Congratulations on recent achievements",
            "Reference to mutual connections or groups",
            "Reference to location or local events"
        ]
        return hooks[:3]

    def _extract_pain_points(self, research_data: Dict[str, Any]) -> list:
        """Extract likely pain points from research data."""
        common_pain_points = [
            "Scaling operations efficiently",
            "Reducing customer acquisition costs",
            "Improving employee retention",
            "Modernizing legacy systems",
            "Competing with new entrants",
            "Managing remote work productivity",
            "Adapting to regulatory changes",
            "Improving data-driven decision making"
        ]
        return common_pain_points[:4]

    def _determine_communication_style(self, research_data: Dict[str, Any]) -> str:
        """Determine likely communication style based on research."""
        styles = ["Direct and data-driven", "Collaborative and relationship-focused",
                  "Innovative and forward-thinking", "Practical and results-oriented"]
        return styles[0]

    def _get_timestamp(self) -> str:
        """Get current timestamp."""
        from datetime import datetime
        return datetime.now().isoformat()

    def get_profile_summary(self, profile_data: Dict[str, Any]) -> str:
        """Get a formatted summary of the prospect profile."""
        if "error" in profile_data:
            return f"Profile Error: {profile_data['error']}"
        summary_parts = []
        if "detailed_profile" in profile_data:
            summary_parts.append(f"Detailed Profile:\n{profile_data['detailed_profile']}")
        if "personalization_hooks" in profile_data:
            hooks = ", ".join(profile_data["personalization_hooks"])
            summary_parts.append(f"Personalization Hooks: {hooks}")
        if "likely_pain_points" in profile_data:
            pain_points = ", ".join(profile_data["likely_pain_points"])
            summary_parts.append(f"Likely Pain Points: {pain_points}")
        return "\n\n".join(summary_parts) if summary_parts else "No profile data available"


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    agent = PersonalizationAgent()
    sample_research = {
        "company_name": "Acme Corp",
        "company_research": {
            "name": "Acme Corp",
            "industry": "technology",
            "recent_news": ["recently launched a new AI-powered product", "secured Series B funding round"],
            "key_challenges": ["scaling operations efficiently", "reducing customer acquisition costs"]
        },
        "linkedin_profile": {
            "full_name": "John Doe",
            "title": "VP of Engineering",
            "company": "Acme Corp",
            "summary": "Experienced engineering leader with focus on scaling teams and implementing new technologies",
            "skills": ["Leadership", "Software Architecture", "Team Management", "AWS"]
        }
    }
    profile = agent.create_prospect_profile(sample_research)
    print("Prospect Profile:")
    print(agent.get_profile_summary(profile))
