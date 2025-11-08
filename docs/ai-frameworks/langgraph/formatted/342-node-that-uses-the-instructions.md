---
title: "Langgraph: Node that *uses* the instructions"
description: "Node that *uses* the instructions section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Node that *uses* the instructions

def call_model(state: State, store: BaseStore):
    namespace = ("agent_instructions", )
    instructions = store.get(namespace, key="agent_a")[0]
    # Application logic
    prompt = prompt_template.format(instructions=instructions.value["instructions"])
    ...

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Long-term memory](./341-long-term-memory.md)

**Next:** [Node that updates instructions →](./343-node-that-updates-instructions.md)
