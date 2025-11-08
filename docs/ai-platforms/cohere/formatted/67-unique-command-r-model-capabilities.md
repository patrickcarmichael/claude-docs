---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Unique Command R Model Capabilities

Command R has been trained on a massive corpus of diverse texts in multiple languages, and can perform a wide array of text-generation tasks. Moreover, Command R has been trained with a particular focus on excelling in some of the most critical business use-cases.

### Multilingual Capabilities

We want Command R to serve as many people, organizations, and markets as possible, so the new Command R is capable of interacting in many languages to a fairly high degree of accuracy.

The model is optimized to perform well in the following languages: English, French, Spanish, Italian, German, Brazilian Portuguese, Japanese, Korean, Simplified Chinese, and Arabic.

Additionally, pre-training data has been included for the following 13 languages: Russian, Polish, Turkish, Vietnamese, Dutch, Czech, Indonesian, Ukrainian, Romanian, Greek, Hindi, Hebrew, Persian.

The model has been trained to respond in the language of the user. Here's an example:

*Prompt*
```Text
Écris une description de produit pour une voiture électrique en 50 à 75 mots
```
*Generation*
```text TEXT
Découvrez la voiture électrique qui va révolutionner votre façon de conduire.
Avec son design élégant, cette voiture offre une expérience de conduite unique
avec une accélération puissante et une autonomie impressionnante. Sa
technologie avancée vous garantit une charge rapide et une fiabilité inégalée.
Avec sa conception innovante et durable, cette voiture est parfaite pour les 
trajets urbains et les longues distances. Profitez d'une conduite silencieuse
et vivez l'expérience de la voiture électrique!
```
Command R can not only be used to generate text in several languages but can also perform cross-lingual tasks such as translation or answering questions about content in other languages.

### Retrieval Augmented Generation

Command R has been trained with the ability to ground its generations. This means that it can generate responses based on a list of supplied document snippets, and it will include citations in its response indicating the source of the information.

For more information, check out our dedicated guide on [retrieval augmented generation](/docs/retrieval-augmented-generation-rag).

### Tool Use

Command R has been trained with conversational tool use capabilities. This functionality takes a conversation as input (with an optional user-system preamble), along with a list of available tools. The model will then generate a json-formatted list of actions to execute on a subset of those tools. For more information, check out our dedicated [tool use](/docs/tool-use) guide.


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
