---
title: "Crewai: Create an agent with the tool"
description: "Create an agent with the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent with the tool

research_agent = Agent(
    role="Research Coordinator",
    goal="Coordinate and execute market research tasks",
    backstory="You are an expert at coordinating research tasks and leveraging automation tools.",
    tools=[market_research_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create tool with custom inputs](./2378-create-tool-with-custom-inputs.md)

**Next:** [Create and execute a task with custom parameters →](./2380-create-and-execute-a-task-with-custom-parameters.md)
