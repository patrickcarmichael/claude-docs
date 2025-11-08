---
title: "Crewai: Task to create a new text document"
description: "Task to create a new text document section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to create a new text document

create_doc_task = Task(
    description="Create a new text document named 'meeting_notes.txt' with content 'Meeting Notes from January 2024: Key discussion points and action items.'",
    agent=word_agent,
    expected_output="New text document 'meeting_notes.txt' created successfully."
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with Microsoft Word capabilities](./1872-create-an-agent-with-microsoft-word-capabilities.md)

**Next:** [Run the task →](./1874-run-the-task.md)
