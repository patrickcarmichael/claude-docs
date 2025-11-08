---
title: "Langgraph: Can I use LangGraph Studio without logging in to LangSmith"
description: "Can I use LangGraph Studio without logging in to LangSmith section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Can I use LangGraph Studio without logging in to LangSmith


Yes! You can use the [development version of LangGraph Server](../tutorials/langgraph-platform/local-server.md) to run the backend locally.
This will connect to the studio frontend hosted as part of LangSmith.
If you set an environment variable of `LANGSMITH_TRACING=false`, then no traces will be sent to LangSmith.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Does LangGraph work with OSS LLMs?](./377-does-langgraph-work-with-oss-llms.md)

**Next:** [What does "nodes executed" mean for LangGraph Platform usage? →](./379-what-does-nodes-executed-mean-for-langgraph-platfo.md)
