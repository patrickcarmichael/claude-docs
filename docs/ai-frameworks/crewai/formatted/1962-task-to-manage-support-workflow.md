---
title: "Crewai: Task to manage support workflow"
description: "Task to manage support workflow section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage support workflow

support_task = Task(
    description="Create a ticket for login issues, add troubleshooting comments, and update status to resolved",
    agent=support_agent,
    expected_output="Support ticket managed through complete resolution workflow"
)

crew = Crew(
    agents=[support_agent],
    tasks=[support_task]
)

crew.kickoff()
```

### Advanced Ticket Management

```python  theme={null}
from crewai import Agent, Task, Crew

ticket_manager = Agent(
    role="Ticket Manager",
    goal="Manage support ticket workflows and ensure timely resolution",
    backstory="An AI assistant that specializes in support ticket triage and workflow optimization.",
    apps=['zendesk']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Zendesk actions only](./1961-create-agent-with-specific-zendesk-actions-only.md)

**Next:** [Task to manage ticket lifecycle →](./1963-task-to-manage-ticket-lifecycle.md)
