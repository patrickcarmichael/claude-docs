---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[outlook_agent],
    tasks=[send_email_task]
)

crew.kickoff()
```

### Email Management and Search

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to send an email](./1830-task-to-send-an-email.md)

**Next:** [Create an agent focused on email management →](./1832-create-an-agent-focused-on-email-management.md)
