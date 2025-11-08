---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[clickup_agent],
    tasks=[create_task]
)

crew.kickoff()
```

### Filtering Specific ClickUp Tools

```python  theme={null}

task_coordinator = Agent(
    role="Task Coordinator",
    goal="Create and manage tasks efficiently",
    backstory="An AI assistant that focuses on task creation and status management.",
    apps=['clickup/create_task']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new task](./1636-task-to-create-a-new-task.md)

**Next:** [Task to manage task workflow →](./1638-task-to-manage-task-workflow.md)
