---
title: "Crewai: Task to automate issue management"
description: "Task to automate issue management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to automate issue management

automation_task = Task(
    description="""
    1. Search for all unassigned issues using JQL
    2. Get available assignees for each project
    3. Automatically assign issues based on workload and expertise
    4. Update issue priorities based on age and type
    5. Create weekly sprint planning issues
    """,
    agent=automation_manager,
    expected_output="Issues automatically assigned and sprint planning issues created"
)

crew = Crew(
    agents=[automation_manager],
    tasks=[automation_task]
)

crew.kickoff()
```

### Advanced Schema-Based Operations

```python  theme={null}
from crewai import Agent, Task, Crew

schema_specialist = Agent(
    role="Schema Specialist",
    goal="Handle complex Jira operations using dynamic schemas",
    backstory="An AI assistant that can work with dynamic Jira schemas and custom issue types.",
    apps=['jira']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to analyze project status](./1776-task-to-analyze-project-status.md)

**Next:** [Task using schema-based operations →](./1778-task-using-schema-based-operations.md)
