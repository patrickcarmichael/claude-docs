---
title: "Crewai: Using Multimodal Agents"
description: "Using Multimodal Agents section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Using Multimodal Agents


CrewAI supports multimodal agents that can process both text and non-text content like images. This guide will show you how to enable and use multimodal capabilities in your agents.

### Enabling Multimodal Capabilities

To create a multimodal agent, simply set the `multimodal` parameter to `True` when initializing your agent:

```python  theme={null}
from crewai import Agent

agent = Agent(
    role="Image Analyst",
    goal="Analyze and extract insights from images",
    backstory="An expert in visual content interpretation with years of experience in image analysis",
    multimodal=True  # This enables multimodal capabilities
)
```

When you set `multimodal=True`, the agent is automatically configured with the necessary tools for handling non-text content, including the `AddImageTool`.

### Working with Images

The multimodal agent comes pre-configured with the `AddImageTool`, which allows it to process images. You don't need to manually add this tool - it's automatically included when you enable multimodal capabilities.

Here's a complete example showing how to use a multimodal agent to analyze an image:

```python  theme={null}
from crewai import Agent, Task, Crew

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Using Multimodal Agents](./2107-using-multimodal-agents.md)

**Next:** [Create a multimodal agent →](./2109-create-a-multimodal-agent.md)
