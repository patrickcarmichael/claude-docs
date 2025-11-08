---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## How to Start with the Cohere Toolkit

> Build and deploy RAG applications quickly with the Cohere Toolkit, which offers pre-built front-end and back-end components.

[Cohere Toolkit](https://github.com/cohere-ai/cohere-toolkit) is a collection of pre-built components enabling developers to quickly build and deploy [retrieval augmented generation](/docs/retrieval-augmented-generation-rag) (RAG) applications. With it, you can cut time-to-launch down from months to weeks, and deploy in as little as a few minutes.

The pre-built components fall into two big categories: front-end and back end.

* **Front-end**: The Cohere Toolkit front end is a web application built in Next.js. It includes a simple SQL database out of the box to store conversation history, documents, and citations, directly in the app.
* **Back-end**: The Cohere Toolkit back-end contains the preconfigured data sources and retrieval code needed to set up RAG on custom data sources, which are called "retrieval chains"). Users can also configure which model to use, selecting from Cohere models hosted on our native platform, Azure, or AWS Sagemaker. By default, we have configured a Langchain data retriever to test RAG on Wikipedia and your own uploaded documents.

Here's an image that shows how these different components work together:

<img src="file:675a981f-50fb-41e8-833a-5cde990ba811" />

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
