---
title: "Crewai: Create an agent with Slack capabilities"
description: "Create an agent with Slack capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Slack capabilities

slack_agent = Agent(
    role="Team Communication Manager",
    goal="Facilitate team communication and coordinate collaboration efficiently",
    backstory="An AI assistant specialized in team communication and workspace coordination.",
    apps=['slack']  # All Slack actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1924-usage-examples.md)

**Next:** [Task to send project updates →](./1926-task-to-send-project-updates.md)
