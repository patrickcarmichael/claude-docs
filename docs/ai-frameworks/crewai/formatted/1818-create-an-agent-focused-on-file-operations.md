---
title: "Crewai: Create an agent focused on file operations"
description: "Create an agent focused on file operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent focused on file operations

file_operator = Agent(
    role="File Operator",
    goal="Upload, download, and manage files with precision",
    backstory="An AI assistant skilled in file handling and content management.",
    apps=['microsoft_onedrive/upload_file', 'microsoft_onedrive/download_file', 'microsoft_onedrive/get_file_info']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1817-run-the-task.md)

**Next:** [Task to upload and manage a file →](./1819-task-to-upload-and-manage-a-file.md)
