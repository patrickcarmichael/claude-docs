---
title: "Crewai: Task to analyze data and create reports"
description: "Task to analyze data and create reports section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to analyze data and create reports

analysis_task = Task(
    description="""
    1. Retrieve all sales data from the current month's spreadsheet
    2. Analyze the data for trends and patterns
    3. Create a summary report in a new row with key metrics
    """,
    agent=data_analyst,
    expected_output="Sales data analyzed and summary report created with key insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Spreadsheet Creation and Management

```python  theme={null}
from crewai import Agent, Task, Crew

spreadsheet_manager = Agent(
    role="Spreadsheet Manager",
    goal="Create and manage spreadsheets efficiently",
    backstory="An AI assistant that specializes in creating and organizing spreadsheets.",
    apps=['google_sheets']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to collect and organize data](./1732-task-to-collect-and-organize-data.md)

**Next:** [Task to create and set up new spreadsheets →](./1734-task-to-create-and-set-up-new-spreadsheets.md)
