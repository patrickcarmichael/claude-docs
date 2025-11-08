---
title: "Langgraph: How to manage conversation history in a ReAct Agent"
description: "How to manage conversation history in a ReAct Agent section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

# How to manage conversation history in a ReAct Agent


!!! info "Prerequisites"
    This guide assumes familiarity with the following:

    - <a href="../create-react-agent">Prebuilt create_react_agent</a>
    - <a href="../../concepts/persistence">Persistence</a>
    - <a href="../../concepts/memory/#short-term-memory">Short-term Memory</a>
    - [Trimming Messages](https://python.langchain.com/docs/how_to/trim_messages/)

Message history can grow quickly and exceed LLM context window size, whether you're building chatbots with many conversation turns or agentic systems with numerous tool calls. There are several strategies for managing the message history:

* <a href="#keep-the-original-message-history-unmodified">message trimming</a> — remove first or last N messages in the history
* <a href="#summarizing-message-history">summarization</a> — summarize earlier messages in the history and replace them with a summary
* custom strategies (e.g., message filtering, etc.)

To manage message history in `create_react_agent`, you need to define a `pre_model_hook` function or [runnable](https://python.langchain.com/docs/concepts/runnables/) that takes graph state an returns a state update:

* Trimming example:
    ```python hl_lines="1 2 3 4 19 25"
    from langchain_core.messages.utils import (
        trim_messages, 
        count_tokens_approximately
    )
    from langgraph.prebuilt import create_react_agent
    
    # This function will be called every time before the node that calls LLM
    def pre_model_hook(state):
        trimmed_messages = trim_messages(
            state["messages"],
            strategy="last",
            token_counter=count_tokens_approximately,
            max_tokens=384,
            start_on="human",
            end_on=("human", "tool"),
        )
        # You can return updated messages either under `llm_input_messages` or 
        # `messages` key (see the note below)
        return {"llm_input_messages": trimmed_messages}

    checkpointer = InMemorySaver()
    agent = create_react_agent(
        model,
        tools,
        pre_model_hook=pre_model_hook,
        checkpointer=checkpointer,
    )
    ```

* Summarization example:
    ```python hl_lines="1 20 27 28"
    from langmem.short_term import SummarizationNode
    from langchain_core.messages.utils import count_tokens_approximately
    from langgraph.prebuilt.chat_agent_executor import AgentState
    from langgraph.checkpoint.memory import InMemorySaver
    from typing import Any
    
    model = ChatOpenAI(model="gpt-4o")
    
    summarization_node = SummarizationNode(
        token_counter=count_tokens_approximately,
        model=model,
        max_tokens=384,
        max_summary_tokens=128,
        output_messages_key="llm_input_messages",
    )

    class State(AgentState):
        # NOTE: we're adding this key to keep track of previous summary information
        # to make sure we're not summarizing on every LLM call
        context: dict[str, Any]
    
    
    checkpointer = InMemorySaver()
    graph = create_react_agent(
        model,
        tools,
        pre_model_hook=summarization_node,
        state_schema=State,
        checkpointer=checkpointer,
    )
    ```

!!! Important
    
    * To **keep the original message history unmodified** in the graph state and pass the updated history **only as the input to the LLM**, return updated messages under `llm_input_messages` key
    * To **overwrite the original message history** in the graph state with the updated history, return updated messages under `messages` key
    
    To overwrite the `messages` key, you need to do the following:

    ```python
    from langchain_core.messages import RemoveMessage
    from langgraph.graph.message import REMOVE_ALL_MESSAGES

    def pre_model_hook(state):
        updated_messages = ...
        return {
            "messages": [RemoveMessage(id=REMOVE_ALL_MESSAGES), *updated_messages]
            ...
        }
    ```

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Example: simple chatbot with short-term memory](./172-example-simple-chatbot-with-short-term-memory.md)

**Next:** [Setup →](./174-setup.md)
