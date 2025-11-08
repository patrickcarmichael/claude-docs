# Subgraph

**Navigation:** [← Previous](./01-how-to-interact-with-the-deployment-using-remotegraph.md) | [Index](./index.md) | [Next →](./03-abbreviated-list-of-sp-500-companies-for-demonstration.md)

---

# Subgraph

def subgraph_node_1(state: SubgraphState):
    return {"bar": "hi! " + state["bar"]}

subgraph_builder = StateGraph(SubgraphState)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()


# Parent graph

class State(TypedDict):
    foo: str

def call_subgraph(state: State):
    subgraph_output = subgraph.invoke({"bar": state["foo"]})  # (1)!
    return {"foo": subgraph_output["bar"]}  # (2)!

builder = StateGraph(State)
builder.add_node("node_1", call_subgraph)
builder.add_edge(START, "node_1")
graph = builder.compile()
```

1. Transform the state to the subgraph state
2. Transform response back to the parent state




??? example "Full example: different state schemas"

    ```python
    from typing_extensions import TypedDict
    from langgraph.graph.state import StateGraph, START

    # Define subgraph
    class SubgraphState(TypedDict):
        # note that none of these keys are shared with the parent graph state
        bar: str
        baz: str
    
    def subgraph_node_1(state: SubgraphState):
        return {"baz": "baz"}
    
    def subgraph_node_2(state: SubgraphState):
        return {"bar": state["bar"] + state["baz"]}
    
    subgraph_builder = StateGraph(SubgraphState)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_node(subgraph_node_2)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
    subgraph = subgraph_builder.compile()
    
    # Define parent graph
    class ParentState(TypedDict):
        foo: str
    
    def node_1(state: ParentState):
        return {"foo": "hi! " + state["foo"]}
    
    def node_2(state: ParentState):
        response = subgraph.invoke({"bar": state["foo"]})  # (1)!
        return {"foo": response["bar"]}  # (2)!
    
    
    builder = StateGraph(ParentState)
    builder.add_node("node_1", node_1)
    builder.add_node("node_2", node_2)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    graph = builder.compile()
    
    for chunk in graph.stream({"foo": "foo"}, subgraphs=True):
        print(chunk)
    ```

    1. Transform the state to the subgraph state
    2. Transform response back to the parent state

    ```
    ((), {'node_1': {'foo': 'hi! foo'}})
    (('node_2:9c36dd0f-151a-cb42-cbad-fa2f851f9ab7',), {'grandchild_1': {'my_grandchild_key': 'hi Bob, how are you'}})
    (('node_2:9c36dd0f-151a-cb42-cbad-fa2f851f9ab7',), {'grandchild_2': {'bar': 'hi! foobaz'}})
    ((), {'node_2': {'foo': 'hi! foobaz'}})
    ```




??? example "Full example: different state schemas (two levels of subgraphs)"

    This is an example with two levels of subgraphs: parent -> child -> grandchild.

    ```python
    # Grandchild graph
    from typing_extensions import TypedDict
    from langgraph.graph.state import StateGraph, START, END
    
    class GrandChildState(TypedDict):
        my_grandchild_key: str
    
    def grandchild_1(state: GrandChildState) -> GrandChildState:
        # NOTE: child or parent keys will not be accessible here
        return {"my_grandchild_key": state["my_grandchild_key"] + ", how are you"}
    
    
    grandchild = StateGraph(GrandChildState)
    grandchild.add_node("grandchild_1", grandchild_1)
    
    grandchild.add_edge(START, "grandchild_1")
    grandchild.add_edge("grandchild_1", END)
    
    grandchild_graph = grandchild.compile()
    
    # Child graph
    class ChildState(TypedDict):
        my_child_key: str
    
    def call_grandchild_graph(state: ChildState) -> ChildState:
        # NOTE: parent or grandchild keys won't be accessible here
        grandchild_graph_input = {"my_grandchild_key": state["my_child_key"]}  # (1)!
        grandchild_graph_output = grandchild_graph.invoke(grandchild_graph_input)
        return {"my_child_key": grandchild_graph_output["my_grandchild_key"] + " today?"}  # (2)!
    
    child = StateGraph(ChildState)
    child.add_node("child_1", call_grandchild_graph)  # (3)!
    child.add_edge(START, "child_1")
    child.add_edge("child_1", END)
    child_graph = child.compile()
    
    # Parent graph
    class ParentState(TypedDict):
        my_key: str
    
    def parent_1(state: ParentState) -> ParentState:
        # NOTE: child or grandchild keys won't be accessible here
        return {"my_key": "hi " + state["my_key"]}
    
    def parent_2(state: ParentState) -> ParentState:
        return {"my_key": state["my_key"] + " bye!"}
    
    def call_child_graph(state: ParentState) -> ParentState:
        child_graph_input = {"my_child_key": state["my_key"]}  # (4)!
        child_graph_output = child_graph.invoke(child_graph_input)
        return {"my_key": child_graph_output["my_child_key"]}  # (5)!
    
    parent = StateGraph(ParentState)
    parent.add_node("parent_1", parent_1)
    parent.add_node("child", call_child_graph)  # (6)!
    parent.add_node("parent_2", parent_2)
    
    parent.add_edge(START, "parent_1")
    parent.add_edge("parent_1", "child")
    parent.add_edge("child", "parent_2")
    parent.add_edge("parent_2", END)
    
    parent_graph = parent.compile()
    
    for chunk in parent_graph.stream({"my_key": "Bob"}, subgraphs=True):
        print(chunk)
    ```

    1. We're transforming the state from the child state channels (`my_child_key`) to the child state channels (`my_grandchild_key`)
    2. We're transforming the state from the grandchild state channels (`my_grandchild_key`) back to the child state channels (`my_child_key`)
    3. We're passing a function here instead of just compiled graph (`grandchild_graph`)
    4. We're transforming the state from the parent state channels (`my_key`) to the child state channels (`my_child_key`)
    5. We're transforming the state from the child state channels (`my_child_key`) back to the parent state channels (`my_key`)
    6. We're passing a function here instead of just a compiled graph (`child_graph`)

    ```
    ((), {'parent_1': {'my_key': 'hi Bob'}})
    (('child:2e26e9ce-602f-862c-aa66-1ea5a4655e3b', 'child_1:781bb3b1-3971-84ce-810b-acf819a03f9c'), {'grandchild_1': {'my_grandchild_key': 'hi Bob, how are you'}})
    (('child:2e26e9ce-602f-862c-aa66-1ea5a4655e3b',), {'child_1': {'my_child_key': 'hi Bob, how are you today?'}})
    ((), {'child': {'my_key': 'hi Bob, how are you today?'}})
    ((), {'parent_2': {'my_key': 'hi Bob, how are you today? bye!'}})
    ```





## Add persistence 

You only need to **provide the checkpointer when compiling the parent graph**. LangGraph will automatically propagate the checkpointer to the child subgraphs.

```python
from langgraph.graph import START, StateGraph
from langgraph.checkpoint.memory import MemorySaver
from typing_extensions import TypedDict

class State(TypedDict):
    foo: str


# Subgraph

def subgraph_node_1(state: State):
    return {"foo": state["foo"] + "bar"}

subgraph_builder = StateGraph(State)
subgraph_builder.add_node(subgraph_node_1)
subgraph_builder.add_edge(START, "subgraph_node_1")
subgraph = subgraph_builder.compile()


# Parent graph

builder = StateGraph(State)
builder.add_node("node_1", subgraph)
builder.add_edge(START, "node_1")

checkpointer = MemorySaver()
graph = builder.compile(checkpointer=checkpointer)
```    




If you want the subgraph to **have its own memory**, you can compile it with the appropriate checkpointer option. This is useful in [multi-agent](../concepts/multi_agent.md) systems, if you want agents to keep track of their internal message histories:

```python
subgraph_builder = StateGraph(...)
subgraph = subgraph_builder.compile(checkpointer=True)
```





## View subgraph state

When you enable [persistence](../concepts/persistence.md), you can [inspect the graph state](../concepts/persistence.md#checkpoints) (checkpoint) via the appropriate method. To view the subgraph state, you can use the subgraphs option.

You can inspect the graph state via `graph.get_state(config)`. To view the subgraph state, you can use `graph.get_state(config, subgraphs=True)`.




!!! important "Available **only** when interrupted"

    Subgraph state can only be viewed **when the subgraph is interrupted**. Once you resume the graph, you won't be able to access the subgraph state.

??? example "View interrupted subgraph state"

    ```python
    from langgraph.graph import START, StateGraph
    from langgraph.checkpoint.memory import MemorySaver
    from langgraph.types import interrupt, Command
    from typing_extensions import TypedDict
    
    class State(TypedDict):
        foo: str
    
    # Subgraph
    
    def subgraph_node_1(state: State):
        value = interrupt("Provide value:")
        return {"foo": state["foo"] + value}
    
    subgraph_builder = StateGraph(State)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    
    subgraph = subgraph_builder.compile()
    
    # Parent graph
        
    builder = StateGraph(State)
    builder.add_node("node_1", subgraph)
    builder.add_edge(START, "node_1")
    
    checkpointer = MemorySaver()
    graph = builder.compile(checkpointer=checkpointer)
    
    config = {"configurable": {"thread_id": "1"}}
    
    graph.invoke({"foo": ""}, config)
    parent_state = graph.get_state(config)
    subgraph_state = graph.get_state(config, subgraphs=True).tasks[0].state  # (1)!
    
    # resume the subgraph
    graph.invoke(Command(resume="bar"), config)
    ```
    
    1. This will be available only when the subgraph is interrupted. Once you resume the graph, you won't be able to access the subgraph state.





## Stream subgraph outputs

To include outputs from subgraphs in the streamed outputs, you can set the subgraphs option in the stream method of the parent graph. This will stream outputs from both the parent graph and any subgraphs.

```python
for chunk in graph.stream(
    {"foo": "foo"},
    subgraphs=True, # (1)!
    stream_mode="updates",
):
    print(chunk)
```

1. Set `subgraphs=True` to stream outputs from subgraphs.




??? example "Stream from subgraphs"

    ```python
    from typing_extensions import TypedDict
    from langgraph.graph.state import StateGraph, START

    # Define subgraph
    class SubgraphState(TypedDict):
        foo: str
        bar: str
    
    def subgraph_node_1(state: SubgraphState):
        return {"bar": "bar"}
    
    def subgraph_node_2(state: SubgraphState):
        # note that this node is using a state key ('bar') that is only available in the subgraph
        # and is sending update on the shared state key ('foo')
        return {"foo": state["foo"] + state["bar"]}
    
    subgraph_builder = StateGraph(SubgraphState)
    subgraph_builder.add_node(subgraph_node_1)
    subgraph_builder.add_node(subgraph_node_2)
    subgraph_builder.add_edge(START, "subgraph_node_1")
    subgraph_builder.add_edge("subgraph_node_1", "subgraph_node_2")
    subgraph = subgraph_builder.compile()
    
    # Define parent graph
    class ParentState(TypedDict):
        foo: str
    
    def node_1(state: ParentState):
        return {"foo": "hi! " + state["foo"]}
    
    builder = StateGraph(ParentState)
    builder.add_node("node_1", node_1)
    builder.add_node("node_2", subgraph)
    builder.add_edge(START, "node_1")
    builder.add_edge("node_1", "node_2")
    graph = builder.compile()

    for chunk in graph.stream(
        {"foo": "foo"},
        stream_mode="updates",
        subgraphs=True, # (1)!
    ):
        print(chunk)
    ```
  
    1. Set `subgraphs=True` to stream outputs from subgraphs.

    ```
    ((), {'node_1': {'foo': 'hi! foo'}})
    (('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_1': {'bar': 'bar'}})
    (('node_2:e58e5673-a661-ebb0-70d4-e298a7fc28b7',), {'subgraph_node_2': {'foo': 'hi! foobar'}})
    ((), {'node_2': {'foo': 'hi! foobar'}})
    ```




---
how-tos/multi_agent.md
---


# Build multi-agent systems

A single agent might struggle if it needs to specialize in multiple domains or manage many tools. To tackle this, you can break your agent into smaller, independent agents and composing them into a [multi-agent system](../concepts/multi_agent.md).

In multi-agent systems, agents need to communicate between each other. They do so via [handoffs](#handoffs) — a primitive that describes which agent to hand control to and the payload to send to that agent.

This guide covers the following:

* implementing [handoffs](#handoffs) between agents
* using handoffs and the prebuilt [agent](../agents/agents.md) to [build a custom multi-agent system](#build-a-multi-agent-system)

To get started with building multi-agent systems, check out LangGraph [prebuilt implementations](#prebuilt-implementations) of two of the most popular multi-agent architectures — [supervisor](../agents/multi-agent.md#supervisor) and [swarm](../agents/multi-agent.md#swarm).


## Handoffs

To set up communication between the agents in a multi-agent system you can use [**handoffs**](../concepts/multi_agent.md#handoffs) — a pattern where one agent *hands off* control to another. Handoffs allow you to specify:

- **destination**: target agent to navigate to (e.g., name of the LangGraph node to go to)
- **payload**: information to pass to that agent (e.g., state update)

### Create handoffs

To implement handoffs, you can return `Command` objects from your agent nodes or tools:

```python hl_lines="13 14 23 24 25"
from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import create_react_agent, InjectedState
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.types import Command

def create_handoff_tool(*, agent_name: str, description: str | None = None):
    name = f"transfer_to_{agent_name}"
    description = description or f"Transfer to {agent_name}"

    @tool(name, description=description)
    def handoff_tool(
        state: Annotated[MessagesState, InjectedState], # (1)!
        tool_call_id: Annotated[str, InjectedToolCallId],
    ) -> Command:
        tool_message = {
            "role": "tool",
            "content": f"Successfully transferred to {agent_name}",
            "name": name,
            "tool_call_id": tool_call_id,
        }
        return Command(  # (2)!
            goto=agent_name,  # (3)!
            update={"messages": state["messages"] + [tool_message]},  # (4)!
            graph=Command.PARENT,  # (5)!
        )
    return handoff_tool
```

1. Access the [state](../concepts/low_level.md#state) of the agent that is calling the handoff tool using the [InjectedState](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.InjectedState) annotation. 
2. The `Command` primitive allows specifying a state update and a node transition as a single operation, making it useful for implementing handoffs.
3. Name of the agent or node to hand off to.
4. Take the agent's messages and **add** them to the parent's **state** as part of the handoff. The next agent will see the parent state.
5. Indicate to LangGraph that we need to navigate to agent node in a **parent** multi-agent graph.

!!! tip

    If you want to use tools that return `Command`, you can either use prebuilt [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) components, or implement your own tool-executing node that collects `Command` objects returned by the tools and returns a list of them, e.g.:
    
    ```python
    def call_tools(state):
        ...
        commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
        return commands
    ```




!!! Important

    This handoff implementation assumes that:
    
    - each agent receives overall message history (across all agents) in the multi-agent system as its input. If you want more control over agent inputs, see [this section](#control-agent-inputs)
    - each agent outputs its internal messages history to the overall message history of the multi-agent system. If you want more control over **how agent outputs are added**, wrap the agent in a separate node function:

      ```python hl_lines="5"
      def call_hotel_assistant(state):
          # return agent's final response,
          # excluding inner monologue
          response = hotel_assistant.invoke(state)
          return {"messages": response["messages"][-1]}
      ```




### Control agent inputs

You can use the [`Send()`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send) primitive to directly send data to the worker agents during the handoff. For example, you can request that the calling agent populate a task description for the next agent:

```python hl_lines="5 26"
from typing import Annotated
from langchain_core.tools import tool, InjectedToolCallId
from langgraph.prebuilt import InjectedState
from langgraph.graph import StateGraph, START, MessagesState
from langgraph.types import Command, Send

