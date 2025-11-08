---
title: "Crewai: Task to manage presentation library"
description: "Task to manage presentation library section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage presentation library

library_task = Task(
    description="""
    1. List all existing presentations
    2. Generate thumbnails for presentation previews
    3. Upload supporting files to Drive and link to presentations
    4. Organize presentations by topic and date
    """,
    agent=library_manager,
    expected_output="Presentation library organized with thumbnails and linked supporting files"
)

crew = Crew(
    agents=[library_manager],
    tasks=[library_task]
)

crew.kickoff()
```

### Automated Presentation Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

presentation_automator = Agent(
    role="Presentation Automator",
    goal="Automate presentation creation and management workflows",
    backstory="An AI assistant that automates complex presentation workflows and content generation.",
    apps=['google_slides']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create data-driven presentations](./1748-task-to-create-data-driven-presentations.md)

**Next:** [Complex presentation automation task →](./1750-complex-presentation-automation-task.md)
