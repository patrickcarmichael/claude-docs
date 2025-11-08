---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## The example below generates outputs for each of the n search results, where n is specified by the limit parameter.

collection = client.collections.get("Legal_Docs_RAG")
response = collection.generate.near_text(
    query=search_query,
    limit=1,
    single_prompt="Translate this into French -  {title}: {description}",
)

for obj in response.objects:
    print("Retrieved results")
    print("-----------------")
    print(obj.properties["title"])
    print(obj.properties["description"])
    print("Generated output")
    print("-----------------")
    print(obj.generated)
```
You'll see something like this:
```
Retrieved results
-----------------
Bankruptcy Law Overview
Comprehensive introduction to bankruptcy law, including Chapter 7 and Chapter 13 bankruptcy proceedings. Discusses the eligibility requirements for filing bankruptcy, the process of liquidating assets and discharging debts, and the impact of bankruptcy on credit scores and future financial opportunities.
Generated output
-----------------
Voici une traduction possible :

Aperçu du droit des faillites : Introduction complète au droit des faillites, y compris les procédures de faillite en vertu des chapitres 7 et 13. Discute des conditions d'admissibilité pour déposer une demande de faillite, du processus de liquidation des actifs et de libération des dettes, ainsi que de l'impact de la faillite sur les cotes de crédit et les opportunités financières futures.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
