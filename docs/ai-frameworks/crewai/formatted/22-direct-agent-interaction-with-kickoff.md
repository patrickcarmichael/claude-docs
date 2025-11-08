---
title: "Crewai: Direct Agent Interaction with `kickoff()`"
description: "Direct Agent Interaction with `kickoff()` section of Crewai documentation"
source: "https://docs.crewai.com/en/concepts/agents"
last_updated: "2025-11-08"
---

## Direct Agent Interaction with `kickoff()`


Agents can be used directly without going through a task or crew workflow using the `kickoff()` method. This provides a simpler way to interact with an agent when you don't need the full crew orchestration capabilities.

### How `kickoff()` Works

The `kickoff()` method allows you to send messages directly to an agent and get a response, similar to how you would interact with an LLM but with all the agent's capabilities (tools, reasoning, etc.).

```python Code theme={null}
from crewai import Agent
from crewai_tools import SerperDevTool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Disable auto-summarization and use RAG instead](./21-disable-auto-summarization-and-use-rag-instead.md)

**Next:** [Create an agent →](./23-create-an-agent.md)