def create_task_description_handoff_tool(
    *, agent_name: str, description: str | None = None
):
    name = f"transfer_to_{agent_name}"
    description = description or f"Ask {agent_name} for help."

    @tool(name, description=description)
    def handoff_tool(
        # this is populated by the calling agent
        task_description: Annotated[
            str,
            "Description of what the next agent should do, including all of the relevant context.",
        ],
        # these parameters are ignored by the LLM
        state: Annotated[MessagesState, InjectedState],
    ) -> Command:
        task_description_message = {"role": "user", "content": task_description}
        agent_input = {**state, "messages": [task_description_message]}
        return Command(
            goto=[Send(agent_name, agent_input)],
            graph=Command.PARENT,
        )

    return handoff_tool
```




See the multi-agent [supervisor](../tutorials/multi_agent/agent_supervisor.md#4-create-delegation-tasks) example for a full example of using [`Send()`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Send) in handoffs.


## Build a multi-agent system

You can use handoffs in any agents built with LangGraph. We recommend using the prebuilt [agent](../agents/overview.md) or [`ToolNode`](./tool-calling.md#toolnode), as they natively support handoffs tools returning `Command`. Below is an example of how you can implement a multi-agent system for booking travel using handoffs:

```python hl_lines="16 17 21 22 28 29"
from langgraph.prebuilt import create_react_agent
from langgraph.graph import StateGraph, START, MessagesState

def create_handoff_tool(*, agent_name: str, description: str | None = None):
    # same implementation as above
    ...
    return Command(...)


# Handoffs
transfer_to_hotel_assistant = create_handoff_tool(agent_name="hotel_assistant")
transfer_to_flight_assistant = create_handoff_tool(agent_name="flight_assistant")


# Define agents
flight_assistant = create_react_agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[..., transfer_to_hotel_assistant],
    name="flight_assistant"
)
hotel_assistant = create_react_agent(
    model="anthropic:claude-3-5-sonnet-latest",
    tools=[..., transfer_to_flight_assistant],
    name="hotel_assistant"
)


# Define multi-agent graph
multi_agent_graph = (
    StateGraph(MessagesState)
    .add_node(flight_assistant)
    .add_node(hotel_assistant)
    .add_edge(START, "flight_assistant")
    .compile()
)
```




??? example "Full example: Multi-agent system for booking travel"

    ```python hl_lines="56 57 66 67 68 94 96 100 102 124"
    from typing import Annotated
    from langchain_core.messages import convert_to_messages
    from langchain_core.tools import tool, InjectedToolCallId
    from langgraph.prebuilt import create_react_agent, InjectedState
    from langgraph.graph import StateGraph, START, MessagesState
    from langgraph.types import Command
    
    # We'll use `pretty_print_messages` helper to render the streamed agent outputs nicely
    
    def pretty_print_message(message, indent=False):
        pretty_message = message.pretty_repr(html=True)
        if not indent:
            print(pretty_message)
            return
    
        indented = "\n".join("\t" + c for c in pretty_message.split("\n"))
        print(indented)
    
    
    def pretty_print_messages(update, last_message=False):
        is_subgraph = False
        if isinstance(update, tuple):
            ns, update = update
            # skip parent graph updates in the printouts
            if len(ns) == 0:
                return
    
            graph_id = ns[-1].split(":")[0]
            print(f"Update from subgraph {graph_id}:")
            print("\n")
            is_subgraph = True
    
        for node_name, node_update in update.items():
            update_label = f"Update from node {node_name}:"
            if is_subgraph:
                update_label = "\t" + update_label
    
            print(update_label)
            print("\n")
    
            messages = convert_to_messages(node_update["messages"])
            if last_message:
                messages = messages[-1:]
    
            for m in messages:
                pretty_print_message(m, indent=is_subgraph)
            print("\n")


    def create_handoff_tool(*, agent_name: str, description: str | None = None):
        name = f"transfer_to_{agent_name}"
        description = description or f"Transfer to {agent_name}"
    
        @tool(name, description=description)
        def handoff_tool(
            state: Annotated[MessagesState, InjectedState], # (1)!
            tool_call_id: Annotated[str, InjectedToolCallId],
        ) -> Command:
            tool_message = {
                "role": "tool",
                "content": f"Successfully transferred to {agent_name}",
                "name": name,
                "tool_call_id": tool_call_id,
            }
            return Command(  # (2)!
                goto=agent_name,  # (3)!
                update={"messages": state["messages"] + [tool_message]},  # (4)!
                graph=Command.PARENT,  # (5)!
            )
        return handoff_tool
    
    # Handoffs
    transfer_to_hotel_assistant = create_handoff_tool(
        agent_name="hotel_assistant",
        description="Transfer user to the hotel-booking assistant.",
    )
    transfer_to_flight_assistant = create_handoff_tool(
        agent_name="flight_assistant",
        description="Transfer user to the flight-booking assistant.",
    )
    
    # Simple agent tools
    def book_hotel(hotel_name: str):
        """Book a hotel"""
        return f"Successfully booked a stay at {hotel_name}."
    
    def book_flight(from_airport: str, to_airport: str):
        """Book a flight"""
        return f"Successfully booked a flight from {from_airport} to {to_airport}."
    
    # Define agents
    flight_assistant = create_react_agent(
        model="anthropic:claude-3-5-sonnet-latest",
        tools=[book_flight, transfer_to_hotel_assistant],
        prompt="You are a flight booking assistant",
        name="flight_assistant"
    )
    hotel_assistant = create_react_agent(
        model="anthropic:claude-3-5-sonnet-latest",
        tools=[book_hotel, transfer_to_flight_assistant],
        prompt="You are a hotel booking assistant",
        name="hotel_assistant"
    )
    
    # Define multi-agent graph
    multi_agent_graph = (
        StateGraph(MessagesState)
        .add_node(flight_assistant)
        .add_node(hotel_assistant)
        .add_edge(START, "flight_assistant")
        .compile()
    )
    
    # Run the multi-agent graph
    for chunk in multi_agent_graph.stream(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "book a flight from BOS to JFK and a stay at McKittrick Hotel"
                }
            ]
        },
        subgraphs=True
    ):
        pretty_print_messages(chunk)
    ```

    1. Access agent's state
    2. The `Command` primitive allows specifying a state update and a node transition as a single operation, making it useful for implementing handoffs.
    3. Name of the agent or node to hand off to.
    4. Take the agent's messages and **add** them to the parent's **state** as part of the handoff. The next agent will see the parent state.
    5. Indicate to LangGraph that we need to navigate to agent node in a **parent** multi-agent graph.





## Multi-turn conversation

Users might want to engage in a *multi-turn conversation* with one or more agents. To build a system that can handle this, you can create a node that uses an [`interrupt`](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt) to collect user input and routes back to the **active** agent.

The agents can then be implemented as nodes in a graph that executes agent steps and determines the next action:

1. **Wait for user input** to continue the conversation, or  
2. **Route to another agent** (or back to itself, such as in a loop) via a [handoff](#handoffs)

```python
def human(state) -> Command[Literal["agent", "another_agent"]]:
    """A node for collecting user input."""
    user_input = interrupt(value="Ready for user input.")

    # Determine the active agent.
    active_agent = ...

    ...
    return Command(
        update={
            "messages": [{
                "role": "human",
                "content": user_input,
            }]
        },
        goto=active_agent
    )

def agent(state) -> Command[Literal["agent", "another_agent", "human"]]:
    # The condition for routing/halting can be anything, e.g. LLM tool call / structured output, etc.
    goto = get_next_agent(...)  # 'agent' / 'another_agent'
    if goto:
        return Command(goto=goto, update={"my_state_key": "my_state_value"})
    else:
        return Command(goto="human") # Go to human node
```




??? example "Full example: multi-agent system for travel recommendations"

    In this example, we will build a team of travel assistant agents that can communicate with each other via handoffs.
    
    We will create 2 agents:
    
    * travel_advisor: can help with travel destination recommendations. Can ask hotel_advisor for help.
    * hotel_advisor: can help with hotel recommendations. Can ask travel_advisor for help.

    ```python
    from langchain_anthropic import ChatAnthropic
    from langgraph.graph import MessagesState, StateGraph, START
    from langgraph.prebuilt import create_react_agent, InjectedState
    from langgraph.types import Command, interrupt
    from langgraph.checkpoint.memory import InMemorySaver
    
    
    model = ChatAnthropic(model="claude-3-5-sonnet-latest")

    class MultiAgentState(MessagesState):
        last_active_agent: str
    
    
    # Define travel advisor tools and ReAct agent
    travel_advisor_tools = [
        get_travel_recommendations,
        make_handoff_tool(agent_name="hotel_advisor"),
    ]
    travel_advisor = create_react_agent(
        model,
        travel_advisor_tools,
        prompt=(
            "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
            "If you need hotel recommendations, ask 'hotel_advisor' for help. "
            "You MUST include human-readable response before transferring to another agent."
        ),
    )
    
    
    def call_travel_advisor(
        state: MultiAgentState,
    ) -> Command[Literal["hotel_advisor", "human"]]:
        # You can also add additional logic like changing the input to the agent / output from the agent, etc.
        # NOTE: we're invoking the ReAct agent with the full history of messages in the state
        response = travel_advisor.invoke(state)
        update = {**response, "last_active_agent": "travel_advisor"}
        return Command(update=update, goto="human")
    
    
    # Define hotel advisor tools and ReAct agent
    hotel_advisor_tools = [
        get_hotel_recommendations,
        make_handoff_tool(agent_name="travel_advisor"),
    ]
    hotel_advisor = create_react_agent(
        model,
        hotel_advisor_tools,
        prompt=(
            "You are a hotel expert that can provide hotel recommendations for a given destination. "
            "If you need help picking travel destinations, ask 'travel_advisor' for help."
            "You MUST include human-readable response before transferring to another agent."
        ),
    )
    
    
    def call_hotel_advisor(
        state: MultiAgentState,
    ) -> Command[Literal["travel_advisor", "human"]]:
        response = hotel_advisor.invoke(state)
        update = {**response, "last_active_agent": "hotel_advisor"}
        return Command(update=update, goto="human")
    
    
    def human_node(
        state: MultiAgentState, config
    ) -> Command[Literal["hotel_advisor", "travel_advisor", "human"]]:
        """A node for collecting user input."""
    
        user_input = interrupt(value="Ready for user input.")
        active_agent = state["last_active_agent"]
    
        return Command(
            update={
                "messages": [
                    {
                        "role": "human",
                        "content": user_input,
                    }
                ]
            },
            goto=active_agent,
        )
    
    
    builder = StateGraph(MultiAgentState)
    builder.add_node("travel_advisor", call_travel_advisor)
    builder.add_node("hotel_advisor", call_hotel_advisor)
    
    # This adds a node to collect human input, which will route
    # back to the active agent.
    builder.add_node("human", human_node)
    
    # We'll always start with a general travel advisor.
    builder.add_edge(START, "travel_advisor")
    
    
    checkpointer = InMemorySaver()
    graph = builder.compile(checkpointer=checkpointer)
    ```
    
    Let's test a multi turn conversation with this application.

    ```python
    import uuid
    
    thread_config = {"configurable": {"thread_id": str(uuid.uuid4())}}
    
    inputs = [
        # 1st round of conversation,
        {
            "messages": [
                {"role": "user", "content": "i wanna go somewhere warm in the caribbean"}
            ]
        },
        # Since we're using `interrupt`, we'll need to resume using the Command primitive.
        # 2nd round of conversation,
        Command(
            resume="could you recommend a nice hotel in one of the areas and tell me which area it is."
        ),
        # 3rd round of conversation,
        Command(
            resume="i like the first one. could you recommend something to do near the hotel?"
        ),
    ]
    
    for idx, user_input in enumerate(inputs):
        print()
        print(f"--- Conversation Turn {idx + 1} ---")
        print()
        print(f"User: {user_input}")
        print()
        for update in graph.stream(
            user_input,
            config=thread_config,
            stream_mode="updates",
        ):
            for node_id, value in update.items():
                if isinstance(value, dict) and value.get("messages", []):
                    last_message = value["messages"][-1]
                    if isinstance(last_message, dict) or last_message.type != "ai":
                        continue
                    print(f"{node_id}: {last_message.content}")
    ```
    
    ```
    --- Conversation Turn 1 ---
    
    User: {'messages': [{'role': 'user', 'content': 'i wanna go somewhere warm in the caribbean'}]}
    
    travel_advisor: Based on the recommendations, Aruba would be an excellent choice for your Caribbean getaway! Aruba is known as "One Happy Island" and offers:
    - Year-round warm weather with consistent temperatures around 82°F (28°C)
    - Beautiful white sand beaches like Eagle Beach and Palm Beach
    - Clear turquoise waters perfect for swimming and snorkeling
    - Minimal rainfall and location outside the hurricane belt
    - A blend of Caribbean and Dutch culture
    - Great dining options and nightlife
    - Various water sports and activities
    
    Would you like me to get some specific hotel recommendations in Aruba for your stay? I can transfer you to our hotel advisor who can help with accommodations.
    
    --- Conversation Turn 2 ---
    
    User: Command(resume='could you recommend a nice hotel in one of the areas and tell me which area it is.')
    
    hotel_advisor: Based on the recommendations, I can suggest two excellent options:
    
    1. The Ritz-Carlton, Aruba - Located in Palm Beach
    - This luxury resort is situated in the vibrant Palm Beach area
    - Known for its exceptional service and amenities
    - Perfect if you want to be close to dining, shopping, and entertainment
    - Features multiple restaurants, a casino, and a world-class spa
    - Located on a pristine stretch of Palm Beach
    
    2. Bucuti & Tara Beach Resort - Located in Eagle Beach
    - An adults-only boutique resort on Eagle Beach
    - Known for being more intimate and peaceful
    - Award-winning for its sustainability practices
    - Perfect for a romantic getaway or peaceful vacation
    - Located on one of the most beautiful beaches in the Caribbean
    
    Would you like more specific information about either of these properties or their locations?
    
    --- Conversation Turn 3 ---
    
    User: Command(resume='i like the first one. could you recommend something to do near the hotel?')
    
    travel_advisor: Near the Ritz-Carlton in Palm Beach, here are some highly recommended activities:
    
    1. Visit the Palm Beach Plaza Mall - Just a short walk from the hotel, featuring shopping, dining, and entertainment
    2. Try your luck at the Stellaris Casino - It's right in the Ritz-Carlton
    3. Take a sunset sailing cruise - Many depart from the nearby pier
    4. Visit the California Lighthouse - A scenic landmark just north of Palm Beach
    5. Enjoy water sports at Palm Beach:
       - Jet skiing
       - Parasailing
       - Snorkeling
       - Stand-up paddleboarding
    
    Would you like more specific information about any of these activities or would you like to know about other options in the area?
    ```





## Prebuilt implementations

LangGraph comes with prebuilt implementations of two of the most popular multi-agent architectures:

- [supervisor](../agents/multi-agent.md#supervisor) — individual agents are coordinated by a central supervisor agent. The supervisor controls all communication flow and task delegation, making decisions about which agent to invoke based on the current context and task requirements. You can use [`langgraph-supervisor`](https://github.com/langchain-ai/langgraph-supervisor-py) library to create a supervisor multi-agent systems.
- [swarm](../agents/multi-agent.md#supervisor) — agents dynamically hand off control to one another based on their specializations. The system remembers which agent was last active, ensuring that on subsequent interactions, the conversation resumes with that agent. You can use [`langgraph-swarm`](https://github.com/langchain-ai/langgraph-swarm-py) library to create a swarm multi-agent systems.




---
how-tos/run-id-langsmith.md
---


# How to pass custom run ID or set tags and metadata for graph runs in LangSmith

!!! tip "Prerequisites"
    This guide assumes familiarity with the following:
    
    - [LangSmith Documentation](https://docs.smith.langchain.com)
    - [LangSmith Platform](https://smith.langchain.com)
    - [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)
    - [Add metadata and tags to traces](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#add-metadata-and-tags-to-traces)
    - [Customize run name](https://docs.smith.langchain.com/how_to_guides/tracing/trace_with_langchain#customize-run-name)

Debugging graph runs can sometimes be difficult to do in an IDE or terminal. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read the [LangSmith documentation](https://docs.smith.langchain.com) for more information on how to get started.

To make it easier to identify and analyzed traces generated during graph invocation, you can set additional configuration at run time (see [RunnableConfig](https://api.python.langchain.com/en/latest/runnables/langchain_core.runnables.config.RunnableConfig.html#langchain_core.runnables.config.RunnableConfig)):

| **Field**   | **Type**            | **Description**                                                                                                    |
|-------------|---------------------|--------------------------------------------------------------------------------------------------------------------|
| run_name    | `str`               | Name for the tracer run for this call. Defaults to the name of the class.                                          |
| run_id      | `UUID`              | Unique identifier for the tracer run for this call. If not provided, a new UUID will be generated.                 |
| tags        | `List[str]`         | Tags for this call and any sub-calls (e.g., a Chain calling an LLM). You can use these to filter calls.            |
| metadata    | `Dict[str, Any]`    | Metadata for this call and any sub-calls (e.g., a Chain calling an LLM). Keys should be strings, values should be JSON-serializable. |

LangGraph graphs implement the [LangChain Runnable Interface](https://python.langchain.com/api_reference/core/runnables/langchain_core.runnables.base.Runnable.html) and accept a second argument (`RunnableConfig`) in methods like `invoke`, `ainvoke`, `stream` etc.

The LangSmith platform will allow you to search and filter traces based on `run_name`, `run_id`, `tags` and `metadata`.


## TLDR

```python
import uuid

