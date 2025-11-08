---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Building a Generative AI Agent with Cohere

> This page describes building a generative-AI powered agent with Cohere.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt7_v2.ipynb">
  Open in Colab
</a>

Tool use extends the ideas from [RAG](/v2/docs/rag-with-cohere), where external systems are used to guide the response of an LLM, but by leveraging a much bigger set of tools than what’s possible with RAG. The concept of tool use leverages LLMs' useful feature of being able to act as a reasoning and decision-making engine.

While RAG enables applications that can *answer questions*, tool use enables those that can *automate tasks*.

Tool use also enables developers to build agentic applications that can take actions, that is, doing both read and write operations on an external system.

In this tutorial, you'll learn about:

* Creating tools
* Tool planning and calling
* Tool execution
* Response and citation generation
* Multi-step tool use

You'll learn these by building an onboarding assistant for new hires.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
