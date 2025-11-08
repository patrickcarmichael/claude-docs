---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Download dataset

For this example, we'll be using [MultiFIN](https://aclanthology.org/2023.findings-eacl.66.pdf) - an open-source dataset of financial article headlines in 15 different languages (including English, Turkish, Danish, Spanish, Polish, Greek, Finnish, Hebrew, Japanese, Hungarian, Norwegian, Russian, Italian, Icelandic, and Swedish).

We've prepared a CSV version of the MultiFIN dataset that includes an additional column containing English translations. While we won't use these translations for the model itself, they'll help us understand the results when we encounter headlines in Danish or Spanish. We'll load this CSV file into a pandas dataframe.
```python PYTHON
url = "https://raw.githubusercontent.com/cohere-ai/cohere-aws/main/notebooks/bedrock/multiFIN_train.csv"
df = pd.read_csv(url)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
