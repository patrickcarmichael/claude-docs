---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[asana_agent],
    tasks=[create_project_task]
)

crew.kickoff()
```

### Filtering Specific Asana Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new project](./1612-task-to-create-a-new-project.md)

**Next:** [Create agent with specific Asana actions only →](./1614-create-agent-with-specific-asana-actions-only.md)
