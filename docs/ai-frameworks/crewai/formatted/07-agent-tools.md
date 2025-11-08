---
title: "Crewai: Agent Tools"
description: "Agent Tools section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Agent Tools


Agents can be equipped with various tools to enhance their capabilities. CrewAI supports tools from:

* [CrewAI Toolkit](https://github.com/joaomdmoura/crewai-tools)
* [LangChain Tools](https://python.langchain.com/docs/integrations/tools)

Here's how to add tools to an agent:

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool, WikipediaTools

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create an agent with all available parameters](./06-create-an-agent-with-all-available-parameters.md)

**Next:** [Create tools →](./08-create-tools.md)
