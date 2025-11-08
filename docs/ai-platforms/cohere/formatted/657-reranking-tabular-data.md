---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Reranking tabular data

Many enterprises rely on tabular data, such as relational databases, CSVs, and Excel. To perform reranking, you can transform a dataframe into a list of JSON records and use Rerank 3's JSON capabilities to rank them. We follow the same steps in the previous example, where we convert the data into YAML format before passing it to the Rerank endpoint.

Here's an example of reranking a CSV file that contains employee information.
```python PYTHON
import pandas as pd
from io import StringIO

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
