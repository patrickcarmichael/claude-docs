---
title: "Crewai: Task to create a bug report"
description: "Task to create a bug report section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a bug report

create_bug_task = Task(
    description="Create a high-priority bug report for the authentication system and assign it to the backend team",
    agent=linear_agent,
    expected_output="Bug report created successfully with issue ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Linear capabilities](./1786-create-an-agent-with-linear-capabilities.md)

**Next:** [Run the task →](./1788-run-the-task.md)
