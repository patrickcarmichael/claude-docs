---
title: "Langgraph: Build multi-agent systems"
description: "Build multi-agent systems section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# Build multi-agent systems


A single agent might struggle if it needs to specialize in multiple domains or manage many tools. To tackle this, you can break your agent into smaller, independent agents and composing them into a [multi-agent system](../concepts/multi_agent.md).

In multi-agent systems, agents need to communicate between each other. They do so via [handoffs](#handoffs) — a primitive that describes which agent to hand control to and the payload to send to that agent.

This guide covers the following:

* implementing [handoffs](#handoffs) between agents
* using handoffs and the prebuilt [agent](../agents/agents.md) to [build a custom multi-agent system](#build-a-multi-agent-system)

To get started with building multi-agent systems, check out LangGraph [prebuilt implementations](#prebuilt-implementations) of two of the most popular multi-agent architectures — [supervisor](../agents/multi-agent.md#supervisor) and [swarm](../agents/multi-agent.md#swarm).

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Stream subgraph outputs](./112-stream-subgraph-outputs.md)

**Next:** [Handoffs →](./114-handoffs.md)
