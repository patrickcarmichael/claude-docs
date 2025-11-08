---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Content quality measure with Embed v4

A standard text embeddings model is optimized for only topic similarity between a query and candidate documents. But in many real-world applications, you have redundant information with varying content quality.

For instance, consider a user query of “COVID-19 Symptoms” and compare that to candidate document, “COVID-19 has many symptoms”. This document does not offer high-quality and rich information. However, with a typical embedding model, it will appear high on search results because it is highly similar to the query.

The Embed v4 model is trained to capture both content quality and topic similarity. Through this approach, a search system can extract richer information from documents and is robust against noise.

As an example below, give a query ("COVID-19 Symptoms"), the document with the highest quality ("COVID-19 symptoms can include: a high temperature or shivering...") is ranked first.

Another document ("COVID-19 has many symptoms") is arguably more similar to the query based on what information it contains, yet it is ranked lower as it doesn’t contain that much information.

This demonstrates how Embed v4 helps to surface high-quality documents for a given query.
```python PYTHON

### STEP 1: Embed the documents

documents = [
    "COVID-19 has many symptoms.",
    "COVID-19 symptoms are bad.",
    "COVID-19 symptoms are not nice",
    "COVID-19 symptoms are bad. 5G capabilities include more expansive service coverage, a higher number of available connections, and lower power consumption.",
    "COVID-19 is a disease caused by a virus. The most common symptoms are fever, chills, and sore throat, but there are a range of others.",
    "COVID-19 symptoms can include: a high temperature or shivering (chills); a new, continuous cough; a loss or change to your sense of smell or taste; and many more",
    "Dementia has the following symptom: Experiencing memory loss, poor judgment, and confusion.",
    "COVID-19 has the following symptom: Experiencing memory loss, poor judgment, and confusion.",
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
