---
title: "Crewai: Task to list files and create a folder"
description: "Task to list files and create a folder section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to list files and create a folder

organize_files_task = Task(
    description="List all files in my OneDrive root directory and create a new folder called 'Project Documents'.",
    agent=onedrive_agent,
    expected_output="List of files displayed and new folder 'Project Documents' created."
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Microsoft OneDrive capabilities](./1815-create-an-agent-with-microsoft-onedrive-capabiliti.md)

**Next:** [Run the task →](./1817-run-the-task.md)
