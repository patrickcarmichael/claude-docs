---
title: "Crewai: Create agent with specific Google Sheets actions only"
description: "Create agent with specific Google Sheets actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Google Sheets actions only

data_collector = Agent(
    role="Data Collector",
    goal="Collect and organize data in spreadsheets",
    backstory="An AI assistant that focuses on data collection and organization.",
    apps=[
        'google_sheets/get_values',
        'google_sheets/update_values'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1730-run-the-task.md)

**Next:** [Task to collect and organize data →](./1732-task-to-collect-and-organize-data.md)
