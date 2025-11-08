---
title: "Crewai: Task to create data-driven presentations"
description: "Task to create data-driven presentations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create data-driven presentations

visualization_task = Task(
    description="""
    1. Create a new presentation for monthly sales report
    2. Import data from the sales spreadsheet
    3. Create charts and visualizations from the imported data
    4. Generate thumbnails for slide previews
    """,
    agent=data_visualizer,
    expected_output="Data-driven presentation created with imported spreadsheet data and visualizations"
)

crew = Crew(
    agents=[data_visualizer],
    tasks=[visualization_task]
)

crew.kickoff()
```

### Presentation Library Management

```python  theme={null}
from crewai import Agent, Task, Crew

library_manager = Agent(
    role="Presentation Library Manager",
    goal="Manage and organize presentation libraries",
    backstory="An AI assistant that manages presentation collections and file organization.",
    apps=['google_slides']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create and update presentations](./1747-task-to-create-and-update-presentations.md)

**Next:** [Task to manage presentation library →](./1749-task-to-manage-presentation-library.md)
