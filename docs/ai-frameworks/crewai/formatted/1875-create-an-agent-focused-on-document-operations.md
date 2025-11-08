---
title: "Crewai: Create an agent focused on document operations"
description: "Create an agent focused on document operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent focused on document operations

document_reader = Agent(
    role="Document Reader",
    goal="Retrieve and analyze document content and properties",
    backstory="An AI assistant skilled in reading and analyzing document content.",
    apps=['microsoft_word/get_documents', 'microsoft_word/get_document_content', 'microsoft_word/get_document_properties']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1874-run-the-task.md)

**Next:** [Task to list and read documents →](./1876-task-to-list-and-read-documents.md)
