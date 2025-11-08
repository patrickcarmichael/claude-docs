---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.
```python PYTHON
! pip install cohere -qq
```
```python PYTHON
import json
import os
import cohere

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
