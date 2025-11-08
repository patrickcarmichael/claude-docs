---
title: "Crewai: Task to organize files"
description: "Task to organize files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize files

organization_task = Task(
    description="Create a folder structure for the marketing team and organize existing files",
    agent=file_organizer_agent,
    expected_output="Folder structure created and files organized"
)

crew = Crew(
    agents=[file_organizer_agent],
    tasks=[organization_task]
)

crew.kickoff()
```

### Advanced File Management

```python  theme={null}
from crewai import Agent, Task, Crew

file_manager = Agent(
    role="File Manager",
    goal="Maintain organized file structure and manage document lifecycle",
    backstory="An experienced file manager who ensures documents are properly organized and accessible.",
    apps=['box']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Box actions only](./1626-create-agent-with-specific-box-actions-only.md)

**Next:** [Complex task involving multiple Box operations →](./1628-complex-task-involving-multiple-box-operations.md)
