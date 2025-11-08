---
title: "Crewai: Create an agent with Excel capabilities"
description: "Create an agent with Excel capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Excel capabilities

excel_agent = Agent(
    role="Excel Data Manager",
    goal="Manage Excel workbooks and data efficiently",
    backstory="An AI assistant specialized in Excel data management and analysis.",
    apps=['microsoft_excel']  # All Excel actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1799-usage-examples.md)

**Next:** [Task to create and populate a workbook →](./1801-task-to-create-and-populate-a-workbook.md)
