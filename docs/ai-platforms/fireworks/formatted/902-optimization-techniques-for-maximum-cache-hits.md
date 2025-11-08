---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Optimization techniques for maximum cache hits

Due to the autoregressive nature of LLMs, even a single-token difference can invalidate the cache from that token onward. Here are key strategies to maximize your cache hit rates:

### Keep your prompt prefix stable

The most critical rule for effective prompt caching is maintaining a stable prefix. Any change to the beginning of your prompt will invalidate the entire cache chain that follows.

>   **⚠️ Warning**
>
>   **Common mistake:** Including timestamps or other dynamic content at the beginning of your system prompt.
```python
  # ❌ DON'T: This kills cache hit rates

  system_prompt = f"""
  Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
  You are a helpful AI assistant...
  """
```
  Even a one-second difference in the timestamp will invalidate the entire cache, making it completely ineffective.

### Structure prompts for caching success

**✅ DO:** Place static content first, dynamic content last
```python
from fireworks import LLM

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
