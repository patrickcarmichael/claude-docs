---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Unlocking the Power of Multimodal Embeddings

> Multimodal embeddings convert text and images into embeddings for search and classification (API v2).

<img src="file:7e36b26c-4bca-4a04-b751-977fb8ccd384" alt="embeddings." />

<Note title="This Guide Uses the Embed API.">
  You can find the API reference for the api [here](/reference/embed)

  Image capabilities are only compatible with `v4.0` and `v3.0` models, but `v4.0` has features that `v3.0` does not have. Consult the embedding [documentation](https://docs.cohere.com/docs/cohere-embed) for more details.
</Note>

In this guide, we show you how to use the embed endpoint to embed a series of images. This guide uses a simple dataset of graphs to illustrate how semantic search can be done over images with Cohere. To see an end-to-end example of retrieval, check out this [notebook](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/Multimodal_Semantic_Search.ipynb).

### Introduction to Multimodal Embeddings

Information is often represented in multiple modalities. A document, for instance, may contain text, images, and graphs, while a product can be described through images, its title, and a written description. This combination of elements often leads to a comprehensive semantic understanding of the subject matter. Traditional embedding models have been limited to a single modality, and even multimodal embedding models often suffer from degradation in `text-to-text` or `text-to-image` retrieval tasks. `embed-v4.0` and the `embed-v3.0` series of models, however, are fully multimodal, enabling them to embed both images and text effectively. We have achieved state-of-the-art performance without compromising text-to-text retrieval capabilities.

### How to use Multimodal Embeddings

#### 1. Prepare your Image for Embeddings

```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
