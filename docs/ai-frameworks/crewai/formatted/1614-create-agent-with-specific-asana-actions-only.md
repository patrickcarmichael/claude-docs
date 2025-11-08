---
title: "Crewai: Create agent with specific Asana actions only"
description: "Create agent with specific Asana actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Asana actions only

task_manager_agent = Agent(
    role="Task Manager",
    goal="Create and manage tasks efficiently",
    backstory="An AI assistant that focuses on task creation and management.",
    apps=[
        'asana/create_task',
        'asana/update_task',
        'asana/get_tasks'
    ]  # Specific Asana actions
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1613-run-the-task.md)

**Next:** [Task to create and assign a task →](./1615-task-to-create-and-assign-a-task.md)
