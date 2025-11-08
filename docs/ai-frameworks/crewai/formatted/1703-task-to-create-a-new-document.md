---
title: "Crewai: Task to create a new document"
description: "Task to create a new document section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new document

create_doc_task = Task(
    description="Create a new Google Document titled 'Project Status Report'",
    agent=docs_agent,
    expected_output="New Google Document 'Project Status Report' created successfully"
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Google Docs capabilities](./1702-create-an-agent-with-google-docs-capabilities.md)

**Next:** [Run the task →](./1704-run-the-task.md)
