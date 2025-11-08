---
title: "Crewai: Task to format document"
description: "Task to format document section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Task to format document

format_doc_task = Task(
    description="In document 'your_document_id', insert a page break at position 100, create a named range called 'Introduction' for characters 1-50, and apply batch formatting updates.",
    agent=document_formatter,
    expected_output="Document formatted with page break, named range, and styling applied."
)

crew = Crew(
    agents=[document_formatter],
    tasks=[format_doc_task]
)

crew.kickoff()
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent for advanced document operations](./1707-create-an-agent-for-advanced-document-operations.md)

**Next:** [Troubleshooting →](./1709-troubleshooting.md)
