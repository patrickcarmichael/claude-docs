---
title: "Crewai: Task to analyze existing data"
description: "Task to analyze existing data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to analyze existing data

analysis_task = Task(
    description="Analyze sales data in existing workbooks and create summary charts and tables",
    agent=data_analyst,
    expected_output="Data analyzed with summary charts and tables created"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

### Workbook Creation and Structure

```python  theme={null}
from crewai import Agent, Task, Crew

workbook_creator = Agent(
    role="Workbook Creator",
    goal="Create structured Excel workbooks with multiple worksheets and data organization",
    backstory="An AI assistant that creates well-organized Excel workbooks for various business needs.",
    apps=['microsoft_excel']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1802-run-the-task.md)

**Next:** [Task to create structured workbooks →](./1804-task-to-create-structured-workbooks.md)
