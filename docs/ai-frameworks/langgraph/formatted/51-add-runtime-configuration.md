---
title: "Langgraph: Add runtime configuration"
description: "Add runtime configuration section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Add runtime configuration


Sometimes you want to be able to configure your graph when calling it. For example, you might want to be able to specify what LLM or system prompt to use at runtime, _without polluting the graph state with these parameters_.

To add runtime configuration:

1. Specify a schema for your configuration
2. Add the configuration to the function signature for nodes or conditional edges
3. Pass the configuration into the graph.

See below for a simple example:

```python hl_lines="13 14 16 21 29 30"
from langgraph.graph import END, StateGraph, START
from langgraph.runtime import Runtime
from typing_extensions import TypedDict

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Test the graph with a valid input](./50-test-the-graph-with-a-valid-input.md)

**Next:** [1. Specify config schema →](./52-1-specify-config-schema.md)
