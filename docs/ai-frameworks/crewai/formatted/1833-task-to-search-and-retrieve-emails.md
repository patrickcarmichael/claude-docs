---
title: "Crewai: Task to search and retrieve emails"
description: "Task to search and retrieve emails section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to search and retrieve emails

search_emails_task = Task(
    description="Get the latest 20 unread emails and provide a summary of the most important ones.",
    agent=email_manager,
    expected_output="Summary of the most important unread emails with key details."
)

crew = Crew(
    agents=[email_manager],
    tasks=[search_emails_task]
)

crew.kickoff()
```

### Calendar and Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent focused on email management](./1832-create-an-agent-focused-on-email-management.md)

**Next:** [Create an agent for calendar and contact management →](./1834-create-an-agent-for-calendar-and-contact-managemen.md)
