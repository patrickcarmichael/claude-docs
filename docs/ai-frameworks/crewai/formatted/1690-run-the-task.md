---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[contacts_agent],
    tasks=[contact_management_task]
)

crew.kickoff()
```

### Directory Search and Management

```python  theme={null}
from crewai import Agent, Task, Crew

directory_manager = Agent(
    role="Directory Manager",
    goal="Search and manage directory people and contacts",
    backstory="An AI assistant that specializes in directory management and people search.",
    apps=[
        'google_contacts/search_directory_people',
        'google_contacts/list_directory_people',
        'google_contacts/search_contacts'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to retrieve and organize contacts](./1689-task-to-retrieve-and-organize-contacts.md)

**Next:** [Task to search and manage directory →](./1691-task-to-search-and-manage-directory.md)
