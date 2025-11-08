---
title: "Crewai: Create an agent with Google Calendar capabilities"
description: "Create an agent with Google Calendar capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Google Calendar capabilities

calendar_agent = Agent(
    role="Schedule Manager",
    goal="Manage calendar events and scheduling efficiently",
    backstory="An AI assistant specialized in calendar management and scheduling coordination.",
    apps=['google_calendar']  # All Google Calendar actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1673-usage-examples.md)

**Next:** [Task to create a meeting →](./1675-task-to-create-a-meeting.md)
