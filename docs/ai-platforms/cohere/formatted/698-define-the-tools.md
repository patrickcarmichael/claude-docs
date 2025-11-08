---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Define the tools

tools = [
    {
        "type": "function",
        "function": {
            "name": "search_faqs",
            "description": "Given a user query, searches a company's frequently asked questions (FAQs) list and returns the most relevant matches to the query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query from the user",
                    }
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_emails",
            "description": "Given a user query, searches a person's emails and returns the most relevant matches to the query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query from the user",
                    }
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "Creates a new calendar event of the specified duration at the specified time and date. A new event cannot be created on the same time as an existing event.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "the date on which the event starts, formatted as mm/dd/yy",
                    },
                    "time": {
                        "type": "string",
                        "description": "the time of the event, formatted using 24h military time formatting",
                    },
                    "duration": {
                        "type": "number",
                        "description": "the number of hours the event lasts for",
                    },
                },
                "required": ["date", "time", "duration"],
            },
        },
    },
]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
