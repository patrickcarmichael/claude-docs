---
title: "Langgraph: How to create a ReAct agent from scratch (Functional API)"
description: "How to create a ReAct agent from scratch (Functional API) section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to create a ReAct agent from scratch (Functional API)


!!! info "Prerequisites"
    This guide assumes familiarity with the following:
    
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models)
    - [Messages](https://python.langchain.com/docs/concepts/messages)
    - [Tool Calling](https://python.langchain.com/docs/concepts/tool_calling/)
    - <a href="../../concepts/functional_api/#entrypoint">Entrypoints</a> and <a href="../../concepts/functional_api/#task">Tasks</a>

This guide demonstrates how to implement a ReAct agent using the LangGraph <a href="../../concepts/functional_api">Functional API</a>.

The ReAct agent is a <a href="../../concepts/agentic_concepts/#tool-calling-agent">tool-calling agent</a> that operates as follows:

1. Queries are issued to a chat model;
2. If the model generates no <a href="../../concepts/agentic_concepts/#tool-calling">tool calls</a>, we return the model response.
3. If the model generates tool calls, we execute the tool calls with available tools, append them as [tool messages](https://python.langchain.com/docs/concepts/messages/) to our message list, and repeat the process.

This is a simple and versatile set-up that can be extended with memory, human-in-the-loop capabilities, and other features. See the dedicated <a href="../../how-tos/#prebuilt-react-agent">how-to guides</a> for examples.

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Disabling streaming](./238-disabling-streaming.md)

**Next:** [Setup →](./240-setup.md)
