---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[teams_agent],
    tasks=[explore_teams_task]
)

crew.kickoff()
```

### Messaging and Communication

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to list teams and channels](./1859-task-to-list-teams-and-channels.md)

**Next:** [Create an agent focused on messaging →](./1861-create-an-agent-focused-on-messaging.md)
