---
title: "Crewai: Create an agent for file organization and sharing"
description: "Create an agent for file organization and sharing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent for file organization and sharing

file_organizer = Agent(
    role="File Organizer",
    goal="Organize files and create sharing links for collaboration",
    backstory="An AI assistant that excels at organizing files and managing sharing permissions.",
    apps=['microsoft_onedrive/search_files', 'microsoft_onedrive/move_item', 'microsoft_onedrive/share_item', 'microsoft_onedrive/create_folder']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to upload and manage a file](./1819-task-to-upload-and-manage-a-file.md)

**Next:** [Task to organize and share files →](./1821-task-to-organize-and-share-files.md)
