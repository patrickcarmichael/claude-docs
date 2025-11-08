---
title: "Crewai: Setting Up the DALL-E Tool"
description: "Setting Up the DALL-E Tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Setting Up the DALL-E Tool


<Steps>
  <Step title="Import the DALL-E tool">
    ```python  theme={null}
    from crewai_tools import DallETool
    ```
  </Step>

  <Step title="Add the DALL-E tool to your agent configuration">
    ```python  theme={null}
    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config['researcher'],
            tools=[SerperDevTool(), DallETool()],  # Add DallETool to the list of tools
            allow_delegation=False,
            verbose=True
        )
    ```
  </Step>
</Steps>

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./2024-prerequisites.md)

**Next:** [Using the DALL-E Tool →](./2026-using-the-dall-e-tool.md)
