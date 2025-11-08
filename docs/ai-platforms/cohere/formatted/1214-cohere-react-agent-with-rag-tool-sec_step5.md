---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere ReAct Agent with RAG Tool \[#sec\_step5]

Finally, we build a simple agent that utilizes the RAG pipeline defined above. We do this by granting the agent access to two tools:

* the end-to-end RAG pipeline
* a Python interpreter

The intention behind coupling these tools is to enable the model to perform mathematical and other postprocessing operations on RAG outputs using Python.
```python PYTHON
from langchain.agents import Tool
from langchain_experimental.utilities import PythonREPL
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere
from langchain.tools.retriever import create_retriever_tool
from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_core.tools import tool

class react_agent():
    def __init__(self,rag_retriever,model="command-a-03-2025",temperature=0.2):
        self.llm = ChatCohere(model=model, temperature=temperature)
        self.preamble="""

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
