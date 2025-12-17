"""
CrewAI Tasks for Portfolio Builder
===================================
This module defines tasks that the agents will perform to enhance portfolios.
"""

from crewai import Task
from crew_agents import content_analyzer, resume_optimizer, portfolio_designer

def create_content_analysis_task(user_data: dict) -> Task:
    """
    Create a task for analyzing user profile content

    Args:
        user_data: Dictionary containing user profile information

    Returns:
        Task object for content analysis
    """
    return Task(
        description=f"""Analyze the following user profile data and provide comprehensive insights:

        Name: {user_data.get('name', 'N/A')}
        Brief: {user_data.get('brief', 'N/A')}
        Skills: {user_data.get('skills', [])}
        Achievements: {user_data.get('achievements', [])}

        Your analysis should include:
        1. Strengths and unique selling points
        2. Areas that need more emphasis or detail
        3. Missing elements that could strengthen the profile
        4. Alignment with current industry trends
        5. Suggestions for better storytelling

        Provide actionable recommendations for improvement.""",
        agent=content_analyzer,
        expected_output="A detailed analysis report with strengths, weaknesses, and actionable recommendations"
    )

def create_resume_optimization_task(career_data: dict) -> Task:
    """
    Create a task for optimizing resume content

    Args:
        career_data: Dictionary containing career and education information

    Returns:
        Task object for resume optimization
    """
    return Task(
        description=f"""Optimize the resume content for maximum impact:

        Education: {career_data.get('education', [])}
        Experience: {career_data.get('experience', 'See timeline data')}
        Skills: {career_data.get('skills', [])}

        Your optimization should include:
        1. Rewrite job descriptions to be more impactful and achievement-focused
        2. Add quantifiable metrics where possible
        3. Ensure ATS-friendly keywords are included
        4. Improve action verbs and power words
        5. Optimize bullet point structure
        6. Ensure consistency in formatting and tense

        Provide the optimized content with explanations for major changes.""",
        agent=resume_optimizer,
        expected_output="Optimized resume content with improved descriptions, metrics, and ATS-friendly formatting"
    )

def create_portfolio_design_task(current_layout: dict) -> Task:
    """
    Create a task for suggesting portfolio design improvements

    Args:
        current_layout: Dictionary describing current portfolio structure

    Returns:
        Task object for portfolio design enhancement
    """
    return Task(
        description=f"""Analyze the current portfolio design and suggest improvements:

        Current Sections: {current_layout.get('sections', [])}
        Color Scheme: {current_layout.get('colors', 'Default Streamlit theme')}
        Layout Type: {current_layout.get('layout', 'Wide layout with sidebar')}

        Your design recommendations should cover:
        1. Visual hierarchy and information architecture
        2. Color scheme and typography improvements
        3. Section ordering and content flow
        4. Interactive elements and engagement features
        5. Mobile responsiveness considerations
        6. Accessibility improvements
        7. Loading performance optimization
        8. Visual elements (charts, graphs, images) placement and style

        Provide specific, actionable design recommendations that can be implemented.""",
        agent=portfolio_designer,
        expected_output="Comprehensive design improvement recommendations with specific implementation suggestions"
    )

def create_comprehensive_enhancement_task(full_profile: dict) -> Task:
    """
    Create a comprehensive task that combines all three agents' expertise

    Args:
        full_profile: Complete profile data

    Returns:
        Task object for comprehensive portfolio enhancement
    """
    return Task(
        description=f"""Perform a comprehensive portfolio enhancement analysis:

        Profile Data: {full_profile}

        This is a collaborative task that requires:
        1. Content analysis and strategic recommendations
        2. Resume content optimization with ATS considerations
        3. Design and UX improvements

        Work together to create a holistic improvement plan that considers:
        - Content quality and impact
        - Technical optimization (ATS, SEO)
        - Visual design and user experience
        - Personal branding consistency
        - Competitive positioning

        Deliver a comprehensive action plan with prioritized recommendations.""",
        agent=content_analyzer,  # Lead agent, can delegate to others
        expected_output="A comprehensive portfolio enhancement plan with prioritized action items across content, optimization, and design"
    )

__all__ = [
    'create_content_analysis_task',
    'create_resume_optimization_task',
    'create_portfolio_design_task',
    'create_comprehensive_enhancement_task'
]
