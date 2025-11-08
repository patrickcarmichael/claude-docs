---
title: "Crewai: Task for data integration"
description: "Task for data integration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task for data integration

integration_task = Task(
    description="""
    1. Get data from multiple SharePoint lists across different sites
    2. Consolidate information into comprehensive reports
    3. Create new list items with aggregated data
    4. Upload analytical reports to executive document library
    5. Update dashboard lists with key metrics
    """,
    agent=data_integrator,
    expected_output="Data integrated across sites with comprehensive reports and updated dashboards"
)

crew = Crew(
    agents=[data_integrator],
    tasks=[integration_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Complex workflow automation task](./1849-complex-workflow-automation-task.md)

**Next:** [Troubleshooting →](./1851-troubleshooting.md)
