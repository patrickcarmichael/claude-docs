---
title: "Crewai: Task to analyze project status"
description: "Task to analyze project status section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to analyze project status

analysis_task = Task(
    description="""
    1. Get all projects and their issue types
    2. Search for all open issues across projects
    3. Analyze issue distribution by status and assignee
    4. Create a summary report issue with findings
    """,
    agent=project_analyst,
    expected_output="Project analysis completed with summary report created"
)

crew = Crew(
    agents=[project_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Automated Issue Management

```python  theme={null}
from crewai import Agent, Task, Crew

automation_manager = Agent(
    role="Automation Manager",
    goal="Automate issue management and workflow processes",
    backstory="An AI assistant that automates repetitive issue management tasks.",
    apps=['jira']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage issue workflow](./1775-task-to-manage-issue-workflow.md)

**Next:** [Task to automate issue management →](./1777-task-to-automate-issue-management.md)
