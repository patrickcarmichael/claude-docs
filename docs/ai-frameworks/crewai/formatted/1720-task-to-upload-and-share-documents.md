---
title: "Crewai: Task to upload and share documents"
description: "Task to upload and share documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to upload and share documents

document_task = Task(
    description="Upload the quarterly report and share it with the finance team",
    agent=file_manager_agent,
    expected_output="Document uploaded and sharing permissions configured"
)

crew = Crew(
    agents=[file_manager_agent],
    tasks=[document_task]
)

crew.kickoff()
```

### Advanced File Management

```python  theme={null}
from crewai import Agent, Task, Crew

file_organizer = Agent(
    role="File Organizer",
    goal="Maintain organized file structure and manage permissions",
    backstory="An experienced file manager who ensures proper organization and access control.",
    apps=['google_drive']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Google Drive actions only](./1719-create-agent-with-specific-google-drive-actions-on.md)

**Next:** [Complex task involving multiple Google Drive operations →](./1721-complex-task-involving-multiple-google-drive-opera.md)
