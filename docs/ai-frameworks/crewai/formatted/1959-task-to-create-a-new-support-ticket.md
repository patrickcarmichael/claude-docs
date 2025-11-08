---
title: "Crewai: Task to create a new support ticket"
description: "Task to create a new support ticket section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new support ticket

create_ticket_task = Task(
    description="Create a high-priority support ticket for John Smith who is unable to access his account after password reset",
    agent=zendesk_agent,
    expected_output="Support ticket created successfully with ticket ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Zendesk capabilities](./1958-create-an-agent-with-zendesk-capabilities.md)

**Next:** [Run the task →](./1960-run-the-task.md)
