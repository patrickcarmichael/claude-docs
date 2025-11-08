---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## LangGraph Agents

LangGraph is a stateful, orchestration framework that brings added control to agent workflows.

To use LangGraph with Cohere, you need to install the LangGraph package. To install it, run `pip install langgraph`.

### Basic Chatbot

This simple chatbot example will illustrate the core concepts of building with LangGraph.
```python PYTHON
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langchain_cohere import ChatCohere


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
