---
title: "Crewai: Create agents and tasks as normal"
description: "Create agents and tasks as normal section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create agents and tasks as normal

researcher = Agent(
    role="Research Specialist",
    goal="Find information on quantum computing",
    backstory="You are a quantum physics expert",
    verbose=True
)

research_task = Task(
    description="Research quantum computing applications",
    expected_output="A summary of practical applications",
    agent=researcher
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The Simplest Way to Customize Prompts](./365-the-simplest-way-to-customize-prompts.md)

**Next:** [Create a crew with your custom prompt file →](./367-create-a-crew-with-your-custom-prompt-file.md)
