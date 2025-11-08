---
title: "Crewai: Task to manage list data"
description: "Task to manage list data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage list data

list_management_task = Task(
    description="Get all lists from the project site, review items, and update status for completed tasks",
    agent=list_manager,
    expected_output="SharePoint lists reviewed and task statuses updated"
)

crew = Crew(
    agents=[list_manager],
    tasks=[list_management_task]
)

crew.kickoff()
```

### Document Library Management

```python  theme={null}
from crewai import Agent, Task, Crew

document_manager = Agent(
    role="Document Manager",
    goal="Manage SharePoint document libraries and files",
    backstory="An AI assistant that specializes in document organization and file management.",
    apps=['microsoft_sharepoint']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1845-run-the-task.md)

**Next:** [Task to manage documents →](./1847-task-to-manage-documents.md)
