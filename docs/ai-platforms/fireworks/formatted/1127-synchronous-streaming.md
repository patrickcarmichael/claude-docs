---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Synchronous streaming

for chunk in llm.completions.create(
    prompt="Tell me a story",
    stream=True
):
    if chunk.choices[0].text:
        print(chunk.choices[0].text, end="")

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
