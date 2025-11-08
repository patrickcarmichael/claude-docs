---
title: "Crewai: Complex task involving multiple Box operations"
description: "Complex task involving multiple Box operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple Box operations

management_task = Task(
    description="""
    1. List all files in the root folder
    2. Create monthly archive folders for the current year
    3. Move old files to appropriate archive folders
    4. Generate a summary report of the file organization
    """,
    agent=file_manager,
    expected_output="Files organized into archive structure with summary report"
)

crew = Crew(
    agents=[file_manager],
    tasks=[management_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to organize files](./1627-task-to-organize-files.md)

**Next:** [ClickUp Integration →](./1629-clickup-integration.md)
