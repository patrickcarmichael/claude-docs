---
title: "Crewai: Create agent with HubSpot contact management capabilities"
description: "Create agent with HubSpot contact management capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with HubSpot contact management capabilities

crm_manager = Agent(
    role="CRM Manager",
    goal="Manage and organize HubSpot contacts efficiently.",
    backstory="An experienced CRM manager who maintains an organized contact database.",
    apps=['hubspot']  # All HubSpot actions including contact management
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a contact](./1763-task-to-create-a-contact.md)

**Next:** [Task to manage contacts →](./1765-task-to-manage-contacts.md)
