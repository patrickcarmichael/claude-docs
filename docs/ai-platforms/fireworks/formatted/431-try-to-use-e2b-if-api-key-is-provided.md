---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Try to use E2B if API key is provided

api_key = os.environ.get("E2B_API_KEY")

if api_key:
    result = e2b_code_execution_reward(
        messages=messages,
        expected_output=expected_output,
        language="python",
        api_key=api_key
    )
else:
    # Fall back to local execution

    result = local_code_execution_reward(
        messages=messages,
        expected_output=expected_output,
        language="python"
    )
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
