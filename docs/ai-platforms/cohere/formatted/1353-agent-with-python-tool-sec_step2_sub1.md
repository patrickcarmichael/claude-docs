---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Agent with Python Tool \[#sec\_step2\_sub1]

In the example below, we show how the python tool can be used to load a dataframe and extract information from it. To do this successfully we need to:

* Pass the file name to the preamble so the model knows how to load the dataframe.
* Pass a preview of the dataframe in the preamble so the model knows which columns/rows to query.

First, let's implement the ReAct agent.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
