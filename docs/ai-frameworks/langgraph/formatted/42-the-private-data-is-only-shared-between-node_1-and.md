---
title: "Langgraph: The private data is only shared between node_1 and node_2"
description: "The private data is only shared between node_1 and node_2 section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# The private data is only shared between node_1 and node_2

def node_1(state: OverallState) -> Node1Output:
    output = {"private_data": "set by node_1"}
    print(f"Entered node `node_1`:\n\tInput: {state}.\n\tReturned: {output}")
    return output

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Output from node_1 contains private data that is not part of the overall state](./41-output-from-node_1-contains-private-data-that-is-n.md)

**Next:** [Node 2 input only requests the private data available after node_1 →](./43-node-2-input-only-requests-the-private-data-availa.md)
