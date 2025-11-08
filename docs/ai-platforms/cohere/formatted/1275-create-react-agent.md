---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create ReAct Agent

The model can smartly pick the right tool(s) for the user query, call them in any sequence, analyze the results and self-reflect.
Once the model considers it has enough information to answer the user question, it generates the final answer.
```python PYTHON
from langchain.agents import AgentExecutor
from langchain_cohere.react_multi_hop.agent import create_cohere_react_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_cohere.chat_models import ChatCohere

llm = ChatCohere(model="command-a-03-2025", temperature=0.3)

preamble = """
You are an expert who answers the user's question with the most relevant datasource. You are equipped with an internet search tool and a special vectorstore of information about how to write good essays.
You also have a 'random_operation_tool' tool, you must use it to compute the random operation between two numbers.
"""


prompt = ChatPromptTemplate.from_template("{input}")

agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search, vectorstore_search, python_tool, random_operation_tool],
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=agent, tools=[internet_search, vectorstore_search, python_tool, random_operation_tool], verbose=True)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
