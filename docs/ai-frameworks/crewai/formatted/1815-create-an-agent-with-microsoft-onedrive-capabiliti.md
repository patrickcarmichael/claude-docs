---
title: "Crewai: Create an agent with Microsoft OneDrive capabilities"
description: "Create an agent with Microsoft OneDrive capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Microsoft OneDrive capabilities

onedrive_agent = Agent(
    role="File Manager",
    goal="Manage files and folders in OneDrive efficiently",
    backstory="An AI assistant specialized in Microsoft OneDrive file operations and organization.",
    apps=['microsoft_onedrive']  # All OneDrive actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1814-usage-examples.md)

**Next:** [Task to list files and create a folder →](./1816-task-to-list-files-and-create-a-folder.md)
