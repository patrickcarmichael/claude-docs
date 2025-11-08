---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Objective

In this notebook, we will guide you through best practices for setting up a RAG pipeline to process documents that contain both tables and text. We will also demonstrate how to create a [ReAct](https://python.langchain.com/v0.1/docs/modules/agents/agent_types/react/) agent with a Cohere model, and then give the agent access to a RAG pipeline tool to improve accuracy. The general structure of the notebook is as follows:

* individual components around parsing, retrieval and generation are covered for documents with mixed tabular and textual data
* a class object is created that can be used to instantiate the pipeline with parametric input
* the RAG pipeline is then used as a tool for a Cohere ReACT agent

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
