---
title: "Langgraph: How to pass custom run ID or set tags and metadata for graph runs in LangSmith"
description: "How to pass custom run ID or set tags and metadata for graph runs in LangSmith section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to pass custom run ID or set tags and metadata for graph runs in LangSmith


!!! tip "Prerequisites"
    This guide assumes familiarity with the following:
    
    - [LangSmith Documentation](https://docs.smith.langchain.com)
    - [LangSmith Platform](https://smith.langchain.com)
    - [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)
    - [Add metadata and tags to traces](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#add-metadata-and-tags-to-traces)
    - [Customize run name](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#customize-run-name)

Debugging graph runs can sometimes be difficult to do in an IDE or terminal. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read the [LangSmith documentation](https://docs.smith.langchain.com) for more information on how to get started.

To make it easier to identify and analyzed traces generated during graph invocation, you can set additional configuration at run time (see [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)):

| **Field**   | **Type**            | **Description**                                                                                                    |
|-------------|---------------------|--------------------------------------------------------------------------------------------------------------------|
| run_name    | `str`               | Name for the tracer run for this call. Defaults to the name of the class.                                          |
| run_id      | `UUID`              | Unique identifier for the tracer run for this call. If not provided, a new UUID will be generated.                 |
| tags        | `List[str]`         | Tags for this call and any sub-calls (e.g., a Chain calling an LLM). You can use these to filter calls.            |
| metadata    | `Dict[str, Any]`    | Metadata for this call and any sub-calls (e.g., a Chain calling an LLM). Keys should be strings, values should be JSON-serializable. |

LangGraph graphs implement the [LangChain Runnable Interface](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html) and accept a second argument (`RunnableConfig`) in methods like `invoke`, `ainvoke`, `stream` etc.

The LangSmith platform will allow you to search and filter traces based on `run_name`, `run_id`, `tags` and `metadata`.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Prebuilt implementations](./120-prebuilt-implementations.md)

**Next:** [TLDR →](./122-tldr.md)
