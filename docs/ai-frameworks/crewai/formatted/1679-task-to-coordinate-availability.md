---
title: "Crewai: Task to coordinate availability"
description: "Task to coordinate availability section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to coordinate availability

availability_task = Task(
    description="""
    1. Get the list of available calendars
    2. Check availability for all calendars next Friday afternoon
    3. Create a team meeting for the first available 2-hour slot
    4. Include Google Meet link and send invitations
    """,
    agent=availability_coordinator,
    expected_output="Team meeting scheduled based on availability with all team members invited"
)

crew = Crew(
    agents=[availability_coordinator],
    tasks=[availability_task]
)

crew.kickoff()
```

### Automated Scheduling Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

scheduling_automator = Agent(
    role="Scheduling Automator",
    goal="Automate scheduling workflows and calendar management",
    backstory="An AI assistant that automates complex scheduling scenarios and calendar workflows.",
    apps=['google_calendar']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage event updates](./1678-task-to-manage-event-updates.md)

**Next:** [Complex scheduling automation task →](./1680-complex-scheduling-automation-task.md)
