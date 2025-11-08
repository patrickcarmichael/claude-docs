---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[shopify_agent],
    tasks=[create_customer_task]
)

crew.kickoff()
```

### Filtering Specific Shopify Tools

```python  theme={null}

store_manager = Agent(
    role="Store Manager",
    goal="Manage customer orders and product catalog",
    backstory="An experienced store manager who handles customer relationships and inventory management.",
    apps=['shopify/create_customer']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new customer](./1913-task-to-create-a-new-customer.md)

**Next:** [Task to manage store operations →](./1915-task-to-manage-store-operations.md)
