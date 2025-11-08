---
title: "Langgraph: Use subgraphs"
description: "Use subgraphs section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Use subgraphs


This guide explains the mechanics of using [subgraphs](../concepts/subgraphs.md). A common application of subgraphs is to build [multi-agent](../concepts/multi_agent.md) systems.

When adding subgraphs, you need to define how the parent graph and the subgraph communicate:

* [Shared state schemas](#shared-state-schemas) — parent and subgraph have **shared state keys** in their state [schemas](../concepts/low_level.md#state)
* [Different state schemas](#different-state-schemas) — **no shared state keys** in parent and subgraph [schemas](../concepts/low_level.md#state)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Integrate with other libraries](./99-integrate-with-other-libraries.md)

**Next:** [Setup →](./101-setup.md)
