---
title: "Crewai: Complex workflow automation task"
description: "Complex workflow automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex workflow automation task

automation_task = Task(
    description="""
    1. Monitor project lists across multiple sites
    2. Create status reports based on list data
    3. Upload reports to designated document libraries
    4. Update project tracking lists with completion status
    5. Archive completed project documents
    6. Send notifications for overdue items
    """,
    agent=workflow_automator,
    expected_output="Automated workflow completed with status reports generated and project tracking updated"
)

crew = Crew(
    agents=[workflow_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

### Data Integration and Reporting

```python  theme={null}
from crewai import Agent, Task, Crew

data_integrator = Agent(
    role="Data Integrator",
    goal="Integrate and analyze data across SharePoint sites and lists",
    backstory="An AI assistant that specializes in data integration and cross-site analysis.",
    apps=['microsoft_sharepoint']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task for site administration](./1848-task-for-site-administration.md)

**Next:** [Task for data integration →](./1850-task-for-data-integration.md)
