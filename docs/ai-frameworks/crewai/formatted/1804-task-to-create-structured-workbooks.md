---
title: "Crewai: Task to create structured workbooks"
description: "Task to create structured workbooks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create structured workbooks

creation_task = Task(
    description="""
    1. Create a new quarterly report workbook
    2. Add multiple worksheets for different departments
    3. Create tables with headers for data organization
    4. Set up charts for key metrics visualization
    """,
    agent=workbook_creator,
    expected_output="Structured workbook created with multiple worksheets, tables, and charts"
)

crew = Crew(
    agents=[workbook_creator],
    tasks=[creation_task]
)

crew.kickoff()
```

### Data Manipulation and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

data_manipulator = Agent(
    role="Data Manipulator",
    goal="Update and manipulate data in Excel worksheets efficiently",
    backstory="An AI assistant that handles data updates, table management, and range operations.",
    apps=['microsoft_excel']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to analyze existing data](./1803-task-to-analyze-existing-data.md)

**Next:** [Task to manipulate data →](./1805-task-to-manipulate-data.md)
