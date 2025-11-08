---
title: "Crewai: Task to collect and organize data"
description: "Task to collect and organize data section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to collect and organize data

data_collection = Task(
    description="Retrieve current inventory data and add new product entries to the inventory spreadsheet",
    agent=data_collector,
    expected_output="Inventory data retrieved and new products added successfully"
)

crew = Crew(
    agents=[data_collector],
    tasks=[data_collection]
)

crew.kickoff()
```

### Data Analysis and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_analyst = Agent(
    role="Data Analyst",
    goal="Analyze spreadsheet data and generate insights",
    backstory="An experienced data analyst who extracts insights from spreadsheet data.",
    apps=['google_sheets']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific Google Sheets actions only](./1731-create-agent-with-specific-google-sheets-actions-o.md)

**Next:** [Task to analyze data and create reports →](./1733-task-to-analyze-data-and-create-reports.md)
