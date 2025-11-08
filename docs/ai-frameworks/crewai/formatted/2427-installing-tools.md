---
title: "Crewai: Installing Tools"
description: "Installing Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Installing Tools


To install a tool:

```bash  theme={null}
crewai tool install <tool-name>
```

This installs the tool and adds it to `pyproject.toml`.

You can use the tool by importing it and adding it to your agents:

```python  theme={null}
from your_tool.tool import YourTool

custom_tool = YourTool()

researcher = Agent(
    role='Market Research Analyst',
    goal='Provide up-to-date market analysis of the AI industry',
    backstory='An expert analyst with a keen eye for market trends.',
    tools=[custom_tool],
    verbose=True
)
```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prerequisites](./2426-prerequisites.md)

**Next:** [Adding other packages after installing a tool →](./2428-adding-other-packages-after-installing-a-tool.md)
