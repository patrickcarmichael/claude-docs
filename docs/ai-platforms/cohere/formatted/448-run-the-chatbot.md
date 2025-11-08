---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run the chatbot

while True:
    user_input = input("User: ")
    print("User: " + user_input)
    if user_input.lower() in ["quit", "exit", "q"]:
        print("Goodbye!")
        break
    for event in graph.stream({"messages": ("user", user_input)}):
        for value in event.values():
            print("Assistant:", value["messages"][-1].content)
```

### Enhancing the Chatbot with Tools

To handle queries our chatbot can't answer "from memory", we'll integrate a web search tool. Our bot can use this tool to find relevant information and provide better responses.
```python PYTHON
from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from langchain_cohere import ChatCohere
from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langchain_core.messages import ToolMessage
from langchain_core.messages import BaseMessage
from typing import Annotated, Literal
from typing_extensions import TypedDict
import json


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
