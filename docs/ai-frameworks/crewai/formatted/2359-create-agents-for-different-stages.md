---
title: "Crewai: Create agents for different stages"
description: "Create agents for different stages section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agents for different stages

researcher = Agent(
    role='AWS Service Researcher',
    goal='Gather information about AWS services',
    backstory='I am specialized in finding detailed AWS service information.',
    tools=[initial_tool]
)

analyst = Agent(
    role='Service Compatibility Analyst',
    goal='Analyze service compatibility and requirements',
    backstory='I analyze AWS services for compatibility and integration possibilities.',
    tools=[followup_tool]
)

summarizer = Agent(
    role='Technical Documentation Writer',
    goal='Create clear technical summaries',
    backstory='I specialize in creating clear, concise technical documentation.',
    tools=[final_tool]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize tools with session management](./2358-initialize-tools-with-session-management.md)

**Next:** [Create tasks →](./2360-create-tasks.md)
