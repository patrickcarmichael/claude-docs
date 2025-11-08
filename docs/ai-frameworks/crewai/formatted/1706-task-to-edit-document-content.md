---
title: "Crewai: Task to edit document content"
description: "Task to edit document content section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to edit document content

edit_content_task = Task(
    description="In document 'your_document_id', insert the text 'Executive Summary: ' at the beginning, then replace all instances of 'TODO' with 'COMPLETED'.",
    agent=text_editor,
    expected_output="Document updated with new text inserted and TODO items replaced."
)

crew = Crew(
    agents=[text_editor],
    tasks=[edit_content_task]
)

crew.kickoff()
```

### Advanced Document Operations

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent focused on text editing](./1705-create-an-agent-focused-on-text-editing.md)

**Next:** [Create an agent for advanced document operations →](./1707-create-an-agent-for-advanced-document-operations.md)
