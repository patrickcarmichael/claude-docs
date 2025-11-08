---
title: "Crewai: Create an agent for meeting management"
description: "Create an agent for meeting management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent for meeting management

meeting_scheduler = Agent(
    role="Meeting Scheduler",
    goal="Create and manage Teams meetings",
    backstory="An AI assistant that handles meeting scheduling and organization.",
    apps=['microsoft_teams/create_meeting', 'microsoft_teams/search_online_meetings_by_join_url']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to send a message and retrieve recent messages](./1862-task-to-send-a-message-and-retrieve-recent-message.md)

**Next:** [Task to create a meeting →](./1864-task-to-create-a-meeting.md)
