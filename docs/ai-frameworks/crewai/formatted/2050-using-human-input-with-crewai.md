---
title: "Crewai: Using human input with CrewAI"
description: "Using human input with CrewAI section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using human input with CrewAI


To integrate human input into agent execution, set the `human_input` flag in the task definition. When enabled, the agent prompts the user for input before delivering its final answer.
This input can provide extra context, clarify ambiguities, or validate the agent's output.

### Example:

```shell  theme={null}
pip install crewai
```

```python Code theme={null}
import os
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool

os.environ["SERPER_API_KEY"] = "Your Key"  # serper.dev API key
os.environ["OPENAI_API_KEY"] = "Your Key"

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Human input in agent execution](./2049-human-input-in-agent-execution.md)

**Next:** [Loading Tools →](./2051-loading-tools.md)
