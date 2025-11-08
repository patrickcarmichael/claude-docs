---
title: "Crewai: Task to list workspace users"
description: "Task to list workspace users section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to list workspace users

user_management_task = Task(
    description="List all users in the workspace and provide a summary of team members",
    agent=notion_agent,
    expected_output="Complete list of workspace users with their details"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Notion capabilities](./1886-create-an-agent-with-notion-capabilities.md)

**Next:** [Run the task →](./1888-run-the-task.md)
