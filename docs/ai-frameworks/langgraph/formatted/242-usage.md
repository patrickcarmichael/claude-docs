---
title: "Langgraph: Usage"
description: "Usage section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Usage


To use our agent, we invoke it with a messages list. Based on our implementation, these can be LangChain [message](https://python.langchain.com/docs/concepts/messages/) objects or OpenAI-style dicts:

```python
user_message = {"role": "user", "content": "What's the weather in san francisco?"}
print(user_message)

for step in agent.stream([user_message]):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': "What's the weather in san francisco?"}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_tNnkrjnoz6MNfCHJpwfuEQ0v)
 Call ID: call_tNnkrjnoz6MNfCHJpwfuEQ0v
  Args:
    location: san francisco

call_tool:
================================= Tool Message =================================

It's sunny!

call_model:
================================== Ai Message ==================================

The weather in San Francisco is sunny!
```python
Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool. Check out the LangSmith trace [here](https://smith.langchain.com/public/d5a0d5ea-bdaa-4032-911e-7db177c8141b/r).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Create ReAct agent](./241-create-react-agent.md)

**Next:** [Add thread-level persistence →](./243-add-thread-level-persistence.md)