# Generate a random UUID -- it must be a UUID
config = {"run_id": uuid.uuid4()}, "tags": ["my_tag1"], "metadata": {"a": 5}}

# Works with all standard Runnable methods 

# like invoke, batch, ainvoke, astream_events etc
graph.stream(inputs, config, stream_mode="values")
```

The rest of the how to guide will show a full agent.


## Setup

First, let's install the required packages and set our API keys

```python
%%capture --no-stderr
%pip install --quiet -U langgraph langchain_openai
```

```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
_set_env("LANGSMITH_API_KEY")
```

!!! tip
    Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. [LangSmith](https://docs.smith.langchain.com) lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com).


## Define the graph

For this example we will use the [prebuilt ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/).

```python
from langchain_openai import ChatOpenAI
from typing import Literal
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool


# First we initialize the model we want to use.
model = ChatOpenAI(model="gpt-4o", temperature=0)



# For this tutorial we will use custom tool that returns pre-defined values for weather in two cities (NYC & SF)
@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It might be cloudy in nyc"
    elif city == "sf":
        return "It's always sunny in sf"
    else:
        raise AssertionError("Unknown city")


tools = [get_weather]



# Define the graph
graph = create_react_agent(model, tools=tools)
```


## Run your graph

Now that we've defined our graph let's run it once and view the trace in LangSmith. In order for our trace to be easily accessible in LangSmith, we will pass in a custom `run_id` in the config.

This assumes that you have set your `LANGSMITH_API_KEY` environment variable.

Note that you can also configure what project to trace to by setting the `LANGCHAIN_PROJECT` environment variable, by default runs will be traced to the `default` project.

```python
import uuid


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


inputs = {"messages": [("user", "what is the weather in sf")]}

config = {"run_name": "agent_007", "tags": ["cats are awesome"]}

print_stream(graph.stream(inputs, config, stream_mode="values"))
```

**Output:**
```
================================ Human Message ==================================

what is the weather in sf
================================== Ai Message ===================================
Tool Calls:
  get_weather (call_9ZudXyMAdlUjptq9oMGtQo8o)
 Call ID: call_9ZudXyMAdlUjptq9oMGtQo8o
  Args:
    city: sf
================================= Tool Message ==================================
Name: get_weather

It's always sunny in sf
================================== Ai Message ===================================

The weather in San Francisco is currently sunny.
```


## View the trace in LangSmith

Now that we've ran our graph, let's head over to LangSmith and view our trace. First click into the project that you traced to (in our case the default project). You should see a run with the custom run name "agent_007".

![LangSmith Trace View](assets/d38d1f2b-0f4c-4707-b531-a3c749de987f.png)

In addition, you will be able to filter traces after the fact using the tags or metadata provided. For example,

![LangSmith Filter View](assets/410e0089-2ab8-46bb-a61a-827187fd46b3.png) 

---
how-tos/tool-calling.md
---


# Call tools

[Tools](../concepts/tools.md) encapsulate a callable function and its input schema. These can be passed to compatible chat models, allowing the model to decide whether to invoke a tool and determine the appropriate arguments.

You can [define your own tools](#define-a-tool) or use [prebuilt tools](#prebuilt-tools)


## Define a tool

Define a basic tool with the [@tool](https://python.langchain.com/api_reference/core/tools/langchain_core.tools.convert.tool.html) decorator:

```python hl_lines="3"
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```






## Run a tool

Tools conform to the [Runnable interface](https://python.langchain.com/docs/concepts/runnables/), which means you can run a tool using the `invoke` method:

```python
multiply.invoke({"a": 6, "b": 7})  # returns 42
```





If the tool is invoked with `type="tool_call"`, it will return a [ToolMessage](https://python.langchain.com/docs/concepts/messages/#toolmessage):

```python
tool_call = {
    "type": "tool_call",
    "id": "1",
    "args": {"a": 42, "b": 7}
}
multiply.invoke(tool_call) # returns a ToolMessage object
```

Output:

```pycon
ToolMessage(content='294', name='multiply', tool_call_id='1')
```






## Use in an agent

To create a tool-calling agent, you can use the prebuilt [create_react_agent](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent):

```python hl_lines="2 9"
from langchain_core.tools import tool
from langgraph.prebuilt import create_react_agent

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet",
    tools=[multiply]
)
agent.invoke({"messages": [{"role": "user", "content": "what's 42 x 7?"}]})
```





### Dynamically select tools

Configure tool availability at runtime based on context:

```python hl_lines="30 42 44 56"
from dataclasses import dataclass
from typing import Literal

from langchain.chat_models import init_chat_model
from langchain_core.tools import tool

from langgraph.prebuilt import create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState
from langgraph.runtime import Runtime


@dataclass
class CustomContext:
    tools: list[Literal["weather", "compass"]]


@tool
def weather() -> str:
    """Returns the current weather conditions."""
    return "It's nice and sunny."


@tool
def compass() -> str:
    """Returns the direction the user is facing."""
    return "North"

model = init_chat_model("anthropic:claude-sonnet-4-20250514")

def configure_model(state: AgentState, runtime: Runtime[CustomContext]):
    """Configure the model with tools based on runtime context."""
    selected_tools = [
        tool
        for tool in [weather, compass]
        if tool.name in runtime.context.tools
    ]
    return model.bind_tools(selected_tools)


agent = create_react_agent(
    # Dynamically configure the model with tools based on runtime context
    configure_model,
    # Initialize with all tools available
    tools=[weather, compass]
)

output = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "Who are you and what tools do you have access to?",
            }
        ]
    },
    context=CustomContext(tools=["weather"]),  # Only enable the weather tool
)

print(output["messages"][-1].text())
```

!!! version-added "Added in version 0.6.0"




## Use in a workflow

If you are writing a custom workflow, you will need to:

1. register the tools with the chat model
2. call the tool if the model decides to use it

Use `model.bind_tools()` to register the tools with the model.

```python hl_lines="5"
from langchain.chat_models import init_chat_model

model = init_chat_model(model="claude-3-5-haiku-latest")

model_with_tools = model.bind_tools([multiply])
```





LLMs automatically determine if a tool invocation is necessary and handle calling the tool with the appropriate arguments.

??? example "Extended example: attach tools to a chat model"

    ```python hl_lines="10"
    from langchain_core.tools import tool
    from langchain.chat_models import init_chat_model

    @tool
    def multiply(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([multiply])

    response_message = model_with_tools.invoke("what's 42 x 7?")
    tool_call = response_message.tool_calls[0]

    multiply.invoke(tool_call)
    ```

    ```pycon
    ToolMessage(
        content='294',
        name='multiply',
        tool_call_id='toolu_0176DV4YKSD8FndkeuuLj36c'
    )
    ```




#### ToolNode

To execute tools in custom workflows, use the prebuilt [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) or implement your own custom node.

`ToolNode` is a specialized node for executing tools in a workflow. It provides the following features:

- Supports both synchronous and asynchronous tools.
- Executes multiple tools concurrently.
- Handles errors during tool execution (`handle_tool_errors=True`, enabled by default). See [handling tool errors](#handle-errors) for more details.

`ToolNode` operates on [`MessagesState`](../concepts/low_level.md#messagesstate):

- **Input**: `MessagesState`, where the last message is an `AIMessage` containing the `tool_calls` parameter.
- **Output**: `MessagesState` updated with the resulting [`ToolMessage`](https://python.langchain.com/docs/concepts/messages/#toolmessage) from executed tools.

```python hl_lines="1 14"
from langgraph.prebuilt import ToolNode

def get_weather(location: str):
    """Call to get the current weather."""
    if location.lower() in ["sf", "san francisco"]:
        return "It's 60 degrees and foggy."
    else:
        return "It's 90 degrees and sunny."

def get_coolest_cities():
    """Get a list of coolest cities"""
    return "nyc, sf"

tool_node = ToolNode([get_weather, get_coolest_cities])
tool_node.invoke({"messages": [...]})
```





??? example "Single tool call"

    ```python hl_lines="13"
    from langchain_core.messages import AIMessage
    from langgraph.prebuilt import ToolNode

    # Define tools
    @tool
    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    message_with_single_tool_call = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id",
                "type": "tool_call",
            }
        ],
    )

    tool_node.invoke({"messages": [message_with_single_tool_call]})
    ```

    ```
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id')]}
    ```




??? example "Multiple tool calls"

    ```python hl_lines="17 37"
    from langchain_core.messages import AIMessage
    from langgraph.prebuilt import ToolNode

    # Define tools

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    def get_coolest_cities():
        """Get a list of coolest cities"""
        return "nyc, sf"

    tool_node = ToolNode([get_weather, get_coolest_cities])

    message_with_multiple_tool_calls = AIMessage(
        content="",
        tool_calls=[
            {
                "name": "get_coolest_cities",
                "args": {},
                "id": "tool_call_id_1",
                "type": "tool_call",
            },
            {
                "name": "get_weather",
                "args": {"location": "sf"},
                "id": "tool_call_id_2",
                "type": "tool_call",
            },
        ],
    )

    tool_node.invoke({"messages": [message_with_multiple_tool_calls]})  # (1)!
    ```

    1. `ToolNode` will execute both tools in parallel

    ```
    {
        'messages': [
            ToolMessage(content='nyc, sf', name='get_coolest_cities', tool_call_id='tool_call_id_1'),
            ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='tool_call_id_2')
        ]
    }
    ```




??? example "Use with a chat model"

    ```python hl_lines="11 14 17"
    from langchain.chat_models import init_chat_model
    from langgraph.prebuilt import ToolNode

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([get_weather])  # (1)!


    response_message = model_with_tools.invoke("what's the weather in sf?")
    tool_node.invoke({"messages": [response_message]})
    ```

    1. Use `.bind_tools()` to attach the tool schema to the chat model

    ```
    {'messages': [ToolMessage(content="It's 60 degrees and foggy.", name='get_weather', tool_call_id='toolu_01Pnkgw5JeTRxXAU7tyHT4UW')]}
    ```




??? example "Use in a tool-calling agent"

    This is an example of creating a tool-calling agent from scratch using `ToolNode`. You can also use LangGraph's prebuilt [agent](../agents/agents.md).

    ```python hl_lines="12 15 33"
    from langchain.chat_models import init_chat_model
    from langgraph.prebuilt import ToolNode
    from langgraph.graph import StateGraph, MessagesState, START, END

    def get_weather(location: str):
        """Call to get the current weather."""
        if location.lower() in ["sf", "san francisco"]:
            return "It's 60 degrees and foggy."
        else:
            return "It's 90 degrees and sunny."

    tool_node = ToolNode([get_weather])

    model = init_chat_model(model="claude-3-5-haiku-latest")
    model_with_tools = model.bind_tools([get_weather])

    def should_continue(state: MessagesState):
        messages = state["messages"]
        last_message = messages[-1]
        if last_message.tool_calls:
            return "tools"
        return END

    def call_model(state: MessagesState):
        messages = state["messages"]
        response = model_with_tools.invoke(messages)
        return {"messages": [response]}

    builder = StateGraph(MessagesState)

    # Define the two nodes we will cycle between
    builder.add_node("call_model", call_model)
    builder.add_node("tools", tool_node)

    builder.add_edge(START, "call_model")
    builder.add_conditional_edges("call_model", should_continue, ["tools", END])
    builder.add_edge("tools", "call_model")

    graph = builder.compile()

    graph.invoke({"messages": [{"role": "user", "content": "what's the weather in sf?"}]})
    ```

    ```
    {
        'messages': [
            HumanMessage(content="what's the weather in sf?"),
            AIMessage(
                content=[{'text': "I'll help you check the weather in San Francisco right now.", 'type': 'text'}, {'id': 'toolu_01A4vwUEgBKxfFVc5H3v1CNs', 'input': {'location': 'San Francisco'}, 'name': 'get_weather', 'type': 'tool_use'}],
                tool_calls=[{'name': 'get_weather', 'args': {'location': 'San Francisco'}, 'id': 'toolu_01A4vwUEgBKxfFVc5H3v1CNs', 'type': 'tool_call'}]
            ),
            ToolMessage(content="It's 60 degrees and foggy."),
            AIMessage(content="The current weather in San Francisco is 60 degrees and foggy. Typical San Francisco weather with its famous marine layer!")
        ]
    }
    ```





## Tool customization

For more control over tool behavior, use the `@tool` decorator.

### Parameter descriptions

Auto-generate descriptions from docstrings:

```python hl_lines="1 3"
from langchain_core.tools import tool

