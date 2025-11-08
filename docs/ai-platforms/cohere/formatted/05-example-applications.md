---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example Applications

Try [the playground](https://dashboard.cohere.com/playground) to see what an LLM-powered conversational agent can look like. It is able to converse, summarize text, and write emails and articles.

<img src="file:ae2c54eb-7e06-4587-83ff-1baf15bbb8ff" />

Our goal, however, is to enable you to build your own LLM-powered applications. The [Chat endpoint](/docs/chat-api), for example, can be used to build a conversational agent powered by the Command family of models.

<img src="file:190c8a21-ae98-40af-9cc6-e1e814043d5c" alt="A diagram of a conversational agent." />

### Retrieval-Augmented Generation (RAG)

“Grounding” refers to the practice of allowing an LLM to access external data sources – like the internet or a company’s internal technical documentation – which leads to better, more factual generations.

Chat is being used with grounding enabled in the screenshot below, and you can see how accurate and information-dense its reply is.

<img src="file:1a0b5f30-bae0-4d4e-b369-4edbc74d1d23" />

What’s more, advanced RAG capabilities allow you to see what underlying query the model generates when completing its tasks, and its output includes [citations](/docs/documents-and-citations) pointing you to where it found the information it uses. Both the query and the citations can be leveraged alongside the Cohere Embed and Rerank models to build a remarkably powerful RAG system, such as the one found in [this guide](https://cohere.com/llmu/rag-chatbot).

<img src="file:b0b67642-d519-4cec-bf98-1bde60f2adcc" />

[Click here](/docs/serving-platform) to learn more about the Cohere serving platform.

### Advanced Search & Retrieval

Embeddings enable you to search based on what a phrase *means* rather than simply what keywords it *contains*, leading to search systems that incorporate context and user intent better than anything that has come before.

<img src="file:19f1d300-01fe-4315-b15e-4a1b276012b4" alt="How a query returns results." />

Learn more about semantic search [here](https://cohere.com/llmu/what-is-semantic-search).

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
