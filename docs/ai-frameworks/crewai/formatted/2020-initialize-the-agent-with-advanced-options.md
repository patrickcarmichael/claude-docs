---
title: "Crewai: Initialize the agent with advanced options"
description: "Initialize the agent with advanced options section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

# Initialize the agent with advanced options

agent = Agent(
  role='Research Analyst',
  goal='Provide up-to-date market analysis',
  backstory='An expert analyst with a keen eye for market trends.',
  tools=[search_tool],
  memory=True, # Enable memory
  verbose=True,
  max_rpm=None, # No limit on requests per minute
  max_iter=25, # Default value for maximum iterations
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Initialize a search tool](./2019-initialize-a-search-tool.md)

**Next:** [Delegation and Autonomy →](./2021-delegation-and-autonomy.md)
