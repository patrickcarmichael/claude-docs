---
title: "Crewai: Create an agent with Google Docs capabilities"
description: "Create an agent with Google Docs capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Google Docs capabilities

docs_agent = Agent(
    role="Document Creator",
    goal="Create and manage Google Docs documents efficiently",
    backstory="An AI assistant specialized in Google Docs document creation and editing.",
    apps=['google_docs']  # All Google Docs actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1701-usage-examples.md)

**Next:** [Task to create a new document →](./1703-task-to-create-a-new-document.md)
