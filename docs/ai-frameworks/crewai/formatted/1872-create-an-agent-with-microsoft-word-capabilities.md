---
title: "Crewai: Create an agent with Microsoft Word capabilities"
description: "Create an agent with Microsoft Word capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Microsoft Word capabilities

word_agent = Agent(
    role="Document Manager",
    goal="Manage Word documents and text files efficiently",
    backstory="An AI assistant specialized in Microsoft Word document operations and content management.",
    apps=['microsoft_word']  # All Word actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1871-usage-examples.md)

**Next:** [Task to create a new text document →](./1873-task-to-create-a-new-text-document.md)
