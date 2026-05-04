"""
Content Optimizer Prompts for the Cold Email System.
Contains prompt templates for content optimization tasks.
"""

from langchain_core.prompts import PromptTemplate


class ContentOptimizerPrompts:
    """Collection of prompts for content optimizer agent."""

    @staticmethod
    def get_spam_scoring_prompt() -> str:
        """Get the spam scoring prompt template."""
        return """You are an email deliverability expert. Analyze the following email content for spam indicators and provide a spam likelihood score from 0-100.

EMAIL CONTENT:
Subject: {subject}
Body: {body}

ANALYSIS CHECKLIST:
- Spam trigger words (free, guarantee, limited time, act now, etc.)
- Excessive punctuation or capitalization
- Suspicious phrases or patterns
- Image-to-text ratio (if applicable)
- Sender reputation factors
- Content quality and relevance

Provide:
1. Spam score (0-100, where 0 is not spam and 100 is definitely spam)
2. List of specific spam indicators found
3. List of trust indicators found
4. Recommendations to reduce spam score

Format your response as:
SPAM_SCORE: [score]
SPAM_INDICATORS: [comma-separated list or "None"]
TRUST_INDICATORS: [comma-separated list or "None"]
RECOMMENDATIONS: [comma-separated list of actionable recommendations]
"""

    @staticmethod
    def get_content_improvement_prompt() -> str:
        """Get the content improvement prompt template."""
        return """You are an email optimization specialist. Improve the following email content to reduce spam likelihood while maintaining effectiveness and personalization.

ORIGINAL EMAIL:
Subject: {subject}
Body: {body}

SPAM ANALYSIS:
Spam Score: {spam_score}/100
Spam Indicators: {spam_indicators}
Trust Indicators: {trust_indicators}

TASK:
Create an improved version of the email that:
1. Reduces spam likelihood by addressing identified spam indicators
2. Maintains all personalization and key messaging
3. Preserves the call-to-action and value proposition
4. Keeps a professional, conversational tone
5. Adds trust indicators where appropriate

Provide ONLY the improved email in the same format:
Subject: [improved subject]
Body: [improved body]
"""

    @staticmethod
    def get_subject_line_prompt() -> str:
        """Get the subject line optimization prompt template."""
        return """You are an email subject line expert. Optimize the following subject line for better open rates while reducing spam likelihood.

ORIGINAL SUBJECT: {original_subject}
CURRENT SPAM SCORE: {spam_score}/100
SPAM INDICATORS: {spam_indicators}

TASK:
Generate 5 optimized subject line variations that:
1. Reduce spam likelihood (avoid spam trigger words, excessive caps/punctuation)
2. Maintain or improve personalization and relevance
3. Are under 50 characters when possible
4. Create curiosity or urgency appropriately
5. Avoid sounding generic or salesy

Return only the 5 subject lines, one per line, numbered 1-5.
"""