---
title: "Crewai: Task to create a new customer"
description: "Task to create a new customer section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new customer

create_customer_task = Task(
    description="Create a new premium customer John Doe with email john.doe@example.com",
    agent=stripe_agent,
    expected_output="Customer created successfully with customer ID"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Stripe capabilities](./1941-create-an-agent-with-stripe-capabilities.md)

**Next:** [Run the task →](./1943-run-the-task.md)
