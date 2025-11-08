---
title: "Crewai: Run the task"
description: "Run the task section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Run the task

crew = Crew(
    agents=[notion_agent],
    tasks=[user_management_task]
)

crew.kickoff()
```

### Filtering Specific Notion Tools

```python  theme={null}
comment_manager = Agent(
    role="Comment Manager",
    goal="Create and manage comments on Notion pages",
    backstory="An AI assistant that focuses on facilitating discussions through comments.",
    apps=['notion/create_comment']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to list workspace users](./1887-task-to-list-workspace-users.md)

**Next:** [Task to create comments on pages →](./1889-task-to-create-comments-on-pages.md)
