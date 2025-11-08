---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

@agent
def researcher(self) -> Agent:
    '''
    This agent uses the LinkupSearchTool to retrieve contextual information
    from the Linkup API.
    '''
    return Agent(
        config=self.agents_config["researcher"],
        tools=[linkup_tool]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with your API key](./1102-initialize-the-tool-with-your-api-key.md)

**Next:** [Parameters →](./1104-parameters.md)
