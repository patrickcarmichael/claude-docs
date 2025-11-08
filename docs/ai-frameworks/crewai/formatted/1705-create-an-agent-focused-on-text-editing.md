---
title: "Crewai: Create an agent focused on text editing"
description: "Create an agent focused on text editing section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent focused on text editing

text_editor = Agent(
    role="Document Editor",
    goal="Edit and update content in Google Docs documents",
    backstory="An AI assistant skilled in precise text editing and content management.",
    apps=['google_docs/insert_text', 'google_docs/replace_text', 'google_docs/delete_content_range']
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1704-run-the-task.md)

**Next:** [Task to edit document content →](./1706-task-to-edit-document-content.md)
