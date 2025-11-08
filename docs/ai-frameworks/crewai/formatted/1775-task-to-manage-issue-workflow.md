---
title: "Crewai: Task to manage issue workflow"
description: "Task to manage issue workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage issue workflow

issue_workflow = Task(
    description="Create a feature request issue and update the status of related issues",
    agent=issue_coordinator,
    expected_output="Feature request created and related issues updated"
)

crew = Crew(
    agents=[issue_coordinator],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Project Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

project_analyst = Agent(
    role="Project Analyst",
    goal="Analyze project data and generate insights from Jira",
    backstory="An experienced project analyst who extracts insights from project management data.",
    apps=['jira']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1774-run-the-task.md)

**Next:** [Task to analyze project status →](./1776-task-to-analyze-project-status.md)
