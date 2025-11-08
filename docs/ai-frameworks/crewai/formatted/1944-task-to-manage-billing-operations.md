---
title: "Crewai: Task to manage billing operations"
description: "Task to manage billing operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage billing operations

billing_task = Task(
    description="Create a new customer and set up their premium subscription plan",
    agent=billing_manager,
    expected_output="Customer created and subscription activated successfully"
)

crew = Crew(
    agents=[billing_manager],
    tasks=[billing_task]
)

crew.kickoff()
```

### Subscription Management

```python  theme={null}
from crewai import Agent, Task, Crew

subscription_manager = Agent(
    role="Subscription Manager",
    goal="Manage customer subscriptions and optimize recurring revenue",
    backstory="An AI assistant that specializes in subscription lifecycle management and customer retention.",
    apps=['stripe']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1943-run-the-task.md)

**Next:** [Task to manage subscription operations →](./1945-task-to-manage-subscription-operations.md)
