---
title: "Crewai: Create an agent for calendar and contact management"
description: "Create an agent for calendar and contact management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent for calendar and contact management

scheduler = Agent(
    role="Calendar and Contact Manager",
    goal="Manage calendar events and maintain contact information",
    backstory="An AI assistant that handles scheduling and contact organization.",
    apps=['microsoft_outlook/create_calendar_event', 'microsoft_outlook/get_calendar_events', 'microsoft_outlook/create_contact']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to search and retrieve emails](./1833-task-to-search-and-retrieve-emails.md)

**Next:** [Task to create a meeting and add a contact →](./1835-task-to-create-a-meeting-and-add-a-contact.md)
