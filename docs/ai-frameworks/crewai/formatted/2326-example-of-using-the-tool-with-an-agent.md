---
title: "Crewai: Example of using the tool with an agent"
description: "Example of using the tool with an agent section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Example of using the tool with an agent

browser_agent = Agent(
    role="Web Browser Agent",
    goal="Search for and summarize information from the web",
    backstory="An expert at finding and extracting information from websites.",
    tools=[multion_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage](./2325-usage.md)

**Next:** [Create a task for the agent →](./2327-create-a-task-for-the-agent.md)
