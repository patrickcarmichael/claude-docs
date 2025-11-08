---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Multi-Step Tool Use with Cohere

> This page describes how to create a multi-step, tool-using AI agent with Cohere's tool use functionality.

<CookbookHeader href="https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/agents/Vanilla_Multi_Step_Tool_Use.ipynb" />

Tool use allows developers to connect Cohere's models to external tools like search engines, APIs, functions, databases, etc.

Multi-step tool use is an extension of this basic idea, and allows the model to call more than one tool in a sequence of steps, using the results from one tool call in a subsequent step. This process allows the language model to reason, perform dynamic actions, and quickly adapt on the basis of information coming from external sources.

The recommended way to achieve [multi-step tool use with Cohere](https://docs.cohere.com/docs/multi-step-tool-use) is by leveraging the [Langchain framework](https://python.langchain.com/docs/integrations/providers/cohere#react-agent) in Python.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
