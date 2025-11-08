---
title: "Crewai: Define an agent that uses the tool"
description: "Define an agent that uses the tool section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Define an agent that uses the tool

@agent
def web_researcher(self) -> Agent:
    '''
    This agent uses the HyperbrowserLoadTool to scrape websites
    and extract information.
    '''
    return Agent(
        config=self.agents_config["web_researcher"],
        tools=[tool]
    )
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize the tool with your API key](./1264-initialize-the-tool-with-your-api-key.md)

**Next:** [Parameters →](./1266-parameters.md)
