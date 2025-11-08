---
title: "Crewai: Complex task involving analytics and reporting"
description: "Complex task involving analytics and reporting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving analytics and reporting

analytics_task = Task(
    description="""
    1. Search for all open tickets from the last 30 days
    2. Analyze ticket resolution times and customer satisfaction
    3. Identify common issues and support patterns
    4. Generate weekly support performance report
    """,
    agent=support_analyst,
    expected_output="Comprehensive support analytics report with performance insights and recommendations"
)

crew = Crew(
    agents=[support_analyst],
    tasks=[analytics_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage ticket lifecycle](./1963-task-to-manage-ticket-lifecycle.md)

**Next:** [CrewAI AMP →](./1965-crewai-amp.md)
