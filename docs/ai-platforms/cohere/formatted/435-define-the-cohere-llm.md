---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the Cohere LLM

llm = ChatCohere(
    cohere_api_key="COHERE_API_KEY", model="command-a-03-2025"
)

llm_with_tools = llm.bind_tools(
    tools=[web_search, vectorstore], preamble=preamble
)

messages = [
    HumanMessage("Who will the Bears draft first in the NFL draft?")
]
response = llm_with_tools.invoke(messages, force_single_step=True)
print(response.response_metadata["tool_calls"])

messages = [HumanMessage("What are the types of agent memory?")]
response = llm_with_tools.invoke(messages, force_single_step=True)
print(response.response_metadata["tool_calls"])

messages = [HumanMessage("Hi, How are you?")]
response = llm_with_tools.invoke(messages, force_single_step=True)
print("tool_calls" in response.response_metadata)
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
