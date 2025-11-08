---
title: "Crewai: Create agent with specific Box actions only"
description: "Create agent with specific Box actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Box actions only

file_organizer_agent = Agent(
    role="File Organizer",
    goal="Organize and manage file storage efficiently",
    backstory="An AI assistant that focuses on file organization and storage management.",
    apps=['box/create_folder', 'box/save_file', 'box/list_files']  # Specific Box actions
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1625-run-the-task.md)

**Next:** [Task to organize files →](./1627-task-to-organize-files.md)
