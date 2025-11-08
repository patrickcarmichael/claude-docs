---
title: "Crewai: Task to manage event updates"
description: "Task to manage event updates section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage event updates

event_management = Task(
    description="""
    1. List all events for this week
    2. Update any events that need location changes to include video conference links
    3. Check availability for upcoming meetings
    """,
    agent=event_manager,
    expected_output="Weekly events updated with proper locations and availability checked"
)

crew = Crew(
    agents=[event_manager],
    tasks=[event_management]
)

crew.kickoff()
```

### Availability and Calendar Management

```python  theme={null}
from crewai import Agent, Task, Crew

availability_coordinator = Agent(
    role="Availability Coordinator",
    goal="Coordinate availability and manage calendars for scheduling",
    backstory="An AI assistant that specializes in availability management and calendar coordination.",
    apps=['google_calendar']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to schedule a meeting with availability check](./1677-task-to-schedule-a-meeting-with-availability-check.md)

**Next:** [Task to coordinate availability →](./1679-task-to-coordinate-availability.md)
