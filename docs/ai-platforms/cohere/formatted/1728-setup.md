---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Setup

First, let's import the necessary libraries.
```python PYTHON
%pip install -U cohere pydantic-ai
```
```python PYTHON
import requests
import cohere
import pandas as pd
from pydantic_ai import Agent
from pydantic_ai.models import KnownModelName
from collections import Counter

import os
co = cohere.ClientV2(os.getenv("COHERE_API_KEY"))
```
```python PYTHON
import nest_asyncio
nest_asyncio.apply()
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
