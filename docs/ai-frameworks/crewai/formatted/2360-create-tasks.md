---
title: "Crewai: Create tasks"
description: "Create tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create tasks

research_task = Task(
    description="Find all available AWS services in us-west-2 region.",
    agent=researcher
)

analysis_task = Task(
    description="Analyze which services support IPv6 and their implementation requirements.",
    agent=analyst
)

summary_task = Task(
    description="Create a summary of IPv6-compatible services and their key features.",
    agent=summarizer
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agents for different stages](./2359-create-agents-for-different-stages.md)

**Next:** [Create a crew with the agents and tasks →](./2361-create-a-crew-with-the-agents-and-tasks.md)
