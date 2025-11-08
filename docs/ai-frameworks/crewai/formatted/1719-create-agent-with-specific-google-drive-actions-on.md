---
title: "Crewai: Create agent with specific Google Drive actions only"
description: "Create agent with specific Google Drive actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Google Drive actions only

file_manager_agent = Agent(
    role="Document Manager",
    goal="Upload and manage documents efficiently",
    backstory="An AI assistant that focuses on document upload and organization.",
    apps=[
        'google_drive/upload_file',
        'google_drive/create_folder',
        'google_drive/share_file'
    ]  # Specific Google Drive actions
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1718-run-the-task.md)

**Next:** [Task to upload and share documents →](./1720-task-to-upload-and-share-documents.md)
