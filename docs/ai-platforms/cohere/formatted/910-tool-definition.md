---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Tool definition

* v1: uses Python types to define tools.
* v2: uses JSON schema to define tools.

**v1**
```python PYTHON
def get_weather(location):
    return {"temperature": "20C"}


functions_map = {"get_weather": get_weather}

tools_v1 = [
    {
        "name": "get_weather",
        "description": "Gets the weather of a given location",
        "parameter_definitions": {
            "location": {
                "description": "The location to get weather, example: San Francisco, CA",
                "type": "str",
                "required": True,
            }
        },
    },
]
```
**v2**
```python PYTHON
def get_weather(location):
    return [{"temperature": "20C"}]
    # You can return a list of objects e.g. [{"url": "abc.com", "text": "..."}, {"url": "xyz.com", "text": "..."}]


functions_map = {"get_weather": get_weather}

tools_v2 = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "the location to get weather, example: San Fransisco, CA",
                    }
                },
                "required": ["location"],
            },
        },
    },
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
