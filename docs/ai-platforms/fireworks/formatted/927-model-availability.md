---
title: "Fireworks Documentation"
description: "Formatted documentation for Fireworks"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Model Availability

Fireworks hosts several purpose-built embeddings models, which are optimized specifically for tasks like semantic search and document similarity comparison. We host the SOTA Qwen3 Embeddings family of models:

* `fireworks/qwen3-embedding-8b` (\*available on serverless)
* `fireworks/qwen3-embedding-4b`
* `fireworks/qwen3-embedding-0p6b`

<AccordionGroup>
  <Accordion title="Use any LLM as an embeddings model">
    You can retrieve embeddings from any LLM in our model library. Here are some examples of LLMs that work with the embeddings API:

    * `fireworks/glm-4p5`
    * `fireworks/gpt-oss-20b`
    * `fireworks/kimi-k2-instruct-0905`
    * `fireworks/deepseek-r1-0528`
  </Accordion>

  <Accordion title="Bring your own model">
    You can also retrieve embeddings from any models you bring yourself through [custom model upload](/models/uploading-custom-models).
  </Accordion>

  <Accordion title="BERT-based models (legacy)">
    These BERT-based models are available on serverless only:

    * `nomic-ai/nomic-embed-text-v1.5`
    * `nomic-ai/nomic-embed-text-v1`
    * `WhereIsAI/UAE-Large-V1`
    * `thenlper/gte-large`
    * `thenlper/gte-base`
    * `BAAI/bge-base-en-v1.5`
    * `BAAI/bge-small-en-v1.5`
    * `mixedbread-ai/mxbai-embed-large-v1`
    * `sentence-transformers/all-MiniLM-L6-v2`
    * `sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2`
  </Accordion>
</AccordionGroup>

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
