---
title: "Crewai: Task to create a new project"
description: "Task to create a new project section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new project

create_project_task = Task(
    description="Create a new project called 'Q1 Marketing Campaign' in the Marketing workspace",
    agent=asana_agent,
    expected_output="Confirmation that the project was created successfully with project ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Asana capabilities](./1611-create-an-agent-with-asana-capabilities.md)

**Next:** [Run the task →](./1613-run-the-task.md)
