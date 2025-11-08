---
title: "Crewai: Task to create a new customer"
description: "Task to create a new customer section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new customer

create_customer_task = Task(
    description="Create a new VIP customer Jane Smith with email jane.smith@example.com and phone +1-555-0123",
    agent=shopify_agent,
    expected_output="Customer created successfully with customer ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Shopify capabilities](./1912-create-an-agent-with-shopify-capabilities.md)

**Next:** [Run the task →](./1914-run-the-task.md)
