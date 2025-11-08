---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## https://huggingface.co/datasets/MongoDB/fake_tech_companies_market_reports

dataset = load_dataset(
    "MongoDB/fake_tech_companies_market_reports",
    split="train",
    streaming=True,
)
dataset_df = dataset.take(100)

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
