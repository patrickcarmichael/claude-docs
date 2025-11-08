---
title: "Crewai: Task to manage sales pipeline"
description: "Task to manage sales pipeline section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage sales pipeline

pipeline_task = Task(
    description="Create a qualified lead and convert it to an opportunity with $50,000 value",
    agent=sales_manager,
    expected_output="Lead created and opportunity established successfully"
)

crew = Crew(
    agents=[sales_manager],
    tasks=[pipeline_task]
)

crew.kickoff()
```

### Contact and Account Management

```python  theme={null}
from crewai import Agent, Task, Crew

account_manager = Agent(
    role="Account Manager",
    goal="Manage customer accounts and maintain strong relationships",
    backstory="An AI assistant that specializes in account management and customer relationship building.",
    apps=['salesforce']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1902-run-the-task.md)

**Next:** [Task to manage customer accounts →](./1904-task-to-manage-customer-accounts.md)
