---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[linear_agent],
    tasks=[create_bug_task]
)

crew.kickoff()
```

### Filtering Specific Linear Tools

```python  theme={null}

issue_manager = Agent(
    role="Issue Manager",
    goal="Create and manage Linear issues efficiently",
    backstory="An AI assistant that focuses on issue creation and lifecycle management.",
    apps=['linear/create_issue']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a bug report](./1787-task-to-create-a-bug-report.md)

**Next:** [Task to manage issue workflow →](./1789-task-to-manage-issue-workflow.md)
