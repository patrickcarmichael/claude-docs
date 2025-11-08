---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Call the reward function

result = reward_fn(messages=[
    {"role": "user", "content": "Hello"},
    {"role": "assistant", "content": "Hi there! How can I help you today?"}
])

print(f"Score: {result.score}")
```

### Remote Mode

```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
