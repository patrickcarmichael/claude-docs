---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## nice! now let's ask a follow-up question

q2 = "plot revenue numbers"
a2_no_mem = agent_executor.invoke({
   "input": q2,
})
```
````txt title="Output"
[1m> Entering new AgentExecutor chain...[0m
[32;1m[1;3mPlan: I will ask the user for clarification on what data they would like to visualise.
Action: ```json JSON
[
    {
        "tool_name": "directly_answer",
        "parameters": {}
    }
]
```
Relevant Documents: None
Cited Documents: None
Answer: Hello, could you please clarify what data you would like to see plotted?
Grounded answer: Hello, could you please clarify what data you would like to see plotted?[0m

[1m> Finished chain.[0m
````

Without memory, the model cannot answer follow up questions because it misses the necessary previous context

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
