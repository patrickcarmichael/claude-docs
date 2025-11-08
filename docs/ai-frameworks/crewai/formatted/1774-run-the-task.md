---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[jira_agent],
    tasks=[create_bug_task]
)

crew.kickoff()
```

### Filtering Specific Jira Tools

```python  theme={null}

issue_coordinator = Agent(
    role="Issue Coordinator",
    goal="Create and manage Jira issues efficiently",
    backstory="An AI assistant that focuses on issue creation and management.",
    apps=['jira']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a bug report](./1773-task-to-create-a-bug-report.md)

**Next:** [Task to manage issue workflow →](./1775-task-to-manage-issue-workflow.md)
