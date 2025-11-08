---
title: "Crewai: Task to manage issue workflow"
description: "Task to manage issue workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage issue workflow

issue_workflow = Task(
    description="Create a feature request issue and update the status of related issues to reflect current progress",
    agent=issue_manager,
    expected_output="Feature request created and related issues updated"
)

crew = Crew(
    agents=[issue_manager],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Project and Team Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate projects and teams in Linear efficiently",
    backstory="An experienced project coordinator who manages development cycles and team workflows.",
    apps=['linear']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1788-run-the-task.md)

**Next:** [Task to coordinate project setup →](./1790-task-to-coordinate-project-setup.md)
