---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Try out an example

llm = ChatCohere(model="command-a-03-2025", temperature=0)
agent_executor = create_csv_agent(llm, "movies_tickets.csv")
resp = agent_executor.invoke(
    {"input": "Who all watched Shawshank redemption?"}
)
print(resp.get("output"))
```
The output returned is:
```
John, Jerry, Jack and Jeremy watched Shawshank Redemption.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
