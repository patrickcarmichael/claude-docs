---
title: "Crewai: Create agent with specific Zendesk actions only"
description: "Create agent with specific Zendesk actions only section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agent with specific Zendesk actions only

support_agent = Agent(
    role="Customer Support Agent",
    goal="Handle customer inquiries and resolve support issues efficiently",
    backstory="An experienced support agent who specializes in ticket resolution and customer communication.",
    apps=['zendesk/create_ticket']  # Specific Zendesk actions
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Run the task](./1960-run-the-task.md)

**Next:** [Task to manage support workflow →](./1962-task-to-manage-support-workflow.md)
