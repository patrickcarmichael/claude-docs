---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Iterate over the retrieved objects and print their details

for obj in response.objects:
    title = obj.properties.get("title")
    description = obj.properties.get("description")
    metadata_distance = obj.metadata.distance
    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Metadata Distance: {metadata_distance}")
    print("-" * 50)
```
The output will look something like this:
```
Semantic Search
**************************************************
Title: Bankruptcy Law Overview
Description: Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.
Metadata Distance: 0.41729819774627686
--------------------------------------------------
Title: Tax Law for Businesses
Description: Detailed guide to tax laws affecting businesses, including corporate income tax, payroll taxes, sales and use taxes, and tax deductions. Explores tax planning strategies, such as deferring income and accelerating expenses, as well as compliance requirements and penalties for non-compliance with tax laws.
Metadata Distance: 0.6903179883956909
--------------------------------------------------
Title: Consumer Protection Laws
Description: Comprehensive guide to consumer protection laws, including truth in advertising, product safety, and debt collection practices. Discusses the rights of consumers under federal and state laws, such as the right to sue for damages and the right to cancel certain contracts, as well as the role of government agencies in enforcing consumer protection laws.
Metadata Distance: 0.7075160145759583
--------------------------------------------------
```
This code sets up Rerank infrastructure:
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
