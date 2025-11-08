---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Force JSON object response format

> Generate outputs in JSON objects with the new 'response_format' parameter, now available with the 'command-nightly' model.

Users can now force `command-nightly`to generate outputs in JSON objects by setting the `response_format` parameter in the Chat API. Users can also specify a JSON schema for the output.

This feature is available across all of Cohere's SDKs (Python, Typescript, Java, Go).

Example request for forcing JSON response format:
```Text cURL
POST https://api.cohere.ai/v1/chat
{
    "message": "Generate a JSON that represents a person, with name and age",
    "model": "command-nightly",
    "response_format": {
        "type": "json_object"
    }
}
```
<br />

Example request for forcing JSON response format in user defined schema:
```Text cURL
POST https://api.cohere.ai/v1/chat
{
    "message": "Generate a JSON that represents a person, with name and age",
    "model": "command-nightly",
    "response_format": {
        "type": "json_object",
        "schema": {
            "type": "object",
            "required": ["name", "age"],
            "properties": {
                "name": { "type": "string" },
                "age": { "type": "integer" }
            }
        }
    }
}
```javascript
Currently only compatible with \`command-nightly model.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
