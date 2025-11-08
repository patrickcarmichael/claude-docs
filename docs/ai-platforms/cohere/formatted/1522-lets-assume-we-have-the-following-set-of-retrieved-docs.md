---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## let's assume we have the following set of retrieved docs

retrieved_docs = ['2022 Q3 AAPL.pdf', '2023 Q1 MSFT.pdf', '2023 Q1 AAPL.pdf']

print(f'Query: {query}')
print(f'Golden docs: {golden_docs}')
print(f'Retrieved docs: {retrieved_docs}')
```
```txt title="Output"
Query: How has Apple's total net sales changed over time?
Golden docs: ['2022 Q3 AAPL.pdf', '2023 Q1 AAPL.pdf', '2023 Q2 AAPL.pdf', '2023 Q3 AAPL.pdf']
Retrieved docs: ['2022 Q3 AAPL.pdf', '2023 Q1 MSFT.pdf', '2023 Q1 AAPL.pdf']
```
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
