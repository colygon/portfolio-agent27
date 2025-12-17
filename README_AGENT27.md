# Agent 27 - Portfolio Builder CrewAI Upgrade

## Quick Summary

This is the **Agent 27** upgrade of the Portfolio Builder application, enhanced with CrewAI multi-agent capabilities.

### Original Project
- **Repository**: https://github.com/mehulgupta2016154/resume_builder
- **Type**: Streamlit-based portfolio/resume builder
- **Description**: Interactive portfolio website with career timeline, skills visualization, research papers, and more

### CrewAI Upgrade

**Three AI Agents Created:**

1. **Content Analyzer Agent** - Analyzes profile content and provides strategic insights
2. **Resume Optimizer Agent** - Optimizes resume content for ATS and impact
3. **Portfolio Designer Agent** - Suggests design and UX improvements

### Key Features Added

- AI-powered portfolio analysis and recommendations
- Resume optimization with ATS compatibility
- Design and UX enhancement suggestions
- Comprehensive review combining all three agents
- Downloadable analysis reports
- New Streamlit page: "AI Portfolio Enhancement"

### Quick Start

```bash
# Clone the repository
git clone https://github.com/colygon/portfolio-agent27.git
cd portfolio-agent27

# Checkout the upgrade branch
git checkout crewai-upgrade

# Install dependencies
pip install -r requirements.txt

# Set up OpenAI API key
export OPENAI_API_KEY='your-key-here'

# Run the app
streamlit run streamlit_app.py
```

### Documentation

See **CREWAI_UPGRADE.md** for complete documentation including:
- Architecture details
- Usage instructions
- API setup
- Troubleshooting
- Future enhancements

### Files Added

```
portfolio-agent27/
├── crew_agents.py              # Agent definitions
├── crew_tasks.py               # Task definitions
├── crew_workflow.py            # Workflow orchestration
├── pages/
│   └── AI Portfolio Enhancement.py  # Streamlit UI
├── CREWAI_UPGRADE.md          # Complete documentation
├── .env.example               # Environment template
└── requirements.txt           # Updated with CrewAI deps
```

### Dependencies

- `crewai>=0.86.0` - Multi-agent framework
- `langchain-openai>=0.3.0` - LLM integration
- `python-dotenv>=1.0.0` - Environment management

### Branch Information

- **Main Branch**: Original portfolio code
- **crewai-upgrade Branch**: CrewAI enhanced version (current)

### Agent Info

- **Agent ID**: Agent 27
- **Fork Location**: /Users/colinlowenberg/crew/portfolio-agent27
- **Remote**: https://github.com/colygon/portfolio-agent27
- **Upgrade Branch**: crewai-upgrade

### Status

✅ Complete - All tasks finished and pushed to remote repository

---

**Upgraded by Agent 27** | **Date**: 2025-12-17
