---
title: "Langgraph: We now add a conditional edge"
description: "We now add a conditional edge section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# We now add a conditional edge

workflow.add_conditional_edges(
    # First, we define the start node. We use `agent`.
    # This means these are the edges taken after the `agent` node is called.
    "agent",
    # Next, we pass in the function that will determine which node is called next.
    should_continue,
    # Finally we pass in a mapping.
    # The keys are strings, and the values are other nodes.
    # END is a special node marking that the graph should finish.
    # What will happen is we will call `should_continue`, and then the output of that
    # will be matched against the keys in this mapping.
    # Based on which one it matches, that node will then be called.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Set the entrypoint as `agent`](./209-set-the-entrypoint-as-agent.md)

**Next:** [We now add a normal edge from `tools` to `agent`. →](./211-we-now-add-a-normal-edge-from-tools-to-agent.md)
