---
title: "Crewai: Task to create a meeting and add a contact"
description: "Task to create a meeting and add a contact section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a meeting and add a contact

schedule_task = Task(
    description="Create a calendar event for tomorrow at 2 PM titled 'Team Meeting' with location 'Conference Room A', and create a new contact for 'John Smith' with email 'john.smith@example.com' and job title 'Project Manager'.",
    agent=scheduler,
    expected_output="Calendar event created and new contact added successfully."
)

crew = Crew(
    agents=[scheduler],
    tasks=[schedule_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent for calendar and contact management](./1834-create-an-agent-for-calendar-and-contact-managemen.md)

**Next:** [Troubleshooting →](./1836-troubleshooting.md)
