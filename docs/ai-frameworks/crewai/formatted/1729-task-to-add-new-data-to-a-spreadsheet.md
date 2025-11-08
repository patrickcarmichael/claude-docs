---
title: "Crewai: Task to add new data to a spreadsheet"
description: "Task to add new data to a spreadsheet section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to add new data to a spreadsheet

data_entry_task = Task(
    description="Add a new customer record to the customer database spreadsheet with name, email, and signup date",
    agent=sheets_agent,
    expected_output="New customer record added successfully to the spreadsheet"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Sheets capabilities](./1728-create-an-agent-with-google-sheets-capabilities.md)

**Next:** [Run the task →](./1730-run-the-task.md)
