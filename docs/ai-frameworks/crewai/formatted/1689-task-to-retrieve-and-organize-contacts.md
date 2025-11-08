---
title: "Crewai: Task to retrieve and organize contacts"
description: "Task to retrieve and organize contacts section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to retrieve and organize contacts

contact_management_task = Task(
    description="Retrieve all contacts and organize them by company affiliation",
    agent=contacts_agent,
    expected_output="Contacts retrieved and organized by company with summary report"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Contacts capabilities](./1688-create-an-agent-with-google-contacts-capabilities.md)

**Next:** [Run the task →](./1690-run-the-task.md)
