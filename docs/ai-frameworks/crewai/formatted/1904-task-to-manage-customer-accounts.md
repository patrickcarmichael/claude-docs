---
title: "Crewai: Task to manage customer accounts"
description: "Task to manage customer accounts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage customer accounts

account_task = Task(
    description="""
    1. Create a new account for TechCorp Inc.
    2. Add John Doe as the primary contact for this account
    3. Create a follow-up task for next week to check on their project status
    """,
    agent=account_manager,
    expected_output="Account, contact, and follow-up task created successfully"
)

crew = Crew(
    agents=[account_manager],
    tasks=[account_task]
)

crew.kickoff()
```

### Advanced SOQL Queries and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Sales Data Analyst",
    goal="Generate insights from Salesforce data using SOQL queries",
    backstory="An analytical AI that excels at extracting meaningful insights from CRM data.",
    apps=['salesforce']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage sales pipeline](./1903-task-to-manage-sales-pipeline.md)

**Next:** [Complex task involving SOQL queries and data analysis →](./1905-complex-task-involving-soql-queries-and-data-analy.md)
