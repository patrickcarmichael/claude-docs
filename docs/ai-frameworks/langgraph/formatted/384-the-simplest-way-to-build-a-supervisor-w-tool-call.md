---
title: "Langgraph: the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph"
description: "the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# the simplest way to build a supervisor w/ tool-calling is to use prebuilt ReAct agent graph

# that consists of a tool-calling LLM node (i.e. supervisor) and a tool-executing node
supervisor = create_react_agent(model, tools)
```

### Hierarchical

As you add more agents to your system, it might become too hard for the supervisor to manage all of them. The supervisor might start making poor decisions about which agent to call next, or the context might become too complex for a single supervisor to keep track of. In other words, you end up with the same problems that motivated the multi-agent architecture in the first place.

To address this, you can design your system _hierarchically_. For example, you can create separate, specialized teams of agents managed by individual supervisors, and a top-level supervisor to manage the teams.

```python
from typing import Literal
from langchain_openai import ChatOpenAI
from langgraph.graph import StateGraph, MessagesState, START, END
from langgraph.types import Command
model = ChatOpenAI()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← this is the agent function that will be called as tool](./383-this-is-the-agent-function-that-will-be-called-as-.md)

**Next:** [define team 1 (same as the single supervisor example above) →](./385-define-team-1-same-as-the-single-supervisor-exampl.md)
