---
title: "Crewai: Create an agent with HubSpot capabilities"
description: "Create an agent with HubSpot capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with HubSpot capabilities

hubspot_agent = Agent(
    role="CRM Manager",
    goal="Manage company and contact records in HubSpot",
    backstory="An AI assistant specialized in CRM management.",
    apps=['hubspot']  # All HubSpot actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1758-usage-examples.md)

**Next:** [Task to create a new company →](./1760-task-to-create-a-new-company.md)
