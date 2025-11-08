---
title: "Langgraph: The overall state of the graph (this is the public state shared across nodes)"
description: "The overall state of the graph (this is the public state shared across nodes) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# The overall state of the graph (this is the public state shared across nodes)

class OverallState(BaseModel):
    a: str

def node(state: OverallState):
    return {"a": "goodbye"}

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Invoke the graph with the initial state](./47-invoke-the-graph-with-the-initial-state.md)

**Next:** [Build the state graph →](./49-build-the-state-graph.md)
