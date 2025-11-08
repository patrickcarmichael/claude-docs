---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-Step Tool Use

Multi-step is enabled by default. Here's an example of using it to put together a simple agent:
```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import (
    create_cohere_react_agent,
)
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere import ChatCohere

from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from pydantic import BaseModel, Field

os.environ["TAVILY_API_KEY"] = "TAVILY_API_KEY"

internet_search = TavilySearchResults()
internet_search.name = "internet_search"
internet_search.description = "Returns a list of relevant document snippets for a textual query retrieved from the internet."


class TavilySearchInput(BaseModel):
    query: str = Field(
        description="Query to search the internet with"
    )


internet_search.args_schema = TavilySearchInput

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
