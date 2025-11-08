---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## **Step 4: Make a RAG request to Command using document mode**

Now that we have our nicely formatted chunks from the 10-K, we can pass them directly into Command using the Cohere SDK. By passing the chunks into the `documents` kwarg, we enable document mode, which will perform grounded inference on the documents you pass in.

You can see this for yourself by inspecting the `response.citations` field to check where the model is citing from.

You can learn more about the `chat` endpoint by checking out the API reference [here](https://docs.cohere.com/reference/chat).
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
