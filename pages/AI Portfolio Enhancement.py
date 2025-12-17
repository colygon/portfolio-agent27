"""
AI Portfolio Enhancement Page
==============================
This page integrates CrewAI agents to provide AI-powered portfolio enhancement suggestions.
"""

import streamlit as st
import sys
import os

# Add parent directory to path to import crew modules
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from crew_workflow import PortfolioEnhancementCrew
from constant import info

st.set_page_config(page_title="AI Portfolio Enhancement", page_icon="🤖", layout="wide")

st.title("🤖 AI-Powered Portfolio Enhancement")
st.markdown("---")

st.info("""
This page uses **CrewAI** with three specialized AI agents to analyze and enhance your portfolio:
- **Content Analyzer**: Reviews your profile content and provides strategic insights
- **Resume Optimizer**: Optimizes your resume for ATS and impact
- **Portfolio Designer**: Suggests design and UX improvements
""")

# Check for OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    st.warning("⚠️ OpenAI API key not found in environment variables.")
    st.markdown("""
    To use this feature, you need to set your OpenAI API key:
    ```bash
    export OPENAI_API_KEY='your-api-key-here'
    ```
    """)
    st.stop()

# Initialize the crew
@st.cache_resource
def get_crew():
    return PortfolioEnhancementCrew()

crew = get_crew()

# Tabs for different enhancement options
tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Content Analysis",
    "📝 Resume Optimization",
    "🎨 Design Enhancement",
    "🚀 Comprehensive Review"
])

with tab1:
    st.header("Content Analysis")
    st.markdown("Get AI-powered insights on your profile content, achievements, and skills.")

    if st.button("Analyze My Content", key="analyze_content"):
        with st.spinner("🤖 AI agents analyzing your content..."):
            try:
                # Prepare user data from constant.py
                user_data = {
                    'name': info.get('name', 'N/A'),
                    'brief': info.get('Brief', 'N/A'),
                    'skills': info.get('skills', []),
                    'achievements': info.get('achievements', [])
                }

                result = crew.analyze_portfolio(user_data)

                st.success("✅ Analysis Complete!")
                st.markdown("### Analysis Results")
                st.markdown(result)

                # Download option
                st.download_button(
                    label="📥 Download Analysis",
                    data=result,
                    file_name="content_analysis.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("Make sure your OpenAI API key is valid and has sufficient credits.")

with tab2:
    st.header("Resume Optimization")
    st.markdown("Optimize your resume content for better impact and ATS compatibility.")

    if st.button("Optimize My Resume", key="optimize_resume"):
        with st.spinner("🤖 AI agents optimizing your resume..."):
            try:
                # Prepare career data
                career_data = {
                    'education': info.get('edu', pd.DataFrame()).to_dict('records') if 'edu' in info else [],
                    'skills': info.get('skills', []),
                    'achievements': info.get('achievements', []),
                    'experience': 'See timeline data in main app'
                }

                result = crew.optimize_resume(career_data)

                st.success("✅ Optimization Complete!")
                st.markdown("### Optimization Results")
                st.markdown(result)

                # Download option
                st.download_button(
                    label="📥 Download Optimized Content",
                    data=result,
                    file_name="resume_optimization.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error during optimization: {str(e)}")
                st.info("Make sure your OpenAI API key is valid and has sufficient credits.")

with tab3:
    st.header("Design Enhancement")
    st.markdown("Get suggestions to improve your portfolio's visual design and user experience.")

    if st.button("Enhance My Design", key="enhance_design"):
        with st.spinner("🤖 AI agents analyzing your design..."):
            try:
                # Prepare layout data
                layout_data = {
                    'sections': [
                        'About Me',
                        'Career Snapshot',
                        'Skills & Tools',
                        'Education',
                        'Research Papers',
                        'Achievements',
                        'Medium Profile',
                        'YouTube Channel'
                    ],
                    'colors': 'Streamlit default theme (white/gray with accent colors)',
                    'layout': 'Wide layout with sidebar for contact info and resume download'
                }

                result = crew.enhance_design(layout_data)

                st.success("✅ Design Analysis Complete!")
                st.markdown("### Design Recommendations")
                st.markdown(result)

                # Download option
                st.download_button(
                    label="📥 Download Design Recommendations",
                    data=result,
                    file_name="design_enhancement.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error during design analysis: {str(e)}")
                st.info("Make sure your OpenAI API key is valid and has sufficient credits.")

with tab4:
    st.header("Comprehensive Portfolio Review")
    st.markdown("Get a complete analysis combining content, optimization, and design insights.")

    if st.button("Run Comprehensive Review", key="comprehensive"):
        with st.spinner("🤖 All AI agents working together on your portfolio... This may take a few minutes."):
            try:
                # Prepare full profile data
                import pandas as pd

                full_profile = {
                    'name': info.get('name', 'N/A'),
                    'brief': info.get('Brief', 'N/A'),
                    'skills': info.get('skills', []),
                    'achievements': info.get('achievements', []),
                    'education': info.get('edu', pd.DataFrame()).to_dict('records') if 'edu' in info else [],
                }

                result = crew.comprehensive_enhancement(full_profile)

                st.success("✅ Comprehensive Review Complete!")
                st.markdown("### Complete Enhancement Plan")
                st.markdown(result)

                # Download option
                st.download_button(
                    label="📥 Download Complete Enhancement Plan",
                    data=result,
                    file_name="comprehensive_enhancement.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"❌ Error during comprehensive review: {str(e)}")
                st.info("Make sure your OpenAI API key is valid and has sufficient credits.")

# Footer
st.markdown("---")
st.markdown("""
### 💡 Tips for Best Results:
- Ensure your OpenAI API key is set in environment variables
- Review the suggestions and apply what fits your personal brand
- Use the downloaded reports for reference when updating your portfolio
- Run the analysis periodically as you gain new experience and skills

### 🔧 Technical Details:
This feature is powered by:
- **CrewAI** (>=0.86.0): Multi-agent orchestration framework
- **LangChain OpenAI** (>=0.3.0): LLM integration layer
- **GPT-4**: Advanced language model for analysis and recommendations
""")