@tool("multiply_tool", parse_docstring=True)
def multiply(a: int, b: int) -> int:
    """Multiply two numbers.

    Args:
        a: First operand
        b: Second operand
    """
    return a * b
```





### Explicit input schema

Define schemas using `args_schema`:

```python hl_lines="9"
from pydantic import BaseModel, Field
from langchain_core.tools import tool

class MultiplyInputSchema(BaseModel):
    """Multiply two numbers"""
    a: int = Field(description="First operand")
    b: int = Field(description="Second operand")

@tool("multiply_tool", args_schema=MultiplyInputSchema)
def multiply(a: int, b: int) -> int:
    return a * b
```



### Tool name

Override the default tool name using the first argument or name property:

```python hl_lines="3"
from langchain_core.tools import tool

@tool("multiply_tool")
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```






## Context management

Tools within LangGraph sometimes require context data, such as runtime-only arguments (e.g., user IDs or session details), that should not be controlled by the model. LangGraph provides three methods for managing such context:

| Type                                    | Usage Scenario                           | Mutable | Lifetime                 |
| --------------------------------------- | ---------------------------------------- | ------- | ------------------------ |
| [Configuration](#configuration)         | Static, immutable runtime data           | ❌      | Single invocation        |
| [Short-term memory](#short-term-memory) | Dynamic, changing data during invocation | ✅      | Single invocation        |
| [Long-term memory](#long-term-memory)   | Persistent, cross-session data           | ✅      | Across multiple sessions |

### Configuration

Use configuration when you have **immutable** runtime data that tools require, such as user identifiers. You pass these arguments via [`RunnableConfig`](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) at invocation and access them in the tool:

```python hl_lines="5 13"
from langchain_core.tools import tool
from langchain_core.runnables import RunnableConfig

@tool
def get_user_info(config: RunnableConfig) -> str:
    """Retrieve user information based on user ID."""
    user_id = config["configurable"].get("user_id")
    return "User is John Smith" if user_id == "user_123" else "Unknown user"


# Invocation example with an agent
agent.invoke(
    {"messages": [{"role": "user", "content": "look up user info"}]},
    config={"configurable": {"user_id": "user_123"}}
)
```





??? example "Extended example: Access config in tools"

    ```python hl_lines="6 9 19"
    from langchain_core.runnables import RunnableConfig
    from langchain_core.tools import tool
    from langgraph.prebuilt import create_react_agent

    def get_user_info(
        config: RunnableConfig,
    ) -> str:
        """Look up user info."""
        user_id = config["configurable"].get("user_id")
        return "User is John Smith" if user_id == "user_123" else "Unknown user"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_user_info],
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "look up user information"}]},
        config={"configurable": {"user_id": "user_123"}}
    )
    ```




### Short-term memory

Short-term memory maintains **dynamic** state that changes during a single execution.

To **access** (read) the graph state inside the tools, you can use a special parameter **annotation** — [`InjectedState`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.InjectedState):

```python hl_lines="12"
from typing import Annotated, NotRequired
from langchain_core.tools import tool
from langgraph.prebuilt import InjectedState, create_react_agent
from langgraph.prebuilt.chat_agent_executor import AgentState

class CustomState(AgentState):
    # The user_name field in short-term state
    user_name: NotRequired[str]

@tool
def get_user_name(
    state: Annotated[CustomState, InjectedState]
) -> str:
    """Retrieve the current user-name from state."""
    # Return stored name or a default if not set
    return state.get("user_name", "Unknown user")


# Example agent setup
agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[get_user_name],
    state_schema=CustomState,
)


# Invocation: reads the name from state (initially empty)
agent.invoke({"messages": "what's my name?"})
```





Use a tool that returns a `Command` to **update** `user_name` and append a confirmation message:

```python hl_lines="12 13 14 15 16 17"
from typing import Annotated
from langgraph.types import Command
from langchain_core.messages import ToolMessage
from langchain_core.tools import tool, InjectedToolCallId

@tool
def update_user_name(
    new_name: str,
    tool_call_id: Annotated[str, InjectedToolCallId]
) -> Command:
    """Update user-name in short-term memory."""
    return Command(update={
        "user_name": new_name,
        "messages": [
            ToolMessage(f"Updated user name to {new_name}", tool_call_id=tool_call_id)
        ]
    })
```





!!! important

    If you want to use tools that return `Command` and update graph state, you can either use prebuilt [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent) / [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) components, or implement your own tool-executing node that collects `Command` objects returned by the tools and returns a list of them, e.g.:

    ```python
    def call_tools(state):
        ...
        commands = [tools_by_name[tool_call["name"]].invoke(tool_call) for tool_call in tool_calls]
        return commands
    ```




### Long-term memory

Use [long-term memory](../concepts/memory.md#long-term-memory) to store user-specific or application-specific data across conversations. This is useful for applications like chatbots, where you want to remember user preferences or other information.

To use long-term memory, you need to:

1. [Configure a store](memory/add-memory.md#add-long-term-memory) to persist data across invocations.
2. Access the store from within tools.

To **access** information in the store:

```python hl_lines="4 11 13"
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.config import get_store

@tool
def get_user_info(config: RunnableConfig) -> str:
    """Look up user info."""
    # Same as that provided to `builder.compile(store=store)`
    # or `create_react_agent`
    store = get_store()
    user_id = config["configurable"].get("user_id")
    user_info = store.get(("users",), user_id)
    return str(user_info.value) if user_info else "Unknown user"

builder = StateGraph(...)
...
graph = builder.compile(store=store)
```





??? example "Access long-term memory"

    ```python hl_lines="7 9 22 24 30 36"
    from langchain_core.runnables import RunnableConfig
    from langchain_core.tools import tool
    from langgraph.config import get_store
    from langgraph.prebuilt import create_react_agent
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore() # (1)!

    store.put(  # (2)!
        ("users",),  # (3)!
        "user_123",  # (4)!
        {
            "name": "John Smith",
            "language": "English",
        } # (5)!
    )

    @tool
    def get_user_info(config: RunnableConfig) -> str:
        """Look up user info."""
        # Same as that provided to `create_react_agent`
        store = get_store() # (6)!
        user_id = config["configurable"].get("user_id")
        user_info = store.get(("users",), user_id) # (7)!
        return str(user_info.value) if user_info else "Unknown user"

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[get_user_info],
        store=store # (8)!
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "look up user information"}]},
        config={"configurable": {"user_id": "user_123"}}
    )
    ```

    1. The `InMemoryStore` is a store that stores data in memory. In a production setting, you would typically use a database or other persistent storage. Please review the [store documentation][../reference/store.md) for more options. If you're deploying with **LangGraph Platform**, the platform will provide a production-ready store for you.
    2. For this example, we write some sample data to the store using the `put` method. Please see the [BaseStore.put](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore.put) API reference for more details.
    3. The first argument is the namespace. This is used to group related data together. In this case, we are using the `users` namespace to group user data.
    4. A key within the namespace. This example uses a user ID for the key.
    5. The data that we want to store for the given user.
    6. The `get_store` function is used to access the store. You can call it from anywhere in your code, including tools and prompts. This function returns the store that was passed to the agent when it was created.
    7. The `get` method is used to retrieve data from the store. The first argument is the namespace, and the second argument is the key. This will return a `StoreValue` object, which contains the value and metadata about the value.
    8. The `store` is passed to the agent. This enables the agent to access the store when running tools. You can also use the `get_store` function to access the store from anywhere in your code.




To **update** information in the store:

```python hl_lines="4 11 13"
from langchain_core.runnables import RunnableConfig
from langchain_core.tools import tool
from langgraph.graph import StateGraph
from langgraph.config import get_store

@tool
def save_user_info(user_info: str, config: RunnableConfig) -> str:
    """Save user info."""
    # Same as that provided to `builder.compile(store=store)`
    # or `create_react_agent`
    store = get_store()
    user_id = config["configurable"].get("user_id")
    store.put(("users",), user_id, user_info)
    return "Successfully saved user info."

builder = StateGraph(...)
...
graph = builder.compile(store=store)
```





??? example "Update long-term memory"

    ```python hl_lines="18 20 26 32"
    from typing_extensions import TypedDict

    from langchain_core.tools import tool
    from langgraph.config import get_store
    from langchain_core.runnables import RunnableConfig
    from langgraph.prebuilt import create_react_agent
    from langgraph.store.memory import InMemoryStore

    store = InMemoryStore() # (1)!

    class UserInfo(TypedDict): # (2)!
        name: str

    @tool
    def save_user_info(user_info: UserInfo, config: RunnableConfig) -> str: # (3)!
        """Save user info."""
        # Same as that provided to `create_react_agent`
        store = get_store() # (4)!
        user_id = config["configurable"].get("user_id")
        store.put(("users",), user_id, user_info) # (5)!
        return "Successfully saved user info."

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[save_user_info],
        store=store
    )

    # Run the agent
    agent.invoke(
        {"messages": [{"role": "user", "content": "My name is John Smith"}]},
        config={"configurable": {"user_id": "user_123"}} # (6)!
    )

    # You can access the store directly to get the value
    store.get(("users",), "user_123").value
    ```

    1. The `InMemoryStore` is a store that stores data in memory. In a production setting, you would typically use a database or other persistent storage. Please review the [store documentation](../reference/store.md) for more options. If you're deploying with **LangGraph Platform**, the platform will provide a production-ready store for you.
    2. The `UserInfo` class is a `TypedDict` that defines the structure of the user information. The LLM will use this to format the response according to the schema.
    3. The `save_user_info` function is a tool that allows an agent to update user information. This could be useful for a chat application where the user wants to update their profile information.
    4. The `get_store` function is used to access the store. You can call it from anywhere in your code, including tools and prompts. This function returns the store that was passed to the agent when it was created.
    5. The `put` method is used to store data in the store. The first argument is the namespace, and the second argument is the key. This will store the user information in the store.
    6. The `user_id` is passed in the config. This is used to identify the user whose information is being updated.





## Advanced tool features

### Immediate return

Use `return_direct=True` to immediately return a tool's result without executing additional logic.

This is useful for tools that should not trigger further processing or tool calls, allowing you to return results directly to the user.

```python hl_lines="1"
@tool(return_direct=True)
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b
```





??? example "Extended example: Using return_direct in a prebuilt agent"

    ```python hl_lines="4"
    from langchain_core.tools import tool
    from langgraph.prebuilt import create_react_agent

    @tool(return_direct=True)
    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    agent = create_react_agent(
        model="anthropic:claude-3-7-sonnet-latest",
        tools=[add]
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "what's 3 + 5?"}]}
    )
    ```




!!! important "Using without prebuilt components"

    If you are building a custom workflow and are not relying on `create_react_agent` or `ToolNode`, you will also
    need to implement the control flow to handle `return_direct=True`.




### Force tool use

If you need to force a specific tool to be used, you will need to configure this at the **model** level using the `tool_choice` parameter in the bind_tools method.

Force specific tool usage via tool_choice:

```python hl_lines="11"
@tool(return_direct=True)
def greet(user_name: str) -> int:
    """Greet user."""
    return f"Hello {user_name}!"

tools = [greet]

configured_model = model.bind_tools(
    tools,
    # Force the use of the 'greet' tool
    tool_choice={"type": "tool", "name": "greet"}
)
```





??? example "Extended example: Force tool usage in an agent"

    To force the agent to use specific tools, you can set the `tool_choice` option in `model.bind_tools()`:

    ```python hl_lines="3 11"
    from langchain_core.tools import tool

    @tool(return_direct=True)
    def greet(user_name: str) -> int:
        """Greet user."""
        return f"Hello {user_name}!"

    tools = [greet]

    agent = create_react_agent(
        model=model.bind_tools(tools, tool_choice={"type": "tool", "name": "greet"}),
        tools=tools
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "Hi, I am Bob"}]}
    )
    ```




!!! Warning "Avoid infinite loops"

    Forcing tool usage without stopping conditions can create infinite loops. Use one of the following safeguards:

    - Mark the tool with [`return_direct=True`](#immediate-return) to end the loop after execution.
    - Set [`recursion_limit`](../concepts/low_level.md#recursion-limit) to restrict the number of execution steps.




!!! tip "Tool choice configuration"

    The `tool_choice` parameter is used to configure which tool should be used by the model when it decides to call a tool. This is useful when you want to ensure that a specific tool is always called for a particular task or when you want to override the model's default behavior of choosing a tool based on its internal logic.

    Note that not all models support this feature, and the exact configuration may vary depending on the model you are using.

### Disable parallel calls

For supported providers, you can disable parallel tool calling by setting `parallel_tool_calls=False` via the `model.bind_tools()` method:

```python hl_lines="3"
model.bind_tools(
    tools,
    parallel_tool_calls=False
)
```





??? example "Extended example: disable parallel tool calls in a prebuilt agent"

    ```python hl_lines="15"
    from langchain.chat_models import init_chat_model

    def add(a: int, b: int) -> int:
        """Add two numbers"""
        return a + b

    def multiply(a: int, b: int) -> int:
        """Multiply two numbers."""
        return a * b

    model = init_chat_model("anthropic:claude-3-5-sonnet-latest", temperature=0)
    tools = [add, multiply]
    agent = create_react_agent(
        # disable parallel tool calls
        model=model.bind_tools(tools, parallel_tool_calls=False),
        tools=tools
    )

    agent.invoke(
        {"messages": [{"role": "user", "content": "what's 3 + 5 and 4 * 7?"}]}
    )
    ```




### Handle errors

LangGraph provides built-in error handling for tool execution through the prebuilt [ToolNode](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode) component, used both independently and in prebuilt agents.

By **default**, `ToolNode` catches exceptions raised during tool execution and returns them as `ToolMessage` objects with a status indicating an error.

```python
from langchain_core.messages import AIMessage
from langgraph.prebuilt import ToolNode

def multiply(a: int, b: int) -> int:
    if a == 42:
        raise ValueError("The ultimate error")
    return a * b


