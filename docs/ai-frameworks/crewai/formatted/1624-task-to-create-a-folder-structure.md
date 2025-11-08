---
title: "Crewai: Task to create a folder structure"
description: "Task to create a folder structure section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a folder structure

create_structure_task = Task(
    description="Create a folder called 'Project Files' in the root directory and upload a document from URL",
    agent=box_agent,
    expected_output="Folder created and file uploaded successfully"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Box capabilities](./1623-create-an-agent-with-box-capabilities.md)

**Next:** [Run the task →](./1625-run-the-task.md)
