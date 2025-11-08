---
title: "Langgraph: 2. Define a graph that accesses the config in a node"
description: "2. Define a graph that accesses the config in a node section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# 2. Define a graph that accesses the config in a node

class State(TypedDict):
    my_state_value: str

def node(state: State, runtime: Runtime[ContextSchema]):
    if runtime.context["my_runtime_value"] == "a":
        return {"my_state_value": 1}
    elif runtime.context["my_runtime_value"] == "b":
        return {"my_state_value": 2}
    else:
        raise ValueError("Unknown values.")

builder = StateGraph(State, context_schema=ContextSchema)
builder.add_node(node)
builder.add_edge(START, "node")
builder.add_edge("node", END)

graph = builder.compile()

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← 1. Specify config schema](./52-1-specify-config-schema.md)

**Next:** [3. Pass in configuration at runtime: →](./54-3-pass-in-configuration-at-runtime.md)
