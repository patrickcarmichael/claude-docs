---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embed

These models can be used to generate embeddings from text or classify it based on various parameters. Embeddings can be used for estimating semantic similarity between two sentences, choosing a sentence which is most likely to follow another sentence, or categorizing user feedback. The Representation model comes with a variety of helper functions, such as for detecting the language of an input.

| Model Name                      | Description                                                                                                               | Modalities                                   | Dimensions                                 | Context Length | Similarity Metric                                             | Endpoints                                                             |
| ------------------------------- | ------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | ------------------------------------------ | -------------- | ------------------------------------------------------------- | --------------------------------------------------------------------- |
| `embed-v4.0`                    | A model that allows for text and images to be classified or turned into embeddings                                        | Text, Images, Mixed texts/images (i.e. PDFs) | One of '\[256, 512, 1024, 1536 (default)]' | 128k           | Cosine Similarity, Dot Product Similarity, Euclidean Distance | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-v3.0`            | A model that allows for text to be classified or turned into embeddings. English only.                                    | Text, Images                                 | 1024                                       | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-english-light-v3.0`      | A smaller, faster version of `embed-english-v3.0`. Almost as capable, but a lot faster. English only.                     | Text, Images                                 | 384                                        | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |
| `embed-multilingual-v3.0`       | Provides multilingual classification and embedding support. [See supported languages here.](/docs/supported-languages)    | Text, Images                                 | 1024                                       | 512            | Cosine Similarity                                             | [Embed](/reference/embed), [Embed Jobs](/reference/embed-jobs)        |
| `embed-multilingual-light-v3.0` | A smaller, faster version of `embed-multilingual-v3.0`. Almost as capable, but a lot faster. Supports multiple languages. | Text, Images                                 | 384                                        | 512            | Cosine Similarity                                             | [Embed](/reference/embed),  <br />[Embed Jobs](/reference/embed-jobs) |

### Using Embed Models on Different Platforms

In this table, we provide some important context for using Cohere Embed models on Amazon Bedrock, Amazon SageMaker, and more.

| Model Name                      | Amazon Bedrock Model ID        | Amazon SageMaker      | Azure AI Foundry        | Oracle OCI Generative AI Service                                                                             |
| :------------------------------ | :----------------------------- | :-------------------- | :---------------------- | :----------------------------------------------------------------------------------------------------------- |
| `embed-v4.0`                    | (Coming Soon)                  | Unique per deployment | `cohere-embed-v-4-plan` | (Coming Soon)                                                                                                |
| `embed-english-v3.0`            | `cohere.embed-english-v3`      | Unique per deployment | Unique per deployment   | `cohere.embed-english-image-v3.0` (for images), `cohere.embed-english-v3.0` (for text)                       |
| `embed-english-light-v3.0`      | N/A                            | Unique per deployment | N/A                     | `cohere.embed-english-light-image-v3.0` (for images), `cohere.embed-english-light-v3.0` (for text)           |
| `embed-multilingual-v3.0`       | `cohere.embed-multilingual-v3` | Unique per deployment | Unique per deployment   | `cohere.embed-multilingual-image-v3.0` (for images), `cohere.embed-multilingual-v3.0` (for text)             |
| `embed-multilingual-light-v3.0` | N/A                            | Unique per deployment | N/A                     | `cohere.embed-multilingual-light-image-v3.0` (for images), `cohere.embed-multilingual-light-v3.0` (for text) |
| `embed-english-v2.0`            | N/A                            | Unique per deployment | N/A                     | N/A                                                                                                          |
| `embed-english-light-v2.0`      | N/A                            | Unique per deployment | N/A                     | `cohere.embed-english-light-v2.0`                                                                            |
| `embed-multilingual-v2.0`       | N/A                            | Unique per deployment | N/A                     | N/A                                                                                                          |

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
