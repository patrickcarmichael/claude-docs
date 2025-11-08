---
title: "Langgraph: Invoke the graph with an input and print the result"
description: "Invoke the graph with an input and print the result section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Invoke the graph with an input and print the result

print(graph.invoke({"question": "hi"}))
```

```json
{'answer': 'bye'}
```

Notice that the output of invoke only includes the output schema.

### Pass private state between nodes

In some cases, you may want nodes to exchange information that is crucial for intermediate logic but doesn't need to be part of the main schema of the graph. This private data is not relevant to the overall input/output of the graph and should only be shared between certain nodes.

Below, we'll create an example sequential graph consisting of three nodes (node_1, node_2 and node_3), where private data is passed between the first two steps (node_1 and node_2), while the third step (node_3) only has access to the public overall state.

```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Build the graph with input and output schemas specified](./38-build-the-graph-with-input-and-output-schemas-spec.md)

**Next:** [The overall state of the graph (this is the public state shared across nodes) →](./40-the-overall-state-of-the-graph-this-is-the-public-.md)
