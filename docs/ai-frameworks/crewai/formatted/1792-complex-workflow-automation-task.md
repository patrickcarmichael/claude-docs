---
title: "Crewai: Complex workflow automation task"
description: "Complex workflow automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex workflow automation task

automation_task = Task(
    description="""
    1. Search for issues that have been in progress for more than 7 days
    2. Update their priorities based on due dates and project importance
    3. Create weekly sprint planning issues for each team
    4. Archive completed issues from the previous cycle
    5. Generate project status reports as new issues
    """,
    agent=workflow_automator,
    expected_output="Development workflow automated with updated priorities, sprint planning, and status reports"
)

crew = Crew(
    agents=[workflow_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create issue hierarchy](./1791-task-to-create-issue-hierarchy.md)

**Next:** [Troubleshooting →](./1793-troubleshooting.md)
