---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## finally, let's write a function to convert the Agents output to a json

def convert_to_json(string: str) -> json:
    return json.loads(
                string.replace("\xa0", " ")
                .replace("json", "")
                .replace("`", "")
                .replace("`", "")
            )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
