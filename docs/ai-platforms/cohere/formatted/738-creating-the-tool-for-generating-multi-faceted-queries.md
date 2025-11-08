---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Creating the tool for generating multi-faceted queries

With the `search_code_examples` modified, we now need to modify the tool definition as well. Here, we are adding the two new properties to the tool definition:

* `programming_language`: This is a string property which we provide a list of options for the model to choose from. We do this by adding "Possible enum values" to the description, which in our case is `py, js`.
* `endpoints`: We want the model to be able to choose from more than one endpoint, and so here we define an array property. When defining an array property, we need to specify the type of the items in the array using the `items` key, which in our case is `string`. We also provide a list of endpoint options for the model to choose from, which is `chat, embed, rerank, classify`.

We make only the `query` parameter required, while the other two parameters are optional.
```python PYTHON
tools = [search_code_examples_detailed_tool]
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
