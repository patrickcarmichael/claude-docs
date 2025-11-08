---
title: "Langgraph: Node 3 only has access to the overall state (no access to private data from node_1)"
description: "Node 3 only has access to the overall state (no access to private data from node_1) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Node 3 only has access to the overall state (no access to private data from node_1)

def node_3(state: OverallState) -> OverallState:
    output = {"a": "set by node_3"}
    print(f"Entered node `node_3`:\n\tInput: {state}.\n\tReturned: {output}")
    return output

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Node 2 input only requests the private data available after node_1](./43-node-2-input-only-requests-the-private-data-availa.md)

**Next:** [Connect nodes in a sequence →](./45-connect-nodes-in-a-sequence.md)
