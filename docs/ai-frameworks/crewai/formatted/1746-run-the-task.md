---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[slides_agent],
    tasks=[create_presentation_task]
)

crew.kickoff()
```

### Presentation Content Management

```python  theme={null}
from crewai import Agent, Task, Crew

content_manager = Agent(
    role="Content Manager",
    goal="Manage presentation content and updates",
    backstory="An AI assistant that focuses on content creation and presentation updates.",
    apps=[
        'google_slides/create_blank_presentation',
        'google_slides/batch_update_presentation',
        'google_slides/get_presentation'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a presentation](./1745-task-to-create-a-presentation.md)

**Next:** [Task to create and update presentations →](./1747-task-to-create-and-update-presentations.md)
