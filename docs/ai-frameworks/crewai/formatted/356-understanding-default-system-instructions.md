---
title: "Crewai: Understanding Default System Instructions"
description: "Understanding Default System Instructions section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Understanding Default System Instructions


<Warning>
  **Production Transparency Issue**: CrewAI automatically injects default instructions into your prompts that you might not be aware of. This section explains what's happening under the hood and how to gain full control.
</Warning>

When you define an agent with `role`, `goal`, and `backstory`, CrewAI automatically adds additional system instructions that control formatting and behavior. Understanding these default injections is crucial for production systems where you need full prompt transparency.

### What CrewAI Automatically Injects

Based on your agent configuration, CrewAI adds different default instructions:

#### For Agents Without Tools

```text  theme={null}
"I MUST use these formats, my job depends on it!"
```

#### For Agents With Tools

```text  theme={null}
"IMPORTANT: Use the following format in your response:

Thought: you should always think about what to do
Action: the action to take, only one name of [tool_names]
Action Input: the input to the action, just a simple JSON object...
```

#### For Structured Outputs (JSON/Pydantic)

````text  theme={null}
"Ensure your final answer contains only the content in the following format: {output_format}
Ensure the final output does not include any code block markers like ```json or ```python."
````

### Viewing the Complete System Prompt

To see exactly what prompt is being sent to your LLM, you can inspect the generated prompt:

```python  theme={null}
from crewai import Agent, Crew, Task
from crewai.utilities.prompts import Prompts

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Understanding CrewAI's Prompt System](./355-understanding-crewais-prompt-system.md)

**Next:** [Create your agent →](./357-create-your-agent.md)
