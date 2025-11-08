---
title: "Crewai: Task to coordinate team communication"
description: "Task to coordinate team communication section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to coordinate team communication

coordination_task = Task(
    description="Send task completion notifications to team members and update project channels",
    agent=communication_manager,
    expected_output="Team notifications sent and project channels updated successfully"
)

crew = Crew(
    agents=[communication_manager],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Advanced Messaging with Block Kit

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Slack actions only](./1928-create-agent-with-specific-slack-actions-only.md)

**Next:** [Create agent with Slack messaging capabilities →](./1930-create-agent-with-slack-messaging-capabilities.md)
