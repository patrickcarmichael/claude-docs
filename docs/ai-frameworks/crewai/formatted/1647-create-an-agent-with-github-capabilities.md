---
title: "Crewai: Create an agent with Github capabilities"
description: "Create an agent with Github capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Github capabilities

github_agent = Agent(
    role="Repository Manager",
    goal="Manage GitHub repositories, issues, and releases efficiently",
    backstory="An AI assistant specialized in repository management and issue tracking.",
    apps=['github']  # All Github actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1646-usage-examples.md)

**Next:** [Task to create a new issue →](./1648-task-to-create-a-new-issue.md)
