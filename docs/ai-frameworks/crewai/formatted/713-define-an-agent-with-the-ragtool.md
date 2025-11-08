---
title: "Crewai: Define an agent with the RagTool"
description: "Define an agent with the RagTool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent with the RagTool

@agent
def knowledge_expert(self) -> Agent:
    return Agent(
        config=self.agents_config["knowledge_expert"],
        allow_delegation=False,
        tools=[rag_tool]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool and add content](./712-initialize-the-tool-and-add-content.md)

**Next:** [Advanced Configuration →](./714-advanced-configuration.md)
