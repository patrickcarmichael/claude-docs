---
title: "Crewai: Complex workflow task"
description: "Complex workflow task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex workflow task

workflow_task = Task(
    description="""
    1. Get all customer data from the main customer spreadsheet
    2. Create a new monthly summary spreadsheet
    3. Append summary data to the new spreadsheet
    4. Update customer status based on activity metrics
    5. Generate reports with proper formatting
    """,
    agent=workflow_manager,
    expected_output="Monthly customer workflow completed with new spreadsheet and updated data"
)

crew = Crew(
    agents=[workflow_manager],
    tasks=[workflow_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to update data based on conditions](./1735-task-to-update-data-based-on-conditions.md)

**Next:** [Troubleshooting →](./1737-troubleshooting.md)
