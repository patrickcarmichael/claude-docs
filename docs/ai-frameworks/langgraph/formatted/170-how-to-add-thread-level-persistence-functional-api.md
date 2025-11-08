---
title: "Langgraph: How to add thread-level persistence (functional API)"
description: "How to add thread-level persistence (functional API) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to add thread-level persistence (functional API)


!!! info "Prerequisites"

    This guide assumes familiarity with the following:
    
    - <a href="../../concepts/functional_api/">Functional API</a>
    - <a href="../../concepts/persistence/">Persistence</a>
    - <a href="../../concepts/memory/">Memory</a>
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)

!!! info "Not needed for LangGraph API users"

    If you're using the LangGraph API, you needn't manually implement a checkpointer. The API automatically handles checkpointing for you. This guide is relevant when implementing LangGraph in your own custom server.

Many AI applications need memory to share context across multiple interactions on the same <a href="../../concepts/persistence#threads">thread</a> (e.g., multiple turns of a conversation). In LangGraph functional API, this kind of memory can be added to any [entrypoint()][langgraph.func.entrypoint] workflow using [thread-level persistence](https://langchain-ai.github.io/langgraph/concepts/persistence).

When creating a LangGraph workflow, you can set it up to persist its results by using a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#basecheckpointsaver):

1. Create an instance of a checkpointer:

    ```python
    from langgraph.checkpoint.memory import InMemorySaver
    
    checkpointer = InMemorySaver()       
    ```

2. Pass `checkpointer` instance to the `entrypoint()` decorator:

    ```python
    from langgraph.func import entrypoint
    
    @entrypoint(checkpointer=checkpointer)
    def workflow(inputs)
        ...
    ```

3. Optionally expose `previous` parameter in the workflow function signature:

    ```python
    @entrypoint(checkpointer=checkpointer)
    def workflow(
        inputs,
        *,
        # you can optionally specify `previous` in the workflow function signature
        # to access the return value from the workflow as of the last execution
        previous
    ):
        previous = previous or []
        combined_inputs = previous + inputs
        result = do_something(combined_inputs)
        ...
    ```

4. Optionally choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous`:

    ```python
    @entrypoint(checkpointer=checkpointer)
    def workflow(inputs, *, previous):
        ...
        result = do_something(...)
        return entrypoint.final(value=result, save=combine(inputs, result))
    ```

This guide shows how you can add thread-level persistence to your workflow.

!!! tip "Note"

    If you need memory that is __shared__ across multiple conversations or users (cross-thread persistence), check out this <a href="../cross-thread-persistence-functional">how-to guide</a>.

!!! tip "Note"

    If you need to add thread-level persistence to a `StateGraph`, check out this <a href="../persistence">how-to guide</a>.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Test multi-turn conversation](./169-test-multi-turn-conversation.md)

**Next:** [Setup →](./171-setup.md)
