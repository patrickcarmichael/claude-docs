---
title: "Crewai: Task to create and set up new spreadsheets"
description: "Task to create and set up new spreadsheets section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create and set up new spreadsheets

setup_task = Task(
    description="""
    1. Create a new spreadsheet for quarterly reports
    2. Set up proper headers and structure
    3. Add initial data and formatting
    """,
    agent=spreadsheet_manager,
    expected_output="New quarterly report spreadsheet created and properly structured"
)

crew = Crew(
    agents=[spreadsheet_manager],
    tasks=[setup_task]
)

crew.kickoff()
```

### Automated Data Updates

```python  theme={null}
from crewai import Agent, Task, Crew

data_updater = Agent(
    role="Data Updater",
    goal="Automatically update and maintain spreadsheet data",
    backstory="An AI assistant that maintains data accuracy and updates records automatically.",
    apps=['google_sheets']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to analyze data and create reports](./1733-task-to-analyze-data-and-create-reports.md)

**Next:** [Task to update data based on conditions →](./1735-task-to-update-data-based-on-conditions.md)
