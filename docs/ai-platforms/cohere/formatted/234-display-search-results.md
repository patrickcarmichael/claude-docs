---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Display search results

for idx, docs_idx in enumerate(top_doc_idxs):
    print(f"Rank: {idx+1}")
    print(f"Document: {documents[docs_idx]}\n")
```
Here's a sample output:
```
Rank: 1
Document: Travailler de l'étranger : Il est possible de travailler à distance depuis un autre pays. Il suffit de coordonner avec votre responsable et de vous assurer d'être disponible pendant les heures de travail.

Rank: 2
Document: Avantages pour la santé et le bien-être : Nous nous soucions de votre bien-être et proposons des adhésions à des salles de sport, des cours de yoga sur site et une assurance santé complète.

Rank: 3
Document: Fréquence des évaluations de performance : Nous organisons des bilans informels tous les trimestres et des évaluations formelles deux fois par an.

Rank: 4
Document: Remboursement des frais de voyage : Gérez facilement vos frais de voyage en les soumettant via notre outil financier. Les approbations sont rapides et simples.
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
