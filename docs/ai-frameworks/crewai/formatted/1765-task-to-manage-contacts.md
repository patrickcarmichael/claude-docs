---
title: "Crewai: Task to manage contacts"
description: "Task to manage contacts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage contacts

contact_task = Task(
    description="Create a new contact for 'Jane Smith' at 'Global Tech Inc.' with email 'jane.smith@globaltech.com'.",
    agent=crm_manager,
    expected_output="Contact database updated with the new contact."
)

crew = Crew(
    agents=[crm_manager],
    tasks=[contact_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with HubSpot integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agent with HubSpot contact management capabilities](./1764-create-agent-with-hubspot-contact-management-capab.md)

**Next:** [Jira Integration →](./1766-jira-integration.md)
