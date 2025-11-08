---
title: "Crewai: Create an agent with Zendesk capabilities"
description: "Create an agent with Zendesk capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Zendesk capabilities

zendesk_agent = Agent(
    role="Support Manager",
    goal="Manage customer support tickets and provide excellent customer service",
    backstory="An AI assistant specialized in customer support operations and ticket management.",
    apps=['zendesk']  # All Zendesk actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1957-usage-examples.md)

**Next:** [Task to create a new support ticket →](./1959-task-to-create-a-new-support-ticket.md)
