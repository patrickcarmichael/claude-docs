---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Send a chat message with chat history, note the last message is the current user message

current_message_and_history = [
    HumanMessage(content="knock knock"),
    AIMessage(content="Who's there?"),
    HumanMessage(content="Tank"),
]
print(llm.invoke(current_message_and_history))
```

### Cohere Agents with LangChain

LangChain [Agents](https://python.langchain.com/docs/how_to/#agents) use a language model to choose a sequence of actions to take.

To use Cohere's multi hop agent create a `create_cohere_react_agent` and pass in the LangChain tools you would like to use.

For example, using an internet search tool to get essay writing advice from Cohere with citations:
```python PYTHON
from langchain_cohere import ChatCohere
from langchain_cohere.react_multi_hop.agent import (
    create_cohere_react_agent,
)
from langchain.agents import AgentExecutor
from langchain_community.tools.tavily_search import (
    TavilySearchResults,
)
from langchain_core.prompts import ChatPromptTemplate

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
