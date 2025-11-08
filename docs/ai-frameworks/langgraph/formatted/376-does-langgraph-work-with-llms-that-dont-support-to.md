---
title: "Langgraph: Does LangGraph work with LLMs that don't support tool calling?"
description: "Does LangGraph work with LLMs that don't support tool calling? section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Does LangGraph work with LLMs that don't support tool calling?


Yes! You can use LangGraph with any LLMs. The main reason we use LLMs that support tool calling is that this is often the most convenient way to have the LLM make its decision about what to do. If your LLM does not support tool calling, you can still use it - you just need to write a bit of logic to convert the raw LLM string response to a decision about what to do.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Is LangGraph Platform open source?](./375-is-langgraph-platform-open-source.md)

**Next:** [Does LangGraph work with OSS LLMs? →](./377-does-langgraph-work-with-oss-llms.md)
