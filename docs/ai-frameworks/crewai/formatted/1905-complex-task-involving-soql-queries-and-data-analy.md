---
title: "Crewai: Complex task involving SOQL queries and data analysis"
description: "Complex task involving SOQL queries and data analysis section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving SOQL queries and data analysis

analysis_task = Task(
    description="""
    1. Execute a SOQL query to find all opportunities closing this quarter
    2. Search for contacts at companies with opportunities over $100K
    3. Create a summary report of the sales pipeline status
    4. Update high-value opportunities with next steps
    """,
    agent=data_analyst,
    expected_output="Comprehensive sales pipeline analysis with actionable insights"
)

crew = Crew(
    agents=[data_analyst],
    tasks=[analysis_task]
)

crew.kickoff()
```

This comprehensive documentation covers all the Salesforce tools organized by functionality, making it easy for users to find the specific operations they need for their CRM automation tasks.

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with Salesforce integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage customer accounts](./1904-task-to-manage-customer-accounts.md)

**Next:** [Shopify Integration →](./1906-shopify-integration.md)
