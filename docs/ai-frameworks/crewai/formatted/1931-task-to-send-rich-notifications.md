---
title: "Crewai: Task to send rich notifications"
description: "Task to send rich notifications section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to send rich notifications

notification_task = Task(
    description="""
    1. Send a formatted project completion message to #general with progress charts
    2. Send direct messages to team leads with task summaries
    3. Create interactive notification with action buttons for team feedback
    """,
    agent=notification_agent,
    expected_output="Rich notifications sent with interactive elements and formatted content"
)

crew = Crew(
    agents=[notification_agent],
    tasks=[notification_task]
)

crew.kickoff()
```

### Message Search and Analytics

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with Slack messaging capabilities](./1930-create-agent-with-slack-messaging-capabilities.md)

**Next:** [Create agent with Slack search and user management capabilities →](./1932-create-agent-with-slack-search-and-user-management.md)
