---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Create an agent

agent = create_cohere_react_agent(
    llm=llm,
    tools=[internet_search],
    prompt=ChatPromptTemplate.from_template("{question}"),
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
