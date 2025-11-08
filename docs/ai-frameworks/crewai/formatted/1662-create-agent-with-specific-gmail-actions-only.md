---
title: "Crewai: Create agent with specific Gmail actions only"
description: "Create agent with specific Gmail actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Gmail actions only

email_coordinator = Agent(
    role="Email Coordinator",
    goal="Coordinate email communications and manage drafts",
    backstory="An AI assistant that focuses on email coordination and draft management.",
    apps=[
        'gmail/send_email',
        'gmail/fetch_emails',
        'gmail/create_draft'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1661-run-the-task.md)

**Next:** [Task to prepare and send emails →](./1663-task-to-prepare-and-send-emails.md)
