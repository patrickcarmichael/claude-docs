---
title: "Crewai: Create a CrewAI agent that uses the tool"
description: "Create a CrewAI agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a CrewAI agent that uses the tool

aws_expert = Agent(
    role='AWS Service Expert',
    goal='Help users understand AWS services and quotas',
    backstory='I am an expert in AWS services and can provide detailed information about them.',
    tools=[agent_tool],
    verbose=True
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./2350-initialize-the-tool.md)

**Next:** [Create a task for the agent →](./2352-create-a-task-for-the-agent.md)
