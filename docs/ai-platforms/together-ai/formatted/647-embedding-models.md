---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embedding models

| Model Name                     | Model String for API                       | Model Size | Embedding Dimension | Context Window |
| :----------------------------- | ------------------------------------------ | :--------- | :------------------ | :------------- |
| M2-BERT-80M-32K-Retrieval      | togethercomputer/m2-bert-80M-32k-retrieval | 80M        | 768                 | 32768          |
| BGE-Large-EN-v1.5              | BAAI/bge-large-en-v1.5                     | 326M       | 1024                | 512            |
| BGE-Base-EN-v1.5               | BAAI/bge-base-en-v1.5                      | 102M       | 768                 | 512            |
| GTE-Modernbert-base            | Alibaba-NLP/gte-modernbert-base            | 149M       | 768                 | 8192           |
| Multilingual-e5-large-instruct | intfloat/multilingual-e5-large-instruct    | 560M       | 1024                | 514            |

**Embedding Model Examples**

* [Contextual RAG](https://docs.together.ai/docs/how-to-implement-contextual-rag-from-anthropic) - An open source implementation of contextual RAG by Anthropic
* [Code Generation Agent](https://github.com/togethercomputer/together-cookbook/blob/main/Agents/Looping_Agent_Workflow.ipynb) - An agent workflow to generate and iteratively improve code
* [Multimodal Search and Image Generation](https://github.com/togethercomputer/together-cookbook/blob/main/Multimodal_Search_and_Conditional_Image_Generation.ipynb) - Search for images and generate more similar ones
* [Visualizing Embeddings](https://github.com/togethercomputer/together-cookbook/blob/main/Embedding_Visualization.ipynb) - Visualizing and clustering vector embeddings

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
