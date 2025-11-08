---
title: "Crewai: Task to create a meeting"
description: "Task to create a meeting section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a meeting

create_meeting_task = Task(
    description="Create a team standup meeting for tomorrow at 9 AM with the development team",
    agent=calendar_agent,
    expected_output="Meeting created successfully with Google Meet link"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Calendar capabilities](./1674-create-an-agent-with-google-calendar-capabilities.md)

**Next:** [Run the task →](./1676-run-the-task.md)
