---
title: "Crewai: Create agent with specific HubSpot actions only"
description: "Create agent with specific HubSpot actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific HubSpot actions only

contact_creator = Agent(
    role="Contact Creator",
    goal="Create new contacts in HubSpot",
    backstory="An AI assistant that focuses on creating new contact entries in the CRM.",
    apps=['hubspot/create_contact']  # Only contact creation action
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1761-run-the-task.md)

**Next:** [Task to create a contact →](./1763-task-to-create-a-contact.md)
