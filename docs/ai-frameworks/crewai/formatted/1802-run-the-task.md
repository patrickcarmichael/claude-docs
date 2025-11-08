---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[excel_agent],
    tasks=[data_management_task]
)

crew.kickoff()
```

### Data Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze data in Excel and create comprehensive reports",
    backstory="An AI assistant that specializes in data analysis and Excel reporting.",
    apps=[
        'microsoft_excel/get_workbooks',
        'microsoft_excel/get_range_data',
        'microsoft_excel/create_chart',
        'microsoft_excel/add_table'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create and populate a workbook](./1801-task-to-create-and-populate-a-workbook.md)

**Next:** [Task to analyze existing data →](./1803-task-to-analyze-existing-data.md)
