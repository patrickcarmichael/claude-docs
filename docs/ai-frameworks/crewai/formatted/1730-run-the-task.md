---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[sheets_agent],
    tasks=[data_entry_task]
)

crew.kickoff()
```

### Filtering Specific Google Sheets Tools

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to add new data to a spreadsheet](./1729-task-to-add-new-data-to-a-spreadsheet.md)

**Next:** [Create agent with specific Google Sheets actions only →](./1731-create-agent-with-specific-google-sheets-actions-o.md)
