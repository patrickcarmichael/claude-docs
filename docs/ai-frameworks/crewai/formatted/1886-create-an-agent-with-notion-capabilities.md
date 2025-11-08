---
title: "Crewai: Create an agent with Notion capabilities"
description: "Create an agent with Notion capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Notion capabilities

notion_agent = Agent(
    role="Workspace Manager",
    goal="Manage workspace users and facilitate collaboration through comments",
    backstory="An AI assistant specialized in user management and team collaboration.",
    apps=['notion']  # All Notion actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1885-usage-examples.md)

**Next:** [Task to list workspace users →](./1887-task-to-list-workspace-users.md)
