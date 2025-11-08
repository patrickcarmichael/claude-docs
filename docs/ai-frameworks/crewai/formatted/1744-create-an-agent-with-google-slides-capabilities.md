---
title: "Crewai: Create an agent with Google Slides capabilities"
description: "Create an agent with Google Slides capabilities section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with Google Slides capabilities

slides_agent = Agent(
    role="Presentation Manager",
    goal="Create and manage presentations efficiently",
    backstory="An AI assistant specialized in presentation creation and content management.",
    apps=['google_slides']  # All Google Slides actions will be available
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./1743-usage-examples.md)

**Next:** [Task to create a presentation →](./1745-task-to-create-a-presentation.md)
