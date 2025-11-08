---
title: "Crewai: Task to organize files"
description: "Task to organize files section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to organize files

organize_files_task = Task(
    description="List all files in the root directory and organize them into appropriate folders",
    agent=drive_agent,
    expected_output="Summary of files organized with folder structure"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Drive capabilities](./1716-create-an-agent-with-google-drive-capabilities.md)

**Next:** [Run the task →](./1718-run-the-task.md)
