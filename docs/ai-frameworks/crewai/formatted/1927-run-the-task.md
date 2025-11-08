---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[slack_agent],
    tasks=[update_task]
)

crew.kickoff()
```

### Filtering Specific Slack Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to send project updates](./1926-task-to-send-project-updates.md)

**Next:** [Create agent with specific Slack actions only →](./1928-create-agent-with-specific-slack-actions-only.md)
