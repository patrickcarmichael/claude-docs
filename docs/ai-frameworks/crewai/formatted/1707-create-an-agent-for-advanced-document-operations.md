---
title: "Crewai: Create an agent for advanced document operations"
description: "Create an agent for advanced document operations section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent for advanced document operations

document_formatter = Agent(
    role="Document Formatter",
    goal="Apply advanced formatting and structure to Google Docs",
    backstory="An AI assistant that handles complex document formatting and organization.",
    apps=['google_docs/batch_update', 'google_docs/insert_page_break', 'google_docs/create_named_range']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Task to edit document content](./1706-task-to-edit-document-content.md)

**Next:** [Task to format document →](./1708-task-to-format-document.md)
