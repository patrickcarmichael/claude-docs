---
title: "Crewai: Complex task involving multiple ClickUp operations"
description: "Complex task involving multiple ClickUp operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple ClickUp operations

project_coordination = Task(
    description="""
    1. Get all open tasks in the current space
    2. Identify overdue tasks and update their status
    3. Create a weekly report task summarizing project progress
    4. Assign the report task to the team lead
    """,
    agent=project_manager,
    expected_output="Project status updated and weekly report task created and assigned"
)

crew = Crew(
    agents=[project_manager],
    tasks=[project_coordination]
)

crew.kickoff()
```

### Task Search and Management

```python  theme={null}
from crewai import Agent, Task, Crew

task_analyst = Agent(
    role="Task Analyst",
    goal="Analyze task patterns and optimize team productivity",
    backstory="An AI assistant that analyzes task data to improve team efficiency.",
    apps=['clickup']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage task workflow](./1638-task-to-manage-task-workflow.md)

**Next:** [Task to analyze and optimize task distribution →](./1640-task-to-analyze-and-optimize-task-distribution.md)
