---
title: "Crewai: Task to coordinate team activities"
description: "Task to coordinate team activities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to coordinate team activities

coordination_task = Task(
    description="""
    1. List all users in the workspace
    2. Get detailed information for specific team members
    3. Create comments on relevant pages to notify team members about updates
    """,
    agent=team_coordinator,
    expected_output="Team coordination completed with user information gathered and notifications sent"
)

crew = Crew(
    agents=[team_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Collaboration and Communication

```python  theme={null}
from crewai import Agent, Task, Crew

collaboration_facilitator = Agent(
    role="Collaboration Facilitator",
    goal="Facilitate team collaboration through comments and user management",
    backstory="An AI assistant that specializes in team collaboration and communication.",
    apps=['notion']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create comments on pages](./1889-task-to-create-comments-on-pages.md)

**Next:** [Task to facilitate collaboration →](./1891-task-to-facilitate-collaboration.md)
