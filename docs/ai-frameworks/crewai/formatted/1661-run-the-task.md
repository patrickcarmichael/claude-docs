---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[gmail_agent],
    tasks=[send_email_task]
)

crew.kickoff()
```

### Filtering Specific Gmail Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to send a follow-up email](./1660-task-to-send-a-follow-up-email.md)

**Next:** [Create agent with specific Gmail actions only →](./1662-create-agent-with-specific-gmail-actions-only.md)
