---
title: "Crewai: Define an agent with the AIMindTool"
description: "Define an agent with the AIMindTool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent with the AIMindTool

@agent
def data_analyst(self) -> Agent:
    return Agent(
        config=self.agents_config["data_analyst"],
        allow_delegation=False,
        tools=[aimind_tool]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./639-initialize-the-tool.md)

**Next:** [Conclusion →](./641-conclusion.md)
