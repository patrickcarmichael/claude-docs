---
title: "Langgraph: Keep the original message history unmodified"
description: "Keep the original message history unmodified section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Keep the original message history unmodified


Let's build a ReAct agent with a step that manages the conversation history: when the length of the history exceeds a specified number of tokens, we will call [`trim_messages`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) utility that that will reduce the history while satisfying LLM provider constraints.

There are two ways that the updated message history can be applied inside ReAct agent:

  * <a href="#keep-the-original-message-history-unmodified">**Keep the original message history unmodified**</a> in the graph state and pass the updated history **only as the input to the LLM**
  * <a href="#overwrite-the-original-message-history">**Overwrite the original message history**</a> in the graph state with the updated history

Let's start by implementing the first one. We'll need to first define model and tools for our agent:

```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0)

def get_weather(location: str) -> str:
    """Use this to get weather information."""
    if any([city in location.lower() for city in ["nyc", "new york city"]]):
        return "It might be cloudy in nyc, with a chance of rain and temperatures up to 80 degrees."
    elif any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's always sunny in sf"
    else:
        return f"I am not sure what the weather is in {location}"

tools = [get_weather]
```

Now let's implement `pre_model_hook` — a function that will be added as a new node and called every time **before** the node that calls the LLM (the `agent` node).

Our implementation will wrap the `trim_messages` call and return the trimmed messages under `llm_input_messages`. This will **keep the original message history unmodified** in the graph state and pass the updated history **only as the input to the LLM**

```python hl_lines="4 5 6 7 22 29"
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from langchain_core.messages.utils import (
    trim_messages,
    count_tokens_approximately,
)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Setup](./174-setup.md)

**Next:** [This function will be added as a new node in ReAct agent graph →](./176-this-function-will-be-added-as-a-new-node-in-react.md)
