---
title: "Crewai: Complex task involving multiple operations"
description: "Complex task involving multiple operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple operations

analytics_task = Task(
    description="""
    1. Retrieve recent customer data and order history
    2. Identify abandoned carts from the last 7 days
    3. Analyze product performance and inventory levels
    4. Generate recommendations for customer retention
    """,
    agent=analytics_agent,
    expected_output="Comprehensive e-commerce analytics report with actionable insights"
)

crew = Crew(
    agents=[analytics_agent],
    tasks=[analytics_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Shopify integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage product catalog](./1916-task-to-manage-product-catalog.md)

**Next:** [Slack Integration →](./1918-slack-integration.md)
