---
title: "Crewai: Create an agent with Box capabilities"
description: "Create an agent with Box capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Box capabilities

box_agent = Agent(
    role="Document Manager",
    goal="Manage files and folders in Box efficiently",
    backstory="An AI assistant specialized in document management and file organization.",
    apps=['box']  # All Box actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1622-usage-examples.md)

**Next:** [Task to create a folder structure →](./1624-task-to-create-a-folder-structure.md)
