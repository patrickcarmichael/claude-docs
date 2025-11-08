---
title: "Crewai: Task to manage subscription operations"
description: "Task to manage subscription operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage subscription operations

subscription_task = Task(
    description="""
    1. Create a new product "Premium Service Plan" with advanced features
    2. Set up subscription plans with different tiers
    3. Create customers and assign them to appropriate plans
    4. Monitor subscription status and handle billing issues
    """,
    agent=subscription_manager,
    expected_output="Subscription management system configured with customers and active plans"
)

crew = Crew(
    agents=[subscription_manager],
    tasks=[subscription_task]
)

crew.kickoff()
```

### Financial Analytics and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

financial_analyst = Agent(
    role="Financial Analyst",
    goal="Analyze payment data and generate financial insights",
    backstory="An analytical AI that excels at extracting insights from payment and subscription data.",
    apps=['stripe']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage billing operations](./1944-task-to-manage-billing-operations.md)

**Next:** [Complex task involving financial analysis →](./1946-complex-task-involving-financial-analysis.md)
