---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Array

### With specific types

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "cities": {
                "type": "array",
                "items": {"type": "string"},
            }
        },
        "required": ["cities"],
    },
}

message = "Generate a JSON listing three cities in Japan."
```
Example output:
```mdx wordWrap
{
  "cities": [
    "Tokyo",
    "Kyoto",
    "Osaka"
  ]
}
```

### Without specific types

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "cities": {
                "type": "array",
            }
        },
        "required": ["cities"],
    },
}

message = "Generate a JSON listing three cities in Japan."
```
Example output:
```mdx wordWrap
{
  "cities": [
    "Tokyo",
    "Kyoto",
    "Osaka"
  ]
}
```

### Lists of lists

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "coordinates": {
                "type": "array",
                "items": {
                    "type": "array",
                    "items": {"type": "number"},
                },
            }
        },
        "required": ["coordinates"],
    },
}

message = "Generate a JSON of three random coordinates."
```
Example output:
```mdx wordWrap
{
    "coordinates": [
        [-31.28333, 146.41667],
        [78.95833, 11.93333],
        [44.41667, -75.68333]
    ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
