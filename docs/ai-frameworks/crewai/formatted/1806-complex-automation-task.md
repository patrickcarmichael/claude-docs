---
title: "Crewai: Complex automation task"
description: "Complex automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex automation task

automation_task = Task(
    description="""
    1. Scan all Excel workbooks for specific data patterns
    2. Create consolidated reports from multiple workbooks
    3. Generate charts and tables for trend analysis
    4. Set up named ranges for easy data reference
    5. Create dashboard worksheets with key metrics
    6. Clean up unused worksheets and tables
    """,
    agent=excel_automator,
    expected_output="Automated Excel workflow completed with consolidated reports and dashboards"
)

crew = Crew(
    agents=[excel_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Financial Modeling and Analysis

```python  theme={null}
from crewai import Agent, Task, Crew

financial_modeler = Agent(
    role="Financial Modeler",
    goal="Create financial models and analysis in Excel",
    backstory="An AI assistant specialized in financial modeling and analysis using Excel.",
    apps=['microsoft_excel']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manipulate data](./1805-task-to-manipulate-data.md)

**Next:** [Task for financial modeling →](./1807-task-for-financial-modeling.md)
