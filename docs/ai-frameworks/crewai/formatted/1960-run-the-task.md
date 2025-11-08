---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[zendesk_agent],
    tasks=[create_ticket_task]
)

crew.kickoff()
```

### Filtering Specific Zendesk Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new support ticket](./1959-task-to-create-a-new-support-ticket.md)

**Next:** [Create agent with specific Zendesk actions only →](./1961-create-agent-with-specific-zendesk-actions-only.md)
