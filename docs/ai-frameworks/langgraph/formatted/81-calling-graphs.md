---
title: "Langgraph: Calling graphs"
description: "Calling graphs section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Calling graphs


The **Functional API** and the [**Graph API**](../concepts/low_level.md) can be used together in the same application as they share the same underlying runtime.

```python
from langgraph.func import entrypoint
from langgraph.graph import StateGraph

builder = StateGraph()
...
some_graph = builder.compile()

@entrypoint()
def some_workflow(some_input: dict) -> int:
    # Call a graph defined using the graph API
    result_1 = some_graph.invoke(...)
    # Call another graph defined using the graph API
    result_2 = another_graph.invoke(...)
    return {
        "result_1": result_1,
        "result_2": result_2
    }
```

??? example "Extended example: calling a simple graph from the functional API"

    ```python
    import uuid
    from typing import TypedDict
    from langgraph.func import entrypoint
    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.graph import StateGraph

    # Define the shared state type
    class State(TypedDict):
        foo: int

    # Define a simple transformation node
    def double(state: State) -> State:
        return {"foo": state["foo"] * 2}

    # Build the graph using the Graph API
    builder = StateGraph(State)
    builder.add_node("double", double)
    builder.set_entry_point("double")
    graph = builder.compile()

    # Define the functional API workflow
    checkpointer = InMemorySaver()

    @entrypoint(checkpointer=checkpointer)
    def workflow(x: int) -> dict:
        result = graph.invoke({"foo": x})
        return {"bar": result["foo"]}

    # Execute the workflow
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    print(workflow.invoke(5, config=config))  # Output: {'bar': 10}
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Parallel execution](./80-parallel-execution.md)

**Next:** [Call other entrypoints →](./82-call-other-entrypoints.md)
