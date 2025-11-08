---
title: "Crewai: Task to manage ticket lifecycle"
description: "Task to manage ticket lifecycle section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage ticket lifecycle

ticket_workflow = Task(
    description="""
    1. Create a new support ticket for account access issues
    2. Add internal notes with troubleshooting steps
    3. Update ticket priority based on customer tier
    4. Add resolution comments and close the ticket
    """,
    agent=ticket_manager,
    expected_output="Complete ticket lifecycle managed from creation to resolution"
)

crew = Crew(
    agents=[ticket_manager],
    tasks=[ticket_workflow]
)

crew.kickoff()
```

### Support Analytics and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

support_analyst = Agent(
    role="Support Analyst",
    goal="Analyze support metrics and generate insights for team performance",
    backstory="An analytical AI that excels at extracting insights from support data and ticket patterns.",
    apps=['zendesk']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage support workflow](./1962-task-to-manage-support-workflow.md)

**Next:** [Complex task involving analytics and reporting →](./1964-complex-task-involving-analytics-and-reporting.md)
