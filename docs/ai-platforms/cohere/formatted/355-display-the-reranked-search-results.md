---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display the reranked search results

print("Reranked Search Results:")
for obj in rerank_response.objects:
    title = obj.properties.get("title")
    description = obj.properties.get("description")
    rerank_score = getattr(
        obj.metadata, "rerank_score", None
    )  # Get the rerank score metadata

    print(f"Title: {title}")
    print(f"Description: {description}")
    print(f"Rerank Score: {rerank_score}")
    print("-" * 50)
```
Here's what the output looks like:
```
Reranked Search Results:
Title: Bankruptcy Law Overview
Description: Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.
Rerank Score: 0.8951567
--------------------------------------------------
Title: Tax Law for Businesses
Description: Detailed guide to tax laws affecting businesses, including corporate income tax, payroll taxes, sales and use taxes, and tax deductions. Explores tax planning strategies, such as deferring income and accelerating expenses, as well as compliance requirements and penalties for non-compliance with tax laws.
Rerank Score: 7.071895e-06
--------------------------------------------------
Title: Consumer Protection Laws
Description: Comprehensive guide to consumer protection laws, including truth in advertising, product safety, and debt collection practices. Discusses the rights of consumers under federal and state laws, such as the right to sue for damages and the right to cancel certain contracts, as well as the role of government agencies in enforcing consumer protection laws.
Rerank Score: 6.4895394e-06
--------------------------------------------------
```
Based on the rerank scores, it's clear that the Bankruptcy Law Overview is the most relevant result, while the other two documents (Tax Law for Businesses and Consumer Protection Laws) have significantly lower scores, indicating they are less relevant to the query. Therefore, we should focus only on the most relevant result and can skip the other two.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
