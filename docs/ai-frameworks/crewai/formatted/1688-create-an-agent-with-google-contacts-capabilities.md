---
title: "Crewai: Create an agent with Google Contacts capabilities"
description: "Create an agent with Google Contacts capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Google Contacts capabilities

contacts_agent = Agent(
    role="Contact Manager",
    goal="Manage contacts and directory information efficiently",
    backstory="An AI assistant specialized in contact management and directory operations.",
    apps=['google_contacts']  # All Google Contacts actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1687-usage-examples.md)

**Next:** [Task to retrieve and organize contacts →](./1689-task-to-retrieve-and-organize-contacts.md)
