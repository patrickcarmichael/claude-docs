---
title: "Langgraph: How to build a multi-agent network (functional API)"
description: "How to build a multi-agent network (functional API) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to build a multi-agent network (functional API)


!!! info "Prerequisites" 
    This guide assumes familiarity with the following:

    - <a href="../../concepts/multi_agent">Multi-agent systems</a>
    - <a href="../../concepts/functional_api">Functional API</a>
    - <a href="../../concepts/low_level/#command">Command</a>
    - <a href="../../concepts/low_level/">LangGraph Glossary</a>

In this how-to guide we will demonstrate how to implement a <a href="../../concepts/multi_agent#network">multi-agent network</a> architecture where each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. We will be using <a href="../../concepts/functional_api">functional API</a> — individual agents will be defined as tasks and the agent handoffs will be defined in the main [entrypoint()][langgraph.func.entrypoint]:

```python
from langgraph.func import entrypoint
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← NOTE: we're passing the store object here when creating a workflow via entrypoint()](./149-note-were-passing-the-store-object-here-when-creat.md)

**Next:** [Define a tool to signal intent to hand off to a different agent →](./151-define-a-tool-to-signal-intent-to-hand-off-to-a-di.md)
