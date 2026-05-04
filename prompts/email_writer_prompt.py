"""
Email Writer Prompts for the Cold Email System.
Contains prompt templates for email generation tasks.
"""

from langchain_core.prompts import PromptTemplate


class EmailWriterPrompts:
    """Collection of prompts for email writer agent."""

    @staticmethod
    def get_email_generation_prompt() -> str:
        """Get the email generation prompt template."""
        return """You are an expert cold email copywriter specializing in B2B outreach.
Your task is to write a highly personalized, compelling cold email using the AIDA (Attention, Interest, Desire, Action) framework.

PROSPECT INFORMATION:
{prospect_profile}

YOUR SOLUTION:
Solution Name: {solution_name}
Key Benefits:
{key_benefits}

RESEARCH INSIGHTS:
{research_summary}

TASK:
Write a cold email that:
1. Grabs attention with a personalized hook referencing the prospect's recent activity, company news, or shared interest
2. Builds interest by connecting your solution to their specific pain points or goals
3. Creates desire by highlighting the most relevant benefits for their situation
4. Ends with a clear, low-pressure call-to-action (e.g., scheduling a brief call)

REQUIREMENTS:
- Keep the email concise (3-4 short paragraphs max)
- Use a professional but conversational tone
- Avoid spammy language and excessive exclamation points
- Personalize extensively using the prospect's name, company, and research insights
- Focus on value proposition, not features
- Include exactly one call-to-action

EMAIL FORMAT:
Subject: [Compelling subject line that incorporates personalization]

Body:
[Email body following AIDA structure]

Write only the email in the specified format, nothing else.
"""

    @staticmethod
    def get_subject_optimization_prompt() -> str:
        """Get the subject line optimization prompt template."""
        return """You are an email subject line expert. Your task is to optimize cold email subject lines for maximum open rates.

ORIGINAL SUBJECT:
{original_subject}

PROSPECT CONTEXT:
{prospect_profile}

YOUR SOLUTION:
Solution Name: {solution_name}

TASK:
Generate 5 variations of the subject line that:
1. Are personalized and relevant to the prospect
2. Create curiosity or urgency without being spammy
3. Reference the prospect's company, role, or recent activity when possible
4. Are under 50 characters when possible
5. Avoid all caps, excessive punctuation, and spam trigger words

Return only the 5 subject lines, one per line, numbered 1-5.
"""

    @staticmethod
    def get_email_parse_prompt() -> str:
        """Get the email parsing prompt template."""
        return """You are an email parsing assistant. Extract the subject line and body from the following email text.

EMAIL TEXT:
{email_text}

TASK:
Return the subject and body in the following format:
Subject: [extracted subject]
Body: [extracted body]

If no clear subject line is present, generate one based on the body content.
"""

    @staticmethod
    def get_fallback_prompt() -> str:
        """Get the fallback email generation prompt for when structured output fails."""
        return """Write a personalized cold email for the following prospect:

PROSPECT:
{prospect_profile}

YOUR SOLUTION:
Solution Name: {solution_name}
Key Benefits:
{key_benefits}

Make the email:
- Personalized and relevant
- Professional yet conversational
- Focused on value, not features
- 3-4 short paragraphs
- With a clear call-to-action

Return only the email body.
"""