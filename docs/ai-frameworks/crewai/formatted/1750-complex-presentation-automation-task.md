---
title: "Crewai: Complex presentation automation task"
description: "Complex presentation automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex presentation automation task

automation_task = Task(
    description="""
    1. Create multiple presentations for different departments
    2. Import relevant data from various spreadsheets
    3. Update existing presentations with new content
    4. Generate thumbnails for all presentations
    5. Link supporting documents from Drive
    6. Create a master index presentation with links to all others
    """,
    agent=presentation_automator,
    expected_output="Automated presentation workflow completed with multiple presentations and organized structure"
)

crew = Crew(
    agents=[presentation_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Template and Content Creation

```python  theme={null}
from crewai import Agent, Task, Crew

template_creator = Agent(
    role="Template Creator",
    goal="Create presentation templates and standardized content",
    backstory="An AI assistant that creates consistent presentation templates and content standards.",
    apps=['google_slides']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage presentation library](./1749-task-to-manage-presentation-library.md)

**Next:** [Task to create templates →](./1751-task-to-create-templates.md)
