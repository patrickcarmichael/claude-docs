---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## define a tag match on the title, text match on the text field, and numeric filter on the views field

filter_data = (
    (Tag("title") == "Elizabeth II")
    & (Text("text") % "born")
    & (Num("views") > 4500)
)

query_embedding = co.embed(
    "When was she born?", input_type="search_query", as_buffer=True
)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
