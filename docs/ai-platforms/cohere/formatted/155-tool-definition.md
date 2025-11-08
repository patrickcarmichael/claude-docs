---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool definition

The pre-requisite, or Step 0, before we can run a tool use workflow, is to define the tools. We can break this further into two steps:

* Creating the tool
* Defining the tool schema

<img src="file:33a473c5-584d-4c28-9f82-7a012a568c76" alt="Tool definition" />

### Creating the tool

A tool can be any function that you create or external services that return an object for a given input. Some examples: a web search engine, an email service, an SQL database, a vector database, a weather data service, a sports data service, or even another LLM.

In this example, we define a `get_weather` function that returns the temperature for a given query, which is the location. You can implement any logic here, but to simplify the example, here we are hardcoding the return value to be the same for all queries.
```python PYTHON
def get_weather(location):
    # Implement any logic here

    return [{"temperature": "20°C"}]
    # Return a JSON object string, or a list of tool content blocks e.g. [{"url": "abc.com", "text": "..."}, {"url": "xyz.com", "text": "..."}]


functions_map = {"get_weather": get_weather}
```
The Chat endpoint accepts [a string or a list of objects](https://docs.cohere.com/reference/chat#request.body.messages.tool.content) as the tool results. Thus, you should format the return value in this way. The following are some examples.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
