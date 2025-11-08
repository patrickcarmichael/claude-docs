---
title: "Crewai: Task to create a new issue"
description: "Task to create a new issue section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new issue

create_issue_task = Task(
    description="Create a bug report issue for the login functionality in the main repository",
    agent=github_agent,
    expected_output="Issue created successfully with issue number"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Github capabilities](./1647-create-an-agent-with-github-capabilities.md)

**Next:** [Run the task →](./1649-run-the-task.md)
