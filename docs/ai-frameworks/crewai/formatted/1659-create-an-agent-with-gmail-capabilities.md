---
title: "Crewai: Create an agent with Gmail capabilities"
description: "Create an agent with Gmail capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Gmail capabilities

gmail_agent = Agent(
    role="Email Manager",
    goal="Manage email communications and messages efficiently",
    backstory="An AI assistant specialized in email management and communication.",
    apps=['gmail']  # All Gmail actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1658-usage-examples.md)

**Next:** [Task to send a follow-up email →](./1660-task-to-send-a-follow-up-email.md)
