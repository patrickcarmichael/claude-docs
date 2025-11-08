---
title: "Crewai: Create an agent for document management"
description: "Create an agent for document management section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent for document management

document_organizer = Agent(
    role="Document Organizer",
    goal="Organize and clean up document collections",
    backstory="An AI assistant that helps maintain organized document libraries.",
    apps=['microsoft_word/get_documents', 'microsoft_word/get_document_properties', 'microsoft_word/delete_document']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to list and read documents](./1876-task-to-list-and-read-documents.md)

**Next:** [Task to organize documents →](./1878-task-to-organize-documents.md)
