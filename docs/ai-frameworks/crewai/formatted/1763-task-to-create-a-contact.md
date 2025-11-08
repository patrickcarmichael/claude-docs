---
title: "Crewai: Task to create a contact"
description: "Task to create a contact section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a contact

create_contact = Task(
    description="Create a new contact for 'John Doe' with email 'john.doe@example.com'.",
    agent=contact_creator,
    expected_output="Contact created successfully in HubSpot."
)

crew = Crew(
    agents=[contact_creator],
    tasks=[create_contact]
)

crew.kickoff()
```

### Contact Management

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with specific HubSpot actions only](./1762-create-agent-with-specific-hubspot-actions-only.md)

**Next:** [Create agent with HubSpot contact management capabilities →](./1764-create-agent-with-hubspot-contact-management-capab.md)
