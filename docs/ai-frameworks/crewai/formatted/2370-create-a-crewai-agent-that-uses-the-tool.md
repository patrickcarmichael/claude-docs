---
title: "Crewai: Create a CrewAI agent that uses the tool"
description: "Create a CrewAI agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a CrewAI agent that uses the tool

automation_coordinator = Agent(
    role='Automation Coordinator',
    goal='Coordinate and execute automated crew tasks',
    backstory='I am an expert at leveraging automation tools to execute complex workflows.',
    tools=[automation_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./2369-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./2371-create-a-task-for-the-agent.md)
