---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multilingual semantic search

The Embed endpoint also supports multilingual semantic search via `embed-v4.0` and previous `embed-multilingual-...` models. This means you can perform semantic search on texts in different languages.

Specifically, you can do both multilingual and cross-lingual searches using one single model.

Specifically, you can do both multilingual and cross-lingual searches using one single model.
```python PYTHON

### STEP 1: Embed the documents

documents = [
    "Remboursement des frais de voyage : Gérez facilement vos frais de voyage en les soumettant via notre outil financier. Les approbations sont rapides et simples.",
    "Travailler de l'étranger : Il est possible de travailler à distance depuis un autre pays. Il suffit de coordonner avec votre responsable et de vous assurer d'être disponible pendant les heures de travail.",
    "Avantages pour la santé et le bien-être : Nous nous soucions de votre bien-être et proposons des adhésions à des salles de sport, des cours de yoga sur site et une assurance santé complète.",
    "Fréquence des évaluations de performance : Nous organisons des bilans informels tous les trimestres et des évaluations formelles deux fois par an.",
]

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
