---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[hubspot_agent],
    tasks=[create_company_task]
)

crew.kickoff()
```

### Filtering Specific HubSpot Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new company](./1760-task-to-create-a-new-company.md)

**Next:** [Create agent with specific HubSpot actions only →](./1762-create-agent-with-specific-hubspot-actions-only.md)
