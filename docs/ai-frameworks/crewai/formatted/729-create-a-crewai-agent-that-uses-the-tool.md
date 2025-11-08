---
title: "Crewai: Create a CrewAI agent that uses the tool"
description: "Create a CrewAI agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a CrewAI agent that uses the tool

researcher = Agent(
    role='Knowledge Base Researcher',
    goal='Find information about company policies',
    backstory='I am a researcher specialized in retrieving and analyzing company documentation.',
    tools=[kb_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./728-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./730-create-a-task-for-the-agent.md)
