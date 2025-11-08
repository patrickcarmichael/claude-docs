---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[onedrive_agent],
    tasks=[organize_files_task]
)

crew.kickoff()
```

### File Upload and Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to list files and create a folder](./1816-task-to-list-files-and-create-a-folder.md)

**Next:** [Create an agent focused on file operations →](./1818-create-an-agent-focused-on-file-operations.md)
