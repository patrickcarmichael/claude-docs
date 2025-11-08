---
title: "Crewai: Task to analyze email patterns"
description: "Task to analyze email patterns section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to analyze email patterns

analysis_task = Task(
    description="""
    Search for all unread emails from the last 7 days,
    categorize them by sender domain,
    and create a summary report of communication patterns
    """,
    agent=email_analyst,
    expected_output="Email analysis report with communication patterns and recommendations"
)

crew = Crew(
    agents=[email_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Thread Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with Gmail search and analysis capabilities](./1664-create-agent-with-gmail-search-and-analysis-capabi.md)

**Next:** [Create agent with Gmail thread management capabilities →](./1666-create-agent-with-gmail-thread-management-capabili.md)
