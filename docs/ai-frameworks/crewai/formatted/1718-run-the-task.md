---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[drive_agent],
    tasks=[organize_files_task]
)

crew.kickoff()
```

### Filtering Specific Google Drive Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize files](./1717-task-to-organize-files.md)

**Next:** [Create agent with specific Google Drive actions only →](./1719-create-agent-with-specific-google-drive-actions-on.md)
