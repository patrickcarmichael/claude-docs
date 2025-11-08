---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Defining tools

Tools are defined using [JSON Schema](https://json-schema.org/understanding-json-schema/reference) format. Each tool requires:

* **name**: Function identifier (a-z, A-Z, 0-9, underscores, dashes; max 64 characters)
* **description**: Clear explanation of what the function does (used by the model to decide when to call it)
* **parameters**: JSON Schema object describing the function's parameters

<Tip>
  Write detailed descriptions and parameter definitions. The model relies on these to select the correct tool and provide appropriate arguments.
</Tip>

### Parameter types

JSON Schema supports: `string`, `number`, `integer`, `object`, `array`, `boolean`, and `null`. You can also:

* Use `enum` to restrict values to specific options
* Mark parameters as `required` or optional
* Provide descriptions for each parameter

<Accordion title="Example: Defining multiple tools">
```python
  tools = [
      {
          "type": "function",
          "function": {
              "name": "get_weather",
              "description": "Get current weather for a location",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "location": {
                          "type": "string",
                          "description": "City name, e.g. San Francisco"
                      },
                      "unit": {
                          "type": "string",
                          "enum": ["celsius", "fahrenheit"],
                          "description": "Temperature unit"
                      }
                  },
                  "required": ["location"]
              }
          }
      },
      {
          "type": "function",
          "function": {
              "name": "search_restaurants",
              "description": "Search for restaurants by cuisine type",
              "parameters": {
                  "type": "object",
                  "properties": {
                      "cuisine": {
                          "type": "string",
                          "description": "Type of cuisine (e.g., Italian, Mexican)"
                      },
                      "location": {
                          "type": "string",
                          "description": "City or neighborhood"
                      },
                      "price_range": {
                          "type": "string",
                          "enum": ["$", "$$", "$$$", "$$$$"]
                      }
                  },
                  "required": ["cuisine", "location"]
              }
          }
      }
  ]
```
</Accordion>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
