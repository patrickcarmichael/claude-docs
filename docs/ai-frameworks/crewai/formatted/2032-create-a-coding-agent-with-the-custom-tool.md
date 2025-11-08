---
title: "Crewai: Create a coding agent with the custom tool"
description: "Create a coding agent with the custom tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Create a coding agent with the custom tool

coding_agent = Agent(
        role="Data Scientist",
        goal="Produce amazing reports on AI",
        backstory="You work with data and AI",
        tools=[MyCustomTool(result_as_answer=True)],
    )

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Forcing Tool Output as Result](./2031-forcing-tool-output-as-result.md)

**Next:** [Assuming the tool's execution and result population occurs within the system →](./2033-assuming-the-tools-execution-and-result-population.md)
