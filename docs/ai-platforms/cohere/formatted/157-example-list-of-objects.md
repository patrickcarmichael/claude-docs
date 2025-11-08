---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example: List of objects

weather_search_results = [
    {"city": "Toronto", "date": "250207", "temperature": "20°C"},
    {"city": "Toronto", "date": "250208", "temperature": "21°C"},
]
```

### Defining the tool schema

We also need to define the tool schemas in a format that can be passed to the Chat endpoint. The schema follows the [JSON Schema specification](https://json-schema.org/understanding-json-schema) and must contain the following fields:

* `name`: the name of the tool.
* `description`: a description of what the tool is and what it is used for.
* `parameters`: a list of parameters that the tool accepts. For each parameter, we need to define the following fields:
  * `type`: the type of the parameter.
  * `properties`: the name of the parameter and the following fields:
    * `type`: the type of the parameter.
    * `description`: a description of what the parameter is and what it is used for.
  * `required`: a list of required properties by name, which appear as keys in the `properties` object

This schema informs the LLM about what the tool does, and the LLM decides whether to use a particular tool based on the information that it contains.

Therefore, the more descriptive and clear the schema, the more likely the LLM will make the right tool call decisions.

In a typical development cycle, some fields such as `name`, `description`, and `properties` will likely require a few rounds of iterations in order to get the best results (a similar approach to prompt engineering).
```python PYTHON
tools = [
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
                        "description": "the location to get the weather, example: San Francisco.",
                    }
                },
                "required": ["location"],
            },
        },
    },
]
```
>   **📝 Note**
>
> The endpoint supports a subset of the JSON Schema specification. Refer to the 

  [Structured Outputs documentation](https://docs.cohere.com/docs/structured-outputs#parameter-types-support)

   for the list of supported and unsupported parameters.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