# Default error handling (enabled by default)
tool_node = ToolNode([multiply])

message = AIMessage(
    content="",
    tool_calls=[{
        "name": "multiply",
        "args": {"a": 42, "b": 7},
        "id": "tool_call_id",
        "type": "tool_call"
    }]
)

result = tool_node.invoke({"messages": [message]})
```

Output:

```pycon
{'messages': [
    ToolMessage(
        content="Error: ValueError('The ultimate error')\n Please fix your mistakes.",
        name='multiply',
        tool_call_id='tool_call_id',
        status='error'
    )
]}
```





#### Disable error handling

To propagate exceptions directly, disable error handling:

```python
tool_node = ToolNode([multiply], handle_tool_errors=False)
```





With error handling disabled, exceptions raised by tools will propagate up, requiring explicit management.

#### Custom error messages

Provide a custom error message by setting the error handling parameter to a string:

```python
tool_node = ToolNode(
    [multiply],
    handle_tool_errors="Can't use 42 as the first operand, please switch operands!"
)
```

Example output:

```python
{'messages': [
    ToolMessage(
        content="Can't use 42 as the first operand, please switch operands!",
        name='multiply',
        tool_call_id='tool_call_id',
        status='error'
    )
]}
```





#### Error handling in agents

Error handling in prebuilt agents (`create_react_agent`) leverages `ToolNode`:

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=[multiply]
)


# Default error handling
agent.invoke({"messages": [{"role": "user", "content": "what's 42 x 7?"}]})
```

To disable or customize error handling in prebuilt agents, explicitly pass a configured `ToolNode`:

```python
custom_tool_node = ToolNode(
    [multiply],
    handle_tool_errors="Cannot use 42 as a first operand!"
)

agent_custom = create_react_agent(
    model="anthropic:claude-3-7-sonnet-latest",
    tools=custom_tool_node
)

agent_custom.invoke({"messages": [{"role": "user", "content": "what's 42 x 7?"}]})
```





### Handle large numbers of tools

As the number of available tools grows, you may want to limit the scope of the LLM's selection, to decrease token consumption and to help manage sources of error in LLM reasoning.

To address this, you can dynamically adjust the tools available to a model by retrieving relevant tools at runtime using semantic search.

See [`langgraph-bigtool`](https://github.com/langchain-ai/langgraph-bigtool) prebuilt library for a ready-to-use implementation.


## Prebuilt tools

### LLM provider tools

You can use prebuilt tools from model providers by passing a dictionary with tool specs to the `tools` parameter of `create_react_agent`. For example, to use the `web_search_preview` tool from OpenAI:

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model="openai:gpt-4o-mini",
    tools=[{"type": "web_search_preview"}]
)
response = agent.invoke(
    {"messages": ["What was a positive news story from today?"]}
)
```

Please consult the documentation for the specific model you are using to see which tools are available and how to use them.




### LangChain tools

Additionally, LangChain supports a wide range of prebuilt tool integrations for interacting with APIs, databases, file systems, web data, and more. These tools extend the functionality of agents and enable rapid development.

You can browse the full list of available integrations in the [LangChain integrations directory](https://python.langchain.com/docs/integrations/tools/).

Some commonly used tool categories include:

- **Search**: Bing, SerpAPI, Tavily
- **Code interpreters**: Python REPL, Node.js REPL
- **Databases**: SQL, MongoDB, Redis
- **Web data**: Web scraping and browsing
- **APIs**: OpenWeatherMap, NewsAPI, and others

These integrations can be configured and added to your agents using the same `tools` parameter shown in the examples above.





---
how-tos/cross-thread-persistence-functional.ipynb
---


# How to add cross-thread persistence (functional API)

!!! info "Prerequisites"

    This guide assumes familiarity with the following:
    
    - <a href="../../concepts/functional_api/">Functional API</a>
    - <a href="../../concepts/persistence/">Persistence</a>
    - <a href="../../concepts/memory/">Memory</a>
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)

LangGraph allows you to persist data across **different <a href="../../concepts/persistence/#threads">threads</a>**. For instance, you can store information about users (their names or preferences) in a shared (cross-thread) memory and reuse them in the new threads (e.g., new conversations).

When using the <a href="../../concepts/functional_api/">functional API</a>, you can set it up to store and retrieve memories by using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface:

1. Create an instance of a `Store`

    ```python
    from langgraph.store.memory import InMemoryStore, BaseStore
    
    store = InMemoryStore()
    ```

2. Pass the `store` instance to the `entrypoint()` decorator and expose `store` parameter in the function signature:

    ```python
    from langgraph.func import entrypoint

    @entrypoint(store=store)
    def workflow(inputs: dict, store: BaseStore):
        my_task(inputs).result()
        ...
    ```
    
In this guide, we will show how to construct and use a workflow that has a shared memory implemented using the [Store](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) interface.

!!! note Note

    Support for the [`Store`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.32`.

    Support for __index__ and __query__ arguments of the [`Store`](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore) API that is used in this guide was added in LangGraph `v0.2.54`.

!!! tip "Note"

    If you need to add cross-thread persistence to a `StateGraph`, check out this <a href="../cross-thread-persistence">how-to guide</a>.


## Setup

First, let's install the required packages and set our API keys


```shell
pip install -U langchain_anthropic langchain_openai langgraph
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("ANTHROPIC_API_KEY")
_set_env("OPENAI_API_KEY")
```

