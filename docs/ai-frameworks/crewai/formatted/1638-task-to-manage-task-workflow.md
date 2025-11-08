---
title: "Crewai: Task to manage task workflow"
description: "Task to manage task workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage task workflow

task_workflow = Task(
    description="Create a task for project planning and assign it to the development team",
    agent=task_coordinator,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_coordinator],
    tasks=[task_workflow]
)

crew.kickoff()
```

### Advanced Project Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_manager = Agent(
    role="Project Manager",
    goal="Coordinate project activities and track team productivity",
    backstory="An experienced project manager who ensures projects are delivered on time.",
    apps=['clickup']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1637-run-the-task.md)

**Next:** [Complex task involving multiple ClickUp operations →](./1639-complex-task-involving-multiple-clickup-operations.md)
