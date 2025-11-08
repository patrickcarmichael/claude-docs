---
title: "Langgraph: Agent architectures"
description: "Agent architectures section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Agent architectures


Many LLM applications implement a particular control flow of steps before and / or after LLM calls. As an example, [RAG](https://github.com/langchain-ai/rag-from-scratch) performs retrieval of documents relevant to a user question, and passes those documents to an LLM in order to ground the model's response in the provided document context. 

Instead of hard-coding a fixed control flow, we sometimes want LLM systems that can pick their own control flow to solve more complex problems! This is one definition of an [agent](https://blog.langchain.dev/what-is-an-agent/): *an agent is a system that uses an LLM to decide the control flow of an application.* There are many ways that an LLM can control application:

- An LLM can route between two potential paths
- An LLM can decide which of many tools to call
- An LLM can decide whether the generated answer is sufficient or more work is needed

As a result, there are many different types of [agent architectures](https://blog.langchain.dev/what-is-a-cognitive-architecture/), which give an LLM varying levels of control. 

![Agent Types](img/agent_types.png)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← search for "memories" within this namespace, filtering on content equivalence, sorted by vector similarity](./346-search-for-memories-within-this-namespace-filterin.md)

**Next:** [Router →](./348-router.md)
