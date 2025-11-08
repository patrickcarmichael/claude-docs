---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

coding_agent = Agent(
    role="Coding Agent",
    goal="Generate high quality code and verify that the output is code",
    backstory="An experienced coder who can generate high quality python code.",
    tools=[patronus_eval_tool],
    verbose=True,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./2242-initialize-the-tool.md)

**Next:** [Example task to generate and evaluate code →](./2244-example-task-to-generate-and-evaluate-code.md)
