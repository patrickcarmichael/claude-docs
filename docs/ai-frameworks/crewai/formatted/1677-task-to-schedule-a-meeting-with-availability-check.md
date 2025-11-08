---
title: "Crewai: Task to schedule a meeting with availability check"
description: "Task to schedule a meeting with availability check section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to schedule a meeting with availability check

schedule_meeting = Task(
    description="Check availability for next week and schedule a project review meeting with stakeholders",
    agent=meeting_coordinator,
    expected_output="Meeting scheduled after checking availability of all participants"
)

crew = Crew(
    agents=[meeting_coordinator],
    tasks=[schedule_meeting]
)

crew.kickoff()
```

### Event Management and Updates

```python  theme={null}
from crewai import Agent, Task, Crew

event_manager = Agent(
    role="Event Manager",
    goal="Manage and update calendar events efficiently",
    backstory="An experienced event manager who handles event logistics and updates.",
    apps=['google_calendar']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1676-run-the-task.md)

**Next:** [Task to manage event updates →](./1678-task-to-manage-event-updates.md)
