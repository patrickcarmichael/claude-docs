---
title: "Crewai: Task to create a new company"
description: "Task to create a new company section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new company

create_company_task = Task(
    description="Create a new company in HubSpot with name 'Innovate Corp' and domain 'innovatecorp.com'.",
    agent=hubspot_agent,
    expected_output="Company created successfully with confirmation"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with HubSpot capabilities](./1759-create-an-agent-with-hubspot-capabilities.md)

**Next:** [Run the task →](./1761-run-the-task.md)
