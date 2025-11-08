---
title: "Crewai: Complex communication automation task"
description: "Complex communication automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex communication automation task

automation_task = Task(
    description="""
    1. List all workspace users and identify team roles
    2. Get specific user information for project stakeholders
    3. Create automated status update comments on key project pages
    4. Facilitate team communication through targeted comments
    """,
    agent=communication_automator,
    expected_output="Automated communication workflow completed with user management and comments"
)

crew = Crew(
    agents=[communication_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to facilitate collaboration](./1891-task-to-facilitate-collaboration.md)

**Next:** [Troubleshooting →](./1893-troubleshooting.md)
