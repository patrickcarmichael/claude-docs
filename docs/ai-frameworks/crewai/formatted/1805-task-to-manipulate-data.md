---
title: "Crewai: Task to manipulate data"
description: "Task to manipulate data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manipulate data

manipulation_task = Task(
    description="""
    1. Get data from existing worksheets
    2. Update specific ranges with new information
    3. Add new rows to existing tables
    4. Create additional charts based on updated data
    5. Organize data across multiple worksheets
    """,
    agent=data_manipulator,
    expected_output="Data updated across worksheets with new charts and organized structure"
)

crew = Crew(
    agents=[data_manipulator],
    tasks=[manipulation_task]
)

crew.kickoff()
```

### Advanced Excel Automation

```python  theme={null}
from crewai import Agent, Task, Crew

excel_automator = Agent(
    role="Excel Automator",
    goal="Automate complex Excel workflows and data processing",
    backstory="An AI assistant that automates sophisticated Excel operations and data workflows.",
    apps=['microsoft_excel']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create structured workbooks](./1804-task-to-create-structured-workbooks.md)

**Next:** [Complex automation task →](./1806-complex-automation-task.md)
