---
title: "Crewai: Complex task involving financial analysis"
description: "Complex task involving financial analysis section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving financial analysis

analytics_task = Task(
    description="""
    1. Retrieve balance transactions for the current month
    2. Analyze customer payment patterns and subscription trends
    3. Identify high-value customers and subscription performance
    4. Generate monthly financial performance report
    """,
    agent=financial_analyst,
    expected_output="Comprehensive financial analysis with payment insights and recommendations"
)

crew = Crew(
    agents=[financial_analyst],
    tasks=[analytics_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage subscription operations](./1945-task-to-manage-subscription-operations.md)

**Next:** [Subscription Status Reference →](./1947-subscription-status-reference.md)
