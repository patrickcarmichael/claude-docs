---
title: "Langgraph: Build the graph with input and output schemas specified"
description: "Build the graph with input and output schemas specified section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Build the graph with input and output schemas specified

builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
builder.add_node(answer_node)  # Add the answer node
builder.add_edge(START, "answer_node")  # Define the starting edge
builder.add_edge("answer_node", END)  # Define the ending edge
graph = builder.compile()  # Compile the graph

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Define the node that processes the input and generates an answer](./37-define-the-node-that-processes-the-input-and-gener.md)

**Next:** [Invoke the graph with an input and print the result →](./39-invoke-the-graph-with-an-input-and-print-the-resul.md)