!!! tip "Set up [LangSmith](https://smith.langchain.com) for LangGraph development"

    Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started [here](https://docs.smith.langchain.com)


## Example: simple chatbot with long-term memory

### Define store

In this example we will create a workflow that will be able to retrieve information about a user's preferences. We will do so by defining an `InMemoryStore` - an object that can store data in memory and query that data.

When storing objects using the `Store` interface you define two things:

* the namespace for the object, a tuple (similar to directories)
* the object key (similar to filenames)

In our example, we'll be using `("memories", <user_id>)` as namespace and random UUID as key for each new memory.

Importantly, to determine the user, we will be passing `user_id` via the config keyword argument of the node function.

Let's first define our store!


```python
from langgraph.store.memory import InMemoryStore
from langchain_openai import OpenAIEmbeddings

in_memory_store = InMemoryStore(
    index={
        "embed": OpenAIEmbeddings(model="text-embedding-3-small"),
        "dims": 1536,
    }
)
```

### Create workflow


```python
import uuid

from langchain_anthropic import ChatAnthropic
from langchain_core.runnables import RunnableConfig
from langchain_core.messages import BaseMessage
from langgraph.func import entrypoint, task
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.store.base import BaseStore


model = ChatAnthropic(model="claude-3-5-sonnet-latest")


@task
def call_model(messages: list[BaseMessage], memory_store: BaseStore, user_id: str):
    namespace = ("memories", user_id)
    last_message = messages[-1]
    memories = memory_store.search(namespace, query=str(last_message.content))
    info = "\n".join([d.value["data"] for d in memories])
    system_msg = f"You are a helpful assistant talking to the user. User info: {info}"

    # Store new memories if the user asks the model to remember
    if "remember" in last_message.content.lower():
        memory = "User name is Bob"
        memory_store.put(namespace, str(uuid.uuid4()), {"data": memory})

    response = model.invoke([{"role": "system", "content": system_msg}] + messages)
    return response



# NOTE: we're passing the store object here when creating a workflow via entrypoint()
@entrypoint(checkpointer=InMemorySaver(), store=in_memory_store)
def workflow(
    inputs: list[BaseMessage],
    *,
    previous: list[BaseMessage],
    config: RunnableConfig,
    store: BaseStore,
):
    user_id = config["configurable"]["user_id"]
    previous = previous or []
    inputs = add_messages(previous, inputs)
    response = call_model(inputs, store, user_id).result()
    return entrypoint.final(value=response, save=add_messages(inputs, response))
```

!!! note Note

    If you're using LangGraph Cloud or LangGraph Studio, you __don't need__ to pass store to the entrypoint decorator, since it's done automatically.

### Run the workflow!

Now let's specify a user ID in the config and tell the model our name:


```python
config = {"configurable": {"thread_id": "1", "user_id": "1"}}
input_message = {"role": "user", "content": "Hi! Remember: my name is Bob"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Hello Bob! Nice to meet you. I'll remember that your name is Bob. How can I help you today?
```

```python
config = {"configurable": {"thread_id": "2", "user_id": "1"}}
input_message = {"role": "user", "content": "what is my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Your name is Bob.
```
We can now inspect our in-memory store and verify that we have in fact saved the memories for the user:


```python
for memory in in_memory_store.search(("memories", "1")):
    print(memory.value)
```
```output
{'data': 'User name is Bob'}
```
Let's now run the workflow for another user to verify that the memories about the first user are self contained:


```python
config = {"configurable": {"thread_id": "3", "user_id": "2"}}
input_message = {"role": "user", "content": "what is my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

I don't have any information about your name. I can only see our current conversation without any prior context or personal details about you. If you'd like me to know your name, feel free to tell me!
```

---
how-tos/multi-agent-network-functional.ipynb
---


# How to build a multi-agent network (functional API)

!!! info "Prerequisites" 
    This guide assumes familiarity with the following:

    - <a href="../../concepts/multi_agent">Multi-agent systems</a>
    - <a href="../../concepts/functional_api">Functional API</a>
    - <a href="../../concepts/low_level/#command">Command</a>
    - <a href="../../concepts/low_level/">LangGraph Glossary</a>

In this how-to guide we will demonstrate how to implement a <a href="../../concepts/multi_agent#network">multi-agent network</a> architecture where each agent can communicate with every other agent (many-to-many connections) and can decide which agent to call next. We will be using <a href="../../concepts/functional_api">functional API</a> — individual agents will be defined as tasks and the agent handoffs will be defined in the main [entrypoint()][langgraph.func.entrypoint]:

```python
from langgraph.func import entrypoint
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool



# Define a tool to signal intent to hand off to a different agent
@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"



# define an agent
travel_advisor_tools = [transfer_to_hotel_advisor, ...]
travel_advisor = create_react_agent(model, travel_advisor_tools)



# define a task that calls an agent
@task
def call_travel_advisor(messages):
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]



# define the multi-agent network workflow
@entrypoint()
def workflow(messages):
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        messages = messages + agent_messages
        call_active_agent = get_next_agent(messages)
    return messages
```


## Setup

First, let's install the required packages


```shell
pip install -U langgraph langchain-anthropic
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("ANTHROPIC_API_KEY")
```
```output
ANTHROPIC_API_KEY:  ········
```
<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>


## Travel agent example

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

* `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
* `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.

This is a fully-connected network - every agent can talk to any other agent. 

First, let's create some of the tools that the agents will be using:


```python
import random
from typing_extensions import Literal
from langchain_core.tools import tool


@tool
def get_travel_recommendations():
    """Get recommendation for travel destinations"""
    return random.choice(["aruba", "turks and caicos"])


@tool
def get_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
    """Get hotel recommendations for a given destination."""
    return {
        "aruba": [
            "The Ritz-Carlton, Aruba (Palm Beach)"
            "Bucuti & Tara Beach Resort (Eagle Beach)"
        ],
        "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
    }[location]


@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"


@tool(return_direct=True)
def transfer_to_travel_advisor():
    """Ask travel advisor agent for help."""
    return "Successfully transferred to travel advisor"
```

!!! note "Transfer tools"

    You might have noticed that we're using `@tool(return_direct=True)` in the transfer tools. This is done so that individual agents (e.g., `travel_advisor`) can exit the ReAct loop early once these tools are called. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent. 
    
    **NOTE**: This is meant to work with the prebuilt [`create_react_agent`][langgraph.prebuilt.chat_agent_executor.create_react_agent] -- if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `return_direct`.

Now let's define our agent tasks and combine them into a single multi-agent network workflow:


```python
from langchain_core.messages import AIMessage
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task

model = ChatAnthropic(model="claude-3-5-sonnet-latest")


# Define travel advisor ReAct agent
travel_advisor_tools = [
    get_travel_recommendations,
    transfer_to_hotel_advisor,
]
travel_advisor = create_react_agent(
    model,
    travel_advisor_tools,
    prompt=(
        "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
        "If you need hotel recommendations, ask 'hotel_advisor' for help. "
        "You MUST include human-readable response before transferring to another agent."
    ),
)


@task
def call_travel_advisor(messages):
    # You can also add additional logic like changing the input to the agent / output from the agent, etc.
    # NOTE: we're invoking the ReAct agent with the full history of messages in the state
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]



# Define hotel advisor ReAct agent
hotel_advisor_tools = [get_hotel_recommendations, transfer_to_travel_advisor]
hotel_advisor = create_react_agent(
    model,
    hotel_advisor_tools,
    prompt=(
        "You are a hotel expert that can provide hotel recommendations for a given destination. "
        "If you need help picking travel destinations, ask 'travel_advisor' for help."
        "You MUST include human-readable response before transferring to another agent."
    ),
)


@task
def call_hotel_advisor(messages):
    response = hotel_advisor.invoke({"messages": messages})
    return response["messages"]


@entrypoint()
def workflow(messages):
    messages = add_messages([], messages)

    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        messages = add_messages(messages, agent_messages)
        ai_msg = next(m for m in reversed(agent_messages) if isinstance(m, AIMessage))
        if not ai_msg.tool_calls:
            break

        tool_call = ai_msg.tool_calls[-1]
        if tool_call["name"] == "transfer_to_travel_advisor":
            call_active_agent = call_travel_advisor
        elif tool_call["name"] == "transfer_to_hotel_advisor":
            call_active_agent = call_hotel_advisor
        else:
            raise ValueError(f"Expected transfer tool, got '{tool_call['name']}'")

    return messages
```

Lastly, let's define a helper to render the agent outputs:


```python
from langchain_core.messages import convert_to_messages


def pretty_print_messages(update):
    if isinstance(update, tuple):
        ns, update = update
        # skip parent graph updates in the printouts
        if len(ns) == 0:
            return

        graph_id = ns[-1].split(":")[0]
        print(f"Update from subgraph {graph_id}:")
        print("\n")

    for node_name, node_update in update.items():
        print(f"Update from node {node_name}:")
        print("\n")

        for m in convert_to_messages(node_update["messages"]):
            m.pretty_print()
        print("\n")
```

Let's test it out using the same input as our original multi-agent system:


```python
for chunk in workflow.stream(
    [
        {
            "role": "user",
            "content": "i wanna go somewhere warm in the caribbean. pick one destination and give me hotel recommendations",
        }
    ],
    subgraphs=True,
):
    pretty_print_messages(chunk)
```
```output
Update from subgraph call_travel_advisor:


Update from node agent:


================================== Ai Message ==================================

[{'text': "I'll help you find a warm Caribbean destination and then get some hotel recommendations for you.\n\nLet me first get some destination recommendations for the Caribbean region.", 'type': 'text'}, {'id': 'toolu_015vT8PkPq1VXvjrDvSpWUwJ', 'input': {}, 'name': 'get_travel_recommendations', 'type': 'tool_use'}]
Tool Calls:
  get_travel_recommendations (toolu_015vT8PkPq1VXvjrDvSpWUwJ)
 Call ID: toolu_015vT8PkPq1VXvjrDvSpWUwJ
  Args:


Update from subgraph call_travel_advisor:


Update from node tools:


================================= Tool Message =================================
Name: get_travel_recommendations

turks and caicos


Update from subgraph call_travel_advisor:


Update from node agent:


================================== Ai Message ==================================

[{'text': "Based on the recommendation, I suggest Turks and Caicos! This beautiful British Overseas Territory is known for its stunning white-sand beaches, crystal-clear turquoise waters, and year-round warm weather. Grace Bay Beach in Providenciales is consistently ranked among the world's best beaches. The islands offer excellent snorkeling, diving, and water sports opportunities, plus a relaxed Caribbean atmosphere.\n\nNow, let me connect you with our hotel advisor to get some specific hotel recommendations for Turks and Caicos.", 'type': 'text'}, {'id': 'toolu_01JY7pNNWFuaWoe9ymxFYiPV', 'input': {}, 'name': 'transfer_to_hotel_advisor', 'type': 'tool_use'}]
Tool Calls:
  transfer_to_hotel_advisor (toolu_01JY7pNNWFuaWoe9ymxFYiPV)
 Call ID: toolu_01JY7pNNWFuaWoe9ymxFYiPV
  Args:


Update from subgraph call_travel_advisor:


Update from node tools:


================================= Tool Message =================================
Name: transfer_to_hotel_advisor

Successfully transferred to hotel advisor


Update from subgraph call_hotel_advisor:


Update from node agent:


================================== Ai Message ==================================

[{'text': 'Let me get some hotel recommendations for Turks and Caicos:', 'type': 'text'}, {'id': 'toolu_0129ELa7jFocn16bowaGNapg', 'input': {'location': 'turks and caicos'}, 'name': 'get_hotel_recommendations', 'type': 'tool_use'}]
Tool Calls:
  get_hotel_recommendations (toolu_0129ELa7jFocn16bowaGNapg)
 Call ID: toolu_0129ELa7jFocn16bowaGNapg
  Args:
    location: turks and caicos


Update from subgraph call_hotel_advisor:


Update from node tools:


================================= Tool Message =================================
Name: get_hotel_recommendations

["Grace Bay Club", "COMO Parrot Cay"]


Update from subgraph call_hotel_advisor:


Update from node agent:


================================== Ai Message ==================================

Here are two excellent hotel options in Turks and Caicos:

1. Grace Bay Club: This luxury resort is located on the world-famous Grace Bay Beach. It offers all-oceanfront suites, exceptional dining options, and personalized service. The resort features adult-only and family-friendly sections, making it perfect for any type of traveler.

2. COMO Parrot Cay: This exclusive private island resort offers the ultimate luxury escape. It's known for its pristine beach, world-class spa, and holistic wellness programs. The resort provides an intimate, secluded experience with top-notch amenities and service.

Would you like more specific information about either of these properties or would you like to explore hotels in another destination?
```
Voila - `travel_advisor` picks a destination and then makes a decision to call `hotel_advisor` for more info!


---
how-tos/multi-agent-multi-turn-convo-functional.ipynb
---


# How to add multi-turn conversation in a multi-agent application (functional API)

!!! info "Prerequisites"
    This guide assumes familiarity with the following:

    - <a href="../../concepts/multi_agent">Multi-agent systems</a>
    - <a href="../../concepts/human_in_the_loop">Human-in-the-loop</a>
    - <a href="../../concepts/functional_api">Functional API</a>
    - <a href="../../concepts/low_level/#command">Command</a>
    - <a href="../../concepts/low_level/">LangGraph Glossary</a>


In this how-to guide, we’ll build an application that allows an end-user to engage in a *multi-turn conversation* with one or more agents. We'll create a node that uses an <a href="../../reference/types/#langgraph.types.interrupt">`interrupt`</a> to collect user input and routes back to the **active** agent.

The agents will be implemented as tasks in a workflow that executes agent steps and determines the next action:

1. **Wait for user input** to continue the conversation, or
2. **Route to another agent** (or back to itself, such as in a loop) via a <a href="../../concepts/multi_agent/#handoffs">**handoff**</a>.

```python
from langgraph.func import entrypoint, task
from langgraph.prebuilt import create_react_agent
from langchain_core.tools import tool
from langgraph.types import interrupt



# Define a tool to signal intent to hand off to a different agent

# Note: this is not using Command(goto) syntax for navigating to different agents:

# `workflow()` below handles the handoffs explicitly
@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"



# define an agent
travel_advisor_tools = [transfer_to_hotel_advisor, ...]
travel_advisor = create_react_agent(model, travel_advisor_tools)



# define a task that calls an agent
@task
def call_travel_advisor(messages):
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]



# define the multi-agent network workflow
@entrypoint(checkpointer)
def workflow(messages):
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        ai_msg = get_last_ai_msg(agent_messages)
        if not ai_msg.tool_calls:
            user_input = interrupt(value="Ready for user input.")
            messages = messages + [{"role": "user", "content": user_input}]
            continue

        messages = messages + agent_messages
        call_active_agent = get_next_agent(messages)
    return entrypoint.final(value=agent_messages[-1], save=messages)
```


## Setup

First, let's install the required packages


```python

# %%capture --no-stderr

# %pip install -U langgraph langchain-anthropic
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("ANTHROPIC_API_KEY")
```
```output
ANTHROPIC_API_KEY:  ········
```
<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>

In this example we will build a team of travel assistant agents that can communicate with each other.

We will create 2 agents:

* `travel_advisor`: can help with travel destination recommendations. Can ask `hotel_advisor` for help.
* `hotel_advisor`: can help with hotel recommendations. Can ask `travel_advisor` for help.

This is a fully-connected network - every agent can talk to any other agent. 


```python
import random
from typing_extensions import Literal
from langchain_core.tools import tool


@tool
def get_travel_recommendations():
    """Get recommendation for travel destinations"""
    return random.choice(["aruba", "turks and caicos"])


@tool
def get_hotel_recommendations(location: Literal["aruba", "turks and caicos"]):
    """Get hotel recommendations for a given destination."""
    return {
        "aruba": [
            "The Ritz-Carlton, Aruba (Palm Beach)"
            "Bucuti & Tara Beach Resort (Eagle Beach)"
        ],
        "turks and caicos": ["Grace Bay Club", "COMO Parrot Cay"],
    }[location]


@tool(return_direct=True)
def transfer_to_hotel_advisor():
    """Ask hotel advisor agent for help."""
    return "Successfully transferred to hotel advisor"


@tool(return_direct=True)
def transfer_to_travel_advisor():
    """Ask travel advisor agent for help."""
    return "Successfully transferred to travel advisor"
```

!!! note "Transfer tools"

    You might have noticed that we're using `@tool(return_direct=True)` in the transfer tools. This is done so that individual agents (e.g., `travel_advisor`) can exit the ReAct loop early once these tools are called. This is the desired behavior, as we want to detect when the agent calls this tool and hand control off _immediately_ to a different agent. 
    
    **NOTE**: This is meant to work with the prebuilt [`create_react_agent`][langgraph.prebuilt.chat_agent_executor.create_react_agent] -- if you are building a custom agent, make sure to manually add logic for handling early exit for tools that are marked with `return_direct`.

Let's now create our agents using the prebuilt [`create_react_agent`][langgraph.prebuilt.chat_agent_executor.create_react_agent] and our multi-agent workflow. Note that will be calling [`interrupt`][langgraph.types.interrupt] every time after we get the final response from each of the agents.


```python
import uuid

from langchain_core.messages import AIMessage
from langchain_anthropic import ChatAnthropic
from langgraph.prebuilt import create_react_agent
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import interrupt, Command

model = ChatAnthropic(model="claude-3-5-sonnet-latest")


# Define travel advisor ReAct agent
travel_advisor_tools = [
    get_travel_recommendations,
    transfer_to_hotel_advisor,
]
travel_advisor = create_react_agent(
    model,
    travel_advisor_tools,
    prompt=(
        "You are a general travel expert that can recommend travel destinations (e.g. countries, cities, etc). "
        "If you need hotel recommendations, ask 'hotel_advisor' for help. "
        "You MUST include human-readable response before transferring to another agent."
    ),
)


@task
def call_travel_advisor(messages):
    # You can also add additional logic like changing the input to the agent / output from the agent, etc.
    # NOTE: we're invoking the ReAct agent with the full history of messages in the state
    response = travel_advisor.invoke({"messages": messages})
    return response["messages"]



# Define hotel advisor ReAct agent
hotel_advisor_tools = [get_hotel_recommendations, transfer_to_travel_advisor]
hotel_advisor = create_react_agent(
    model,
    hotel_advisor_tools,
    prompt=(
        "You are a hotel expert that can provide hotel recommendations for a given destination. "
        "If you need help picking travel destinations, ask 'travel_advisor' for help."
        "You MUST include human-readable response before transferring to another agent."
    ),
)


@task
def call_hotel_advisor(messages):
    response = hotel_advisor.invoke({"messages": messages})
    return response["messages"]


checkpointer = InMemorySaver()


def string_to_uuid(input_string):
    return str(uuid.uuid5(uuid.NAMESPACE_URL, input_string))


@entrypoint(checkpointer=checkpointer)
def multi_turn_graph(messages, previous):
    previous = previous or []
    messages = add_messages(previous, messages)
    call_active_agent = call_travel_advisor
    while True:
        agent_messages = call_active_agent(messages).result()
        messages = add_messages(messages, agent_messages)
        # Find the last AI message
        # If one of the handoff tools is called, the last message returned
        # by the agent will be a ToolMessage because we set them to have
        # "return_direct=True". This means that the last AIMessage will
        # have tool calls.
        # Otherwise, the last returned message will be an AIMessage with
        # no tool calls, which means we are ready for new input.
        ai_msg = next(m for m in reversed(agent_messages) if isinstance(m, AIMessage))
        if not ai_msg.tool_calls:
            user_input = interrupt(value="Ready for user input.")
            # Add user input as a human message
            # NOTE: we generate unique ID for the human message based on its content
            # it's important, since on subsequent invocations previous user input (interrupt) values
            # will be looked up again and we will attempt to add them again here
            # `add_messages` deduplicates messages based on the ID, ensuring correct message history
            human_message = {
                "role": "user",
                "content": user_input,
                "id": string_to_uuid(user_input),
            }
            messages = add_messages(messages, [human_message])
            continue

        tool_call = ai_msg.tool_calls[-1]
        if tool_call["name"] == "transfer_to_hotel_advisor":
            call_active_agent = call_hotel_advisor
        elif tool_call["name"] == "transfer_to_travel_advisor":
            call_active_agent = call_travel_advisor
        else:
            raise ValueError(f"Expected transfer tool, got '{tool_call['name']}'")

    return entrypoint.final(value=agent_messages[-1], save=messages)
```


## Test multi-turn conversation

Let's test a multi turn conversation with this application.


```python
thread_config = {"configurable": {"thread_id": uuid.uuid4()}}

inputs = [
    # 1st round of conversation,
    {
        "role": "user",
        "content": "i wanna go somewhere warm in the caribbean",
        "id": str(uuid.uuid4()),
    },
    # Since we're using `interrupt`, we'll need to resume using the Command primitive.
    # 2nd round of conversation,
    Command(
        resume="could you recommend a nice hotel in one of the areas and tell me which area it is."
    ),
    # 3rd round of conversation,
    Command(
        resume="i like the first one. could you recommend something to do near the hotel?"
    ),
]

for idx, user_input in enumerate(inputs):
    print()
    print(f"--- Conversation Turn {idx + 1} ---")
    print()
    print(f"User: {user_input}")
    print()
    for update in multi_turn_graph.stream(
        user_input,
        config=thread_config,
        stream_mode="updates",
    ):
        for node_id, value in update.items():
            if isinstance(value, list) and value:
                last_message = value[-1]
                if isinstance(last_message, dict) or last_message.type != "ai":
                    continue
                print(f"{node_id}: {last_message.content}")
```
```output
--- Conversation Turn 1 ---

User: {'role': 'user', 'content': 'i wanna go somewhere warm in the caribbean', 'id': 'f48d82a7-7efa-43f5-ad4c-541758c95f61'}

call_travel_advisor: Based on the recommendations, Aruba would be an excellent choice for your Caribbean getaway! Known as "One Happy Island," Aruba offers:
- Year-round warm weather with consistent temperatures around 82°F (28°C)
- Beautiful white sand beaches like Eagle Beach and Palm Beach
- Crystal clear waters perfect for swimming and snorkeling
- Minimal rainfall and location outside the hurricane belt
- Rich culture blending Dutch and Caribbean influences
- Various activities from water sports to desert-like landscape exploration
- Excellent dining and shopping options

Would you like me to help you find suitable accommodations in Aruba? I can transfer you to our hotel advisor who can recommend specific hotels based on your preferences.

--- Conversation Turn 2 ---

User: Command(resume='could you recommend a nice hotel in one of the areas and tell me which area it is.')

call_hotel_advisor: I can recommend two excellent options in different areas:

1. The Ritz-Carlton, Aruba - Located in Palm Beach
- Luxury beachfront resort
- Located in the vibrant Palm Beach area, known for its lively atmosphere
- Close to restaurants, shopping, and nightlife
- Perfect for those who want a more active vacation with plenty of amenities nearby

2. Bucuti & Tara Beach Resort - Located in Eagle Beach
- Adults-only boutique resort
- Situated on the quieter Eagle Beach
- Known for its romantic atmosphere and excellent service
- Ideal for couples seeking a more peaceful, intimate setting

Would you like more specific information about either of these properties or their locations?

--- Conversation Turn 3 ---

User: Command(resume='i like the first one. could you recommend something to do near the hotel?')

call_travel_advisor: Near The Ritz-Carlton in Palm Beach, here are some popular activities you can enjoy:

1. Palm Beach Strip - Take a walk along this bustling strip filled with restaurants, shops, and bars
2. Visit the Bubali Bird Sanctuary - Just a short distance away
3. Try your luck at the Stellaris Casino - Located right in The Ritz-Carlton
4. Water Sports at Palm Beach - Right in front of the hotel you can:
   - Go parasailing
   - Try jet skiing
   - Take a sunset sailing cruise
5. Visit the Palm Beach Plaza Mall - High-end shopping just a short walk away
6. Enjoy dinner at Madame Janette's - One of Aruba's most famous restaurants nearby

Would you like more specific information about any of these activities or other suggestions in the area?
```

---
how-tos/persistence-functional.ipynb
---


# How to add thread-level persistence (functional API)

!!! info "Prerequisites"

    This guide assumes familiarity with the following:
    
    - <a href="../../concepts/functional_api/">Functional API</a>
    - <a href="../../concepts/persistence/">Persistence</a>
    - <a href="../../concepts/memory/">Memory</a>
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)

