---
title: "Langgraph: How to add cross-thread persistence (functional API)"
description: "How to add cross-thread persistence (functional API) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to add cross-thread persistence (functional API)


!!! info "Prerequisites"

    This guide assumes familiarity with the following:
    
    - <a href="../../concepts/functional_api/">Functional API</a>
    - <a href="../../concepts/persistence/">Persistence</a>
    - <a href="../../concepts/memory/">Memory</a>
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)

LangGraph allows you to persist data across **different <a href="../../concepts/persistence/#threads">threads</a>**. For instance, you can store information about users (their names or preferences) in a shared (cross-thread) memory and reuse them in the new threads (e.g., new conversations).

When using the <a href="../../concepts/functional_api/">functional API</a>, you can set it up to store and retrieve memories by using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface:

1. Create an instance of a `Store`

    ```python
    from langgraph.store.memory import InMemoryStore, BaseStore
    
    store = InMemoryStore()
    ```

2. Pass the `store` instance to the `entrypoint()` decorator and expose `store` parameter in the function signature:

    ```python
    from langgraph.func import entrypoint

    @entrypoint(store=store)
    def workflow(inputs: dict, store: BaseStore):
        my_task(inputs).result()
        ...
    ```
    
In this guide, we will show how to construct and use a workflow that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface.

!!! note Note

    Support for the [`Store`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.32`.

    Support for __index__ and __query__ arguments of the [`Store`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.54`.

!!! tip "Note"

    If you need to add cross-thread persistence to a `StateGraph`, check out this <a href="../cross-thread-persistence">how-to guide</a>.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prebuilt tools](./145-prebuilt-tools.md)

**Next:** [Setup →](./147-setup.md)
