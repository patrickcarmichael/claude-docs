---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Make the request

response = client.chat.completions.create(
    model="accounts/fireworks/models/deepseek-v3p1",
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "Result",
            "schema": Result.model_json_schema()
        }
    },
    messages=[{
        "role": "user",
        "content": "Who won the US presidential election in 2012? Reply in JSON format."
    }]
)

print(response.choices[0].message.content)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
