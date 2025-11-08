---
title: "Crewai: Create agent with specific Slack actions only"
description: "Create agent with specific Slack actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Slack actions only

communication_manager = Agent(
    role="Communication Coordinator",
    goal="Manage team communications and ensure important messages reach the right people",
    backstory="An experienced communication coordinator who handles team messaging and notifications.",
    apps=[
        'slack/send_message',
        'slack/send_direct_message',
        'slack/search_messages'
    ]  # Using canonical action names from canonical_integrations.yml
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1927-run-the-task.md)

**Next:** [Task to coordinate team communication →](./1929-task-to-coordinate-team-communication.md)
