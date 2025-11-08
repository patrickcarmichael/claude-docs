---
title: "Crewai: Complex task involving multiple Asana operations"
description: "Complex task involving multiple Asana operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple Asana operations

coordination_task = Task(
    description="""
    1. Get all active projects in the workspace
    2. For each project, get the list of incomplete tasks
    3. Create a summary report task in the 'Management Reports' project
    4. Add comments to overdue tasks to request status updates
    """,
    agent=project_coordinator,
    expected_output="Summary report created and status update requests sent for overdue tasks"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create and assign a task](./1615-task-to-create-and-assign-a-task.md)

**Next:** [Box Integration →](./1617-box-integration.md)
