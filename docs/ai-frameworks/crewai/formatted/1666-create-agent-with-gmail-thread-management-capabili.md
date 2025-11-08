---
title: "Crewai: Create agent with Gmail thread management capabilities"
description: "Create agent with Gmail thread management capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with Gmail thread management capabilities

thread_manager = Agent(
    role="Thread Manager",
    goal="Organize and manage email threads efficiently",
    backstory="An AI assistant that specializes in email thread organization and management.",
    apps=[
        'gmail/fetch_thread',
        'gmail/modify_thread',
        'gmail/trash_thread'
    ]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to analyze email patterns](./1665-task-to-analyze-email-patterns.md)

**Next:** [Task to organize email threads →](./1667-task-to-organize-email-threads.md)
