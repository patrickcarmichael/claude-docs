---
title: "Crewai: Task to create and assign a task"
description: "Task to create and assign a task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create and assign a task

task_management = Task(
    description="Create a task called 'Review quarterly reports' and assign it to the appropriate team member",
    agent=task_manager_agent,
    expected_output="Task created and assigned successfully"
)

crew = Crew(
    agents=[task_manager_agent],
    tasks=[task_management]
)

crew.kickoff()
```

### Advanced Project Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Coordinate project activities and track progress",
    backstory="An experienced project coordinator who ensures projects run smoothly.",
    apps=['asana']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Asana actions only](./1614-create-agent-with-specific-asana-actions-only.md)

**Next:** [Complex task involving multiple Asana operations →](./1616-complex-task-involving-multiple-asana-operations.md)
