---
title: "Crewai: Task to send a message and retrieve recent messages"
description: "Task to send a message and retrieve recent messages section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to send a message and retrieve recent messages

messaging_task = Task(
    description="Send a message 'Hello team! This is an automated update from our AI assistant.' to the General channel of team 'your_team_id', then retrieve the last 10 messages from that channel.",
    agent=messenger,
    expected_output="Message sent successfully and recent messages retrieved."
)

crew = Crew(
    agents=[messenger],
    tasks=[messaging_task]
)

crew.kickoff()
```

### Meeting Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent focused on messaging](./1861-create-an-agent-focused-on-messaging.md)

**Next:** [Create an agent for meeting management →](./1863-create-an-agent-for-meeting-management.md)
