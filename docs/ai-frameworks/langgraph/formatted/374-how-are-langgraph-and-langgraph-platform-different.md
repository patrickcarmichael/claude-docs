---
title: "Langgraph: How are LangGraph and LangGraph Platform different?"
description: "How are LangGraph and LangGraph Platform different? section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## How are LangGraph and LangGraph Platform different?


LangGraph is a stateful, orchestration framework that brings added control to agent workflows. LangGraph Platform is a service for deploying and scaling LangGraph applications, with an opinionated API for building agent UXs, plus an integrated developer studio.

| Features            | LangGraph (open source)                                   | LangGraph Platform                                                                                     |
| ------------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| Description         | Stateful orchestration framework for agentic applications | Scalable infrastructure for deploying LangGraph applications                                           |
| SDKs                | Python and JavaScript                                     | Python and JavaScript                                                                                  |
| HTTP APIs           | None                                                      | Yes - useful for retrieving & updating state or long-term memory, or creating a configurable assistant |
| Streaming           | Basic                                                     | Dedicated mode for token-by-token messages                                                             |
| Checkpointer        | Community contributed                                     | Supported out-of-the-box                                                                               |
| Persistence Layer   | Self-managed                                              | Managed Postgres with efficient storage                                                                |
| Deployment          | Self-managed                                              | • Cloud SaaS <br> • Free self-hosted <br> • Enterprise (paid self-hosted)                              |
| Scalability         | Self-managed                                              | Auto-scaling of task queues and servers                                                                |
| Fault-tolerance     | Self-managed                                              | Automated retries                                                                                      |
| Concurrency Control | Simple threading                                          | Supports double-texting                                                                                |
| Scheduling          | None                                                      | Cron scheduling                                                                                        |
| Monitoring          | None                                                      | Integrated with LangSmith for observability                                                            |
| IDE integration     | LangGraph Studio                                          | LangGraph Studio                                                                                       |

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Is LangGraph open source? Is it free?](./373-is-langgraph-open-source-is-it-free.md)

**Next:** [Is LangGraph Platform open source? →](./375-is-langgraph-platform-open-source.md)
