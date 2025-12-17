"""
CrewAI Agents for Portfolio Builder
====================================
This module defines three specialized agents for resume/portfolio enhancement:
1. Content Analyzer Agent - Analyzes user profile data and extracts key insights
2. Resume Optimizer Agent - Optimizes resume content for better presentation
3. Portfolio Designer Agent - Suggests design improvements and layout enhancements
"""

from crewai import Agent
from crewai_tools import Tool
from langchain_openai import ChatOpenAI
import os

# Initialize the LLM
llm = ChatOpenAI(
    model="gpt-4",
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

# Agent 1: Content Analyzer Agent
content_analyzer = Agent(
    role="Content Analyzer Specialist",
    goal="Analyze user profile data, career history, skills, and achievements to extract key insights and identify areas for improvement",
    backstory="""You are an expert in career development and personal branding.
    With years of experience in HR and talent acquisition, you have a keen eye for
    identifying strengths in a professional profile and highlighting areas that need
    enhancement. You understand what recruiters look for and can analyze career
    trajectories to provide actionable insights.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agent 2: Resume Optimizer Agent
resume_optimizer = Agent(
    role="Resume Optimization Expert",
    goal="Optimize resume content by enhancing descriptions, quantifying achievements, and ensuring ATS-friendly formatting",
    backstory="""You are a professional resume writer with expertise in crafting
    compelling narratives that showcase professional accomplishments. You understand
    Applicant Tracking Systems (ATS) and know how to optimize resumes for both
    automated screening and human reviewers. You excel at transforming mundane job
    descriptions into impactful achievement statements with quantifiable metrics.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Agent 3: Portfolio Designer Agent
portfolio_designer = Agent(
    role="Portfolio Design Consultant",
    goal="Suggest design improvements, layout enhancements, and visual elements to make the portfolio more engaging and professional",
    backstory="""You are a UX/UI designer specializing in personal branding and
    portfolio websites. You understand the principles of visual hierarchy, color
    theory, and user experience design. You can suggest improvements to make a
    portfolio stand out while maintaining professionalism and ensuring excellent
    user experience across different devices.""",
    verbose=True,
    allow_delegation=False,
    llm=llm
)

# Custom Tools for the agents
class PortfolioTools:
    """Custom tools for portfolio enhancement"""

    @staticmethod
    def analyze_skills_gap(skills_list: str) -> str:
        """
        Analyzes a list of skills and identifies potential gaps or trending skills to add

        Args:
            skills_list: Comma-separated string of current skills

        Returns:
            Analysis of skill gaps and recommendations
        """
        return f"Analyzing skills: {skills_list}\nThis tool would integrate with job market APIs in production."

    @staticmethod
    def keyword_optimizer(text: str) -> str:
        """
        Optimizes text for ATS keywords and industry-specific terminology

        Args:
            text: Text content to optimize

        Returns:
            Optimized text with improved keywords
        """
        return f"Optimizing text for ATS compatibility: {text[:100]}..."

    @staticmethod
    def design_analyzer(layout_description: str) -> str:
        """
        Analyzes current design layout and provides improvement suggestions

        Args:
            layout_description: Description of current portfolio layout

        Returns:
            Design recommendations and best practices
        """
        return f"Analyzing layout: {layout_description}\nProviding design recommendations..."

# Export agents and tools
__all__ = ['content_analyzer', 'resume_optimizer', 'portfolio_designer', 'PortfolioTools', 'llm']
