---
title: "Langgraph: Task"
description: "Task section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Task


A **task** represents a discrete unit of work, such as an API call or data processing step. It has two key characteristics:

- **Asynchronous Execution**: Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
- **Checkpointing**: Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](persistence.md) for more details).

### Definition

Tasks are defined using the `@task` decorator, which wraps a regular Python function.

```python
from langgraph.func import task

@task()
def slow_computation(input_value):
    # Simulate a long-running operation
    ...
    return result
```

!!! important "Serialization"

    The **outputs** of tasks must be JSON-serializable to support checkpointing.

### Execution

**Tasks** can only be called from within an **entrypoint**, another **task**, or a [state graph node](./low_level.md#nodes).

Tasks _cannot_ be called directly from the main application code.

When you call a **task**, it returns _immediately_ with a future object. A future is a placeholder for a result that will be available later.

To obtain the result of a **task**, you can either wait for it synchronously (using `result()`) or await it asynchronously (using `await`).

=== "Synchronous Invocation"

    ```python
    @entrypoint(checkpointer=checkpointer)
    def my_workflow(some_input: int) -> int:
        future = slow_computation(some_input)
        return future.result()  # Wait for the result synchronously
    ```

=== "Asynchronous Invocation"

    ```python
    @entrypoint(checkpointer=checkpointer)
    async def my_workflow(some_input: int) -> int:
        return await slow_computation(some_input)  # Await result asynchronously
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Entrypoint](./312-entrypoint.md)

**Next:** [When to use a task →](./314-when-to-use-a-task.md)
