---
title: "Crewai: Create an agent with Google Drive capabilities"
description: "Create an agent with Google Drive capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Google Drive capabilities

drive_agent = Agent(
    role="File Manager",
    goal="Manage files and folders in Google Drive efficiently",
    backstory="An AI assistant specialized in document and file management.",
    apps=['google_drive']  # All Google Drive actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1715-usage-examples.md)

**Next:** [Task to organize files →](./1717-task-to-organize-files.md)
