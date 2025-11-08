---
title: "Crewai: Task to create a new release"
description: "Task to create a new release section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new release

release_task = Task(
    description="""
    Create a new release v2.1.0 for the project with:
    - Auto-generated release notes
    - Target the main branch
    - Include a description of new features and bug fixes
    """,
    agent=release_manager,
    expected_output="Release v2.1.0 created successfully with release notes"
)

crew = Crew(
    agents=[release_manager],
    tasks=[release_task]
)

crew.kickoff()
```

### Issue Tracking and Management

```python  theme={null}
from crewai import Agent, Task, Crew

project_coordinator = Agent(
    role="Project Coordinator",
    goal="Track and coordinate project issues and development progress",
    backstory="An AI assistant that helps coordinate development work and track project progress.",
    apps=['github']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage issue workflow](./1650-task-to-manage-issue-workflow.md)

**Next:** [Complex task involving multiple GitHub operations →](./1652-complex-task-involving-multiple-github-operations.md)
