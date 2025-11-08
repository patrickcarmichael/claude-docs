---
title: "Crewai: Create an agent with Microsoft Outlook capabilities"
description: "Create an agent with Microsoft Outlook capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Microsoft Outlook capabilities

outlook_agent = Agent(
    role="Email Assistant",
    goal="Manage emails, calendar events, and contacts efficiently",
    backstory="An AI assistant specialized in Microsoft Outlook operations and communication management.",
    apps=['microsoft_outlook']  # All Outlook actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1828-usage-examples.md)

**Next:** [Task to send an email →](./1830-task-to-send-an-email.md)
