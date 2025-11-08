---
title: "Crewai: Task to send project updates"
description: "Task to send project updates section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to send project updates

update_task = Task(
    description="Send a project status update to the #general channel with current progress",
    agent=slack_agent,
    expected_output="Project update message sent successfully to team channel"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Slack capabilities](./1925-create-an-agent-with-slack-capabilities.md)

**Next:** [Run the task →](./1927-run-the-task.md)
