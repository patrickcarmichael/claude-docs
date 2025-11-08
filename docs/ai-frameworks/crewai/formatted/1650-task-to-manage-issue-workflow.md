---
title: "Crewai: Task to manage issue workflow"
description: "Task to manage issue workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage issue workflow

issue_workflow = Task(
    description="Create a feature request issue and assign it to the development team",
    agent=issue_manager,
    expected_output="Feature request issue created and assigned successfully"
)

crew = Crew(
    agents=[issue_manager],
    tasks=[issue_workflow]
)

crew.kickoff()
```

### Release Management

```python  theme={null}
from crewai import Agent, Task, Crew

release_manager = Agent(
    role="Release Manager",
    goal="Manage software releases and versioning",
    backstory="An experienced release manager who handles version control and release processes.",
    apps=['github']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1649-run-the-task.md)

**Next:** [Task to create a new release →](./1651-task-to-create-a-new-release.md)
