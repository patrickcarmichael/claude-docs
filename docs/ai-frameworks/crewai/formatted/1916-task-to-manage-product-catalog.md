---
title: "Crewai: Task to manage product catalog"
description: "Task to manage product catalog section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to manage product catalog

catalog_task = Task(
    description="""
    1. Create a new product "Premium Coffee Mug" from Coffee Co vendor
    2. Add high-quality product images and descriptions
    3. Search for similar products from the same vendor
    4. Update product tags and pricing strategy
    """,
    agent=product_manager,
    expected_output="Product created and catalog optimized successfully"
)

crew = Crew(
    agents=[product_manager],
    tasks=[catalog_task]
)

crew.kickoff()
```

### Order and Customer Analytics

```python  theme={null}
from crewai import Agent, Task, Crew

analytics_agent = Agent(
    role="E-commerce Analyst",
    goal="Analyze customer behavior and order patterns to optimize store performance",
    backstory="An analytical AI that excels at extracting insights from e-commerce data.",
    apps=['shopify']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage store operations](./1915-task-to-manage-store-operations.md)

**Next:** [Complex task involving multiple operations →](./1917-complex-task-involving-multiple-operations.md)
