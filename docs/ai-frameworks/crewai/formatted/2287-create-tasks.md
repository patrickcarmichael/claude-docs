---
title: "Crewai: Create tasks"
description: "Create tasks section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create tasks

research_task = Task(
    description='Research AI market trends for 2024',
    agent=researcher,
    expected_output='Comprehensive research summary'
)

writing_task = Task(
    description='Create a market research report',
    agent=writer,
    expected_output='Well-structured report with insights',
    context=[research_task]
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create agents](./2286-create-agents.md)

**Next:** [Create and execute crew →](./2288-create-and-execute-crew.md)
