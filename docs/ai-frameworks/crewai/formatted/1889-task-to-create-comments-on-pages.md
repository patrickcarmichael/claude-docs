---
title: "Crewai: Task to create comments on pages"
description: "Task to create comments on pages section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create comments on pages

comment_task = Task(
    description="Create a summary comment on the project status page with key updates",
    agent=comment_manager,
    expected_output="Comment created successfully with project status updates"
)

crew = Crew(
    agents=[comment_manager],
    tasks=[comment_task]
)

crew.kickoff()
```

### User Information and Team Management

```python  theme={null}
from crewai import Agent, Task, Crew

team_coordinator = Agent(
    role="Team Coordinator",
    goal="Coordinate team activities and manage user information",
    backstory="An AI assistant that helps coordinate team activities and manages user information.",
    apps=['notion']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1888-run-the-task.md)

**Next:** [Task to coordinate team activities →](./1890-task-to-coordinate-team-activities.md)
