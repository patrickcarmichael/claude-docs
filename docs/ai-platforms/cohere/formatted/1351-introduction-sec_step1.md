---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Introduction \[#sec\_step1]

The aim of this notebook is to showcase how Cohere Langchain Agents can be used to answer questions over tabular data.
This notebook assumes the input is a set of csv files extracted from Apple's SEC 10K filings.

### Data Loading

We use the sec-api to download the income statement and balance sheet from the SEC 10K .htm file. Please note that the tables need to be parsed such that the index is numerical as the python code generation struggles to filter based on index. We have processed the tables and provided them for you. They can be found [here](https://github.com/cohere-ai/cohere-developer-experience/tree/main/notebooks/agents/financial-csv-agent).
```python PYTHON
income_statement = pd.read_csv('income_statement.csv')
balance_sheet = pd.read_csv('balance_sheet.csv')
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
