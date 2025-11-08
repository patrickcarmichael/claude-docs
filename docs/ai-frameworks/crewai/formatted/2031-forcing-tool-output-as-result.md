---
title: "Crewai: Forcing Tool Output as Result"
description: "Forcing Tool Output as Result section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Forcing Tool Output as Result


To force the tool output as the result of an agent's task, you need to set the `result_as_answer` parameter to `True` when adding a tool to the agent.
This parameter ensures that the tool output is captured and returned as the task result, without any modifications by the agent.

Here's an example of how to force the tool output as the result of an agent's task:

```python Code theme={null}
from crewai.agent import Agent
from my_tool import MyCustomTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Introduction](./2030-introduction.md)

**Next:** [Create a coding agent with the custom tool →](./2032-create-a-coding-agent-with-the-custom-tool.md)
