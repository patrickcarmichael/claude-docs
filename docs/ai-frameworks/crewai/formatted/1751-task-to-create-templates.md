---
title: "Crewai: Task to create templates"
description: "Task to create templates section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create templates

template_task = Task(
    description="""
    1. Create blank presentation templates for different use cases
    2. Add standard layouts and content placeholders
    3. Create sample presentations with best practices
    4. Generate thumbnails for template previews
    5. Upload template assets to Drive and link appropriately
    """,
    agent=template_creator,
    expected_output="Presentation templates created with standardized layouts and linked assets"
)

crew = Crew(
    agents=[template_creator],
    tasks=[template_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex presentation automation task](./1750-complex-presentation-automation-task.md)

**Next:** [Troubleshooting →](./1752-troubleshooting.md)
