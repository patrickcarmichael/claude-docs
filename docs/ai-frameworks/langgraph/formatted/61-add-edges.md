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

!!! tip "Specifying custom names"

    You can specify custom names for nodes using `.add_node`:

    ```python
    builder.add_node("my_node", step_1)
    ```

Note that:

- `.add_edge` takes the names of nodes, which for functions defaults to `node.__name__`.
- We must specify the entry point of the graph. For this we add an edge with the [START node](../concepts/low_level.md#start-node).
- The graph halts when there are no more nodes to execute.

We next [compile](../concepts/low_level.md#compiling-your-graph) our graph. This provides a few basic checks on the structure of the graph (e.g., identifying orphaned nodes). If we were adding persistence to our application via a [checkpointer](../concepts/persistence.md), it would also be passed in here.

```python
graph = builder.compile()
```

LangGraph provides built-in utilities for visualizing your graph. Let's inspect our sequence. See [this guide](#visualize-your-graph) for detail on visualization.

```python
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

![Sequence of steps graph](assets/graph_api_image_2.png)

Let's proceed with a simple invocation:

```python
graph.invoke({"value_1": "c"})
```

```json
{'value_1': 'a b', 'value_2': 10}
```

Note that:

- We kicked off invocation by providing a value for a single state key. We must always provide a value for at least one key.
- The value we passed in was overwritten by the first node.
- The second node updated the value.
- The third node populated a different value.

!!! tip "Built-in shorthand"

    `langgraph>=0.2.46` includes a built-in short-hand `add_sequence` for adding node sequences. You can compile the same graph as follows:

    ```python hl_lines="1"
    builder = StateGraph(State).add_sequence([step_1, step_2, step_3])
    builder.add_edge(START, "step_1")

    graph = builder.compile()

    graph.invoke({"value_1": "c"})
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Add nodes](./60-add-nodes.md)

**Next:** [Create branches →](./62-create-branches.md)
