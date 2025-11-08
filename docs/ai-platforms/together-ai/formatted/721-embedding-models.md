---
title: "Together AI Documentation"
description: "Formatted documentation for Together AI"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Embedding Models

To embed text with Together AI models using the Vercel AI SDK, use the `.textEmbedding()` factory method.
For more on embedding models with the AI SDK see [embed()](/docs/reference/ai-sdk-core/embed).
```js
import { createTogetherAI } from '@ai-sdk/togetherai';
import { embed } from 'ai';

const togetherai = createTogetherAI({
  apiKey: process.env.TOGETHER_API_KEY ?? '',
});

const { embedding } = await embed({
  model: togetherai.textEmbedding('togethercomputer/m2-bert-80M-2k-retrieval'),
  value: 'sunny day at the beach',
});
```
>   **📝 Note**
>
> For a complete list of available embedding models and their model IDs, see the [Together.ai models
  page](https://docs.together.ai/docs/serverless-models#embedding-models).

Some available model IDs include:

* `BAAI/bge-large-en-v1.5`
* `BAAI/bge-base-en-v1.5`
* `Alibaba-NLP/gte-modernbert-base`
* `intfloat/multilingual-e5-large-instruct`

***


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
