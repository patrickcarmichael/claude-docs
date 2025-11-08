---
title: "Crewai: Complex scheduling automation task"
description: "Complex scheduling automation task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex scheduling automation task

automation_task = Task(
    description="""
    1. List all upcoming events for the next two weeks
    2. Identify any scheduling conflicts or back-to-back meetings
    3. Suggest optimal meeting times by checking availability
    4. Create buffer time between meetings where needed
    5. Update event descriptions with agenda items and meeting links
    """,
    agent=scheduling_automator,
    expected_output="Calendar optimized with resolved conflicts, buffer times, and updated meeting details"
)

crew = Crew(
    agents=[scheduling_automator],
    tasks=[automation_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to coordinate availability](./1679-task-to-coordinate-availability.md)

**Next:** [Troubleshooting →](./1681-troubleshooting.md)
