---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Cohere and LangChain (Integration Guide)

> Integrate Cohere with LangChain for advanced chat features, RAG, embeddings, and reranking; this guide includes code examples for each feature.

Cohere [has first class support for LangChain](https://python.langchain.com/docs/integrations/providers/cohere), a framework which enables you to quickly create LLM powered applications. This doc will guide you through how to leverage different Cohere features with LangChain.

### Prerequisite

To use LangChain and Cohere you will need:

* LangChain package. To install it, run `pip install langchain`.

* LangChain Package. To install it, run:
  * `pip install langchain`
  * `pip install langchain-cohere` (to use the Cohere integrations in LangChain)
  * Optional: `pip install langchain-community` (to access third-party integrations such as web search APIs)

* Cohere's SDK. To install it, run `pip install cohere`. If you run into any issues or want more details on Cohere's SDK, [see this wiki](https://github.com/cohere-ai/cohere-python).

* A Cohere API Key. For more details on pricing [see this page](https://cohere.com/pricing). When you create an account with Cohere, we automatically create a trial API key for you. This key will be available on the dashboard where you can copy it, and it's in the dashboard section called "API Keys" as well.

### Integrating LangChain with Cohere Models

The following guides contain technical details on the many ways in which Cohere and LangChain can be used in tandem:

* [Chat on LangChain](/docs/chat-on-langchain)
* [Embed on LangChain](/docs/embed-on-langchain)
* [Rerank on LangChain](/docs/rerank-on-langchain)
* [Tools on LangChain](/docs/tools-on-langchain)


---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
