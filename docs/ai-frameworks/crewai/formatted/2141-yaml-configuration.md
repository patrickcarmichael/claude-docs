---
title: "Crewai: YAML Configuration"
description: "YAML Configuration section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## YAML Configuration


The agent configurations are typically stored in a YAML file. Here's an example of how the `agents.yaml` file might look for the researcher agent:

```yaml  theme={null}
researcher:
    role: >
        LinkedIn Profile Senior Data Researcher
    goal: >
        Uncover detailed LinkedIn profiles based on provided name {name} and domain {domain}
        Generate a Dall-E image based on domain {domain}
    backstory: >
        You're a seasoned researcher with a knack for uncovering the most relevant LinkedIn profiles.
        Known for your ability to navigate LinkedIn efficiently, you excel at gathering and presenting
        professional information clearly and concisely.
    allow_delegation: False
    verbose: True
    llm: groq_llm
    tools:
        - myLinkedInProfileTool
        - mySerperDevTool
        - myDallETool
```

This YAML configuration corresponds to the researcher agent defined in the `LinkedinProfileCrew` class. The configuration specifies the agent's role, goal, backstory, and other properties such as the LLM and tools it uses.

Note how the `llm` and `tools` in the YAML file correspond to the methods decorated with `@llm` and `@tool` in the Python class.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Usage Examples](./2140-usage-examples.md)

**Next:** [Best Practices →](./2142-best-practices.md)
