---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Test a simple calculation

test_cases = [
    {
        'code': 'result = add_numbers(2, 3)',
        'expected': '5'
    },
    {
        'code': 'result = add_numbers(-1, 1)',
        'expected': '0'
    }
]

code_response = """
def add_numbers(a, b):
    return a + b
"""

score = advanced_code_evaluation(code_response, test_cases)
print(f"Code evaluation score: {score}")
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
