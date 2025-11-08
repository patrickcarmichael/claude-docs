---
title: "Crewai: Task to create and update contacts"
description: "Task to create and update contacts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create and update contacts

curation_task = Task(
    description="""
    1. Search for existing contacts related to new business partners
    2. Create new contacts for partners not in the system
    3. Update existing contact information with latest details
    4. Organize contacts into appropriate groups
    """,
    agent=contact_curator,
    expected_output="Contact database updated with new partners and organized groups"
)

crew = Crew(
    agents=[contact_curator],
    tasks=[curation_task]
)

crew.kickoff()
```

### Contact Group Management

```python  theme={null}
from crewai import Agent, Task, Crew

group_organizer = Agent(
    role="Contact Group Organizer",
    goal="Organize contacts into meaningful groups and categories",
    backstory="An AI assistant that specializes in contact organization and group management.",
    apps=['google_contacts']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to search and manage directory](./1691-task-to-search-and-manage-directory.md)

**Next:** [Task to organize contact groups →](./1693-task-to-organize-contact-groups.md)
