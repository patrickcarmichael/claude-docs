---
title: "Langgraph: What’s possible with LangGraph streaming"
description: "What’s possible with LangGraph streaming section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## What’s possible with LangGraph streaming


- [**Stream LLM tokens**](../how-tos/streaming.md#messages) — capture token streams from anywhere: inside nodes, subgraphs, or tools.
- [**Emit progress notifications from tools**](../how-tos/streaming.md#stream-custom-data) — send custom updates or progress signals directly from tool functions.
- [**Stream from subgraphs**](../how-tos/streaming.md#stream-subgraph-outputs) — include outputs from both the parent graph and any nested subgraphs.
- [**Use any LLM**](../how-tos/streaming.md#use-with-any-llm) — stream tokens from any LLM, even if it's not a LangChain model using the `custom` streaming mode.
- [**Use multiple streaming modes**](../how-tos/streaming.md#stream-multiple-modes) — choose from `values` (full state), `updates` (state deltas), `messages` (LLM tokens + metadata), `custom` (arbitrary user data), or `debug` (detailed traces).

---

concepts/functional_api.md

---

---

search:
  boost: 2

---

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Streaming](./306-streaming.md)

**Next:** [Functional API concepts →](./308-functional-api-concepts.md)
