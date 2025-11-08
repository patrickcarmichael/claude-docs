---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Configure payload data sending to API endpoint

data = {
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What is good about Wuhan?"},
    ],
    "max_tokens": 500,
    "temperature": 0.3,
    "stream": "True",
}

body = str.encode(json.dumps(data))

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
