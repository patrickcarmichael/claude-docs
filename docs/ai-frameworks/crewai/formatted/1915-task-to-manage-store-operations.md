---
title: "Crewai: Task to manage store operations"
description: "Task to manage store operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage store operations

store_task = Task(
    description="Create a new customer and process their order for 2 Premium Coffee Mugs",
    agent=store_manager,
    expected_output="Customer created and order processed successfully"
)

crew = Crew(
    agents=[store_manager],
    tasks=[store_task]
)

crew.kickoff()
```

### Product Management with GraphQL

```python  theme={null}
from crewai import Agent, Task, Crew

product_manager = Agent(
    role="Product Manager",
    goal="Manage product catalog and inventory with advanced GraphQL capabilities",
    backstory="An AI assistant that specializes in product management and catalog optimization.",
    apps=['shopify']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1914-run-the-task.md)

**Next:** [Task to manage product catalog →](./1916-task-to-manage-product-catalog.md)
