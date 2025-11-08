---
title: "Crewai: Task for financial modeling"
description: "Task for financial modeling section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task for financial modeling

modeling_task = Task(
    description="""
    1. Create financial model workbooks with multiple scenarios
    2. Set up input tables for assumptions and variables
    3. Create calculation worksheets with formulas and logic
    4. Generate charts for financial projections and trends
    5. Add summary tables for key financial metrics
    6. Create sensitivity analysis tables
    """,
    agent=financial_modeler,
    expected_output="Financial model created with scenarios, calculations, and analysis charts"
)

crew = Crew(
    agents=[financial_modeler],
    tasks=[modeling_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex automation task](./1806-complex-automation-task.md)

**Next:** [Troubleshooting →](./1808-troubleshooting.md)
