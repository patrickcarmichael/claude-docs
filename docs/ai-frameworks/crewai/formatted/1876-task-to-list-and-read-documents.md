---
title: "Crewai: Task to list and read documents"
description: "Task to list and read documents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to list and read documents

read_docs_task = Task(
    description="List all Word documents in my OneDrive, then get the content and properties of the first document found.",
    agent=document_reader,
    expected_output="List of documents with content and properties of the first document."
)

crew = Crew(
    agents=[document_reader],
    tasks=[read_docs_task]
)

crew.kickoff()
```

### Document Cleanup and Organization

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent focused on document operations](./1875-create-an-agent-focused-on-document-operations.md)

**Next:** [Create an agent for document management →](./1877-create-an-agent-for-document-management.md)
