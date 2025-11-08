---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[salesforce_agent],
    tasks=[create_lead_task]
)

crew.kickoff()
```

### Filtering Specific Salesforce Tools

```python  theme={null}

sales_manager = Agent(
    role="Sales Manager",
    goal="Manage leads and opportunities in the sales pipeline",
    backstory="An experienced sales manager who handles lead qualification and opportunity management.",
    apps=['salesforce/create_record_lead']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new lead](./1901-task-to-create-a-new-lead.md)

**Next:** [Task to manage sales pipeline →](./1903-task-to-manage-sales-pipeline.md)
