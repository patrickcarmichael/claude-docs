---
title: "Crewai: Create an agent focused on messaging"
description: "Create an agent focused on messaging section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent focused on messaging

messenger = Agent(
    role="Teams Messenger",
    goal="Send and retrieve messages in Teams channels",
    backstory="An AI assistant skilled in team communication and message management.",
    apps=['microsoft_teams/send_message', 'microsoft_teams/get_messages']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1860-run-the-task.md)

**Next:** [Task to send a message and retrieve recent messages →](./1862-task-to-send-a-message-and-retrieve-recent-message.md)
