---
title: "Langgraph: Add edges"
description: "Add edges section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Add edges

builder.add_edge(START, "step_1")
builder.add_edge("step_1", "step_2")
builder.add_edge("step_2", "step_3")
```

We can also use the built-in shorthand `.add_sequence`:

```python
builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
builder.add_edge(START, "step_1")
```

??? info "Why split application steps into a sequence with LangGraph?"
    LangGraph makes it easy to add an underlying persistence layer to your application.
    This allows state to be checkpointed in between the execution of nodes, so your LangGraph nodes govern:

- How state updates are [checkpointed](../concepts/persistence.md)
- How interruptions are resumed in [human-in-the-loop](../concepts/human_in_the_loop.md) workflows
- How we can "rewind" and branch-off executions using LangGraph's [time travel](../concepts/time-travel.md) features

They also determine how execution steps are [streamed](../concepts/streaming.md), and how your application is visualized
and debugged using [LangGraph Studio](../concepts/langgraph_studio.md).

Let's demonstrate an end-to-end example. We will create a sequence of three steps:

1. Populate a value in a key of the state
2. Update the same value
3. Populate a different value

Let's first define our [state](../concepts/low_level.md#state). This governs the [schema of the graph](../concepts/low_level.md#schema), and can also specify how to apply updates. See [this section](#process-state-updates-with-reducers) for more detail.

In our case, we will just keep track of two values:

```python
from typing_extensions import TypedDict

class State(TypedDict):
    value_1: str
    value_2: int
```

Our [nodes](../concepts/low_level.md#nodes) are just Python functions that read our graph's state and make updates to it. The first argument to this function will always be the state:

```python
def step_1(state: State):
    return {"value_1": "a"}

def step_2(state: State):
    current_value_1 = state["value_1"]
    return {"value_1": f"{current_value_1} b"}

def step_3(state: State):
    return {"value_2": 10}
```

!!! note

    Note that when issuing updates to the state, each node can just specify the value of the key it wishes to update.

    By default, this will **overwrite** the value of the corresponding key. You can also use [reducers](../concepts/low_level.md#reducers) to control how updates are processed— for example, you can append successive updates to a key instead. See [this section](#process-state-updates-with-reducers) for more detail.

Finally, we define the graph. We use [StateGraph](../concepts/low_level.md#stategraph) to define a graph that operates on this state.

We will then use [add_node](../concepts/low_level.md#messagesstate) and [add_edge](../concepts/low_level.md#edges) to populate our graph and define its control flow.

```python
from langgraph.graph import START, StateGraph

builder = StateGraph(State)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add nodes](./58-add-nodes.md)

**Next:** [Add nodes →](./60-add-nodes.md)
