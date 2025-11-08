---
title: "Crewai: Task using schema-based operations"
description: "Task using schema-based operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task using schema-based operations

schema_task = Task(
    description="""
    1. Get all projects and their custom issue types
    2. For each custom issue type, describe the action schema
    3. Create issues using the dynamic schema for complex custom fields
    4. Update issues with custom field values based on business rules
    """,
    agent=schema_specialist,
    expected_output="Custom issues created and updated using dynamic schemas"
)

crew = Crew(
    agents=[schema_specialist],
    tasks=[schema_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to automate issue management](./1777-task-to-automate-issue-management.md)

**Next:** [Troubleshooting →](./1779-troubleshooting.md)
