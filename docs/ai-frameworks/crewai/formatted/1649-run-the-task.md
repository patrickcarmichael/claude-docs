---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[github_agent],
    tasks=[create_issue_task]
)

crew.kickoff()
```

### Filtering Specific GitHub Tools

```python  theme={null}

issue_manager = Agent(
    role="Issue Manager",
    goal="Create and manage GitHub issues efficiently",
    backstory="An AI assistant that focuses on issue tracking and management.",
    apps=['github/create_issue']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to create a new issue](./1648-task-to-create-a-new-issue.md)

**Next:** [Task to manage issue workflow →](./1650-task-to-manage-issue-workflow.md)
