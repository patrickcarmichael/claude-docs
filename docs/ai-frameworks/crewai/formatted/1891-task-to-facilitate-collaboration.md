---
title: "Crewai: Task to facilitate collaboration"
description: "Task to facilitate collaboration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to facilitate collaboration

collaboration_task = Task(
    description="""
    1. Identify active users in the workspace
    2. Create contextual comments on project pages to facilitate discussions
    3. Provide status updates and feedback through comments
    """,
    agent=collaboration_facilitator,
    expected_output="Collaboration facilitated with comments created and team members notified"
)

crew = Crew(
    agents=[collaboration_facilitator],
    tasks=[collaboration_task]
)

crew.kickoff()
```

### Automated Team Communication

```python  theme={null}
from crewai import Agent, Task, Crew

communication_automator = Agent(
    role="Communication Automator",
    goal="Automate team communication and user management workflows",
    backstory="An AI assistant that automates communication workflows and manages user interactions.",
    apps=['notion']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to coordinate team activities](./1890-task-to-coordinate-team-activities.md)

**Next:** [Complex communication automation task →](./1892-complex-communication-automation-task.md)
