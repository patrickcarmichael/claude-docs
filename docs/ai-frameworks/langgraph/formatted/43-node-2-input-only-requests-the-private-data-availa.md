---
title: "Langgraph: Node 2 input only requests the private data available after node_1"
description: "Node 2 input only requests the private data available after node_1 section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Node 2 input only requests the private data available after node_1

class Node2Input(TypedDict):
    private_data: str

def node_2(state: Node2Input) -> OverallState:
    output = {"a": "set by node_2"}
    print(f"Entered node `node_2`:\n\tInput: {state}.\n\tReturned: {output}")
    return output

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The private data is only shared between node_1 and node_2](./42-the-private-data-is-only-shared-between-node_1-and.md)

**Next:** [Node 3 only has access to the overall state (no access to private data from node_1) →](./44-node-3-only-has-access-to-the-overall-state-no-acc.md)
