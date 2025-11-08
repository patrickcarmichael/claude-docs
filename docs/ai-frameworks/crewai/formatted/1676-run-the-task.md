---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[calendar_agent],
    tasks=[create_meeting_task]
)

crew.kickoff()
```

### Filtering Specific Calendar Tools

```python  theme={null}
meeting_coordinator = Agent(
    role="Meeting Coordinator",
    goal="Coordinate meetings and check availability",
    backstory="An AI assistant that focuses on meeting scheduling and availability management.",
    apps=['google_calendar/create_event', 'google_calendar/get_availability']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a meeting](./1675-task-to-create-a-meeting.md)

**Next:** [Task to schedule a meeting with availability check →](./1677-task-to-schedule-a-meeting-with-availability-check.md)
