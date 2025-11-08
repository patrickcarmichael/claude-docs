---
title: "Crewai: Task to list teams and channels"
description: "Task to list teams and channels section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to list teams and channels

explore_teams_task = Task(
    description="List all teams I'm a member of and then get the channels for the first team.",
    agent=teams_agent,
    expected_output="List of teams and channels displayed."
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Microsoft Teams capabilities](./1858-create-an-agent-with-microsoft-teams-capabilities.md)

**Next:** [Run the task →](./1860-run-the-task.md)
