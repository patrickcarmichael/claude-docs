---
title: "Crewai: Task for site administration"
description: "Task for site administration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task for site administration

admin_task = Task(
    description="""
    1. Get information about all accessible SharePoint sites
    2. Analyze site structure and content organization
    3. Identify sites with low activity or outdated content
    4. Generate recommendations for site optimization
    """,
    agent=site_administrator,
    expected_output="Site analysis completed with optimization recommendations"
)

crew = Crew(
    agents=[site_administrator],
    tasks=[admin_task]
)

crew.kickoff()
```

### Automated Content Workflows

```python  theme={null}
from crewai import Agent, Task, Crew

workflow_automator = Agent(
    role="Workflow Automator",
    goal="Automate SharePoint content workflows and processes",
    backstory="An AI assistant that automates complex SharePoint workflows and content management processes.",
    apps=['microsoft_sharepoint']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage documents](./1847-task-to-manage-documents.md)

**Next:** [Complex workflow automation task →](./1849-complex-workflow-automation-task.md)
