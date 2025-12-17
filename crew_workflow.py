"""
CrewAI Workflow for Portfolio Builder
======================================
This module orchestrates the CrewAI agents to work together on portfolio enhancement.
"""

from crewai import Crew, Process
from crew_agents import content_analyzer, resume_optimizer, portfolio_designer
from crew_tasks import (
    create_content_analysis_task,
    create_resume_optimization_task,
    create_portfolio_design_task,
    create_comprehensive_enhancement_task
)
import json
from typing import Dict, Any

class PortfolioEnhancementCrew:
    """
    Orchestrates the portfolio enhancement workflow using CrewAI
    """

    def __init__(self):
        """Initialize the portfolio enhancement crew"""
        self.agents = [content_analyzer, resume_optimizer, portfolio_designer]

    def analyze_portfolio(self, user_data: Dict[str, Any]) -> str:
        """
        Run content analysis on user portfolio

        Args:
            user_data: Dictionary containing user profile information

        Returns:
            Analysis results as string
        """
        task = create_content_analysis_task(user_data)

        crew = Crew(
            agents=[content_analyzer],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return str(result)

    def optimize_resume(self, career_data: Dict[str, Any]) -> str:
        """
        Run resume optimization

        Args:
            career_data: Dictionary containing career information

        Returns:
            Optimization results as string
        """
        task = create_resume_optimization_task(career_data)

        crew = Crew(
            agents=[resume_optimizer],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return str(result)

    def enhance_design(self, layout_data: Dict[str, Any]) -> str:
        """
        Run portfolio design enhancement

        Args:
            layout_data: Dictionary containing current layout information

        Returns:
            Design recommendations as string
        """
        task = create_portfolio_design_task(layout_data)

        crew = Crew(
            agents=[portfolio_designer],
            tasks=[task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return str(result)

    def comprehensive_enhancement(self, full_profile: Dict[str, Any]) -> str:
        """
        Run comprehensive portfolio enhancement using all agents

        Args:
            full_profile: Complete profile data

        Returns:
            Comprehensive enhancement plan as string
        """
        # Create tasks for each agent
        content_task = create_content_analysis_task(full_profile)
        resume_task = create_resume_optimization_task(full_profile)
        design_task = create_portfolio_design_task({
            'sections': ['About', 'Career', 'Skills', 'Education', 'Research', 'Achievements', 'Medium', 'YouTube'],
            'colors': 'Streamlit default theme',
            'layout': 'Wide layout with sidebar'
        })

        # Create crew with all agents and tasks
        crew = Crew(
            agents=self.agents,
            tasks=[content_task, resume_task, design_task],
            process=Process.sequential,
            verbose=True
        )

        result = crew.kickoff()
        return str(result)

    def quick_analysis(self, profile_summary: str) -> Dict[str, str]:
        """
        Run a quick analysis of portfolio using all three agents in parallel

        Args:
            profile_summary: Brief summary of the portfolio

        Returns:
            Dictionary with results from each agent
        """
        results = {}

        # Quick content analysis
        content_data = {'name': 'User', 'brief': profile_summary, 'skills': [], 'achievements': []}
        results['content_analysis'] = self.analyze_portfolio(content_data)

        return results


def run_portfolio_enhancement_demo():
    """
    Demo function to show how the CrewAI workflow works
    """
    # Sample user data (based on the existing constant.py structure)
    sample_data = {
        'name': 'Sample User',
        'brief': 'Data Scientist with 3 years of experience in machine learning and AI',
        'skills': ['Python', 'Machine Learning', 'Deep Learning', 'SQL', 'AWS'],
        'achievements': [
            'Published 2 research papers',
            'Led team of 5 developers',
            'Reduced model training time by 50%'
        ],
        'education': [
            {'degree': 'M.S.', 'field': 'Computer Science', 'year': '2021'},
            {'degree': 'B.S.', 'field': 'Computer Science', 'year': '2019'}
        ]
    }

    print("=" * 80)
    print("Portfolio Enhancement Crew - Demo Mode")
    print("=" * 80)

    crew_workflow = PortfolioEnhancementCrew()

    print("\n[1/3] Running Content Analysis...")
    print("-" * 80)
    content_result = crew_workflow.analyze_portfolio(sample_data)
    print(f"\nContent Analysis Result:\n{content_result}\n")

    print("\n[2/3] Running Resume Optimization...")
    print("-" * 80)
    resume_result = crew_workflow.optimize_resume(sample_data)
    print(f"\nResume Optimization Result:\n{resume_result}\n")

    print("\n[3/3] Running Design Enhancement...")
    print("-" * 80)
    design_data = {
        'sections': ['About', 'Experience', 'Skills', 'Education', 'Projects'],
        'colors': 'Default theme',
        'layout': 'Single column'
    }
    design_result = crew_workflow.enhance_design(design_data)
    print(f"\nDesign Enhancement Result:\n{design_result}\n")

    print("=" * 80)
    print("Demo Complete!")
    print("=" * 80)


if __name__ == "__main__":
    # Run demo if executed directly
    import os

    if not os.getenv("OPENAI_API_KEY"):
        print("WARNING: OPENAI_API_KEY environment variable not set!")
        print("Please set it before running the crew workflow.")
        print("\nExample:")
        print("  export OPENAI_API_KEY='your-api-key-here'")
    else:
        run_portfolio_enhancement_demo()
