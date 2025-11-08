---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[stripe_agent],
    tasks=[create_customer_task]
)

crew.kickoff()
```

### Filtering Specific Stripe Tools

```python  theme={null}

billing_manager = Agent(
    role="Billing Manager",
    goal="Handle customer billing, subscriptions, and payment processing",
    backstory="An experienced billing manager who handles subscription lifecycle and payment operations.",
    apps=['stripe']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new customer](./1942-task-to-create-a-new-customer.md)

**Next:** [Task to manage billing operations →](./1944-task-to-manage-billing-operations.md)
