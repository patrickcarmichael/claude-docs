---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Conversation with expected output in the prompt

messages = [
    {
        "role": "user",
        "content": "Write a Python function to find the sum of a list. Expected output: 15 (for [1,2,3,4,5])"
    },
    {
        "role": "assistant",
        "content": """```python
def sum_list(numbers):
    return sum(numbers)

print(sum_list([1, 2, 3, 4, 5]))
```"""
    }
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
