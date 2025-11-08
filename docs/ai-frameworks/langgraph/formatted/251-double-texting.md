---
title: "Langgraph: Double Texting"
description: "Double Texting section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Double Texting


!!! info "Prerequisites"
    - [LangGraph Server](./langgraph_server.md)

Many times users might interact with your graph in unintended ways. 
For instance, a user may send one message and before the graph has finished running send a second message. 
More generally, users may invoke the graph a second time before the first run has finished.
We call this "double texting".

Currently, LangGraph only addresses this as part of [LangGraph Platform](langgraph_platform.md), not in the open source.
The reason for this is that in order to handle this we need to know how the graph is deployed, and since LangGraph Platform deals with deployment the logic needs to live there.
If you do not want to use LangGraph Platform, we describe the options we have implemented in detail below.

![](img/double_texting.png)

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Learn more](./250-learn-more.md)

**Next:** [Reject →](./252-reject.md)
