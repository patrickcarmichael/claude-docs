---
title: "Crewai: Task to update data based on conditions"
description: "Task to update data based on conditions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to update data based on conditions

update_task = Task(
    description="""
    1. Get spreadsheet properties and structure
    2. Read current data from specific ranges
    3. Update values in target ranges with new data
    4. Append new records to the bottom of the sheet
    """,
    agent=data_updater,
    expected_output="Spreadsheet data updated successfully with new values and records"
)

crew = Crew(
    agents=[data_updater],
    tasks=[update_task]
)

crew.kickoff()
```

### Complex Data Management Workflow

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_manager = Agent(
    role="Data Workflow Manager",
    goal="Manage complex data workflows across multiple spreadsheets",
    backstory="An AI assistant that orchestrates complex data operations across multiple spreadsheets.",
    apps=['google_sheets']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create and set up new spreadsheets](./1734-task-to-create-and-set-up-new-spreadsheets.md)

**Next:** [Complex workflow task →](./1736-complex-workflow-task.md)
