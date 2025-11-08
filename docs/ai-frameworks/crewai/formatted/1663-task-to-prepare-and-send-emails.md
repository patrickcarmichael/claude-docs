---
title: "Crewai: Task to prepare and send emails"
description: "Task to prepare and send emails section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to prepare and send emails

email_coordination = Task(
    description="Search for emails from the marketing team, create a summary draft, and send it to stakeholders",
    agent=email_coordinator,
    expected_output="Summary email sent to stakeholders"
)

crew = Crew(
    agents=[email_coordinator],
    tasks=[email_coordination]
)

crew.kickoff()
```

### Email Search and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Gmail actions only](./1662-create-agent-with-specific-gmail-actions-only.md)

**Next:** [Create agent with Gmail search and analysis capabilities →](./1664-create-agent-with-gmail-search-and-analysis-capabi.md)
