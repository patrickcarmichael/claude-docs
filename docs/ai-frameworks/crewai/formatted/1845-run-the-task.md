---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[sharepoint_agent],
    tasks=[content_organization_task]
)

crew.kickoff()
```

### List Management and Data Operations

```python  theme={null}
from crewai import Agent, Task, Crew

list_manager = Agent(
    role="List Manager",
    goal="Manage SharePoint lists and data efficiently",
    backstory="An AI assistant that focuses on SharePoint list management and data operations.",
    apps=[
        'microsoft_sharepoint/get_site_lists',
        'microsoft_sharepoint/get_list_items',
        'microsoft_sharepoint/create_list_item',
        'microsoft_sharepoint/update_list_item'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize SharePoint content](./1844-task-to-organize-sharepoint-content.md)

**Next:** [Task to manage list data →](./1846-task-to-manage-list-data.md)
