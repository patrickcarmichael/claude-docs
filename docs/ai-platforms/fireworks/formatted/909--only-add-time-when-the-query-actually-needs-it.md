---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ✅ Only add time when the query actually needs it

def build_prompt(user_query, system_base):
    prompt = system_base
    
    # Only add timestamp for time-sensitive queries

    time_keywords = ['today', 'now', 'current', 'latest', 'recent']
    if any(keyword in user_query.lower() for keyword in time_keywords):
        prompt += f"\nCurrent time: {datetime.now().isoformat()}"
    
    prompt += f"\nUser: {user_query}"
    return prompt
```
**Option 3: Move time to user message**
```python
from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
