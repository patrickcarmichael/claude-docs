---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Defining the function for data querying

We'll remove the other tools from Part 1 and just use one – `search_code_examples`.

Now, instead of just the `query` parameter, we'll add two more parameters: `programming_language` and `endpoints`:

* `programming_language`: The programming language of the code example or tutorial.
* `endpoints`: The Cohere endpoints used in the code example or tutorial.

We'll use these parameters as the metadata to filter the code examples and tutorials.

Let's rename the function to `search_code_examples_detailed` to reflect this change.

And as in Part 1, for simplicity, we create `query` as just a mock parameter and no actual search logic will be performed based on it.

**IMPORTANT:**

The source code for tool definitions can be [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py). Make sure to have the `tool_def.py` file in the same directory as this notebook for the imports to work correctly.
```python PYTHON
from tool_def import (
    search_code_examples_detailed,
    search_code_examples_detailed_tool,
)
```
```python PYTHON
functions_map = {
    "search_code_examples_detailed": search_code_examples_detailed,
}
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
