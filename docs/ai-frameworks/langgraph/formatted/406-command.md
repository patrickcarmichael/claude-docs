---
title: "Langgraph: `Command`"
description: "`Command` section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## `Command`


It can be useful to combine control flow (edges) and state updates (nodes). For example, you might want to BOTH perform state updates AND decide which node to go to next in the SAME node. LangGraph provides a way to do so by returning a [`Command`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) object from node functions:

```python
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    return Command(
        # state update
        update={"foo": "bar"},
        # control flow
        goto="my_other_node"
    )
```

With `Command` you can also achieve dynamic control flow behavior (identical to [conditional edges](#conditional-edges)):

```python
def my_node(state: State) -> Command[Literal["my_other_node"]]:
    if state["foo"] == "bar":
        return Command(update={"foo": "baz"}, goto="my_other_node")
```

!!! important

    When returning `Command` in your node functions, you must add return type annotations with the list of node names the node is routing to, e.g. `Command[Literal["my_other_node"]]`. This is necessary for the graph rendering and tells LangGraph that `my_node` can navigate to `my_other_node`.

Check out this [how-to guide](../how-tos/graph-api.md#combine-control-flow-and-state-updates-with-command) for an end-to-end example of how to use `Command`.

### When should I use Command instead of conditional edges?

- Use `Command` when you need to **both** update the graph state **and** route to a different node. For example, when implementing [multi-agent handoffs](./multi_agent.md#handoffs) where it's important to route to a different agent and pass some information to that agent.
- Use [conditional edges](#conditional-edges) to route between nodes conditionally without updating the state.

### Navigating to a node in a parent graph

If you are using [subgraphs](./subgraphs.md), you might want to navigate from a node within a subgraph to a different subgraph (i.e. a different node in the parent graph). To do so, you can specify `graph=Command.PARENT` in `Command`:

```python
def my_node(state: State) -> Command[Literal["other_subgraph"]]:
    return Command(
        update={"foo": "bar"},
        goto="other_subgraph",  # where `other_subgraph` is a node in the parent graph
        graph=Command.PARENT
    )
```

!!! note

    Setting `graph` to `Command.PARENT` will navigate to the closest parent graph.

!!! important "State updates with `Command.PARENT`"

    When you send updates from a subgraph node to a parent graph node for a key that's shared by both parent and subgraph [state schemas](#schema), you **must** define a [reducer](#reducers) for the key you're updating in the parent graph state. See this [example](../how-tos/graph-api.md#navigate-to-a-node-in-a-parent-graph).

This is particularly useful when implementing [multi-agent handoffs](./multi_agent.md#handoffs).

Check out [this guide](../how-tos/graph-api.md#navigate-to-a-node-in-a-parent-graph) for detail.

### Using inside tools

A common use case is updating graph state from inside a tool. For example, in a customer support application you might want to look up customer information based on their account number or ID in the beginning of the conversation.

Refer to [this guide](../how-tos/graph-api.md#use-inside-tools) for detail.

### Human-in-the-loop

`Command` is an important part of human-in-the-loop workflows: when using `interrupt()` to collect user input, `Command` is then used to supply the input and resume execution via `Command(resume="User input")`. Check out [this conceptual guide](./human_in_the_loop.md) for more information.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← `Send`](./405-send.md)

**Next:** [Graph Migrations →](./407-graph-migrations.md)
