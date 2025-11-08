---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere's Embed Models (Details and Application)

> Explore Embed models for text classification and embedding generation in English and multiple languages, with details on dimensions and endpoints.

Embed models can be used to generate embeddings from text or classify it based on various parameters. Embeddings can be used for estimating semantic similarity between two texts, choosing a sentence which is most likely to follow another sentence, or categorizing user feedback. When used with the Classify endpoint, embeddings can be used for any classification or analysis task.

| Latest Model                    | Description                                                                                                                                            | Modality                                     | Dimensions                                 | Max Tokens (Context Length) | Similarity Metric                                             | Endpoints                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------- | ------------------------------------------ | --------------------------- | ------------------------------------------------------------- | --------------------------------------------------------------------- |
| `embed-v4.0`                    | A model that allows for text and images to be classified or turned into embeddings                                                                     | Text, Images, Mixed texts/images (i.e. PDFs) | One of '\[256, 512, 1024, 1536 (default)]' | 128k                        | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed)                                             |
| `embed-english-v3.0`            | A model that allows for text to be classified or turned into embeddings. English only.                                                                 | Text, Images                                 | 1024                                       | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-light-v3.0`      | A smaller, faster version of `embed-english-v3.0`. Almost as capable, but a lot faster. English only.                                                  | Text, Images                                 | 384                                        | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-multilingual-v3.0`       | Provides multilingual classification and embedding support. [See supported languages here.](/docs/supported-languages)                                 | Text, Images                                 | 1024                                       | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed), [Embed Jobs](/reference/embed-jobs)        |
| `embed-multilingual-light-v3.0` | A smaller, faster version of `embed-multilingual-v3.0`. Almost as capable, but a lot faster. [Supports multiple languages.](/docs/supported-languages) | Text, Images                                 | 384                                        | 512                         | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
