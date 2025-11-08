---
title: "Crewai: Task to create and update presentations"
description: "Task to create and update presentations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create and update presentations

content_task = Task(
    description="Create a new presentation and add content slides with charts and text",
    agent=content_manager,
    expected_output="Presentation created with updated content and visual elements"
)

crew = Crew(
    agents=[content_manager],
    tasks=[content_task]
)

crew.kickoff()
```

### Data Integration and Visualization

```python  theme={null}
from crewai import Agent, Task, Crew

data_visualizer = Agent(
    role="Data Visualizer",
    goal="Create presentations with data imported from spreadsheets",
    backstory="An AI assistant that specializes in data visualization and presentation integration.",
    apps=['google_slides']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1746-run-the-task.md)

**Next:** [Task to create data-driven presentations →](./1748-task-to-create-data-driven-presentations.md)
