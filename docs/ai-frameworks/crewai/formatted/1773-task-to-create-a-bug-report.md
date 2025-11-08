---
title: "Crewai: Task to create a bug report"
description: "Task to create a bug report section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a bug report

create_bug_task = Task(
    description="Create a bug report for the login functionality with high priority and assign it to the development team",
    agent=jira_agent,
    expected_output="Bug report created successfully with issue key"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Jira capabilities](./1772-create-an-agent-with-jira-capabilities.md)

**Next:** [Run the task →](./1774-run-the-task.md)
