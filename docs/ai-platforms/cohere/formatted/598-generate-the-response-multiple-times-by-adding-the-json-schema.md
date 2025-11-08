---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Generate the response multiple times by adding the JSON schema

response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            "required": ["title", "category", "status"],
            "properties": {
                "title": {"type": "string"},
                "category": {
                    "type": "string",
                    "enum": ["access", "software"],
                },
                "status": {
                    "type": "string",
                    "enum": ["open", "closed"],
                },
            },
        },
    },
)

json_object = json.loads(response.message.content[0].text)

print(json_object)
```
```
{'title': 'Unable to Access Server', 'category': 'access', 'status': 'open'}
```
Further reading:

* [Documentation on Structured Outputs](https://docs.cohere.com/docs/structured-outputs)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
