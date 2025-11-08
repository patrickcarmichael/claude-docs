---
title: "Crewai: Task to organize contact groups"
description: "Task to organize contact groups section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize contact groups

organization_task = Task(
    description="""
    1. List all existing contact groups
    2. Analyze contact distribution across groups
    3. Create new groups for better organization
    4. Move contacts to appropriate groups based on their information
    """,
    agent=group_organizer,
    expected_output="Contacts organized into logical groups with improved structure"
)

crew = Crew(
    agents=[group_organizer],
    tasks=[organization_task]
)

crew.kickoff()
```

### Comprehensive Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew

contact_specialist = Agent(
    role="Contact Management Specialist",
    goal="Provide comprehensive contact management across all sources",
    backstory="An AI assistant that handles all aspects of contact management including personal, directory, and other contacts.",
    apps=['google_contacts']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create and update contacts](./1692-task-to-create-and-update-contacts.md)

**Next:** [Complex contact management task →](./1694-complex-contact-management-task.md)
