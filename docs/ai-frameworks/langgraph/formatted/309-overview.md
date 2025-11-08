---
title: "Langgraph: Overview"
description: "Overview section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Overview


The **Functional API** allows you to add LangGraph's key features — [persistence](./persistence.md), [memory](../how-tos/memory/add-memory.md), [human-in-the-loop](./human_in_the_loop.md), and [streaming](./streaming.md) — to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model.

The Functional API uses two key building blocks:

- **`@entrypoint`** – Marks a function as the starting point of a workflow, encapsulating logic and managing execution flow, including handling long-running tasks and interrupts.
- **`@task`** – Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.  

This provides a minimal abstraction for building workflows with state management and streaming.

!!! tip

    For information on how to use the functional API, see [Use Functional API](../how-tos/use-functional-api.md).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Functional API concepts](./308-functional-api-concepts.md)

**Next:** [Functional API vs. Graph API →](./310-functional-api-vs-graph-api.md)
