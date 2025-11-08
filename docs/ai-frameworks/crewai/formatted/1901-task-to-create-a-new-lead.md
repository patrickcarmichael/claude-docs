---
title: "Crewai: Task to create a new lead"
description: "Task to create a new lead section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new lead

create_lead_task = Task(
    description="Create a new lead for John Doe from Example Corp with email john.doe@example.com",
    agent=salesforce_agent,
    expected_output="Lead created successfully with lead ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Salesforce capabilities](./1900-create-an-agent-with-salesforce-capabilities.md)

**Next:** [Run the task →](./1902-run-the-task.md)
