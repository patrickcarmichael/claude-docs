---
title: "Langgraph: Call other entrypoints"
description: "Call other entrypoints section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Call other entrypoints


You can call other **entrypoints** from within an **entrypoint** or a **task**.

```python
@entrypoint() # Will automatically use the checkpointer from the parent entrypoint
def some_other_workflow(inputs: dict) -> int:
    return inputs["value"]

@entrypoint(checkpointer=checkpointer)
def my_workflow(inputs: dict) -> int:
    value = some_other_workflow.invoke({"value": 1})
    return value
```

??? example "Extended example: calling another entrypoint"

    ```python
    import uuid
    from langgraph.func import entrypoint
    from langgraph.checkpoint.memory import InMemorySaver

    # Initialize a checkpointer
    checkpointer = InMemorySaver()

    # A reusable sub-workflow that multiplies a number
    @entrypoint()
    def multiply(inputs: dict) -> int:
        return inputs["a"] * inputs["b"]

    # Main workflow that invokes the sub-workflow
    @entrypoint(checkpointer=checkpointer)
    def main(inputs: dict) -> dict:
        result = multiply.invoke({"a": inputs["x"], "b": inputs["y"]})
        return {"product": result}

    # Execute the main workflow
    config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    print(main.invoke({"x": 6, "y": 7}, config=config))  # Output: {'product': 42}
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Calling graphs](./81-calling-graphs.md)

**Next:** [Streaming →](./83-streaming.md)
