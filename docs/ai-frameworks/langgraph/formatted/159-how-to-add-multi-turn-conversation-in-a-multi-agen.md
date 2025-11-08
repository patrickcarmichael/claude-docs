---
title: "Langgraph: How to add multi-turn conversation in a multi-agent application (functional API)"
description: "How to add multi-turn conversation in a multi-agent application (functional API) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to add multi-turn conversation in a multi-agent application (functional API)


!!! info "Prerequisites"
    This guide assumes familiarity with the following:

    - <a href="../../concepts/multi_agent">Multi-agent systems</a>
    - <a href="../../concepts/human_in_the_loop">Human-in-the-loop</a>
    - <a href="../../concepts/functional_api">Functional API</a>
    - <a href="../../concepts/low_level/#command">Command</a>
    - <a href="../../concepts/low_level/">LangGraph Glossary</a>

In this how-to guide, we’ll build an application that allows an end-user to engage in a *multi-turn conversation* with one or more agents. We'll create a node that uses an <a href="../../reference/types/#langgraph.types.interrupt">`interrupt`</a> to collect user input and routes back to the **active** agent.

The agents will be implemented as tasks in a workflow that executes agent steps and determines the next action:

1. **Wait for user input** to continue the conversation, or
2. **Route to another agent** (or back to itself, such as in a loop) via a <a href="../../concepts/multi_agent/#handoffs">**handoff**</a>.

```python
from langgraph.func import entrypoint, task
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langgraph.types import interrupt

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define hotel advisor ReAct agent](./158-define-hotel-advisor-react-agent.md)

**Next:** [Define a tool to signal intent to hand off to a different agent →](./160-define-a-tool-to-signal-intent-to-hand-off-to-a-di.md)
