---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Start using the deployment immediately - no .apply() needed

response = llm.chat.completions.create(
    messages=[{"role": "user", "content": "Hello from my dedicated deployment!"}]
)

print(response.choices[0].message.content)
```
<Check>
  Since you're connecting to an existing deployment, you don't need to call `.apply()` - the deployment is already running and ready to serve requests.
</Check>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
