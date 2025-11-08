---
title: "Crewai: Create an agent with Jira capabilities"
description: "Create an agent with Jira capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Jira capabilities

jira_agent = Agent(
    role="Issue Manager",
    goal="Manage Jira issues and track project progress efficiently",
    backstory="An AI assistant specialized in issue tracking and project management.",
    apps=['jira']  # All Jira actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1771-usage-examples.md)

**Next:** [Task to create a bug report →](./1773-task-to-create-a-bug-report.md)
