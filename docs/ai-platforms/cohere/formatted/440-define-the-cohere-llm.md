---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the Cohere LLM

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY",
    model="command-a-03-2025",
    temperature=0,
)

agent_executor = create_csv_agent(
    llm,
    "titanic.csv",  # https://github.com/langchain-ai/langchain/blob/master/templates/csv-agent/titanic.csv

)

resp = agent_executor.invoke(
    {"input": "How many people were on the titanic?"}
)
print(resp.get("output"))
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
