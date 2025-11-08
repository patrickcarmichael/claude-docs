---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create agent

agent = FunctionCallingAgent.from_tools(
    [multiply_tool, add_tool],
    llm=llm,
    verbose=True,
    allow_parallel_tool_calls=True,
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
