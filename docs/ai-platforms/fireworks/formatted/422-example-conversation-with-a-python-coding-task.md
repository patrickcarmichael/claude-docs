---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example conversation with a Python coding task

messages = [
    {
        "role": "user",
        "content": "Write a Python function to calculate the factorial of a number."
    },
    {
        "role": "assistant",
        "content": """Here's a Python function to calculate the factorial of a number:
```python
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
