---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Others

### Nested objects

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "actions": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "japanese": {"type": "string"},
                        "romaji": {"type": "string"},
                        "english": {"type": "string"},
                    },
                    "required": ["japanese", "romaji", "english"],
                },
            }
        },
        "required": ["actions"],
    },
}

message = "Generate a JSON array of 3 objects with the following fields: japanese, romaji, english. These actions should be japanese verbs provided in the dictionary form."
```
Example output:
```mdx wordWrap
{
    "actions": [
        {
            "japanese": "食べる",
            "romaji": "taberu",
            "english": "to eat"
        },
        {
            "japanese": "話す",
            "romaji": "hanasu",
            "english": "to speak"
        },
        {
            "japanese": "書く",
            "romaji": "kaku",
            "english": "to write"
        }
    ]
}
```

### Enums

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "genre": {
                "type": "string",
                "enum": ["historical fiction", "cozy mystery"],
            },
            "title": {"type": "string"},
        },
        "required": ["title", "genre"],
    },
}

message = "Generate a JSON for a new book idea."
```
Example output:
```mdx wordWrap
{
  "genre": "historical fiction",
  "title": "The Unseen Thread: A Tale of the Silk Road's Secrets and Shadows"
 }
```

### Const

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "city": {
                "type": "object",
                "properties": {
                    "country": {
                        "type": "string",
                        "const": "Thailand",
                    },
                    "city_name": {"type": "string"},
                    "avg_temperature": {"type": "number"},
                },
                "required": [
                    "country",
                    "city_name",
                    "avg_temperature",
                ],
            }
        },
        "required": ["city"],
    },
}

message = "Generate a JSON of a city."
```
Example output:
```mdx wordWrap
{
  "city": {
    "country": "Thailand",
    "city_name": "Bangkok",
    "avg_temperature": 29.083333333333332
  }
}
```

### Pattern

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "product_sku": {
                "type": "string",
                "pattern": "[A-Z]{3}[0-9]{7}",
            }
        },
        "required": ["product_sku"],
    },
}

message = "Generate a JSON of an SKU for a new product line."
```
Example output:
```mdx wordWrap
{
  "product_sku": "PRX0012345"
}
```

### Format

```python PYTHON
response_format = {
    "type": "json_object",
    "schema": {
        "type": "object",
        "properties": {
            "itinerary": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "day_number": {"type": "integer"},
                        "date": {"type": "string", "format": "date"},
                        "places_to_visit": {"type": "string"},
                    },
                    "required": [
                        "day_number",
                        "date",
                        "places_to_visit",
                    ],
                },
            }
        },
        "required": ["itinerary"],
    },
}

message = (
    "Generate a JSON of a 3-day visit of Bali starting Jan 5 2025."
)
```
Example output:
```mdx wordWrap
{
  "itinerary": [
    {
      "day_number": 1,
      "date": "2025-01-05",
      "places_to_visit":  "Tanah Lot Temple, Ubud Monkey Forest, Tegalalang Rice Terraces"
    },
    {
      "day_number": 2,
      "date": "2025-01-06",
      "places_to_visit": "Mount Batur, Tirta Empul Temple, Ubud Art Market"
    },
    {
      "day_number": 3,
      "date": "2025-01-07",
      "places_to_visit": "Uluwatu Temple, Kuta Beach, Seminyak"
    }
  ]
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
