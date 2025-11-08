---
title: "Crewai: Task to coordinate project setup"
description: "Task to coordinate project setup section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to coordinate project setup

project_coordination = Task(
    description="""
    1. Search for engineering teams in Linear
    2. Create a new project for Q2 feature development
    3. Associate the project with relevant teams
    4. Create initial project milestones as issues
    """,
    agent=project_coordinator,
    expected_output="Q2 project created with teams assigned and initial milestones established"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[project_coordination]
)

crew.kickoff()
```

### Issue Hierarchy and Sub-task Management

```python  theme={null}
from crewai import Agent, Task, Crew

task_organizer = Agent(
    role="Task Organizer",
    goal="Organize complex issues into manageable sub-tasks",
    backstory="An AI assistant that breaks down complex development work into organized sub-tasks.",
    apps=['linear']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to manage issue workflow](./1789-task-to-manage-issue-workflow.md)

**Next:** [Task to create issue hierarchy →](./1791-task-to-create-issue-hierarchy.md)
