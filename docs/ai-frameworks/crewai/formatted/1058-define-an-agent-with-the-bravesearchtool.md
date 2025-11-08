---
title: "Crewai: Define an agent with the BraveSearchTool"
description: "Define an agent with the BraveSearchTool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent with the BraveSearchTool

@agent
def researcher(self) -> Agent:
    return Agent(
        config=self.agents_config["researcher"],
        allow_delegation=False,
        tools=[brave_search_tool]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool](./1057-initialize-the-tool.md)

**Next:** [Conclusion →](./1059-conclusion.md)
