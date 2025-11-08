---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## ✅ Round to larger intervals to increase cache hits

current_hour = datetime.now().replace(minute=0, second=0, microsecond=0)
system_prompt = f"""
You are a helpful assistant.
Current hour: {current_hour.strftime('%Y-%m-%d %H:00')}
...
"""
```
**Option 2: Conditional time injection**
```python

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
