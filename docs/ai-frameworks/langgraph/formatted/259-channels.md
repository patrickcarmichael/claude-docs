---
title: "Langgraph: Channels"
description: "Channels section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Channels


Channels are used to communicate between actors (PregelNodes). Each channel has a value type, an update type, and an update function – which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step. LangGraph provides a number of built-in channels:

- [LastValue](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue): The default channel, stores the last value sent to the channel, useful for input and output values, or for sending data from one step to the next.
- [Topic](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic): A configurable PubSub Topic, useful for sending multiple values between **actors**, or for accumulating output. Can be configured to deduplicate values or to accumulate values over the course of multiple steps.
- [BinaryOperatorAggregate](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--advanced-channels-context-and-binaryoperatoraggregate): stores a persistent value, updated by applying a binary operator to the current value and each update sent to the channel, useful for computing aggregates over multiple steps; e.g.,`total = BinaryOperatorAggregate(int, operator.add)`

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Actors](./258-actors.md)

**Next:** [Examples →](./260-examples.md)
