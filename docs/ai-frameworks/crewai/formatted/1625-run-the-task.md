---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[box_agent],
    tasks=[create_structure_task]
)

crew.kickoff()
```

### Filtering Specific Box Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a folder structure](./1624-task-to-create-a-folder-structure.md)

**Next:** [Create agent with specific Box actions only →](./1626-create-agent-with-specific-box-actions-only.md)