!!! info "Not needed for LangGraph API users"

    If you're using the LangGraph API, you needn't manually implement a checkpointer. The API automatically handles checkpointing for you. This guide is relevant when implementing LangGraph in your own custom server.

Many AI applications need memory to share context across multiple interactions on the same <a href="../../concepts/persistence#threads">thread</a> (e.g., multiple turns of a conversation). In LangGraph functional API, this kind of memory can be added to any [entrypoint()][langgraph.func.entrypoint] workflow using [thread-level persistence](https://langchain-ai.github.io/langgraph/concepts/persistence).

When creating a LangGraph workflow, you can set it up to persist its results by using a [checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#basecheckpointsaver):


1. Create an instance of a checkpointer:

    ```python
    from langgraph.checkpoint.memory import InMemorySaver
    
    checkpointer = InMemorySaver()       
    ```

2. Pass `checkpointer` instance to the `entrypoint()` decorator:

    ```python
    from langgraph.func import entrypoint
    
    @entrypoint(checkpointer=checkpointer)
    def workflow(inputs)
        ...
    ```

3. Optionally expose `previous` parameter in the workflow function signature:

    ```python
    @entrypoint(checkpointer=checkpointer)
    def workflow(
        inputs,
        *,
        # you can optionally specify `previous` in the workflow function signature
        # to access the return value from the workflow as of the last execution
        previous
    ):
        previous = previous or []
        combined_inputs = previous + inputs
        result = do_something(combined_inputs)
        ...
    ```

4. Optionally choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous`:

    ```python
    @entrypoint(checkpointer=checkpointer)
    def workflow(inputs, *, previous):
        ...
        result = do_something(...)
        return entrypoint.final(value=result, save=combine(inputs, result))
    ```

This guide shows how you can add thread-level persistence to your workflow.

!!! tip "Note"

    If you need memory that is __shared__ across multiple conversations or users (cross-thread persistence), check out this <a href="../cross-thread-persistence-functional">how-to guide</a>.

!!! tip "Note"

    If you need to add thread-level persistence to a `StateGraph`, check out this <a href="../persistence">how-to guide</a>.


## Setup

First we need to install the packages required


```shell
pip install --quiet -U langgraph langchain_anthropic
```

Next, we need to set API key for Anthropic (the LLM we will use).


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("ANTHROPIC_API_KEY")
```

<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>


## Example: simple chatbot with short-term memory

We will be using a workflow with a single task that calls a [chat model](https://python.langchain.com/docs/concepts/chat_models/).

Let's first define the model we'll be using:


```python
from langchain_anthropic import ChatAnthropic

model = ChatAnthropic(model="claude-3-5-sonnet-latest")
```

Now we can define our task and workflow. To add in persistence, we need to pass in a [Checkpointer](https://langchain-ai.github.io/langgraph/reference/checkpoints/#langgraph.checkpoint.base.BaseCheckpointSaver) to the [entrypoint()][langgraph.func.entrypoint] decorator.


```python
from langchain_core.messages import BaseMessage
from langgraph.graph import add_messages
from langgraph.func import entrypoint, task
from langgraph.checkpoint.memory import InMemorySaver


@task
def call_model(messages: list[BaseMessage]):
    response = model.invoke(messages)
    return response


checkpointer = InMemorySaver()


@entrypoint(checkpointer=checkpointer)
def workflow(inputs: list[BaseMessage], *, previous: list[BaseMessage]):
    if previous:
        inputs = add_messages(previous, inputs)

    response = call_model(inputs).result()
    return entrypoint.final(value=response, save=add_messages(inputs, response))
```

If we try to use this workflow, the context of the conversation will be persisted across interactions:

!!! note Note

    If you're using LangGraph Platform or LangGraph Studio, you __don't need__ to pass checkpointer to the entrypoint decorator, since it's done automatically.

We can now interact with the agent and see that it remembers previous messages!


```python
config = {"configurable": {"thread_id": "1"}}
input_message = {"role": "user", "content": "hi! I'm bob"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Hi Bob! I'm Claude. Nice to meet you! How are you today?
```
You can always resume previous threads:


```python
input_message = {"role": "user", "content": "what's my name?"}
for chunk in workflow.stream([input_message], config, stream_mode="values"):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

Your name is Bob.
```
If we want to start a new conversation, we can pass in a different `thread_id`. Poof! All the memories are gone!


```python
input_message = {"role": "user", "content": "what's my name?"}
for chunk in workflow.stream(
    [input_message],
    {"configurable": {"thread_id": "2"}},
    stream_mode="values",
):
    chunk.pretty_print()
```
```output
================================== Ai Message ==================================

I don't know your name unless you tell me. Each conversation I have starts fresh, so I don't have access to any previous interactions or personal information unless you share it with me.
```
!!! tip "Streaming tokens"

    If you would like to stream LLM tokens from your chatbot, you can use `stream_mode="messages"`. Check out this <a href="../streaming-tokens">how-to guide</a> to learn more.


---
how-tos/create-react-agent-manage-message-history.ipynb
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


## Setup

First, let's install the required packages and set our API keys


```shell
pip install -U langgraph langchain-openai langmem
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
```

<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>


## Keep the original message history unmodified

Let's build a ReAct agent with a step that manages the conversation history: when the length of the history exceeds a specified number of tokens, we will call [`trim_messages`](https://python.langchain.com/api_reference/core/messages/langchain_core.messages.utils.trim_messages.html) utility that that will reduce the history while satisfying LLM provider constraints.

There are two ways that the updated message history can be applied inside ReAct agent:

  * <a href="#keep-the-original-message-history-unmodified">**Keep the original message history unmodified**</a> in the graph state and pass the updated history **only as the input to the LLM**
  * <a href="#overwrite-the-original-message-history">**Overwrite the original message history**</a> in the graph state with the updated history

Let's start by implementing the first one. We'll need to first define model and tools for our agent:


```python
from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4o", temperature=0)


def get_weather(location: str) -> str:
    """Use this to get weather information."""
    if any([city in location.lower() for city in ["nyc", "new york city"]]):
        return "It might be cloudy in nyc, with a chance of rain and temperatures up to 80 degrees."
    elif any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's always sunny in sf"
    else:
        return f"I am not sure what the weather is in {location}"


tools = [get_weather]
```

Now let's implement `pre_model_hook` — a function that will be added as a new node and called every time **before** the node that calls the LLM (the `agent` node).

Our implementation will wrap the `trim_messages` call and return the trimmed messages under `llm_input_messages`. This will **keep the original message history unmodified** in the graph state and pass the updated history **only as the input to the LLM**


```python hl_lines="4 5 6 7 22 29"
from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import InMemorySaver

from langchain_core.messages.utils import (
    trim_messages,
    count_tokens_approximately,
)



# This function will be added as a new node in ReAct agent graph

# that will run every time before the node that calls the LLM.

# The messages returned by this function will be the input to the LLM.
def pre_model_hook(state):
    trimmed_messages = trim_messages(
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=384,
        start_on="human",
        end_on=("human", "tool"),
    )
    return {"llm_input_messages": trimmed_messages}


checkpointer = InMemorySaver()
graph = create_react_agent(
    model,
    tools,
    pre_model_hook=pre_model_hook,
    checkpointer=checkpointer,
)
```


```python
from IPython.display import display, Image

display(Image(graph.get_graph().draw_mermaid_png()))
```

<p>

</p>

We'll also define a utility to render the agent outputs nicely:


```python
def print_stream(stream, output_messages_key="llm_input_messages"):
    for chunk in stream:
        for node, update in chunk.items():
            print(f"Update from node: {node}")
            messages_key = (
                output_messages_key if node == "pre_model_hook" else "messages"
            )
            for message in update[messages_key]:
                if isinstance(message, tuple):
                    print(message)
                else:
                    message.pretty_print()

        print("\n\n")
```

Now let's run the agent with a few different queries to reach the specified max tokens limit:


```python
config = {"configurable": {"thread_id": "1"}}

inputs = {"messages": [("user", "What's the weather in NYC?")]}
result = graph.invoke(inputs, config=config)

inputs = {"messages": [("user", "What's it known for?")]}
result = graph.invoke(inputs, config=config)
```

Let's see how many tokens we have in the message history so far:


```python
messages = result["messages"]
count_tokens_approximately(messages)
```



```output
415
```


You can see that we are close to the `max_tokens` threshold, so on the next invocation we should see `pre_model_hook` kick-in and trim the message history. Let's run it again:


```python
inputs = {"messages": [("user", "where can i find the best bagel?")]}
print_stream(graph.stream(inputs, config=config, stream_mode="updates"))
```
```output
Update from node: pre_model_hook
================================ Human Message =================================

What's it known for?
================================== Ai Message ==================================

New York City is known for a variety of iconic landmarks, cultural institutions, and vibrant neighborhoods. Some of the most notable features include:

1. **Statue of Liberty**: A symbol of freedom and democracy, located on Liberty Island.
2. **Times Square**: Known for its bright lights, Broadway theaters, and bustling atmosphere.
3. **Central Park**: A large public park offering a natural retreat in the middle of the city.
4. **Empire State Building**: An iconic skyscraper offering panoramic views of the city.
5. **Broadway**: Famous for its world-class theater productions.
6. **Wall Street**: The financial hub of the United States.
7. **Museums**: Including the Metropolitan Museum of Art, Museum of Modern Art (MoMA), and the American Museum of Natural History.
8. **Diverse Cuisine**: A melting pot of cultures offering a wide range of culinary experiences.
9. **Cultural Diversity**: A rich tapestry of cultures and communities from around the world.
10. **Fashion**: A global fashion capital, hosting events like New York Fashion Week.

These are just a few highlights of what makes New York City a unique and vibrant place.
================================ Human Message =================================

where can i find the best bagel?



Update from node: agent
================================== Ai Message ==================================

New York City is famous for its bagels, and there are several places renowned for serving some of the best. Here are a few top spots where you can find excellent bagels in NYC:

1. **Ess-a-Bagel**: Known for their large, chewy bagels with a variety of spreads and toppings.
2. **Russ & Daughters**: A classic spot offering traditional bagels with high-quality smoked fish and cream cheese.
3. **H&H Bagels**: Famous for their fresh, hand-rolled bagels.
4. **Murray’s Bagels**: Offers a wide selection of bagels and spreads, with a no-toasting policy to preserve freshness.
5. **Absolute Bagels**: Known for their authentic, fluffy bagels and a variety of cream cheese options.
6. **Tompkins Square Bagels**: Offers creative bagel sandwiches and a wide range of spreads.
7. **Bagel Hole**: Known for their smaller, denser bagels with a crispy crust.

Each of these places has its own unique style and flavor, so it might be worth trying a few to find your personal favorite!
```
You can see that the `pre_model_hook` node now only returned the last 3 messages, as expected. However, the existing message history is untouched:


```python
updated_messages = graph.get_state(config).values["messages"]
assert [(m.type, m.content) for m in updated_messages[: len(messages)]] == [
    (m.type, m.content) for m in messages
]
```


## Overwrite the original message history

Let's now change the `pre_model_hook` to **overwrite** the message history in the graph state. To do this, we’ll return the updated messages under `messages` key. We’ll also include a special `RemoveMessage(REMOVE_ALL_MESSAGES)` object, which tells `create_react_agent` to remove previous messages from the graph state:


```python hl_lines="16 23"
from langchain_core.messages import RemoveMessage
from langgraph.graph.message import REMOVE_ALL_MESSAGES


def pre_model_hook(state):
    trimmed_messages = trim_messages(
        state["messages"],
        strategy="last",
        token_counter=count_tokens_approximately,
        max_tokens=384,
        start_on="human",
        end_on=("human", "tool"),
    )
    # NOTE that we're now returning the messages under the `messages` key
    # We also remove the existing messages in the history to ensure we're overwriting the history
    return {"messages": [RemoveMessage(REMOVE_ALL_MESSAGES)] + trimmed_messages}


checkpointer = InMemorySaver()
graph = create_react_agent(
    model,
    tools,
    pre_model_hook=pre_model_hook,
    checkpointer=checkpointer,
)
```

Now let's run the agent with the same queries as before:


```python
config = {"configurable": {"thread_id": "1"}}

inputs = {"messages": [("user", "What's the weather in NYC?")]}
result = graph.invoke(inputs, config=config)

inputs = {"messages": [("user", "What's it known for?")]}
result = graph.invoke(inputs, config=config)
messages = result["messages"]

inputs = {"messages": [("user", "where can i find the best bagel?")]}
print_stream(
    graph.stream(inputs, config=config, stream_mode="updates"),
    output_messages_key="messages",
)
```
```output
Update from node: pre_model_hook
================================ Remove Message ================================


================================ Human Message =================================

What's it known for?
================================== Ai Message ==================================

New York City is known for a variety of iconic landmarks, cultural institutions, and vibrant neighborhoods. Some of the most notable features include:

1. **Statue of Liberty**: A symbol of freedom and democracy, located on Liberty Island.
2. **Times Square**: Known for its bright lights, Broadway theaters, and bustling atmosphere.
3. **Central Park**: A large public park offering a natural oasis amidst the urban environment.
4. **Empire State Building**: An iconic skyscraper offering panoramic views of the city.
5. **Broadway**: Famous for its world-class theater productions and musicals.
6. **Wall Street**: The financial hub of the United States, located in the Financial District.
7. **Museums**: Including the Metropolitan Museum of Art, Museum of Modern Art (MoMA), and the American Museum of Natural History.
8. **Diverse Cuisine**: A melting pot of cultures, offering a wide range of international foods.
9. **Cultural Diversity**: Known for its diverse population and vibrant cultural scene.
10. **Brooklyn Bridge**: An iconic suspension bridge connecting Manhattan and Brooklyn.

These are just a few highlights, as NYC is a city with endless attractions and activities.
================================ Human Message =================================

where can i find the best bagel?



Update from node: agent
================================== Ai Message ==================================

New York City is famous for its bagels, and there are several places renowned for serving some of the best. Here are a few top spots where you can find delicious bagels in NYC:

1. **Ess-a-Bagel**: Known for its large, chewy bagels and a wide variety of spreads and toppings. Locations in Midtown and the East Village.

2. **Russ & Daughters**: A historic appetizing store on the Lower East Side, famous for its bagels with lox and cream cheese.

3. **Absolute Bagels**: Located on the Upper West Side, this spot is popular for its fresh, fluffy bagels.

4. **Murray’s Bagels**: Known for its traditional, hand-rolled bagels. Located in Greenwich Village.

5. **Tompkins Square Bagels**: Offers a wide selection of bagels and creative cream cheese flavors. Located in the East Village.

6. **Bagel Hole**: A small shop in Park Slope, Brooklyn, known for its classic, no-frills bagels.

7. **Leo’s Bagels**: Located in the Financial District, known for its authentic New York-style bagels.

Each of these places has its own unique style and flavor, so it might be worth trying a few to find your personal favorite!
```
You can see that the `pre_model_hook` node returned the last 3 messages again. However, this time, the message history is modified in the graph state as well:


```python
updated_messages = graph.get_state(config).values["messages"]
assert (
    # First 2 messages in the new history are the same as last 2 messages in the old
    [(m.type, m.content) for m in updated_messages[:2]]
    == [(m.type, m.content) for m in messages[-2:]]
)
```


## Summarizing message history

Finally, let's apply a different strategy for managing message history — summarization. Just as with trimming, you can choose to keep original message history unmodified or overwrite it. The example below will only show the former.

We will use the [`SummarizationNode`](https://langchain-ai.github.io/langmem/guides/summarization/#using-summarizationnode) from the prebuilt `langmem` library. Once the message history reaches the token limit, the summarization node will summarize earlier messages to make sure they fit into `max_tokens`.


```python hl_lines="1 20 28 29"
from langmem.short_term import SummarizationNode
from langgraph.prebuilt.chat_agent_executor import AgentState
from typing import Any

model = ChatOpenAI(model="gpt-4o")
summarization_model = model.bind(max_tokens=128)

summarization_node = SummarizationNode(
    token_counter=count_tokens_approximately,
    model=summarization_model,
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
    # limit the output size to ensure consistent behavior
    model.bind(max_tokens=256),
    tools,
    pre_model_hook=summarization_node,
    state_schema=State,
    checkpointer=checkpointer,
)
```


```python
config = {"configurable": {"thread_id": "1"}}
inputs = {"messages": [("user", "What's the weather in NYC?")]}

result = graph.invoke(inputs, config=config)

inputs = {"messages": [("user", "What's it known for?")]}
result = graph.invoke(inputs, config=config)

inputs = {"messages": [("user", "where can i find the best bagel?")]}
print_stream(graph.stream(inputs, config=config, stream_mode="updates"))
```
```output
Update from node: pre_model_hook
================================ System Message ================================

Summary of the conversation so far: The user asked about the current weather in New York City. In response, the assistant provided information that it might be cloudy, with a chance of rain, and temperatures reaching up to 80 degrees.
================================ Human Message =================================

What's it known for?
================================== Ai Message ==================================

New York City, often referred to as NYC, is known for its:

1. **Landmarks and Iconic Sites**:
   - **Statue of Liberty**: A symbol of freedom and democracy.
   - **Central Park**: A vast green oasis in the middle of the city.
   - **Empire State Building**: Once the tallest building in the world, offering stunning views of the city.
   - **Times Square**: Known for its bright lights and bustling atmosphere.

2. **Cultural Institutions**:
   - **Broadway**: Renowned for theatrical performances and musicals.
   - **Metropolitan Museum of Art** and **Museum of Modern Art (MoMA)**: World-class art collections.
   - **American Museum of Natural History**: Known for its extensive exhibits ranging from dinosaurs to space exploration.
   
3. **Diverse Neighborhoods and Cuisine**:
   - NYC is famous for having a melting pot of cultures, reflected in neighborhoods like Chinatown, Little Italy, and Harlem.
   - The city offers a wide range of international cuisines, from street food to high-end dining.

4. **Financial District**:
   - Home to Wall Street, the New York Stock Exchange (NYSE), and other major financial institutions.

5. **Media and Entertainment**:
   - Major hub for television, film, and media, with numerous studios and networks based there.

6. **Fashion**:
   - Often referred to as one of the "Big Four" fashion capitals, hosting events like New York Fashion Week.

7. **Sports**:
   - Known for its passionate sports culture with teams like the Yankees (MLB), Mets (MLB), Knicks (NBA), and Rangers (NHL).

These elements, among others, contribute to NYC's reputation as a vibrant and dynamic city.
================================ Human Message =================================

where can i find the best bagel?



Update from node: agent
================================== Ai Message ==================================

Finding the best bagel in New York City can be subjective, as there are many beloved spots across the city. However, here are some renowned bagel shops you might want to try:

1. **Ess-a-Bagel**: Known for its chewy and flavorful bagels, located in Midtown and Stuyvesant Town.

2. **Bagel Hole**: A favorite for traditionalists, offering classic and dense bagels, located in Park Slope, Brooklyn.

3. **Russ & Daughters**: A legendary appetizing store on the Lower East Side, famous for their bagels with lox.

4. **Murray’s Bagels**: Located in Greenwich Village, known for their fresh and authentic New York bagels.

5. **Absolute Bagels**: Located on the Upper West Side, they’re known for their fresh, fluffy bagels with a variety of spreads.

6. **Tompkins Square Bagels**: In the East Village, famous for their creative cream cheese options and fresh bagels.

7. **Zabar’s**: A landmark on the Upper West Side known for their classic bagels and smoked fish.

Each of these spots offers a unique take on the classic New York bagel experience, and trying several might be the best way to discover your personal favorite!
```
You can see that the earlier messages have now been replaced with the summary of the earlier conversation!


---
how-tos/autogen-integration-functional.ipynb
---


# How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks

LangGraph is a framework for building agentic and multi-agent applications. LangGraph can be easily integrated with other agent frameworks. 

The primary reasons you might want to integrate LangGraph with other agent frameworks:

- create <a href="../../concepts/multi_agent">multi-agent systems</a> where individual agents are built with different frameworks
- leverage LangGraph to add features like <a href="../../concepts/persistence">persistence</a>, <a href="../../concepts/streaming">streaming</a>, <a href="../../concepts/memory">short and long-term memory</a> and more

The simplest way to integrate agents from other frameworks is by calling those agents inside a LangGraph <a href="../../concepts/low_level/#nodes">node</a>:

```python
import autogen
from langgraph.func import entrypoint, task

autogen_agent = autogen.AssistantAgent(name="assistant", ...)
user_proxy = autogen.UserProxyAgent(name="user_proxy", ...)

@task
def call_autogen_agent(messages):
    response = user_proxy.initiate_chat(
        autogen_agent,
        message=messages[-1],
        ...
    )
    ...


@entrypoint()
def workflow(messages):
    response = call_autogen_agent(messages).result()
    return response


workflow.invoke(
    [
        {
            "role": "user",
            "content": "Find numbers between 10 and 30 in fibonacci sequence",
        }
    ]
)
```

In this guide we show how to build a LangGraph chatbot that integrates with AutoGen, but you can follow the same approach with other frameworks.


## Setup


```python
%pip install autogen langgraph
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
```
```output
OPENAI_API_KEY:  ········
```

## Define AutoGen agent

Here we define our AutoGen agent. Adapted from official tutorial [here](https://github.com/microsoft/autogen/blob/0.2/notebook/agentchat_web_info.ipynb).


```python
import autogen
import os

config_list = [{"model": "gpt-4o", "api_key": os.environ["OPENAI_API_KEY"]}]

llm_config = {
    "timeout": 600,
    "cache_seed": 42,
    "config_list": config_list,
    "temperature": 0,
}

autogen_agent = autogen.AssistantAgent(
    name="assistant",
    llm_config=llm_config,
)

user_proxy = autogen.UserProxyAgent(
    name="user_proxy",
    human_input_mode="NEVER",
    max_consecutive_auto_reply=10,
    is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    code_execution_config={
        "work_dir": "web",
        "use_docker": False,
    },  # Please set use_docker=True if docker is available to run the generated code. Using docker is safer than running the generated code directly.
    llm_config=llm_config,
    system_message="Reply TERMINATE if the task has been solved at full satisfaction. Otherwise, reply CONTINUE, or the reason why the task is not solved yet.",
)
```

---


## Create the workflow

We will now create a LangGraph chatbot graph that calls AutoGen agent.


```python
from langchain_core.messages import convert_to_openai_messages, BaseMessage
from langgraph.func import entrypoint, task
from langgraph.graph import add_messages
from langgraph.checkpoint.memory import InMemorySaver


@task
def call_autogen_agent(messages: list[BaseMessage]):
    # convert to openai-style messages
    messages = convert_to_openai_messages(messages)
    response = user_proxy.initiate_chat(
        autogen_agent,
        message=messages[-1],
        # pass previous message history as context
        carryover=messages[:-1],
    )
    # get the final response from the agent
    content = response.chat_history[-1]["content"]
    return {"role": "assistant", "content": content}



# add short-term memory for storing conversation history
checkpointer = InMemorySaver()


@entrypoint(checkpointer=checkpointer)
def workflow(messages: list[BaseMessage], previous: list[BaseMessage]):
    messages = add_messages(previous or [], messages)
    response = call_autogen_agent(messages).result()
    return entrypoint.final(value=response, save=add_messages(messages, response))
```


## Run the graph

We can now run the graph.


```python hl_lines="2 11"

# pass the thread ID to persist agent outputs for future interactions
config = {"configurable": {"thread_id": "1"}}

for chunk in workflow.stream(
    [
        {
            "role": "user",
            "content": "Find numbers between 10 and 30 in fibonacci sequence",
        }
    ],
    config,
):
    print(chunk)
```
```output
user_proxy (to assistant):

Find numbers between 10 and 30 in fibonacci sequence

--------------------------------------------------------------------------------
assistant (to user_proxy):

To find numbers between 10 and 30 in the Fibonacci sequence, we can generate the Fibonacci sequence and check which numbers fall within this range. Here's a plan:

1. Generate Fibonacci numbers starting from 0.
2. Continue generating until the numbers exceed 30.
3. Collect and print the numbers that are between 10 and 30.

Let's implement this in Python:

\`\`\`python

# filename: fibonacci_range.py

def fibonacci_sequence():
    a, b = 0, 1
    while a <= 30:
        if 10 <= a <= 30:
            print(a)
        a, b = b, a + b

fibonacci_sequence()
\`\`\`

This script will print the Fibonacci numbers between 10 and 30. Please execute the code to see the result.

--------------------------------------------------------------------------------

>>>>>>>> EXECUTING CODE BLOCK 0 (inferred language is python)...
user_proxy (to assistant):

exitcode: 0 (execution succeeded)
Code output: 
13
21


--------------------------------------------------------------------------------
assistant (to user_proxy):

The Fibonacci numbers between 10 and 30 are 13 and 21. 

These numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. 

The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

As you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.

TERMINATE

--------------------------------------------------------------------------------
{'call_autogen_agent': {'role': 'assistant', 'content': 'The Fibonacci numbers between 10 and 30 are 13 and 21. \n\nThese numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. \n\nThe sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...\n\nAs you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.\n\nTERMINATE'}}
{'workflow': {'role': 'assistant', 'content': 'The Fibonacci numbers between 10 and 30 are 13 and 21. \n\nThese numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. \n\nThe sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...\n\nAs you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.\n\nTERMINATE'}}
```
Since we're leveraging LangGraph's [persistence](https://langchain-ai.github.io/langgraph/concepts/persistence/) features we can now continue the conversation using the same thread ID -- LangGraph will automatically pass previous history to the AutoGen agent:


```python hl_lines="8"
for chunk in workflow.stream(
    [
        {
            "role": "user",
            "content": "Multiply the last number by 3",
        }
    ],
    config,
):
    print(chunk)
```
```output
user_proxy (to assistant):

Multiply the last number by 3
Context: 
Find numbers between 10 and 30 in fibonacci sequence
The Fibonacci numbers between 10 and 30 are 13 and 21. 

These numbers are part of the Fibonacci sequence, which is generated by adding the two preceding numbers to get the next number, starting from 0 and 1. 

The sequence goes: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

As you can see, 13 and 21 are the only numbers in this sequence that fall between 10 and 30.

TERMINATE

--------------------------------------------------------------------------------
assistant (to user_proxy):

The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:

21 * 3 = 63

TERMINATE

--------------------------------------------------------------------------------
{'call_autogen_agent': {'role': 'assistant', 'content': 'The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:\n\n21 * 3 = 63\n\nTERMINATE'}}
{'workflow': {'role': 'assistant', 'content': 'The last number in the Fibonacci sequence between 10 and 30 is 21. Multiplying 21 by 3 gives:\n\n21 * 3 = 63\n\nTERMINATE'}}
```

---
how-tos/many-tools.ipynb
---


# How to handle large numbers of tools

<div class="admonition tip">
    <p class="admonition-title">Prerequisites</p>
    <p>
        This guide assumes familiarity with the following:
        <ul>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#tools">
                    Tools
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#chat-models/">
                    Chat Models
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#embedding-models">
                    Embedding Models
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#vector-stores">
                    Vectorstores
                </a>
            </li>   
            <li>
                <a href="https://python.langchain.com/docs/concepts/#documents">
                    Document
                </a>
            </li>
        </ul>
    </p>
</div> 


The subset of available tools to call is generally at the discretion of the model (although many providers also enable the user to [specify or constrain the choice of tool](https://python.langchain.com/docs/how_to/tool_choice/)). As the number of available tools grows, you may want to limit the scope of the LLM's selection, to decrease token consumption and to help manage sources of error in LLM reasoning.

Here we will demonstrate how to dynamically adjust the tools available to a model. Bottom line up front: like [RAG](https://python.langchain.com/docs/concepts/#retrieval) and similar methods, we prefix the model invocation by retrieving over available tools. Although we demonstrate one implementation that searches over tool descriptions, the details of the tool selection can be customized as needed.


## Setup

First, let's install the required packages and set our API keys


```shell
pip install --quiet -U langgraph langchain_openai numpy
```


```python
import getpass
import os


def _set_env(var: str):
    if not os.environ.get(var):
        os.environ[var] = getpass.getpass(f"{var}: ")


_set_env("OPENAI_API_KEY")
```

<div class="admonition tip">
    <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for LangGraph development</p>
    <p style="padding-top: 5px;">
        Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM apps built with LangGraph — read more about how to get started <a href="https://docs.smith.langchain.com">here</a>. 
    </p>
</div>


## Define the tools

Let's consider a toy example in which we have one tool for each publicly traded company in the [S&P 500 index](https://en.wikipedia.org/wiki/S%26P_500). Each tool fetches company-specific information based on the year provided as a parameter.

We first construct a registry that associates a unique identifier with a schema for each tool. We will represent the tools using JSON schema, which can be bound directly to chat models supporting tool calling.


```python
import re
import uuid

from langchain_core.tools import StructuredTool


def create_tool(company: str) -> dict:
    """Create schema for a placeholder tool."""
    # Remove non-alphanumeric characters and replace spaces with underscores for the tool name
    formatted_company = re.sub(r"[^\w\s]", "", company).replace(" ", "_")

    def company_tool(year: int) -> str:
        # Placeholder function returning static revenue information for the company and year
        return f"{company} had revenues of $100 in {year}."

    return StructuredTool.from_function(
        company_tool,
        name=formatted_company,
        description=f"Information about {company}",
    )



---

**Navigation:** [← Previous](./01-how-to-interact-with-the-deployment-using-remotegraph.md) | [Index](./index.md) | [Next →](./03-abbreviated-list-of-sp-500-companies-for-demonstration.md)
