---
title: "Crewai: Create agent with Slack messaging capabilities"
description: "Create agent with Slack messaging capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with Slack messaging capabilities

notification_agent = Agent(
    role="Notification Manager",
    goal="Create rich, interactive notifications and manage workspace communication",
    backstory="An AI assistant that specializes in creating engaging team notifications and updates.",
    apps=['slack/send_message']  # Specific action for sending messages
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to coordinate team communication](./1929-task-to-coordinate-team-communication.md)

**Next:** [Task to send rich notifications →](./1931-task-to-send-rich-notifications.md)
