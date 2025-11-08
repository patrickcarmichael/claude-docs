---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Basic types

### String

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
        },
        "required": ["title", "author"],
    },
}

message = "Generate a JSON describing a book, with the fields 'title' and 'author'"
```
Example output:
```mdx wordWrap
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald"
}
```

### Integer

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "publication_year": {"type": "integer"},
        },
        "required": ["title", "author", "publication_year"],
    },
}

message = "Generate a JSON describing a book, with the fields 'title', 'author' and 'publication_year'"
```
Example output:
```mdx wordWrap
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publication_year": 1925
}
```

### Float

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "temperature": {"type": "number"},
        },
        "required": ["city", "temperature"],
    },
}

message = "Generate a JSON of a city and its average daily temperature in celcius"
```
Example output:
```mdx wordWrap
{
  "city": "Toronto",
  "temperature": 15.6
}
```

### Boolean

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {"type": "string"},
            "is_capital": {"type": "boolean"},
        },
        "required": ["city", "is_capital"],
    },
}

message = "Generate a JSON about a city in Spain and whether it is the capital of its country using 'is_capital'."
```
Example output:
```mdx wordWrap
{
    "city": "Madrid",
    "is_capital": true
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
