---
title: "Crewai: Customizing Agents and Tools"
description: "Customizing Agents and Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Customizing Agents and Tools


Agents are customized by defining their attributes and tools during initialization. Tools are critical for an agent's functionality, enabling them to perform specialized tasks.
The `tools` attribute should be an array of tools the agent can utilize, and it's initialized as an empty list by default. Tools can be added or modified post-agent initialization to adapt to new requirements.

```shell  theme={null}
pip install 'crewai[tools]'
```

### Example: Assigning Tools to an Agent

```python Code theme={null}
import os
from crewai import Agent
from crewai_tools import SerperDevTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Performance and Debugging Settings](./2016-performance-and-debugging-settings.md)

**Next:** [Set API keys for tool initialization →](./2018-set-api-keys-for-tool-initialization.md)
