---
title: "Crewai: Task to manage documents"
description: "Task to manage documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage documents

document_task = Task(
    description="""
    1. Get all files from the main document library
    2. Upload new policy documents to the appropriate folders
    3. Organize files by department and date
    4. Remove outdated documents
    """,
    agent=document_manager,
    expected_output="Document library organized with new files uploaded and outdated files removed"
)

crew = Crew(
    agents=[document_manager],
    tasks=[document_task]
)

crew.kickoff()
```

### Site Administration and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew

site_administrator = Agent(
    role="Site Administrator",
    goal="Administer and analyze SharePoint sites",
    backstory="An AI assistant that handles site administration and provides insights on site usage.",
    apps=['microsoft_sharepoint']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage list data](./1846-task-to-manage-list-data.md)

**Next:** [Task for site administration →](./1848-task-for-site-administration.md)
