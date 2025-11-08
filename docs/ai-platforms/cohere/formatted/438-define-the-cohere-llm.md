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

agent_executor = create_sql_agent(llm, db=db, verbose=True)

resp = agent_executor.invoke(
    "Show me the first 5 rows of the Album table."
)
print(resp)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
