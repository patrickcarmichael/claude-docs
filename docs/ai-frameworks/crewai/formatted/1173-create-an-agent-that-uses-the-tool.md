---
title: "Crewai: Create an agent that uses the tool"
description: "Create an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create an agent that uses the tool

researcher = Agent(
    role='Market Researcher',
    goal='Find information about the latest AI trends',
    backstory='An expert market researcher specializing in technology.',
    tools=[tavily_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1172-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./1174-create-a-task-for-the-agent.md)
