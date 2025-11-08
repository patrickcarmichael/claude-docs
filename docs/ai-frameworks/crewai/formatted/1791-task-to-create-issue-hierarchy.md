---
title: "Crewai: Task to create issue hierarchy"
description: "Task to create issue hierarchy section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create issue hierarchy

hierarchy_task = Task(
    description="""
    1. Search for large feature issues that need to be broken down
    2. For each complex issue, create sub-issues for different components
    3. Update the parent issues with proper descriptions and links to sub-issues
    4. Assign sub-issues to appropriate team members based on expertise
    """,
    agent=task_organizer,
    expected_output="Complex issues broken down into manageable sub-tasks with proper assignments"
)

crew = Crew(
    agents=[task_organizer],
    tasks=[hierarchy_task]
)

crew.kickoff()
```

### Automated Development Workflow

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate development workflow processes in Linear",
    backstory="An AI assistant that automates repetitive development workflow tasks.",
    apps=['linear']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to coordinate project setup](./1790-task-to-coordinate-project-setup.md)

**Next:** [Complex workflow automation task →](./1792-complex-workflow-automation-task.md)
