---
title: "Crewai: Complex task involving multiple GitHub operations"
description: "Complex task involving multiple GitHub operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Complex task involving multiple GitHub operations

coordination_task = Task(
    description="""
    1. Search for all open issues assigned to the current milestone
    2. Identify overdue issues and update their priority labels
    3. Create a weekly progress report issue
    4. Lock resolved issues that have been inactive for 30 days
    """,
    agent=project_coordinator,
    expected_output="Project coordination completed with progress report and issue management"
)

crew = Crew(
    agents=[project_coordinator],
    tasks=[coordination_task]
)

crew.kickoff()
```

### Getting Help

<Card title="Need Help?" icon="headset" href="mailto:support@crewai.com">
  Contact our support team for assistance with GitHub integration setup or troubleshooting.
</Card>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new release](./1651-task-to-create-a-new-release.md)

**Next:** [Gmail Integration →](./1653-gmail-integration.md)
