---
title: "Langgraph: Tool-calling agent"
description: "Tool-calling agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

## Tool-calling agent


While a router allows an LLM to make a single decision, more complex agent architectures expand the LLM's control in two key ways:

1. Multi-step decision making: The LLM can make a series of decisions, one after another, instead of just one.
2. Tool access: The LLM can choose from and use a variety of tools to accomplish tasks.

[ReAct](https://arxiv.org/abs/2210.03629) is a popular general purpose agent architecture that combines these expansions, integrating three core concepts. 

1. [Tool calling](#tool-calling): Allowing the LLM to select and use various tools as needed.
2. [Memory](#memory): Enabling the agent to retain and use information from previous steps.
3. [Planning](#planning): Empowering the LLM to create and follow multi-step plans to achieve goals.

This architecture allows for more complex and flexible agent behaviors, going beyond simple routing to enable dynamic problem-solving with multiple steps. Unlike the original [paper](https://arxiv.org/abs/2210.03629), today's agents rely on LLMs' [tool calling](#tool-calling) capabilities and operate on a list of [messages](./low_level.md#why-use-messages).

In LangGraph, you can use the prebuilt [agent](../agents/agents.md#2-create-an-agent) to get started with tool-calling agents.

### Tool calling

Tools are useful whenever you want an agent to interact with external systems. External systems (e.g., APIs) often require a particular input schema or payload, rather than natural language. When we bind an API, for example, as a tool, we give the model awareness of the required input schema. The model will choose to call a tool based upon the natural language input from the user and it will return an output that adheres to the tool's required schema. 

[Many LLM providers support tool calling](https://python.langchain.com/docs/integrations/chat/) and [tool calling interface](https://blog.langchain.dev/improving-core-tool-interfaces-and-docs-in-langchain/) in LangChain is simple: you can simply pass any Python `function` into `ChatModel.bind_tools(function)`.

![Tools](img/tool_call.png)

### Memory

[Memory](../how-tos/memory/add-memory.md) is crucial for agents, enabling them to retain and utilize information across multiple steps of problem-solving. It operates on different scales:

1. [Short-term memory](../how-tos/memory/add-memory.md#add-short-term-memory): Allows the agent to access information acquired during earlier steps in a sequence.
2. [Long-term memory](../how-tos/memory/add-memory.md#add-long-term-memory): Enables the agent to recall information from previous interactions, such as past messages in a conversation.

LangGraph provides full control over memory implementation:

- [`State`](./low_level.md#state): User-defined schema specifying the exact structure of memory to retain.
- [`Checkpointer`](./persistence.md#checkpoints): Mechanism to store state at every step across different interactions within a session.
- [`Store`](./persistence.md#memory-store): Mechanism to store user-specific or application-level data across sessions.

This flexible approach allows you to tailor the memory system to your specific agent architecture needs. Effective memory management enhances an agent's ability to maintain context, learn from past experiences, and make more informed decisions over time. For a practical guide on adding and managing memory, see [Memory](../how-tos/memory/add-memory.md).

### Planning

In a tool-calling [agent](../agents/overview.md#what-is-an-agent), an LLM is called repeatedly in a while-loop. At each step the agent decides which tools to call, and what the inputs to those tools should be. Those tools are then executed, and the outputs are fed back into the LLM as observations. The while-loop terminates when the agent decides it has enough information to solve the user request and it is not worth calling any more tools.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Router](./348-router.md)

**Next:** [Custom agent architectures →](./350-custom-agent-architectures.md)
