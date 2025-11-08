---
title: "Crewai: Task to create a meeting"
description: "Task to create a meeting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a meeting

schedule_meeting_task = Task(
    description="Create a Teams meeting titled 'Weekly Team Sync' scheduled for tomorrow at 10:00 AM lasting for 1 hour (use proper ISO 8601 format with timezone).",
    agent=meeting_scheduler,
    expected_output="Teams meeting created successfully with meeting details."
)

crew = Crew(
    agents=[meeting_scheduler],
    tasks=[schedule_meeting_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent for meeting management](./1863-create-an-agent-for-meeting-management.md)

**Next:** [Troubleshooting →](./1865-troubleshooting.md)
