# Abbreviated list of S&P 500 companies for demonstration

**Navigation:** [← Previous](./02-subgraph.md) | [Index](./index.md) | [Next →](./04-node-that-uses-the-instructions.md)

---

# Abbreviated list of S&P 500 companies for demonstration
s_and_p_500_companies = [
    "3M",
    "A.O. Smith",
    "Abbott",
    "Accenture",
    "Advanced Micro Devices",
    "Yum! Brands",
    "Zebra Technologies",
    "Zimmer Biomet",
    "Zoetis",
]


# Create a tool for each company and store it in a registry with a unique UUID as the key
tool_registry = {
    str(uuid.uuid4()): create_tool(company) for company in s_and_p_500_companies
}
```


## Define the graph

### Tool selection

We will construct a node that retrieves a subset of available tools given the information in the state-- such as a recent user message. In general, the full scope of [retrieval solutions](https://python.langchain.com/docs/concepts/#retrieval) are available for this step. As a simple solution, we index embeddings of tool descriptions in a vector store, and associate user queries to tools via semantic search.


```python
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_openai import OpenAIEmbeddings

tool_documents = [
    Document(
        page_content=tool.description,
        id=id,
        metadata={"tool_name": tool.name},
    )
    for id, tool in tool_registry.items()
]

vector_store = InMemoryVectorStore(embedding=OpenAIEmbeddings())
document_ids = vector_store.add_documents(tool_documents)
```

### Incorporating with an agent

We will use a typical React agent graph (e.g., as used in the [quickstart](https://langchain-ai.github.io/langgraph/tutorials/introduction/#part-2-enhancing-the-chatbot-with-tools)), with some modifications:

- We add a `selected_tools` key to the state, which stores our selected subset of tools;
- We set the entry point of the graph to be a `select_tools` node, which populates this element of the state;
- We bind the selected subset of tools to the chat model within the `agent` node.


```python
from typing import Annotated

from langchain_openai import ChatOpenAI
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition



# Define the state structure using TypedDict.

# It includes a list of messages (processed by add_messages)

# and a list of selected tool IDs.
class State(TypedDict):
    messages: Annotated[list, add_messages]
    selected_tools: list[str]


builder = StateGraph(State)


# Retrieve all available tools from the tool registry.
tools = list(tool_registry.values())
llm = ChatOpenAI()



# The agent function processes the current state

# by binding selected tools to the LLM.
def agent(state: State):
    # Map tool IDs to actual tools
    # based on the state's selected_tools list.
    selected_tools = [tool_registry[id] for id in state["selected_tools"]]
    # Bind the selected tools to the LLM for the current interaction.
    llm_with_tools = llm.bind_tools(selected_tools)
    # Invoke the LLM with the current messages and return the updated message list.
    return {"messages": [llm_with_tools.invoke(state["messages"])]}



# The select_tools function selects tools based on the user's last message content.
def select_tools(state: State):
    last_user_message = state["messages"][-1]
    query = last_user_message.content
    tool_documents = vector_store.similarity_search(query)
    return {"selected_tools": [document.id for document in tool_documents]}


builder.add_node("agent", agent)
builder.add_node("select_tools", select_tools)

tool_node = ToolNode(tools=tools)
builder.add_node("tools", tool_node)

builder.add_conditional_edges("agent", tools_condition, path_map=["tools", "__end__"])
builder.add_edge("tools", "agent")
builder.add_edge("select_tools", "agent")
builder.add_edge(START, "select_tools")
graph = builder.compile()
```


```python
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

<p>

</p>


```python
user_input = "Can you give me some information about AMD in 2022?"

result = graph.invoke({"messages": [("user", user_input)]})
```


```python
print(result["selected_tools"])
```
```output
['ab9c0d59-3d16-448d-910c-73cf10a26020', 'f5eff8f6-7fb9-47b6-b54f-19872a52db84', '2962e168-9ef4-48dc-8b7c-9227e7956d39', '24a9fb82-19fe-4a88-944e-47bc4032e94a']
```

```python
for message in result["messages"]:
    message.pretty_print()
```
```output
================================ Human Message =================================

Can you give me some information about AMD in 2022?
================================== Ai Message ==================================
Tool Calls:
  Advanced_Micro_Devices (call_CRxQ0oT7NY7lqf35DaRNTJ35)
 Call ID: call_CRxQ0oT7NY7lqf35DaRNTJ35
  Args:
    year: 2022
================================= Tool Message =================================
Name: Advanced_Micro_Devices

Advanced Micro Devices had revenues of $100 in 2022.
================================== Ai Message ==================================

In 2022, Advanced Micro Devices (AMD) had revenues of $100.
```

## Repeating tool selection

To manage errors from incorrect tool selection, we could revisit the `select_tools` node. One option for implementing this is to modify `select_tools` to generate the vector store query using all messages in the state (e.g., with a chat model) and add an edge routing from `tools` to `select_tools`.

We implement this change below. For demonstration purposes, we simulate an error in the initial tool selection by adding a `hack_remove_tool_condition` to the `select_tools` node, which removes the correct tool on the first iteration of the node. Note that on the second iteration, the agent finishes the run as it has access to the correct tool.

<div class="admonition note">
    <p class="admonition-title">Using Pydantic with LangChain</p>
    <p>
        This notebook uses Pydantic v2 <code>BaseModel</code>, which requires <code>langchain-core >= 0.3</code>. Using <code>langchain-core < 0.3</code> will result in errors due to mixing of Pydantic v1 and v2 <code>BaseModels</code>.
    </p>
</div>  


```python
from langchain_core.messages import HumanMessage, SystemMessage, ToolMessage
from langgraph.pregel.retry import RetryPolicy

from pydantic import BaseModel, Field


class QueryForTools(BaseModel):
    """Generate a query for additional tools."""

    query: str = Field(..., description="Query for additional tools.")


def select_tools(state: State):
    """Selects tools based on the last message in the conversation state.

    If the last message is from a human, directly uses the content of the message
    as the query. Otherwise, constructs a query using a system message and invokes
    the LLM to generate tool suggestions.
    """
    last_message = state["messages"][-1]
    hack_remove_tool_condition = False  # Simulate an error in the first tool selection

    if isinstance(last_message, HumanMessage):
        query = last_message.content
        hack_remove_tool_condition = True  # Simulate wrong tool selection
    else:
        assert isinstance(last_message, ToolMessage)
        system = SystemMessage(
            "Given this conversation, generate a query for additional tools. "
            "The query should be a short string containing what type of information "
            "is needed. If no further information is needed, "
            "set more_information_needed False and populate a blank string for the query."
        )
        input_messages = [system] + state["messages"]
        response = llm.bind_tools([QueryForTools], tool_choice=True).invoke(
            input_messages
        )
        query = response.tool_calls[0]["args"]["query"]

    # Search the tool vector store using the generated query
    tool_documents = vector_store.similarity_search(query)
    if hack_remove_tool_condition:
        # Simulate error by removing the correct tool from the selection
        selected_tools = [
            document.id
            for document in tool_documents
            if document.metadata["tool_name"] != "Advanced_Micro_Devices"
        ]
    else:
        selected_tools = [document.id for document in tool_documents]
    return {"selected_tools": selected_tools}


graph_builder = StateGraph(State)
graph_builder.add_node("agent", agent)
graph_builder.add_node(
    "select_tools", select_tools, retry_policy=RetryPolicy(max_attempts=3)
)

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)

graph_builder.add_conditional_edges(
    "agent",
    tools_condition,
)
graph_builder.add_edge("tools", "select_tools")
graph_builder.add_edge("select_tools", "agent")
graph_builder.add_edge(START, "select_tools")
graph = graph_builder.compile()
```


```python
from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

<p>

</p>


```python
user_input = "Can you give me some information about AMD in 2022?"

result = graph.invoke({"messages": [("user", user_input)]})
```


```python
for message in result["messages"]:
    message.pretty_print()
```
```output
================================ Human Message =================================

Can you give me some information about AMD in 2022?
================================== Ai Message ==================================
Tool Calls:
  Accenture (call_qGmwFnENwwzHOYJXiCAaY5Mx)
 Call ID: call_qGmwFnENwwzHOYJXiCAaY5Mx
  Args:
    year: 2022
================================= Tool Message =================================
Name: Accenture

Accenture had revenues of $100 in 2022.
================================== Ai Message ==================================
Tool Calls:
  Advanced_Micro_Devices (call_u9e5UIJtiieXVYi7Y9GgyDpn)
 Call ID: call_u9e5UIJtiieXVYi7Y9GgyDpn
  Args:
    year: 2022
================================= Tool Message =================================
Name: Advanced_Micro_Devices

Advanced Micro Devices had revenues of $100 in 2022.
================================== Ai Message ==================================

In 2022, AMD had revenues of $100.
```

## Next steps

This guide provides a minimal implementation for dynamically selecting tools. There is a host of possible improvements and optimizations:

- **Repeating tool selection**: Here, we repeated tool selection by modifying the `select_tools` node. Another option is to equip the agent with a `reselect_tools` tool, allowing it to re-select tools at its discretion.
- **Optimizing tool selection**: In general, the full scope of [retrieval solutions](https://python.langchain.com/docs/concepts/#retrieval) are available for tool selection. Additional options include:
  - Group tools and retrieve over groups;
  - Use a chat model to select tools or groups of tool.


---
how-tos/react-agent-from-scratch.ipynb
---


# How to create a ReAct agent from scratch

!!! info "Prerequisites"
    This guide assumes familiarity with the following:
    
    - <a href="../../concepts/agentic_concepts/#tool-calling-agent">Tool calling agent</a>
    - [Chat Models](https://python.langchain.com/docs/concepts/chat_models/)
    - [Messages](https://python.langchain.com/docs/concepts/messages/)
    - <a href="../../concepts/low_level/">LangGraph Glossary</a>

Using the prebuilt ReAct agent [create_react_agent][langgraph.prebuilt.chat_agent_executor.create_react_agent] is a great way to get started, but sometimes you might want more control and customization. In those cases, you can create a custom ReAct agent. This guide shows how to implement ReAct agent from scratch using LangGraph.


## Setup

First, let's install the required packages and set our API keys:


```shell
pip install -U langgraph langchain-openai
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
     <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for better debugging</p>
     <p style="padding-top: 5px;">
         Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the <a href="https://docs.smith.langchain.com">docs</a>. 
     </p>
 </div>


## Create ReAct agent

Now that you have installed the required packages and set your environment variables, we can code our ReAct agent!

### Define graph state

We are going to define the most basic ReAct state in this example, which will just contain a list of messages.

For your specific use case, feel free to add any other state keys that you need.


```python
from typing import (
    Annotated,
    Sequence,
    TypedDict,
)
from langchain_core.messages import BaseMessage
from langgraph.graph.message import add_messages


class AgentState(TypedDict):
    """The state of the agent."""

    # add_messages is a reducer
    # See https://langchain-ai.github.io/langgraph/concepts/low_level/#reducers
    messages: Annotated[Sequence[BaseMessage], add_messages]
```

### Define model and tools

Next, let's define the tools and model we will use for our example.


```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

model = ChatOpenAI(model="gpt-4o-mini")


@tool
def get_weather(location: str):
    """Call to get the weather from a specific location."""
    # This is a placeholder for the actual implementation
    # Don't let the LLM know this though 😊
    if any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's sunny in San Francisco, but you better look out if you're a Gemini 😈."
    else:
        return f"I am not sure what the weather is in {location}"


tools = [get_weather]

model = model.bind_tools(tools)
```

### Define nodes and edges

Next let's define our nodes and edges. In our basic ReAct agent there are only two nodes, one for calling the model and one for using tools, however you can modify this basic structure to work better for your use case. The tool node we define here is a simplified version of the prebuilt [`ToolNode`](https://langchain-ai.github.io/langgraph/how-tos/tool-calling/), which has some additional features.

Perhaps you want to add a node for [adding structured output](https://langchain-ai.github.io/langgraph/how-tos/react-agent-structured-output/) or a node for executing some external action (sending an email, adding a calendar event, etc.). Maybe you just want to change the way the `call_model` node works and how `should_continue` decides whether to call tools - the possibilities are endless and LangGraph makes it easy to customize this basic structure for your specific use case.


```python
import json
from langchain_core.messages import ToolMessage, SystemMessage
from langchain_core.runnables import RunnableConfig

tools_by_name = {tool.name: tool for tool in tools}



# Define our tool node
def tool_node(state: AgentState):
    outputs = []
    for tool_call in state["messages"][-1].tool_calls:
        tool_result = tools_by_name[tool_call["name"]].invoke(tool_call["args"])
        outputs.append(
            ToolMessage(
                content=json.dumps(tool_result),
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )
    return {"messages": outputs}



# Define the node that calls the model
def call_model(
    state: AgentState,
    config: RunnableConfig,
):
    # this is similar to customizing the create_react_agent with 'prompt' parameter, but is more flexible
    system_prompt = SystemMessage(
        "You are a helpful AI assistant, please respond to the users query to the best of your ability!"
    )
    response = model.invoke([system_prompt] + state["messages"], config)
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}



# Define the conditional edge that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we finish
    if not last_message.tool_calls:
        return "end"
    # Otherwise if there is, we continue
    else:
        return "continue"
```

### Define the graph

Now that we have defined all of our nodes and edges, we can define and compile our graph. Depending on if you have added more nodes or different edges, you will need to edit this to fit your specific use case.


```python
from langgraph.graph import StateGraph, END


# Define a new graph
workflow = StateGraph(AgentState)


# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("tools", tool_node)


# Set the entrypoint as `agent`

# This means that this node is the first one called
workflow.set_entry_point("agent")


# We now add a conditional edge
workflow.add_conditional_edges(
    # First, we define the start node. We use `agent`.
    # This means these are the edges taken after the `agent` node is called.
    "agent",
    # Next, we pass in the function that will determine which node is called next.
    should_continue,
    # Finally we pass in a mapping.
    # The keys are strings, and the values are other nodes.
    # END is a special node marking that the graph should finish.
    # What will happen is we will call `should_continue`, and then the output of that
    # will be matched against the keys in this mapping.
    # Based on which one it matches, that node will then be called.
    {
        # If `tools`, then we call the tool node.
        "continue": "tools",
        # Otherwise we finish.
        "end": END,
    },
)


# We now add a normal edge from `tools` to `agent`.

# This means that after `tools` is called, `agent` node is called next.
workflow.add_edge("tools", "agent")


# Now we can compile and visualize our graph
graph = workflow.compile()

from IPython.display import Image, display

try:
    display(Image(graph.get_graph().draw_mermaid_png()))
except Exception:
    # This requires some extra dependencies and is optional
    pass
```

<p>

</p>


## Use ReAct agent

Now that we have created our react agent, let's actually put it to the test!


```python

# Helper function for formatting the stream nicely
def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()


inputs = {"messages": [("user", "what is the weather in sf")]}
print_stream(graph.stream(inputs, stream_mode="values"))
```
```output
================================ Human Message =================================

what is the weather in sf
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_azW0cQ4XjWWj0IAkWAxq9nLB)
 Call ID: call_azW0cQ4XjWWj0IAkWAxq9nLB
  Args:
    location: San Francisco
================================= Tool Message =================================
Name: get_weather

"It's sunny in San Francisco, but you better look out if you're a Gemini \ud83d\ude08."
================================== Ai Message ==================================

The weather in San Francisco is sunny! However, it seems there's a playful warning for Geminis. Enjoy the sunshine!
```
Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool.


---
how-tos/react-agent-structured-output.ipynb
---


# How to force tool-calling agent to structure output

<div class="admonition tip">
    <p class="admonition-title">Prerequisites</p>
    <p>
        This guide assumes familiarity with the following:
        <ul>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#structured-output">
                    Structured Output
                </a>
            </li>            
            <li>
                <a href="https://langchain-ai.github.io/langgraph/concepts/agentic_concepts/#tool-calling-agent">
                    Tool calling agent
                </a>
            </li>                
            <li>
                <a href="https://python.langchain.com/docs/concepts/#chat-models">
                    Chat Models
                </a>
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#messages">
                    Messages
                </a>
            </li>
            <li>
                <a href="https://langchain-ai.github.io/langgraph/concepts/low_level/">
                    LangGraph Glossary
                </a>
            </li>
        </ul>
    </p>
</div> 

You might want your agent to return its output in a structured format. For example, if the output of the agent is used by some other downstream software, you may want the output to be in the same structured format every time the agent is invoked to ensure consistency.

This notebook will walk through two different options for forcing a tool calling agent to structure its output. We will be using a basic [ReAct agent](https://langchain-ai.github.io/langgraph/how-tos/create-react-agent/) (a model node and a tool-calling node) together with a third node at the end that will format response for the user. Both of the options will use the same graph structure as shown in the diagram below, but will have different mechanisms under the hood.



**Option 1**



The first way you can force your tool calling agent to have structured output is to bind the output you would like as an additional tool for the `agent` node to use. In contrast to the basic ReAct agent, the `agent` node in this case is not selecting between `tools` and `END` but rather selecting between the specific tools it calls. The expected flow in this case is that the LLM in the `agent` node will first select the action tool, and after receiving the action tool output it will call the response tool, which will then route to the `respond` node which simply structures the arguments from the `agent` node tool call.

**Pros and Cons**

The benefit to this format is that you only need one LLM, and can save money and latency because of this. The downside to this option is that it isn't guaranteed that the single LLM will call the correct tool when you want it to. We can help the LLM by setting `tool_choice` to `any` when we use `bind_tools` which forces the LLM to select at least one tool at every turn, but this is far from a foolproof strategy. In addition, another downside is that the agent might call *multiple* tools, so we need to check for this explicitly in our routing function (or if we are using OpenAI we can set `parallell_tool_calling=False` to ensure only one tool is called at a time).

**Option 2**



The second way you can force your tool calling agent to have structured output is to use a second LLM (in this case `model_with_structured_output`) to respond to the user. 

In this case, you will define a basic ReAct agent normally, but instead of having the `agent` node choose between the `tools` node and ending the conversation, the `agent` node will choose between the `tools` node and the `respond` node. The `respond` node will contain a second LLM that uses structured output, and once called will return directly to the user. You can think of this method as basic ReAct with one extra step before responding to the user. 

**Pros and Cons**

The benefit of this method is that it guarantees structured output (as long as `.with_structured_output` works as expected with the LLM). The downside to using this approach is that it requires making an additional LLM call before responding to the user, which can increase costs as well as latency. In addition, by not providing the `agent` node LLM with information about the desired output schema there is a risk that the `agent` LLM will fail to call the correct tools required to answer in the correct output schema.

Note that both of these options will follow the exact same graph structure (see the diagram above), in that they are both exact replicas of the basic ReAct architecture but with a `respond` node before the end.


## Setup

First, let's install the required packages and set our API keys


```shell
pip install -U langgraph langchain_anthropic
```


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


## Define model, tools, and graph state

Now we can define how we want to structure our output, define our graph state, and also our tools and the models we are going to use.

To use structured output, we will use the `with_structured_output` method from LangChain, which you can read more about [here](https://python.langchain.com/docs/how_to/structured_output/).

We are going to use a single tool in this example for finding the weather, and will return a structured weather response to the user.


```python
from pydantic import BaseModel, Field
from typing import Literal
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic
from langgraph.graph import MessagesState


class WeatherResponse(BaseModel):
    """Respond to the user with this"""

    temperature: float = Field(description="The temperature in fahrenheit")
    wind_directon: str = Field(
        description="The direction of the wind in abbreviated form"
    )
    wind_speed: float = Field(description="The speed of the wind in km/h")



# Inherit 'messages' key from MessagesState, which is a list of chat messages
class AgentState(MessagesState):
    # Final structured response from the agent
    final_response: WeatherResponse


@tool
def get_weather(city: Literal["nyc", "sf"]):
    """Use this to get weather information."""
    if city == "nyc":
        return "It is cloudy in NYC, with 5 mph winds in the North-East direction and a temperature of 70 degrees"
    elif city == "sf":
        return "It is 75 degrees and sunny in SF, with 3 mph winds in the South-East direction"
    else:
        raise AssertionError("Unknown city")


tools = [get_weather]

model = ChatAnthropic(model="claude-3-opus-20240229")

model_with_tools = model.bind_tools(tools)
model_with_structured_output = model.with_structured_output(WeatherResponse)
```


## Option 1: Bind output as tool

Let's now examine how we would use the single LLM option.

### Define Graph

The graph definition is very similar to the one above, the only difference is we no longer call an LLM in the `response` node, and instead bind the `WeatherResponse` tool to our LLM that already contains the `get_weather` tool.


```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

tools = [get_weather, WeatherResponse]


# Force the model to use tools by passing tool_choice="any"
model_with_response_tool = model.bind_tools(tools, tool_choice="any")



# Define the function that calls the model
def call_model(state: AgentState):
    response = model_with_response_tool.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}



# Define the function that responds to the user
def respond(state: AgentState):
    # Construct the final answer from the arguments of the last tool call
    weather_tool_call = state["messages"][-1].tool_calls[0]
    response = WeatherResponse(**weather_tool_call["args"])
    # Since we're using tool calling to return structured output,
    # we need to add  a tool message corresponding to the WeatherResponse tool call,
    # This is due to LLM providers' requirement that AI messages with tool calls
    # need to be followed by a tool message for each tool call
    tool_message = {
        "type": "tool",
        "content": "Here is your structured response",
        "tool_call_id": weather_tool_call["id"],
    }
    # We return the final answer
    return {"final_response": response, "messages": [tool_message]}



# Define the function that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is only one tool call and it is the response tool call we respond to the user
    if (
        len(last_message.tool_calls) == 1
        and last_message.tool_calls[0]["name"] == "WeatherResponse"
    ):
        return "respond"
    # Otherwise we will use the tool node again
    else:
        return "continue"



# Define a new graph
workflow = StateGraph(AgentState)


# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("respond", respond)
workflow.add_node("tools", ToolNode(tools))


# Set the entrypoint as `agent`

# This means that this node is the first one called
workflow.set_entry_point("agent")


# We now add a conditional edge
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "respond": "respond",
    },
)

workflow.add_edge("tools", "agent")
workflow.add_edge("respond", END)
graph = workflow.compile()
```

### Usage

Now we can run our graph to check that it worked as intended:


```python
answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
    "final_response"
]
```


```python
answer
```



```output
WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=3.0)
```


Again, the agent returned a `WeatherResponse` object as we expected.


## Option 2: 2 LLMs

Let's now dive into how we would use a second LLM to force structured output.

### Define Graph

We can now define our graph:


```python
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode
from langchain_core.messages import HumanMessage



# Define the function that calls the model
def call_model(state: AgentState):
    response = model_with_tools.invoke(state["messages"])
    # We return a list, because this will get added to the existing list
    return {"messages": [response]}



# Define the function that responds to the user
def respond(state: AgentState):
    # We call the model with structured output in order to return the same format to the user every time
    # state['messages'][-2] is the last ToolMessage in the convo, which we convert to a HumanMessage for the model to use
    # We could also pass the entire chat history, but this saves tokens since all we care to structure is the output of the tool
    response = model_with_structured_output.invoke(
        [HumanMessage(content=state["messages"][-2].content)]
    )
    # We return the final answer
    return {"final_response": response}



# Define the function that determines whether to continue or not
def should_continue(state: AgentState):
    messages = state["messages"]
    last_message = messages[-1]
    # If there is no function call, then we respond to the user
    if not last_message.tool_calls:
        return "respond"
    # Otherwise if there is, we continue
    else:
        return "continue"



# Define a new graph
workflow = StateGraph(AgentState)


# Define the two nodes we will cycle between
workflow.add_node("agent", call_model)
workflow.add_node("respond", respond)
workflow.add_node("tools", ToolNode(tools))


# Set the entrypoint as `agent`

# This means that this node is the first one called
workflow.set_entry_point("agent")


# We now add a conditional edge
workflow.add_conditional_edges(
    "agent",
    should_continue,
    {
        "continue": "tools",
        "respond": "respond",
    },
)

workflow.add_edge("tools", "agent")
workflow.add_edge("respond", END)
graph = workflow.compile()
```


### Usage

We can now invoke our graph to verify that the output is being structured as desired:


```python
answer = graph.invoke(input={"messages": [("human", "what's the weather in SF?")]})[
    "final_response"
]
```


```python
answer
```



```output
WeatherResponse(temperature=75.0, wind_directon='SE', wind_speed=4.83)
```


As we can see, the agent returned a `WeatherResponse` object as we expected. If would now be easy to use this agent in a more complex software stack without having to worry about the output of the agent not matching the format expected from the next step in the stack.


---
how-tos/disable-streaming.ipynb
---


# How to disable streaming for models that don't support it

<div class="admonition tip">
    <p class="admonition-title">Prerequisites</p>
    <p>
        This guide assumes familiarity with the following:
        <ul>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#streaming">
                    streaming
                </a>                
            </li>
            <li>
                <a href="https://python.langchain.com/docs/concepts/#chat-models/">
                    Chat Models
                </a>
            </li>
        </ul>
    </p>
</div> 

Some chat models, including the new O1 models from OpenAI (depending on when you're reading this), do not support streaming. This can lead to issues when using the [astream_events API](https://python.langchain.com/docs/concepts/#astream_events), as it calls models in streaming mode, expecting streaming to function properly.

In this guide, we’ll show you how to disable streaming for models that don’t support it, ensuring they they're never called in streaming mode, even when invoked through the astream_events API.


```python
from langchain_openai import ChatOpenAI
from langgraph.graph import MessagesState
from langgraph.graph import StateGraph, START, END

llm = ChatOpenAI(model="o1-preview", temperature=1)

graph_builder = StateGraph(MessagesState)


def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()
```


```python
from IPython.display import Image, display

display(Image(graph.get_graph().draw_mermaid_png()))
```

<p>

</p>


## Without disabling streaming

Now that we've defined our graph, let's try to call `astream_events` without disabling streaming. This should throw an error because the `o1` model does not support streaming natively:


```python
input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
try:
    async for event in graph.astream_events(input, version="v2"):
        if event["event"] == "on_chat_model_end":
            print(event["data"]["output"].content, end="", flush=True)
except:
    print("Streaming not supported!")
```
```output
Streaming not supported!
```
An error occurred as we expected, luckily there is an easy fix!


## Disabling streaming

Now without making any changes to our graph, let's set the [disable_streaming](https://python.langchain.com/api_reference/core/language_models/langchain_core.language_models.chat_models.BaseChatModel.html#langchain_core.language_models.chat_models.BaseChatModel.disable_streaming) parameter on our model to be `True` which will solve the problem:


```python
llm = ChatOpenAI(model="o1-preview", temperature=1, disable_streaming=True)

graph_builder = StateGraph(MessagesState)


def chatbot(state: MessagesState):
    return {"messages": [llm.invoke(state["messages"])]}


graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", END)
graph = graph_builder.compile()
```

And now, rerunning with the same input, we should see no errors:


```python
input = {"messages": {"role": "user", "content": "how many r's are in strawberry?"}}
async for event in graph.astream_events(input, version="v2"):
    if event["event"] == "on_chat_model_end":
        print(event["data"]["output"].content, end="", flush=True)
```
```output
There are three "r"s in the word "strawberry".
```

---
how-tos/react-agent-from-scratch-functional.ipynb
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


## Setup

First, let's install the required packages and set our API keys:


```shell
pip install -U langgraph langchain-openai
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
     <p class="admonition-title">Set up <a href="https://smith.langchain.com">LangSmith</a> for better debugging</p>
     <p style="padding-top: 5px;">
         Sign up for LangSmith to quickly spot issues and improve the performance of your LangGraph projects. LangSmith lets you use trace data to debug, test, and monitor your LLM aps built with LangGraph — read more about how to get started in the <a href="https://docs.smith.langchain.com">docs</a>. 
     </p>
 </div>


## Create ReAct agent

Now that you have installed the required packages and set your environment variables, we can create our agent.

### Define model and tools

Let's first define the tools and model we will use for our example. Here we will use a single place-holder tool that gets a description of the weather for a location.

We will use an [OpenAI](https://python.langchain.com/docs/integrations/providers/openai/) chat model for this example, but any model [supporting tool-calling](https://python.langchain.com/docs/integrations/chat/) will suffice.


```python
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool

model = ChatOpenAI(model="gpt-4o-mini")


@tool
def get_weather(location: str):
    """Call to get the weather from a specific location."""
    # This is a placeholder for the actual implementation
    if any([city in location.lower() for city in ["sf", "san francisco"]]):
        return "It's sunny!"
    elif "boston" in location.lower():
        return "It's rainy!"
    else:
        return f"I am not sure what the weather is in {location}"


tools = [get_weather]
```

### Define tasks

We next define the <a href="../../concepts/functional_api/#task">tasks</a> we will execute. Here there are two different tasks:

1. **Call model**: We want to query our chat model with a list of messages.
2. **Call tool**: If our model generates tool calls, we want to execute them.


```python
from langchain_core.messages import ToolMessage
from langgraph.func import entrypoint, task

tools_by_name = {tool.name: tool for tool in tools}


@task
def call_model(messages):
    """Call model with a sequence of messages."""
    response = model.bind_tools(tools).invoke(messages)
    return response


@task
def call_tool(tool_call):
    tool = tools_by_name[tool_call["name"]]
    observation = tool.invoke(tool_call["args"])
    return ToolMessage(content=observation, tool_call_id=tool_call["id"])
```

### Define entrypoint

Our <a href="../../concepts/functional_api/#entrypoint">entrypoint</a> will handle the orchestration of these two tasks. As described above, when our `call_model` task generates tool calls, the `call_tool` task will generate responses for each. We append all messages to a single messages list.

!!! tip
    Note that because tasks return future-like objects, the below implementation executes tools in parallel.


```python
from langgraph.graph.message import add_messages


@entrypoint()
def agent(messages):
    llm_response = call_model(messages).result()
    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in llm_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]

        # Append to message list
        messages = add_messages(messages, [llm_response, *tool_results])

        # Call model again
        llm_response = call_model(messages).result()

    return llm_response
```


## Usage

To use our agent, we invoke it with a messages list. Based on our implementation, these can be LangChain [message](https://python.langchain.com/docs/concepts/messages/) objects or OpenAI-style dicts:


```python
user_message = {"role": "user", "content": "What's the weather in san francisco?"}
print(user_message)

for step in agent.stream([user_message]):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': "What's the weather in san francisco?"}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_tNnkrjnoz6MNfCHJpwfuEQ0v)
 Call ID: call_tNnkrjnoz6MNfCHJpwfuEQ0v
  Args:
    location: san francisco

call_tool:
================================= Tool Message =================================

It's sunny!

call_model:
================================== Ai Message ==================================

The weather in San Francisco is sunny!
```
Perfect! The graph correctly calls the `get_weather` tool and responds to the user after receiving the information from the tool. Check out the LangSmith trace [here](https://smith.langchain.com/public/d5a0d5ea-bdaa-4032-911e-7db177c8141b/r).


## Add thread-level persistence

Adding <a href="../../concepts/persistence#threads">thread-level persistence</a> lets us support conversational experiences with our agent: subsequent invocations will append to the prior messages list, retaining the full conversational context.

To add thread-level persistence to our agent:

1. Select a <a href="../../concepts/persistence#checkpointer-libraries">checkpointer</a>: here we will use <a href="../../reference/checkpoints/#langgraph.checkpoint.memory.InMemorySaver">InMemorySaver</a>, a simple in-memory checkpointer.
2. Update our entrypoint to accept the previous messages state as a second argument. Here, we simply append the message updates to the previous sequence of messages.
3. Choose which values will be returned from the workflow and which will be saved by the checkpointer as `previous` using `entrypoint.final` (optional)


```python hl_lines="3 6 7 8 9 30"
from langgraph.checkpoint.memory import InMemorySaver

checkpointer = InMemorySaver()


@entrypoint(checkpointer=checkpointer)
def agent(messages, previous):
    if previous is not None:
        messages = add_messages(previous, messages)

    llm_response = call_model(messages).result()
    while True:
        if not llm_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in llm_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]

        # Append to message list
        messages = add_messages(messages, [llm_response, *tool_results])

        # Call model again
        llm_response = call_model(messages).result()

    # Generate final response
    messages = add_messages(messages, llm_response)
    return entrypoint.final(value=llm_response, save=messages)
```

We will now need to pass in a config when running our application. The config will specify an identifier for the conversational thread.

!!! tip

    Read more about thread-level persistence in our <a href="../../concepts/persistence/">concepts page</a> and <a href="../../how-tos/#persistence">how-to guides</a>.


```python
config = {"configurable": {"thread_id": "1"}}
```

We start a thread the same way as before, this time passing in the config:


```python hl_lines="4"
user_message = {"role": "user", "content": "What's the weather in san francisco?"}
print(user_message)

for step in agent.stream([user_message], config):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': "What's the weather in san francisco?"}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_lubbUSdDofmOhFunPEZLBz3g)
 Call ID: call_lubbUSdDofmOhFunPEZLBz3g
  Args:
    location: San Francisco

call_tool:
================================= Tool Message =================================

It's sunny!

call_model:
================================== Ai Message ==================================

The weather in San Francisco is sunny!
```
When we ask a follow-up conversation, the model uses the prior context to infer that we are asking about the weather:


```python
user_message = {"role": "user", "content": "How does it compare to Boston, MA?"}
print(user_message)

for step in agent.stream([user_message], config):
    for task_name, message in step.items():
        if task_name == "agent":
            continue  # Just print task updates
        print(f"\n{task_name}:")
        message.pretty_print()
```
```output
{'role': 'user', 'content': 'How does it compare to Boston, MA?'}

call_model:
================================== Ai Message ==================================
Tool Calls:
  get_weather (call_8sTKYAhSIHOdjLD5d6gaswuV)
 Call ID: call_8sTKYAhSIHOdjLD5d6gaswuV
  Args:
    location: Boston, MA

call_tool:
================================= Tool Message =================================

It's rainy!

call_model:
================================== Ai Message ==================================

Compared to San Francisco, which is sunny, Boston, MA is experiencing rainy weather.
```
In the [LangSmith trace](https://smith.langchain.com/public/20a1116b-bb3b-44c1-8765-7a28663439d9/r), we can see that the full conversational context is retained in each model call.


---
concepts/assistants.md
---


# Assistants

**Assistants** allow you to manage configurations (like prompts, LLM selection, tools) separately from your graph's core logic, enabling rapid changes that don't alter the graph architecture. It is a way to create multiple specialized versions of the same graph architecture, each optimized for different use cases through context/configuration variations rather than structural changes.

For example, imagine a general-purpose writing agent built on a common graph architecture. While the structure remains the same, different writing styles—such as blog posts and tweets—require tailored configurations to optimize performance. To support these variations, you can create multiple assistants (e.g., one for blogs and another for tweets) that share the underlying graph but differ in model selection and system prompt.

![assistant versions](img/assistants.png)

The LangGraph Cloud API provides several endpoints for creating and managing assistants and their versions. See the [API reference](../cloud/reference/api/api_ref.html#tag/assistants) for more details.

!!! info

    Assistants are a [LangGraph Platform](langgraph_platform.md) concept. They are not available in the open source LangGraph library.


## Configuration

Assistants build on the LangGraph open source concepts of configuration and [runtime context](low_level.md#runtime-context).


While these features are available in the open source LangGraph library, assistants are only present in [LangGraph Platform](langgraph_platform.md). This is due to the fact that assistants are tightly coupled to your deployed graph. Upon deployment, LangGraph Server will automatically create a default assistant for each graph using the graph's default context and configuration settings.

In practice, an assistant is just an _instance_ of a graph with a specific configuration. Therefore, multiple assistants can reference the same graph but can contain different configurations (e.g. prompts, models, tools). The LangGraph Server API provides several endpoints for creating and managing assistants. See the [API reference](../cloud/reference/api/api_ref.html) and [this how-to](../cloud/how-tos/configuration_cloud.md) for more details on how to create assistants.


## Versioning

Assistants support versioning to track changes over time.
Once you've created an assistant, subsequent edits to that assistant will create new versions. See [this how-to](../cloud/how-tos/configuration_cloud.md#create-a-new-version-for-your-assistant) for more details on how to manage assistant versions.


## Execution

A **run** is an invocation of an assistant. Each run may have its own input, configuration, context, and metadata, which may affect execution and output of the underlying graph. A run can optionally be executed on a [thread](./persistence.md#threads).

The LangGraph Platform API provides several endpoints for creating and managing runs. See the [API reference](../cloud/reference/api/api_ref.html#tag/thread-runs/) for more details.


---
concepts/langgraph_studio.md
---

---
search:
  boost: 2
---


# LangGraph Studio

!!! info "Prerequisites"

    - [LangGraph Platform](./langgraph_platform.md)
    - [LangGraph Server](./langgraph_server.md)
    - [LangGraph CLI](./langgraph_cli.md)

LangGraph Studio is a specialized agent IDE that enables visualization, interaction, and debugging of agentic systems that implement the LangGraph Server API protocol. Studio also integrates with LangSmith to enable tracing, evaluation, and prompt engineering.

![](img/lg_studio.png)


## Features

Key features of LangGraph Studio:

- Visualize your graph architecture
- [Run and interact with your agent](../cloud/how-tos/invoke_studio.md)
- [Manage assistants](../cloud/how-tos/studio/manage_assistants.md)
- [Manage threads](../cloud/how-tos/threads_studio.md)
- [Iterate on prompts](../cloud/how-tos/iterate_graph_studio.md)
- [Run experiments over a dataset](../cloud/how-tos/studio/run_evals.md)
- Manage [long term memory](memory.md)
- Debug agent state via [time travel](time-travel.md)

LangGraph Studio works for graphs that are deployed on [LangGraph Platform](../cloud/quick_start.md) or for graphs that are running locally via the [LangGraph Server](../tutorials/langgraph-platform/local-server.md).

Studio supports two modes:

### Graph mode

Graph mode exposes the full feature-set of Studio and is useful when you would like as many details about the execution of your agent, including the nodes traversed, intermediate states, and LangSmith integrations (such as adding to datasets and playground).

### Chat mode

Chat mode is a simpler UI for iterating on and testing chat-specific agents. It is useful for business users and those who want to test overall agent behavior. Chat mode is only supported for graph's whose state includes or extends [`MessagesState`](https://langchain-ai.github.io/langgraph/how-tos/graph-api/#messagesstate).


## Learn more

- See this guide on how to [get started](../cloud/how-tos/studio/quick_start.md) with LangGraph Studio.


---
concepts/double_texting.md
---

---
search:
  boost: 2
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


## Reject

This is the simplest option, this just rejects any follow-up runs and does not allow double texting. 
See the [how-to guide](../cloud/how-tos/reject_concurrent.md) for configuring the reject double text option.


## Enqueue

This is a relatively simple option which continues the first run until it completes the whole run, then sends the new input as a separate run. 
See the [how-to guide](../cloud/how-tos/enqueue_concurrent.md) for configuring the enqueue double text option.


## Interrupt

This option interrupts the current execution but saves all the work done up until that point. 
It then inserts the user input and continues from there. 

If you enable this option, your graph should be able to handle weird edge cases that may arise. 
For example, you could have called a tool but not yet gotten back a result from running that tool.
You may need to remove that tool call in order to not have a dangling tool call.

See the [how-to guide](../cloud/how-tos/interrupt_concurrent.md) for configuring the interrupt double text option.


## Rollback

This option interrupts the current execution AND rolls back all work done up until that point, including the original run input. It then sends the new user input in, basically as if it was the original input.

See the [how-to guide](../cloud/how-tos/rollback_concurrent.md) for configuring the rollback double text option.


---
concepts/pregel.md
---

---
search:
  boost: 2
---


# LangGraph runtime

[Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) implements LangGraph's runtime, managing the execution of LangGraph applications.

Compiling a [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) or creating an [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) produces a [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) instance that can be invoked with input.




This guide explains the runtime at a high level and provides instructions for directly implementing applications with Pregel.

> **Note:** The [Pregel](https://langchain-ai.github.io/langgraph/reference/pregel/) runtime is named after [Google's Pregel algorithm](https://research.google/pubs/pub37252/), which describes an efficient method for large-scale parallel computation using graphs.






## Overview

In LangGraph, Pregel combines [**actors**](https://en.wikipedia.org/wiki/Actor_model) and **channels** into a single application. **Actors** read data from channels and write data to channels. Pregel organizes the execution of the application into multiple steps, following the **Pregel Algorithm**/**Bulk Synchronous Parallel** model.

Each step consists of three phases:

- **Plan**: Determine which **actors** to execute in this step. For example, in the first step, select the **actors** that subscribe to the special **input** channels; in subsequent steps, select the **actors** that subscribe to channels updated in the previous step.
- **Execution**: Execute all selected **actors** in parallel, until all complete, or one fails, or a timeout is reached. During this phase, channel updates are invisible to actors until the next step.
- **Update**: Update the channels with the values written by the **actors** in this step.

Repeat until no **actors** are selected for execution, or a maximum number of steps is reached.


## Actors

An **actor** is a `PregelNode`. It subscribes to channels, reads data from them, and writes data to them. It can be thought of as an **actor** in the Pregel algorithm. `PregelNodes` implement LangChain's Runnable interface.


## Channels

Channels are used to communicate between actors (PregelNodes). Each channel has a value type, an update type, and an update function – which takes a sequence of updates and modifies the stored value. Channels can be used to send data from one chain to another, or to send data from a chain to itself in a future step. LangGraph provides a number of built-in channels:

- [LastValue](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.LastValue): The default channel, stores the last value sent to the channel, useful for input and output values, or for sending data from one step to the next.
- [Topic](https://langchain-ai.github.io/langgraph/reference/channels/#langgraph.channels.Topic): A configurable PubSub Topic, useful for sending multiple values between **actors**, or for accumulating output. Can be configured to deduplicate values or to accumulate values over the course of multiple steps.
- [BinaryOperatorAggregate](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel--advanced-channels-context-and-binaryoperatoraggregate): stores a persistent value, updated by applying a binary operator to the current value and each update sent to the channel, useful for computing aggregates over multiple steps; e.g.,`total = BinaryOperatorAggregate(int, operator.add)`





## Examples

While most users will interact with Pregel through the [StateGraph](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) API or the [entrypoint](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) decorator, it is possible to interact with Pregel directly.




Below are a few different examples to give you a sense of the Pregel API.

=== "Single node"

    ```python
    from langgraph.channels import EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder

    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b")
    )

    app = Pregel(
        nodes={"node1": node1},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
        },
        input_channels=["a"],
        output_channels=["b"],
    )

    app.invoke({"a": "foo"})
    ```

    ```con
    {'b': 'foofoo'}
    ```




=== "Multiple nodes"

    ```python
    from langgraph.channels import LastValue, EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder

    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b")
    )

    node2 = (
        NodeBuilder().subscribe_only("b")
        .do(lambda x: x + x)
        .write_to("c")
    )


    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": LastValue(str),
            "c": EphemeralValue(str),
        },
        input_channels=["a"],
        output_channels=["b", "c"],
    )

    app.invoke({"a": "foo"})
    ```

    ```con
    {'b': 'foofoo', 'c': 'foofoofoofoo'}
    ```




=== "Topic"

    ```python
    from langgraph.channels import EphemeralValue, Topic
    from langgraph.pregel import Pregel, NodeBuilder

    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b", "c")
    )

    node2 = (
        NodeBuilder().subscribe_to("b")
        .do(lambda x: x["b"] + x["b"])
        .write_to("c")
    )

    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
            "c": Topic(str, accumulate=True),
        },
        input_channels=["a"],
        output_channels=["c"],
    )

    app.invoke({"a": "foo"})
    ```

    ```pycon
    {'c': ['foofoo', 'foofoofoofoo']}
    ```




=== "BinaryOperatorAggregate"

    This examples demonstrates how to use the BinaryOperatorAggregate channel to implement a reducer.

    ```python
    from langgraph.channels import EphemeralValue, BinaryOperatorAggregate
    from langgraph.pregel import Pregel, NodeBuilder


    node1 = (
        NodeBuilder().subscribe_only("a")
        .do(lambda x: x + x)
        .write_to("b", "c")
    )

    node2 = (
        NodeBuilder().subscribe_only("b")
        .do(lambda x: x + x)
        .write_to("c")
    )

    def reducer(current, update):
        if current:
            return current + " | " + update
        else:
            return update

    app = Pregel(
        nodes={"node1": node1, "node2": node2},
        channels={
            "a": EphemeralValue(str),
            "b": EphemeralValue(str),
            "c": BinaryOperatorAggregate(str, operator=reducer),
        },
        input_channels=["a"],
        output_channels=["c"],
    )

    app.invoke({"a": "foo"})
    ```




=== "Cycle"

    This example demonstrates how to introduce a cycle in the graph, by having
    a chain write to a channel it subscribes to. Execution will continue
    until a `None` value is written to the channel.

    ```python
    from langgraph.channels import EphemeralValue
    from langgraph.pregel import Pregel, NodeBuilder, ChannelWriteEntry

    example_node = (
        NodeBuilder().subscribe_only("value")
        .do(lambda x: x + x if len(x) < 10 else None)
        .write_to(ChannelWriteEntry("value", skip_none=True))
    )

    app = Pregel(
        nodes={"example_node": example_node},
        channels={
            "value": EphemeralValue(str),
        },
        input_channels=["value"],
        output_channels=["value"],
    )

    app.invoke({"value": "a"})
    ```

    ```pycon
    {'value': 'aaaaaaaaaaaaaaaa'}
    ```





## High-level API

LangGraph provides two high-level APIs for creating a Pregel application: the [StateGraph (Graph API)](./low_level.md) and the [Functional API](functional_api.md).

=== "StateGraph (Graph API)"

    The [StateGraph (Graph API)](https://langchain-ai.github.io/langgraph/reference/graphs/#langgraph.graph.StateGraph) is a higher-level abstraction that simplifies the creation of Pregel applications. It allows you to define a graph of nodes and edges. When you compile the graph, the StateGraph API automatically creates the Pregel application for you.

    ```python
    from typing import TypedDict, Optional

    from langgraph.constants import START
    from langgraph.graph import StateGraph

    class Essay(TypedDict):
        topic: str
        content: Optional[str]
        score: Optional[float]

    def write_essay(essay: Essay):
        return {
            "content": f"Essay about {essay['topic']}",
        }

    def score_essay(essay: Essay):
        return {
            "score": 10
        }

    builder = StateGraph(Essay)
    builder.add_node(write_essay)
    builder.add_node(score_essay)
    builder.add_edge(START, "write_essay")

    # Compile the graph.
    # This will return a Pregel instance.
    graph = builder.compile()
    ```




    The compiled Pregel instance will be associated with a list of nodes and channels. You can inspect the nodes and channels by printing them.

    ```python
    print(graph.nodes)
    ```

    You will see something like this:

    ```pycon
    {'__start__': <langgraph.pregel.read.PregelNode at 0x7d05e3ba1810>,
     'write_essay': <langgraph.pregel.read.PregelNode at 0x7d05e3ba14d0>,
     'score_essay': <langgraph.pregel.read.PregelNode at 0x7d05e3ba1710>}
    ```

    ```python
    print(graph.channels)
    ```

    You should see something like this

    ```pycon
    {'topic': <langgraph.channels.last_value.LastValue at 0x7d05e3294d80>,
     'content': <langgraph.channels.last_value.LastValue at 0x7d05e3295040>,
     'score': <langgraph.channels.last_value.LastValue at 0x7d05e3295980>,
     '__start__': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e3297e00>,
     'write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e32960c0>,
     'score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8ab80>,
     'branch:__start__:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e32941c0>,
     'branch:__start__:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d88800>,
     'branch:write_essay:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e3295ec0>,
     'branch:write_essay:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8ac00>,
     'branch:score_essay:__self__:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d89700>,
     'branch:score_essay:__self__:score_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8b400>,
     'start:write_essay': <langgraph.channels.ephemeral_value.EphemeralValue at 0x7d05e2d8b280>}
    ```




=== "Functional API"

    In the [Functional API](functional_api.md), you can use an [`entrypoint`](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) to create a Pregel application. The `entrypoint` decorator allows you to define a function that takes input and returns output.

    ```python
    from typing import TypedDict, Optional

    from langgraph.checkpoint.memory import InMemorySaver
    from langgraph.func import entrypoint

    class Essay(TypedDict):
        topic: str
        content: Optional[str]
        score: Optional[float]


    checkpointer = InMemorySaver()

    @entrypoint(checkpointer=checkpointer)
    def write_essay(essay: Essay):
        return {
            "content": f"Essay about {essay['topic']}",
        }

    print("Nodes: ")
    print(write_essay.nodes)
    print("Channels: ")
    print(write_essay.channels)
    ```

    ```pycon
    Nodes:
    {'write_essay': <langgraph.pregel.read.PregelNode object at 0x7d05e2f9aad0>}
    Channels:
    {'__start__': <langgraph.channels.ephemeral_value.EphemeralValue object at 0x7d05e2c906c0>, '__end__': <langgraph.channels.last_value.LastValue object at 0x7d05e2c90c40>, '__previous__': <langgraph.channels.last_value.LastValue object at 0x7d05e1007280>}
    ```





---
concepts/plans.md
---

---
search:
  boost: 2
---


# LangGraph Platform Plans



## Overview
LangGraph Platform is a solution for deploying agentic applications in production.
There are three different plans for using it.

- **Developer**: All [LangSmith](https://smith.langchain.com/) users have access to this plan. You can sign up for this plan simply by creating a LangSmith account. This gives you access to the [local deployment](./deployment_options.md#free-deployment) option.
- **Plus**: All [LangSmith](https://smith.langchain.com/) users with a [Plus account](https://docs.smith.langchain.com/administration/pricing) have access to this plan. You can sign up for this plan simply by upgrading your LangSmith account to the Plus plan type. This gives you access to the [Cloud](./deployment_options.md#cloud-saas) deployment option.
- **Enterprise**: This is separate from LangSmith plans. You can sign up for this plan by [contacting our sales team](https://www.langchain.com/contact-sales). This gives you access to all [deployment options](./deployment_options.md).



## Plan Details

|                                                                  | Developer                                   | Plus                                                  | Enterprise                                          |
|------------------------------------------------------------------|---------------------------------------------|-------------------------------------------------------|-----------------------------------------------------|
| Deployment Options                                               | Local                          | Cloud SaaS                                         | <ul><li>Cloud SaaS</li><li>Self-Hosted Data Plane</li><li>Self-Hosted Control Plane</li><li>Standalone Container</li></ul> |
| Usage                                                            | Free | See [Pricing](https://www.langchain.com/langgraph-platform-pricing) | Custom                                              |
| APIs for retrieving and updating state and conversational history | ✅                                           | ✅                                                     | ✅                                                   |
| APIs for retrieving and updating long-term memory                | ✅                                           | ✅                                                     | ✅                                                   |
| Horizontally scalable task queues and servers                    | ✅                                           | ✅                                                     | ✅                                                   |
| Real-time streaming of outputs and intermediate steps            | ✅                                           | ✅                                                     | ✅                                                   |
| Assistants API (configurable templates for LangGraph apps)       | ✅                                           | ✅                                                     | ✅                                                   |
| Cron scheduling                                                  | --                                          | ✅                                                     | ✅                                                   |
| LangGraph Studio for prototyping                                 | 	✅                                         | ✅                                                    | ✅                                                  |
| Authentication & authorization to call the LangGraph APIs        | --                                          | Coming Soon!                                          | Coming Soon!                                        |
| Smart caching to reduce traffic to LLM API                       | --                                          | Coming Soon!                                          | Coming Soon!                                        |
| Publish/subscribe API for state                                  | --                                          | Coming Soon!                                          | Coming Soon!                                        |
| Scheduling prioritization                                        | --                                          | Coming Soon!                                          | Coming Soon!                                        |

For pricing information, see [LangGraph Platform Pricing](https://www.langchain.com/langgraph-platform-pricing).


## Related

For more information, please see:

* [Deployment Options conceptual guide](./deployment_options.md)
* [LangGraph Platform Pricing](https://www.langchain.com/langgraph-platform-pricing)
* [LangSmith Plans](https://docs.smith.langchain.com/administration/pricing)


---
concepts/template_applications.md
---

---
search:
  boost: 2
---


# Template Applications

Templates are open source reference applications designed to help you get started quickly when building with LangGraph. They provide working examples of common agentic workflows that can be customized to your needs.

You can create an application from a template using the LangGraph CLI.

!!! info "Requirements"

    - Python >= 3.11
    - [LangGraph CLI](https://langchain-ai.github.io/langgraph/cloud/reference/cli/): Requires langchain-cli[inmem] >= 0.1.58


## Install the LangGraph CLI

```bash
pip install "langgraph-cli[inmem]" --upgrade
```

Or via [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (recommended):

```bash
uvx --from "langgraph-cli[inmem]" langgraph dev --help
```






## Available Templates

| Template | Description | Link |
| -------- | ----------- | ------ |
| **New LangGraph Project** | A simple, minimal chatbot with memory. | [Repo](https://github.com/langchain-ai/new-langgraph-project) |
| **ReAct Agent** | A simple agent that can be flexibly extended to many tools. | [Repo](https://github.com/langchain-ai/react-agent) |
| **Memory Agent** | A ReAct-style agent with an additional tool to store memories for use across threads. | [Repo](https://github.com/langchain-ai/memory-agent) |
| **Retrieval Agent** | An agent that includes a retrieval-based question-answering system. | [Repo](https://github.com/langchain-ai/retrieval-agent-template) |
| **Data-Enrichment Agent** | An agent that performs web searches and organizes its findings into a structured format. | [Repo](https://github.com/langchain-ai/data-enrichment) |






## 🌱 Create a LangGraph App

To create a new app from a template, use the `langgraph new` command.

```bash
langgraph new
```

Or via [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (recommended):

```bash
uvx --from "langgraph-cli[inmem]" langgraph new
```






## Next Steps

Review the `README.md` file in the root of your new LangGraph app for more information about the template and how to customize it.

After configuring the app properly and adding your API keys, you can start the app using the LangGraph CLI:

```bash
langgraph dev
```

Or via [`uv`](https://docs.astral.sh/uv/getting-started/installation/) (recommended):

```bash
uvx --from "langgraph-cli[inmem]" --with-editable . langgraph dev
```

!!! info "Missing Local Package?"

    If you are not using `uv` and run into a "`ModuleNotFoundError`" or "`ImportError`", even after installing the local package (`pip install -e .`), it is likely the case that you need to install the CLI into your local virtual environment to make the CLI "aware" of the local package. You can do this by running `python -m pip install "langgraph-cli[inmem]"` and re-activating your virtual environment before running `langgraph dev`.





See the following guides for more information on how to deploy your app:

- **[Launch Local LangGraph Server](../tutorials/langgraph-platform/local-server.md)**: This quick start guide shows how to start a LangGraph Server locally for the **ReAct Agent** template. The steps are similar for other templates.
- **[Deploy to LangGraph Platform](../cloud/quick_start.md)**: Deploy your LangGraph app using LangGraph Platform.


---
concepts/tools.md
---


# Tools

Many AI applications interact with users via natural language. However, some use cases require models to interface directly with external systems—such as APIs, databases, or file systems—using structured input. In these scenarios, [tool calling](../how-tos/tool-calling.md) enables models to generate requests that conform to a specified input schema.

**Tools** encapsulate a callable function and its input schema. These can be passed to compatible [chat models](https://python.langchain.com/docs/concepts/chat_models), allowing the model to decide whether to invoke a tool and with what arguments.





## Tool calling

![Diagram of a tool call by a model](./img/tool_call.png)

Tool calling is typically **conditional**. Based on the user input and available tools, the model may choose to issue a tool call request. This request is returned in an `AIMessage` object, which includes a `tool_calls` field that specifies the tool name and input arguments:

```python
llm_with_tools.invoke("What is 2 multiplied by 3?")

# -> AIMessage(tool_calls=[{'name': 'multiply', 'args': {'a': 2, 'b': 3}, ...}])
```

```
AIMessage(
  tool_calls=[
    ToolCall(name="multiply", args={"a": 2, "b": 3}),
    ...
  ]
)
```





If the input is unrelated to any tool, the model returns only a natural language message:

```python
llm_with_tools.invoke("Hello world!")  # -> AIMessage(content="Hello!")
```





Importantly, the model does not execute the tool—it only generates a request. A separate executor (such as a runtime or agent) is responsible for handling the tool call and returning the result.

See the [tool calling guide](../how-tos/tool-calling.md) for more details.


## Prebuilt tools

LangChain provides prebuilt tool integrations for common external systems including APIs, databases, file systems, and web data.

Browse the [integrations directory](https://python.langchain.com/docs/integrations/tools/) for available tools.




Common categories:

- **Search**: Bing, SerpAPI, Tavily
- **Code execution**: Python REPL, Node.js REPL
- **Databases**: SQL, MongoDB, Redis
- **Web data**: Scraping and browsing
- **APIs**: OpenWeatherMap, NewsAPI, etc.


## Custom tools

You can define custom tools using the `@tool` decorator or plain Python functions. For example:

```python
from langchain_core.tools import tool

@tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b
```





See the [tool calling guide](../how-tos/tool-calling.md) for more details.


## Tool execution

While the model determines when to call a tool, execution of the tool call must be handled by a runtime component.

LangGraph provides prebuilt components for this:

- [`ToolNode`](https://langchain-ai.github.io/langgraph/reference/agents/#langgraph.prebuilt.tool_node.ToolNode): A prebuilt node that executes tools.
- [`create_react_agent`](https://langchain-ai.github.io/langgraph/reference/prebuilt/#langgraph.prebuilt.chat_agent_executor.create_react_agent): Constructs a full agent that manages tool calling automatically.





---
concepts/subgraphs.md
---


# Subgraphs

A subgraph is a [graph](./low_level.md#graphs) that is used as a [node](./low_level.md#nodes) in another graph — this is the concept of encapsulation applied to LangGraph. Subgraphs allow you to build complex systems with multiple components that are themselves graphs.

![Subgraph](./img/subgraph.png)

Some reasons for using subgraphs are:

- building [multi-agent systems](./multi_agent.md)
- when you want to reuse a set of nodes in multiple graphs
- when you want different teams to work on different parts of the graph independently, you can define each part as a subgraph, and as long as the subgraph interface (the input and output schemas) is respected, the parent graph can be built without knowing any details of the subgraph

The main question when adding subgraphs is how the parent graph and subgraph communicate, i.e. how they pass the [state](./low_level.md#state) between each other during the graph execution. There are two scenarios:

- parent and subgraph have **shared state keys** in their state [schemas](./low_level.md#state). In this case, you can [include the subgraph as a node in the parent graph](../how-tos/subgraph.ipynb#shared-state-schemas)

  ```python hl_lines="12 17"
  from langgraph.graph import StateGraph, MessagesState, START

  # Subgraph

  def call_model(state: MessagesState):
      response = model.invoke(state["messages"])
      return {"messages": response}

  subgraph_builder = StateGraph(State)
  subgraph_builder.add_node(call_model)
  ...
  subgraph = subgraph_builder.compile()

  # Parent graph

  builder = StateGraph(State)
  builder.add_node("subgraph_node", subgraph)
  builder.add_edge(START, "subgraph_node")
  graph = builder.compile()
  ...
  graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
  ```





- parent graph and subgraph have **different schemas** (no shared state keys in their state [schemas](./low_level.md#state)). In this case, you have to [call the subgraph from inside a node in the parent graph](../how-tos/subgraph.ipynb#different-state-schemas): this is useful when the parent graph and the subgraph have different state schemas and you need to transform state before or after calling the subgraph

  ```python hl_lines="7 11 19 28"
  from typing_extensions import TypedDict, Annotated
  from langchain_core.messages import AnyMessage
  from langgraph.graph import StateGraph, MessagesState, START
  from langgraph.graph.message import add_messages

  class SubgraphMessagesState(TypedDict):
      subgraph_messages: Annotated[list[AnyMessage], add_messages]

  # Subgraph

  def call_model(state: SubgraphMessagesState):
      response = model.invoke(state["subgraph_messages"])
      return {"subgraph_messages": response}

  subgraph_builder = StateGraph(SubgraphMessagesState)
  subgraph_builder.add_node("call_model_from_subgraph", call_model)
  subgraph_builder.add_edge(START, "call_model_from_subgraph")
  ...
  subgraph = subgraph_builder.compile()

  # Parent graph

  def call_subgraph(state: MessagesState):
      response = subgraph.invoke({"subgraph_messages": state["messages"]})
      return {"messages": response["subgraph_messages"]}

  builder = StateGraph(State)
  builder.add_node("subgraph_node", call_subgraph)
  builder.add_edge(START, "subgraph_node")
  graph = builder.compile()
  ...
  graph.invoke({"messages": [{"role": "user", "content": "hi!"}]})
  ```






---
concepts/langgraph_cloud.md
---

---
search:
  boost: 2
---


# Cloud SaaS

To deploy a [LangGraph Server](../concepts/langgraph_server.md), follow the how-to guide for [how to deploy to Cloud SaaS](../cloud/deployment/cloud.md).


## Overview

The Cloud SaaS deployment option is a fully managed model for deployment where we manage the [control plane](./langgraph_control_plane.md) and [data plane](./langgraph_data_plane.md) in our cloud.

|                                    | [Control plane](../concepts/langgraph_control_plane.md)                                                                                     | [Data plane](../concepts/langgraph_data_plane.md)                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is it?**                    | <ul><li>Control plane UI for creating deployments and revisions</li><li>Control plane APIs for creating deployments and revisions</li></ul> | <ul><li>Data plane "listener" for reconciling deployments with control plane state</li><li>LangGraph Servers</li><li>Postgres, Redis, etc</li></ul> |
| **Where is it hosted?**            | LangChain's cloud                                                                                                                           | LangChain's cloud                                                                                                                                   |
| **Who provisions and manages it?** | LangChain                                                                                                                                   | LangChain                                                                                                                                           |


## Architecture

![Cloud SaaS](./img/self_hosted_control_plane_architecture.png)


---
concepts/langgraph_components.md
---


## Components

The LangGraph Platform consists of components that work together to support the development, deployment, debugging, and monitoring of LangGraph applications:

- [LangGraph Server](./langgraph_server.md): The server defines an opinionated API and architecture that incorporates best practices for deploying agentic applications, allowing you to focus on building your agent logic rather than developing server infrastructure.
- [LangGraph CLI](./langgraph_cli.md): LangGraph CLI is a command-line interface that helps to interact with a local LangGraph
- [LangGraph Studio](./langgraph_studio.md): LangGraph Studio is a specialized IDE that can connect to a LangGraph Server to enable visualization, interaction, and debugging of the application locally.
- [Python/JS SDK](./sdk.md): The Python/JS SDK provides a programmatic way to interact with deployed LangGraph Applications.
- [Remote Graph](../how-tos/use-remote-graph.md): A RemoteGraph allows you to interact with any deployed LangGraph application as though it were running locally.
- [LangGraph control plane](./langgraph_control_plane.md): The LangGraph Control Plane refers to the Control Plane UI where users create and update LangGraph Servers and the Control Plane APIs that support the UI experience.
- [LangGraph data plane](./langgraph_data_plane.md): The LangGraph Data Plane refers to LangGraph Servers, the corresponding infrastructure for each server, and the "listener" application that continuously polls for updates from the LangGraph Control Plane.

![LangGraph components](img/lg_platform.png)


---
concepts/langgraph_standalone_container.md
---

---
search:
  boost: 2
---


# Standalone Container

To deploy a [LangGraph Server](../concepts/langgraph_server.md), follow the how-to guide for [how to deploy a Standalone Container](../cloud/deployment/standalone_container.md).


## Overview

The Standalone Container deployment option is the least restrictive model for deployment. There is no [control plane](./langgraph_control_plane.md). [Data plane](./langgraph_data_plane.md) infrastructure is managed by you.

|                   | [Control plane](../concepts/langgraph_control_plane.md) | [Data plane](../concepts/langgraph_data_plane.md) |
|-------------------|-------------------|------------|
| **What is it?** | n/a | <ul><li>LangGraph Servers</li><li>Postgres, Redis, etc</li></ul> |
| **Where is it hosted?** | n/a | Your cloud |
| **Who provisions and manages it?** | n/a | You |

!!! warning

      LangGraph Platform should not be deployed in serverless environments. Scale to zero may cause task loss and scaling up will not work reliably.


## Architecture

![Standalone Container](./img/langgraph_platform_deployment_architecture.png)


## Compute Platforms

### Kubernetes

The Standalone Container deployment option supports deploying data plane infrastructure to a Kubernetes cluster.

### Docker

The Standalone Container deployment option supports deploying data plane infrastructure to any Docker-supported compute platform.


---
concepts/human_in_the_loop.md
---

---
search:
  boost: 2
tags:
  - human-in-the-loop
  - hil
  - overview
hide:
  - tags
---


# Human-in-the-loop

To review, edit, and approve tool calls in an agent or workflow, [use LangGraph's human-in-the-loop features](../how-tos/human_in_the_loop/add-human-in-the-loop.md) to enable human intervention at any point in a workflow. This is especially useful in large language model (LLM)-driven applications where model output may require validation, correction, or additional context.

<figure markdown="1">
![image](../concepts/img/human_in_the_loop/tool-call-review.png){: style="max-height:400px"}
</figure>

!!! tip

    For information on how to use human-in-the-loop, see [Enable human intervention](../how-tos/human_in_the_loop/add-human-in-the-loop.md) and [Human-in-the-loop using Server API](../cloud/how-tos/add-human-in-the-loop.md).


## Key capabilities

* **Persistent execution state**: Interrupts use LangGraph's [persistence](./persistence.md) layer, which saves the graph state, to indefinitely pause graph execution until you resume. This is possible because LangGraph checkpoints the graph state after each step, which allows the system to persist execution context and later resume the workflow, continuing from where it left off. This supports asynchronous human review or input without time constraints.

    There are two ways to pause a graph:

    - [Dynamic interrupts](../how-tos/human_in_the_loop/add-human-in-the-loop.md#pause-using-interrupt): Use `interrupt` to pause a graph from inside a specific node, based on the current state of the graph.
    - [Static interrupts](../how-tos/human_in_the_loop/add-human-in-the-loop.md#debug-with-interrupts): Use `interrupt_before` and `interrupt_after` to pause the graph at pre-defined points, either before or after a node executes.

    <figure markdown="1">
    ![image](./img/breakpoints.png){: style="max-height:400px"}
    <figcaption>An example graph consisting of 3 sequential steps with a breakpoint before step_3. </figcaption> </figure>

* **Flexible integration points**: Human-in-the-loop logic can be introduced at any point in the workflow. This allows targeted human involvement, such as approving API calls, correcting outputs, or guiding conversations.


## Patterns

There are four typical design patterns that you can implement using `interrupt` and `Command`:

- [Approve or reject](../how-tos/human_in_the_loop/add-human-in-the-loop.md#approve-or-reject): Pause the graph before a critical step, such as an API call, to review and approve the action. If the action is rejected, you can prevent the graph from executing the step, and potentially take an alternative action. This pattern often involves routing the graph based on the human's input.
- [Edit graph state](../how-tos/human_in_the_loop/add-human-in-the-loop.md#review-and-edit-state): Pause the graph to review and edit the graph state. This is useful for correcting mistakes or updating the state with additional information. This pattern often involves updating the state with the human's input.
- [Review tool calls](../how-tos/human_in_the_loop/add-human-in-the-loop.md#review-tool-calls): Pause the graph to review and edit tool calls requested by the LLM before tool execution.
- [Validate human input](../how-tos/human_in_the_loop/add-human-in-the-loop.md#validate-human-input): Pause the graph to validate human input before proceeding with the next step.

---
concepts/server-mcp.md
---

---
tags:
  - mcp
  - platform
hide:
  - tags
---


# MCP endpoint in LangGraph Server

The [Model Context Protocol (MCP)](./mcp.md) is an open protocol for describing tools and data sources in a model-agnostic format, enabling LLMs to discover and use them via a structured API.

[LangGraph Server](./langgraph_server.md) implements MCP using the [Streamable HTTP transport](https://spec.modelcontextprotocol.io/specification/2025-03-26/basic/transports/#streamable-http). This allows LangGraph **agents** to be exposed as **MCP tools**, making them usable with any MCP-compliant client supporting Streamable HTTP.

The MCP endpoint is available at `/mcp` on [LangGraph Server](./langgraph_server.md).


## Requirements

To use MCP, ensure you have the following dependencies installed:

- `langgraph-api >= 0.2.3`
- `langgraph-sdk >= 0.1.61`

Install them with:

```bash
pip install "langgraph-api>=0.2.3" "langgraph-sdk>=0.1.61"
```






## Exposing an agent as MCP tool

When deployed, your agent will appear as a tool in the MCP endpoint
with this configuration:

- **Tool name**: The agent's name.
- **Tool description**: The agent's description.
- **Tool input schema**: The agent's input schema.

### Setting name and description

You can set the name and description of your agent in `langgraph.json`:

```json
{
  "graphs": {
    "my_agent": {
      "path": "./my_agent/agent.py:graph",
      "description": "A description of what the agent does"
    }
  },
  "env": ".env"
}
```




After deployment, you can update the name and description using the LangGraph SDK.

### Schema

Define clear, minimal input and output schemas to avoid exposing unnecessary internal complexity to the LLM.

The default [MessagesState](./low_level.md#messagesstate) uses `AnyMessage`, which supports many message types but is too general for direct LLM exposure.


Instead, define **custom agents or workflows** that use explicitly typed input and output structures.

For example, a workflow answering documentation questions might look like this:

```python
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict


# Define input schema
class InputState(TypedDict):
    question: str


# Define output schema
class OutputState(TypedDict):
    answer: str


# Combine input and output
class OverallState(InputState, OutputState):
    pass


# Define the processing node
def answer_node(state: InputState):
    # Replace with actual logic and do something useful
    return {"answer": "bye", "question": state["question"]}


# Build the graph with explicit schemas
builder = StateGraph(OverallState, input_schema=InputState, output_schema=OutputState)
builder.add_node(answer_node)
builder.add_edge(START, "answer_node")
builder.add_edge("answer_node", END)
graph = builder.compile()


# Run the graph
print(graph.invoke({"question": "hi"}))
```

For more details, see the [low-level concepts guide](https://langchain-ai.github.io/langgraph/concepts/low_level/#state).


## Usage overview

To enable MCP:

- Upgrade to use langgraph-api>=0.2.3. If you are deploying LangGraph Platform, this will be done for you automatically if you create a new revision.
- MCP tools (agents) will be automatically exposed.
- Connect with any MCP-compliant client that supports Streamable HTTP.

### Client

Use an MCP-compliant client to connect to the LangGraph server. The following example shows how to connect using [langchain-mcp-adapters](https://github.com/langchain-ai/langchain-mcp-adapters).

Install the adapter with:

```bash
pip install langchain-mcp-adapters
```

Here is an example of how to connect to a remote MCP endpoint and use an agent as a tool:

```python

# Create server parameters for stdio connection
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client
import asyncio

from langchain_mcp_adapters.tools import load_mcp_tools
from langgraph.prebuilt import create_react_agent

server_params = {
    "url": "https://mcp-finance-agent.xxx.us.langgraph.app/mcp",
    "headers": {
        "X-Api-Key":"lsv2_pt_your_api_key"
    }
}

async def main():
    async with streamablehttp_client(**server_params) as (read, write, _):
        async with ClientSession(read, write) as session:
            # Initialize the connection
            await session.initialize()

            # Load the remote graph as if it was a tool
            tools = await load_mcp_tools(session)

            # Create and run a react agent with the tools
            agent = create_react_agent("openai:gpt-4.1", tools)

            # Invoke the agent with a message
            agent_response = await agent.ainvoke({"messages": "What can the finance agent do for me?"})
            print(agent_response)

if __name__ == "__main__":
    asyncio.run(main())
```






## Session behavior

The current LangGraph MCP implementation does not support sessions. Each `/mcp` request is stateless and independent.


## Authentication

The `/mcp` endpoint uses the same authentication as the rest of the LangGraph API. Refer to the [authentication guide](./auth.md) for setup details.


## Disable MCP

To disable the MCP endpoint, set `disable_mcp` to `true` in your `langgraph.json` configuration file:

```json
{
  "http": {
    "disable_mcp": true
  }
}
```

This will prevent the server from exposing the `/mcp` endpoint.


---
concepts/langgraph_self_hosted_data_plane.md
---

---
search:
  boost: 2
---


# Self-Hosted Data Plane

There are two versions of the self-hosted deployment: [Self-Hosted Data Plane](./deployment_options.md#self-hosted-data-plane) and [Self-Hosted Control Plane](./deployment_options.md#self-hosted-control-plane).

!!! info "Important"

    The Self-Hosted Data Plane deployment option requires an [Enterprise](plans.md) plan.


## Requirements

- You use `langgraph-cli` and/or [LangGraph Studio](./langgraph_studio.md) app to test graph locally.
- You use `langgraph build` command to build image.


## Self-Hosted Data Plane

The [Self-Hosted Data Plane](../cloud/deployment/self_hosted_data_plane.md) deployment option is a "hybrid" model for deployment where we manage the [control plane](./langgraph_control_plane.md) in our cloud and you manage the [data plane](./langgraph_data_plane.md) in your cloud. This option provides a way to securely manage your data plane infrastructure, while offloading control plane management to us. When using the Self-Hosted Data Plane version, you authenticate with a [LangSmith](https://smith.langchain.com/) API key.

|                                    | [Control plane](../concepts/langgraph_control_plane.md)                                                                                     | [Data plane](../concepts/langgraph_data_plane.md)                                                                                                   |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------- |
| **What is it?**                    | <ul><li>Control plane UI for creating deployments and revisions</li><li>Control plane APIs for creating deployments and revisions</li></ul> | <ul><li>Data plane "listener" for reconciling deployments with control plane state</li><li>LangGraph Servers</li><li>Postgres, Redis, etc</li></ul> |
| **Where is it hosted?**            | LangChain's cloud                                                                                                                           | Your cloud                                                                                                                                          |
| **Who provisions and manages it?** | LangChain                                                                                                                                   | You                                                                                                                                                 |

For information on how to deploy a [LangGraph Server](../concepts/langgraph_server.md) to Self-Hosted Data Plane, see [Deploy to Self-Hosted Data Plane](../cloud/deployment/self_hosted_data_plane.md)

### Architecture

![Self-Hosted Data Plane Architecture](./img/self_hosted_data_plane_architecture.png)

### Compute Platforms

- **Kubernetes**: The Self-Hosted Data Plane deployment option supports deploying data plane infrastructure to any Kubernetes cluster.
- **Amazon ECS**: Coming soon!

!!! tip
If you would like to deploy to Kubernetes, you can follow the [Self-Hosted Data Plane deployment guide](../cloud/deployment/self_hosted_data_plane.md).


---
concepts/streaming.md
---

---
search:
boost: 2
---


# Streaming

LangGraph implements a streaming system to surface real-time updates, allowing for responsive and transparent user experiences.

LangGraph’s streaming system lets you surface live feedback from graph runs to your app.  
There are three main categories of data you can stream:

1. **Workflow progress** — get state updates after each graph node is executed.
2. **LLM tokens** — stream language model tokens as they’re generated.
3. **Custom updates** — emit user-defined signals (e.g., “Fetched 10/100 records”).


## What’s possible with LangGraph streaming

- [**Stream LLM tokens**](../how-tos/streaming.md#messages) — capture token streams from anywhere: inside nodes, subgraphs, or tools.
- [**Emit progress notifications from tools**](../how-tos/streaming.md#stream-custom-data) — send custom updates or progress signals directly from tool functions.
- [**Stream from subgraphs**](../how-tos/streaming.md#stream-subgraph-outputs) — include outputs from both the parent graph and any nested subgraphs.
- [**Use any LLM**](../how-tos/streaming.md#use-with-any-llm) — stream tokens from any LLM, even if it's not a LangChain model using the `custom` streaming mode.
- [**Use multiple streaming modes**](../how-tos/streaming.md#stream-multiple-modes) — choose from `values` (full state), `updates` (state deltas), `messages` (LLM tokens + metadata), `custom` (arbitrary user data), or `debug` (detailed traces).

---
concepts/functional_api.md
---

---
search:
  boost: 2
---


# Functional API concepts


## Overview

The **Functional API** allows you to add LangGraph's key features — [persistence](./persistence.md), [memory](../how-tos/memory/add-memory.md), [human-in-the-loop](./human_in_the_loop.md), and [streaming](./streaming.md) — to your applications with minimal changes to your existing code.

It is designed to integrate these features into existing code that may use standard language primitives for branching and control flow, such as `if` statements, `for` loops, and function calls. Unlike many data orchestration frameworks that require restructuring code into an explicit pipeline or DAG, the Functional API allows you to incorporate these capabilities without enforcing a rigid execution model.

The Functional API uses two key building blocks:

- **`@entrypoint`** – Marks a function as the starting point of a workflow, encapsulating logic and managing execution flow, including handling long-running tasks and interrupts.
- **`@task`** – Represents a discrete unit of work, such as an API call or data processing step, that can be executed asynchronously within an entrypoint. Tasks return a future-like object that can be awaited or resolved synchronously.  




This provides a minimal abstraction for building workflows with state management and streaming.

!!! tip

    For information on how to use the functional API, see [Use Functional API](../how-tos/use-functional-api.md).


## Functional API vs. Graph API

For users who prefer a more declarative approach, LangGraph's [Graph API](./low_level.md) allows you to define workflows using a Graph paradigm. Both APIs share the same underlying runtime, so you can use them together in the same application.

Here are some key differences:

- **Control flow**: The Functional API does not require thinking about graph structure. You can use standard Python constructs to define workflows. This will usually trim the amount of code you need to write.
- **Short-term memory**: The **GraphAPI** requires declaring a [**State**](./low_level.md#state) and may require defining [**reducers**](./low_level.md#reducers) to manage updates to the graph state. `@entrypoint` and `@tasks` do not require explicit state management as their state is scoped to the function and is not shared across functions.
- **Checkpointing**: Both APIs generate and use checkpoints. In the **Graph API** a new checkpoint is generated after every [superstep](./low_level.md). In the **Functional API**, when tasks are executed, their results are saved to an existing checkpoint associated with the given entrypoint instead of creating a new checkpoint.
- **Visualization**: The Graph API makes it easy to visualize the workflow as a graph which can be useful for debugging, understanding the workflow, and sharing with others. The Functional API does not support visualization as the graph is dynamically generated during runtime.


## Example

Below we demonstrate a simple application that writes an essay and [interrupts](human_in_the_loop.md) to request human review.

```python
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.func import entrypoint, task
from langgraph.types import interrupt

@task
def write_essay(topic: str) -> str:
    """Write an essay about the given topic."""
    time.sleep(1) # A placeholder for a long-running task.
    return f"An essay about topic: {topic}"

@entrypoint(checkpointer=InMemorySaver())
def workflow(topic: str) -> dict:
    """A simple workflow that writes an essay and asks for a review."""
    essay = write_essay("cat").result()
    is_approved = interrupt({
        # Any json-serializable payload provided to interrupt as argument.
        # It will be surfaced on the client side as an Interrupt when streaming data
        # from the workflow.
        "essay": essay, # The essay we want reviewed.
        # We can add any additional information that we need.
        # For example, introduce a key called "action" with some instructions.
        "action": "Please approve/reject the essay",
    })

    return {
        "essay": essay, # The essay that was generated
        "is_approved": is_approved, # Response from HIL
    }
```





??? example "Detailed Explanation"

    This workflow will write an essay about the topic "cat" and then pause to get a review from a human. The workflow can be interrupted for an indefinite amount of time until a review is provided.

    When the workflow is resumed, it executes from the very start, but because the result of the `writeEssay` task was already saved, the task result will be loaded from the checkpoint instead of being recomputed.

    ```python
    import time
    import uuid
    from langgraph.func import entrypoint, task
    from langgraph.types import interrupt
    from langgraph.checkpoint.memory import InMemorySaver


    @task
    def write_essay(topic: str) -> str:
        """Write an essay about the given topic."""
        time.sleep(1)  # This is a placeholder for a long-running task.
        return f"An essay about topic: {topic}"

    @entrypoint(checkpointer=InMemorySaver())
    def workflow(topic: str) -> dict:
        """A simple workflow that writes an essay and asks for a review."""
        essay = write_essay("cat").result()
        is_approved = interrupt(
            {
                # Any json-serializable payload provided to interrupt as argument.
                # It will be surfaced on the client side as an Interrupt when streaming data
                # from the workflow.
                "essay": essay,  # The essay we want reviewed.
                # We can add any additional information that we need.
                # For example, introduce a key called "action" with some instructions.
                "action": "Please approve/reject the essay",
            }
        )
        return {
            "essay": essay,  # The essay that was generated
            "is_approved": is_approved,  # Response from HIL
        }


    thread_id = str(uuid.uuid4())
    config = {"configurable": {"thread_id": thread_id}}
    for item in workflow.stream("cat", config):
        print(item)
    # > {'write_essay': 'An essay about topic: cat'}
    # > {
    # >     '__interrupt__': (
    # >        Interrupt(
    # >            value={
    # >                'essay': 'An essay about topic: cat',
    # >                'action': 'Please approve/reject the essay'
    # >            },
    # >            id='b9b2b9d788f482663ced6dc755c9e981'
    # >        ),
    # >    )
    # > }
    ```

    An essay has been written and is ready for review. Once the review is provided, we can resume the workflow:

    ```python
    from langgraph.types import Command

    # Get review from a user (e.g., via a UI)
    # In this case, we're using a bool, but this can be any json-serializable value.
    human_review = True

    for item in workflow.stream(Command(resume=human_review), config):
        print(item)
    ```

    ```pycon
    {'workflow': {'essay': 'An essay about topic: cat', 'is_approved': False}}
    ```

    The workflow has been completed and the review has been added to the essay.





## Entrypoint

The [`@entrypoint`](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint) decorator can be used to create a workflow from a function. It encapsulates workflow logic and manages execution flow, including handling _long-running tasks_ and [interrupts](./human_in_the_loop.md).




### Definition

An **entrypoint** is defined by decorating a function with the `@entrypoint` decorator.

The function **must accept a single positional argument**, which serves as the workflow input. If you need to pass multiple pieces of data, use a dictionary as the input type for the first argument.

Decorating a function with an `entrypoint` produces a [`Pregel`](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream) instance which helps to manage the execution of the workflow (e.g., handles streaming, resumption, and checkpointing).

You will usually want to pass a **checkpointer** to the `@entrypoint` decorator to enable persistence and use features like **human-in-the-loop**.

=== "Sync"

    ```python
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(some_input: dict) -> int:
        # some logic that may involve long-running tasks like API calls,
        # and may be interrupted for human-in-the-loop.
        ...
        return result
    ```

=== "Async"

    ```python
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    async def my_workflow(some_input: dict) -> int:
        # some logic that may involve long-running tasks like API calls,
        # and may be interrupted for human-in-the-loop
        ...
        return result
    ```





!!! important "Serialization"

    The **inputs** and **outputs** of entrypoints must be JSON-serializable to support checkpointing. Please see the [serialization](#serialization) section for more details.

### Injectable parameters

When declaring an `entrypoint`, you can request access to additional parameters that will be injected automatically at run time. These parameters include:

| Parameter    | Description                                                                                                                                                        |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **previous** | Access the state associated with the previous `checkpoint` for the given thread. See [short-term-memory](#short-term-memory).                                      |
| **store**    | An instance of [BaseStore][langgraph.store.base.BaseStore]. Useful for [long-term memory](../how-tos/use-functional-api.md#long-term-memory).                      |
| **writer**   | Use to access the StreamWriter when working with Async Python < 3.11. See [streaming with functional API for details](../how-tos/use-functional-api.md#streaming). |
| **config**   | For accessing run time configuration. See [RunnableConfig](https://python.langchain.com/docs/concepts/runnables/#runnableconfig) for information.                  |

!!! important

    Declare the parameters with the appropriate name and type annotation.

??? example "Requesting Injectable Parameters"

    ```python
    from langchain_core.runnables import RunnableConfig
    from langgraph.func import entrypoint
    from langgraph.store.base import BaseStore
    from langgraph.store.memory import InMemoryStore

    in_memory_store = InMemoryStore(...)  # An instance of InMemoryStore for long-term memory

    @entrypoint(
        checkpointer=checkpointer,  # Specify the checkpointer
        store=in_memory_store  # Specify the store
    )
    def my_workflow(
        some_input: dict,  # The input (e.g., passed via `invoke`)
        *,
        previous: Any = None, # For short-term memory
        store: BaseStore,  # For long-term memory
        writer: StreamWriter,  # For streaming custom data
        config: RunnableConfig  # For accessing the configuration passed to the entrypoint
    ) -> ...:
    ```



### Executing

Using the [`@entrypoint`](#entrypoint) yields a [`Pregel`](https://langchain-ai.github.io/langgraph/reference/pregel/#langgraph.pregel.Pregel.stream) object that can be executed using the `invoke`, `ainvoke`, `stream`, and `astream` methods.

=== "Invoke"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }
    my_workflow.invoke(some_input, config)  # Wait for the result synchronously
    ```

=== "Async Invoke"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }
    await my_workflow.ainvoke(some_input, config)  # Await result asynchronously
    ```

=== "Stream"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(some_input, config):
        print(chunk)
    ```

=== "Async Stream"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(some_input, config):
        print(chunk)
    ```





### Resuming

Resuming an execution after an [interrupt](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Interrupt) can be done by passing a **resume** value to the [Command](https://langchain-ai.github.io/langgraph/reference/types/#langgraph.types.Command) primitive.

=== "Invoke"

    ```python
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    my_workflow.invoke(Command(resume=some_resume_value), config)
    ```

=== "Async Invoke"

    ```python
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    await my_workflow.ainvoke(Command(resume=some_resume_value), config)
    ```

=== "Stream"

    ```python
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(Command(resume=some_resume_value), config):
        print(chunk)
    ```

=== "Async Stream"

    ```python
    from langgraph.types import Command

    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(Command(resume=some_resume_value), config):
        print(chunk)
    ```





**Resuming after an error**

To resume after an error, run the `entrypoint` with a `None` and the same **thread id** (config).

This assumes that the underlying **error** has been resolved and execution can proceed successfully.

=== "Invoke"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    my_workflow.invoke(None, config)
    ```

=== "Async Invoke"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    await my_workflow.ainvoke(None, config)
    ```

=== "Stream"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    for chunk in my_workflow.stream(None, config):
        print(chunk)
    ```

=== "Async Stream"

    ```python
    config = {
        "configurable": {
            "thread_id": "some_thread_id"
        }
    }

    async for chunk in my_workflow.astream(None, config):
        print(chunk)
    ```





### Short-term memory

When an `entrypoint` is defined with a `checkpointer`, it stores information between successive invocations on the same **thread id** in [checkpoints](persistence.md#checkpoints).

This allows accessing the state from the previous invocation using the `previous` parameter.

By default, the `previous` parameter is the return value of the previous invocation.

```python
@entrypoint(checkpointer=checkpointer)
def my_workflow(number: int, *, previous: Any = None) -> int:
    previous = previous or 0
    return number + previous

config = {
    "configurable": {
        "thread_id": "some_thread_id"
    }
}

my_workflow.invoke(1, config)  # 1 (previous was None)
my_workflow.invoke(2, config)  # 3 (previous was 1 from the previous invocation)
```





#### `entrypoint.final`

[`entrypoint.final`](https://langchain-ai.github.io/langgraph/reference/func/#langgraph.func.entrypoint.final) is a special primitive that can be returned from an entrypoint and allows **decoupling** the value that is **saved in the checkpoint** from the **return value of the entrypoint**.

The first value is the return value of the entrypoint, and the second value is the value that will be saved in the checkpoint. The type annotation is `entrypoint.final[return_type, save_type]`.

```python
@entrypoint(checkpointer=checkpointer)
def my_workflow(number: int, *, previous: Any = None) -> entrypoint.final[int, int]:
    previous = previous or 0
    # This will return the previous value to the caller, saving
    # 2 * number to the checkpoint, which will be used in the next invocation
    # for the `previous` parameter.
    return entrypoint.final(value=previous, save=2 * number)

config = {
    "configurable": {
        "thread_id": "1"
    }
}

my_workflow.invoke(3, config)  # 0 (previous was None)
my_workflow.invoke(1, config)  # 6 (previous was 3 * 2 from the previous invocation)
```






## Task

A **task** represents a discrete unit of work, such as an API call or data processing step. It has two key characteristics:

- **Asynchronous Execution**: Tasks are designed to be executed asynchronously, allowing multiple operations to run concurrently without blocking.
- **Checkpointing**: Task results are saved to a checkpoint, enabling resumption of the workflow from the last saved state. (See [persistence](persistence.md) for more details).

### Definition

Tasks are defined using the `@task` decorator, which wraps a regular Python function.

```python
from langgraph.func import task

@task()
def slow_computation(input_value):
    # Simulate a long-running operation
    ...
    return result
```





!!! important "Serialization"

    The **outputs** of tasks must be JSON-serializable to support checkpointing.

### Execution

**Tasks** can only be called from within an **entrypoint**, another **task**, or a [state graph node](./low_level.md#nodes).

Tasks _cannot_ be called directly from the main application code.

When you call a **task**, it returns _immediately_ with a future object. A future is a placeholder for a result that will be available later.

To obtain the result of a **task**, you can either wait for it synchronously (using `result()`) or await it asynchronously (using `await`).

=== "Synchronous Invocation"

    ```python
    @entrypoint(checkpointer=checkpointer)
    def my_workflow(some_input: int) -> int:
        future = slow_computation(some_input)
        return future.result()  # Wait for the result synchronously
    ```

=== "Asynchronous Invocation"

    ```python
    @entrypoint(checkpointer=checkpointer)
    async def my_workflow(some_input: int) -> int:
        return await slow_computation(some_input)  # Await result asynchronously
    ```






## When to use a task

**Tasks** are useful in the following scenarios:

- **Checkpointing**: When you need to save the result of a long-running operation to a checkpoint, so you don't need to recompute it when resuming the workflow.
- **Human-in-the-loop**: If you're building a workflow that requires human intervention, you MUST use **tasks** to encapsulate any randomness (e.g., API calls) to ensure that the workflow can be resumed correctly. See the [determinism](#determinism) section for more details.
- **Parallel Execution**: For I/O-bound tasks, **tasks** enable parallel execution, allowing multiple operations to run concurrently without blocking (e.g., calling multiple APIs).
- **Observability**: Wrapping operations in **tasks** provides a way to track the progress of the workflow and monitor the execution of individual operations using [LangSmith](https://docs.smith.langchain.com/).
- **Retryable Work**: When work needs to be retried to handle failures or inconsistencies, **tasks** provide a way to encapsulate and manage the retry logic.


## Serialization

There are two key aspects to serialization in LangGraph:

1. `entrypoint` inputs and outputs must be JSON-serializable.
2. `task` outputs must be JSON-serializable.

These requirements are necessary for enabling checkpointing and workflow resumption. Use python primitives like dictionaries, lists, strings, numbers, and booleans to ensure that your inputs and outputs are serializable.




Serialization ensures that workflow state, such as task results and intermediate values, can be reliably saved and restored. This is critical for enabling human-in-the-loop interactions, fault tolerance, and parallel execution.

Providing non-serializable inputs or outputs will result in a runtime error when a workflow is configured with a checkpointer.


## Determinism

To utilize features like **human-in-the-loop**, any randomness should be encapsulated inside of **tasks**. This guarantees that when execution is halted (e.g., for human in the loop) and then resumed, it will follow the same _sequence of steps_, even if **task** results are non-deterministic.

LangGraph achieves this behavior by persisting **task** and [**subgraph**](./subgraphs.md) results as they execute. A well-designed workflow ensures that resuming execution follows the _same sequence of steps_, allowing previously computed results to be retrieved correctly without having to re-execute them. This is particularly useful for long-running **tasks** or **tasks** with non-deterministic results, as it avoids repeating previously done work and allows resuming from essentially the same.

While different runs of a workflow can produce different results, resuming a **specific** run should always follow the same sequence of recorded steps. This allows LangGraph to efficiently look up **task** and **subgraph** results that were executed prior to the graph being interrupted and avoid recomputing them.


## Idempotency

Idempotency ensures that running the same operation multiple times produces the same result. This helps prevent duplicate API calls and redundant processing if a step is rerun due to a failure. Always place API calls inside **tasks** functions for checkpointing, and design them to be idempotent in case of re-execution. Re-execution can occur if a **task** starts, but does not complete successfully. Then, if the workflow is resumed, the **task** will run again. Use idempotency keys or verify existing results to avoid duplication.


## Common Pitfalls

### Handling side effects

Encapsulate side effects (e.g., writing to a file, sending an email) in tasks to ensure they are not executed multiple times when resuming a workflow.

=== "Incorrect"

    In this example, a side effect (writing to a file) is directly included in the workflow, so it will be executed a second time when resuming the workflow.

    ```python hl_lines="5 6"
    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        # This code will be executed a second time when resuming the workflow.
        # Which is likely not what you want.
        with open("output.txt", "w") as f:
            f.write("Side effect executed")
        value = interrupt("question")
        return value
    ```




=== "Correct"

    In this example, the side effect is encapsulated in a task, ensuring consistent execution upon resumption.

    ```python hl_lines="3 4"
    from langgraph.func import task

    @task
    def write_to_file():
        with open("output.txt", "w") as f:
            f.write("Side effect executed")

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        # The side effect is now encapsulated in a task.
        write_to_file().result()
        value = interrupt("question")
        return value
    ```




### Non-deterministic control flow

Operations that might give different results each time (like getting current time or random numbers) should be encapsulated in tasks to ensure that on resume, the same result is returned.

- In a task: Get random number (5) → interrupt → resume → (returns 5 again) → ...
- Not in a task: Get random number (5) → interrupt → resume → get new random number (7) → ...

This is especially important when using **human-in-the-loop** workflows with multiple interrupts calls. LangGraph keeps a list of resume values for each task/entrypoint. When an interrupt is encountered, it's matched with the corresponding resume value. This matching is strictly **index-based**, so the order of the resume values should match the order of the interrupts.




If order of execution is not maintained when resuming, one `interrupt` call may be matched with the wrong `resume` value, leading to incorrect results.

Please read the section on [determinism](#determinism) for more details.

=== "Incorrect"

    In this example, the workflow uses the current time to determine which task to execute. This is non-deterministic because the result of the workflow depends on the time at which it is executed.

    ```python hl_lines="6"
    from langgraph.func import entrypoint

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        t0 = inputs["t0"]
        t1 = time.time()

        delta_t = t1 - t0

        if delta_t > 1:
            result = slow_task(1).result()
            value = interrupt("question")
        else:
            result = slow_task(2).result()
            value = interrupt("question")

        return {
            "result": result,
            "value": value
        }
    ```




=== "Correct"

    In this example, the workflow uses the input `t0` to determine which task to execute. This is deterministic because the result of the workflow depends only on the input.

    ```python hl_lines="5 6 12"
    import time

    from langgraph.func import task

    @task
    def get_time() -> float:
        return time.time()

    @entrypoint(checkpointer=checkpointer)
    def my_workflow(inputs: dict) -> int:
        t0 = inputs["t0"]
        t1 = get_time().result()

        delta_t = t1 - t0

        if delta_t > 1:
            result = slow_task(1).result()
            value = interrupt("question")
        else:
            result = slow_task(2).result()
            value = interrupt("question")

        return {
            "result": result,
            "value": value
        }
    ```





---
concepts/deployment_options.md
---

---
search:
  boost: 2
---


# Deployment Options


## Free deployment

[Local](../tutorials/langgraph-platform/local-server.md): Deploy for local testing and development.


## Production deployment

There are 4 main options for deploying with the [LangGraph Platform](langgraph_platform.md):

1. [Cloud SaaS](#cloud-saas)

1. [Self-Hosted Data Plane](#self-hosted-data-plane)

1. [Self-Hosted Control Plane](#self-hosted-control-plane)

1. [Standalone Container](#standalone-container)


A quick comparison:

|                      | **Cloud SaaS** | **Self-Hosted Data Plane** | **Self-Hosted Control Plane** | **Standalone Container** |
|----------------------|----------------|----------------------------|-------------------------------|--------------------------|
| **[Control plane UI/API](../concepts/langgraph_control_plane.md)** | Yes | Yes | Yes | No |
| **CI/CD** | Managed internally by platform | Managed externally by you | Managed externally by you | Managed externally by you |
| **Data/compute residency** | LangChain's cloud | Your cloud | Your cloud | Your cloud |
| **LangSmith compatibility** | Trace to LangSmith SaaS | Trace to LangSmith SaaS | Trace to Self-Hosted LangSmith | Optional tracing |
| **[Pricing](https://www.langchain.com/pricing-langgraph-platform)** | Plus | Enterprise | Enterprise | Enterprise |


## Cloud SaaS

The [Cloud SaaS](./langgraph_cloud.md) deployment option is a fully managed model for deployment where we manage the [control plane](./langgraph_control_plane.md) and [data plane](./langgraph_data_plane.md) in our cloud. This option provides a simple way to deploy and manage your LangGraph Servers.

Connect your GitHub repositories to the platform and deploy your LangGraph Servers from the [control plane UI](./langgraph_control_plane.md#control-plane-ui). The build process (i.e. CI/CD) is managed internally by the platform.

For more information, please see:

* [Cloud SaaS Conceptual Guide](./langgraph_cloud.md)
* [How to deploy to Cloud SaaS](../cloud/deployment/cloud.md)


## Self-Hosted Data Plane

!!! info "Important"
    The Self-Hosted Data Plane deployment option requires an [Enterprise](../concepts/plans.md) plan.

The [Self-Hosted Data Plane](./langgraph_self_hosted_data_plane.md) deployment option is a "hybrid" model for deployment where we manage the [control plane](./langgraph_control_plane.md) in our cloud and you manage the [data plane](./langgraph_data_plane.md) in your cloud. This option provides a way to securely manage your data plane infrastructure, while offloading control plane management to us.

Build a Docker image using the [LangGraph CLI](./langgraph_cli.md) and deploy your LangGraph Server from the [control plane UI](./langgraph_control_plane.md#control-plane-ui).

Supported Compute Platforms: [Kubernetes](https://kubernetes.io/), [Amazon ECS](https://aws.amazon.com/ecs/) (coming soon!)

For more information, please see:

* [Self-Hosted Data Plane Conceptual Guide](./langgraph_self_hosted_data_plane.md)
* [How to deploy the Self-Hosted Data Plane](../cloud/deployment/self_hosted_data_plane.md)


## Self-Hosted Control Plane

!!! info "Important"
    The Self-Hosted Control Plane deployment option requires an [Enterprise](../concepts/plans.md) plan.

The [Self-Hosted Control Plane](./langgraph_self_hosted_control_plane.md) deployment option is a fully self-hosted model for deployment where you manage the [control plane](./langgraph_control_plane.md) and [data plane](./langgraph_data_plane.md) in your cloud. This option gives you full control and responsibility of the control plane and data plane infrastructure.

Build a Docker image using the [LangGraph CLI](./langgraph_cli.md) and deploy your LangGraph Server from the [control plane UI](./langgraph_control_plane.md#control-plane-ui).

Supported Compute Platforms: [Kubernetes](https://kubernetes.io/)

For more information, please see:

* [Self-Hosted Control Plane Conceptual Guide](./langgraph_self_hosted_control_plane.md)
* [How to deploy the Self-Hosted Control Plane](../cloud/deployment/self_hosted_control_plane.md)


## Standalone Container

The [Standalone Container](./langgraph_standalone_container.md) deployment option is the least restrictive model for deployment. Deploy standalone instances of a LangGraph Server in your cloud, using any of the [available](./plans.md) license options.

Build a Docker image using the [LangGraph CLI](./langgraph_cli.md) and deploy your LangGraph Server using the container deployment tooling of your choice. Images can be deployed to any compute platform.

For more information, please see:

* [Standalone Container Conceptual Guide](./langgraph_standalone_container.md)
* [How to deploy a Standalone Container](../cloud/deployment/standalone_container.md)


## Related

For more information, please see:

* [LangGraph Platform plans](./plans.md)
* [LangGraph Platform pricing](https://www.langchain.com/langgraph-platform-pricing)


---
concepts/sdk.md
---

---
search:
  boost: 2
---


# LangGraph SDK

LangGraph Platform provides a python SDK for interacting with [LangGraph Server](./langgraph_server.md).

!!! tip "Python SDK reference"

    For detailed information about the Python SDK, see [Python SDK reference docs](../cloud/reference/sdk/python_sdk_ref.md).


## Installation

You can install the LangGraph SDK using the following command:

```bash
pip install langgraph-sdk
```


## Python sync vs. async

The Python SDK provides both synchronous (`get_sync_client`) and asynchronous (`get_client`) clients for interacting with LangGraph Server:

=== "Sync"

    ```python
    from langgraph_sdk import get_sync_client

    client = get_sync_client(url=..., api_key=...)
    client.assistants.search()
    ```

=== "Async"

    ```python
    from langgraph_sdk import get_client

    client = get_client(url=..., api_key=...)
    await client.assistants.search()
    ```


## Learn more

- [Python SDK Reference](../cloud/reference/sdk/python_sdk_ref.md)
- [LangGraph CLI API Reference](../cloud/reference/cli.md)





---
concepts/langgraph_server.md
---

---
search:
  boost: 2
---


# LangGraph Server

**LangGraph Server** offers an API for creating and managing agent-based applications. It is built on the concept of [assistants](assistants.md), which are agents configured for specific tasks, and includes built-in [persistence](persistence.md#memory-store) and a **task queue**. This versatile API supports a wide range of agentic application use cases, from background processing to real-time interactions.

Use LangGraph Server to create and manage [assistants](assistants.md), [threads](./persistence.md#threads), [runs](./assistants.md#execution), [cron jobs](../cloud/concepts/cron_jobs.md), [webhooks](../cloud/concepts/webhooks.md), and more.

!!! tip "API reference"
  
    For detailed information on the API endpoints and data models, see [LangGraph Platform API reference docs](../cloud/reference/api/api_ref.html).


## Application structure

To deploy a LangGraph Server application, you need to specify the graph(s) you want to deploy, as well as any relevant configuration settings, such as dependencies and environment variables.

Read the [application structure](./application_structure.md) guide to learn how to structure your LangGraph application for deployment.


## Parts of a deployment

When you deploy LangGraph Server, you are deploying one or more [graphs](#graphs), a database for [persistence](persistence.md), and a task queue.

### Graphs

When you deploy a graph with LangGraph Server, you are deploying a "blueprint" for an [Assistant](assistants.md). 

An [Assistant](assistants.md) is a graph paired with specific configuration settings. You can create multiple assistants per graph, each with unique settings to accommodate different use cases
that can be served by the same graph.

Upon deployment, LangGraph Server will automatically create a default assistant for each graph using the graph's default configuration settings.

!!! note

    We often think of a graph as implementing an [agent](agentic_concepts.md), but a graph does not necessarily need to implement an agent. For example, a graph could implement a simple
    chatbot that only supports back-and-forth conversation, without the ability to influence any application control flow. In reality, as applications get more complex, a graph will often implement a more complex flow that may use [multiple agents](./multi_agent.md) working in tandem.

### Persistence and task queue

LangGraph Server leverages a database for [persistence](persistence.md) and a task queue.

Currently, only [Postgres](https://www.postgresql.org/) is supported as a database for LangGraph Server and [Redis](https://redis.io/) as the task queue.

If you're deploying using [LangGraph Platform](./langgraph_cloud.md), these components are managed for you. If you're deploying LangGraph Server on your own infrastructure, you'll need to set up and manage these components yourself.

Please review the [deployment options](./deployment_options.md) guide for more information on how these components are set up and managed.


## Learn more

* LangGraph [Application Structure](./application_structure.md) guide explains how to structure your LangGraph application for deployment.
* The [LangGraph Platform API Reference](../cloud/reference/api/api_ref.html) provides detailed information on the API endpoints and data models.


---
concepts/langgraph_platform.md
---

---
search:
  boost: 2
---


# LangGraph Platform

Develop, deploy, scale, and manage agents with **LangGraph Platform** — the purpose-built platform for long-running, agentic workflows.

!!! tip "Get started with LangGraph Platform"

    Check out the [LangGraph Platform quickstart](../tutorials/langgraph-platform/local-server.md) for instructions on how to use LangGraph Platform to run a LangGraph application locally.


## Why use LangGraph Platform?

<div align="center"><iframe width="560" height="315" src="https://www.youtube.com/embed/pfAQxBS5z88?si=XGS6Chydn6lhSO1S" title="What is LangGraph Platform?" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe></div>

LangGraph Platform makes it easy to get your agent running in production —  whether it’s built with LangGraph or another framework — so you can focus on your app logic, not infrastructure. Deploy with one click to get a live endpoint, and use our robust APIs and built-in task queues to handle production scale. 

- **[Streaming Support](../cloud/how-tos/streaming.md)**: As agents grow more sophisticated, they often benefit from streaming both token outputs and intermediate states back to the user. Without this, users are left waiting for potentially long operations with no feedback. LangGraph Server provides multiple streaming modes optimized for various application needs.

- **[Background Runs](../cloud/how-tos/background_run.md)**: For agents that take longer to process (e.g., hours), maintaining an open connection can be impractical. The LangGraph Server supports launching agent runs in the background and provides both polling endpoints and webhooks to monitor run status effectively.
 
- **Support for long runs**: Regular server setups often encounter timeouts or disruptions when handling requests that take a long time to complete. LangGraph Server’s API provides robust support for these tasks by sending regular heartbeat signals, preventing unexpected connection closures during prolonged processes.

- **Handling Burstiness**: Certain applications, especially those with real-time user interaction, may experience "bursty" request loads where numerous requests hit the server simultaneously. LangGraph Server includes a task queue, ensuring requests are handled consistently without loss, even under heavy loads.

- **[Double-texting](../cloud/how-tos/interrupt_concurrent.md)**: In user-driven applications, it’s common for users to send multiple messages rapidly. This “double texting” can disrupt agent flows if not handled properly. LangGraph Server offers built-in strategies to address and manage such interactions.

- **[Checkpointers and memory management](persistence.md#checkpoints)**: For agents needing persistence (e.g., conversation memory), deploying a robust storage solution can be complex. LangGraph Platform includes optimized [checkpointers](persistence.md#checkpoints) and a [memory store](persistence.md#memory-store), managing state across sessions without the need for custom solutions.

- **[Human-in-the-loop support](../cloud/how-tos/human_in_the_loop_breakpoint.md)**: In many applications, users require a way to intervene in agent processes. LangGraph Server provides specialized endpoints for human-in-the-loop scenarios, simplifying the integration of manual oversight into agent workflows.

- **[LangGraph Studio](./langgraph_studio.md)**: Enables visualization, interaction, and debugging of agentic systems that implement the LangGraph Server API protocol. Studio also integrates with LangSmith to enable tracing, evaluation, and prompt engineering.

- **[Deployment](./deployment_options.md)**: There are four ways to deploy on LangGraph Platform: [Cloud SaaS](../concepts/langgraph_cloud.md), [Self-Hosted Data Plane](../concepts/langgraph_self_hosted_data_plane.md), [Self-Hosted Control Plane](../concepts/langgraph_self_hosted_control_plane.md), and [Standalone Container](../concepts/langgraph_standalone_container.md).

---
concepts/tracing.md
---


# Tracing

Traces are a series of steps that your application takes to go from input to output. Each of these individual steps is represented by a run. You can use [LangSmith](https://smith.langchain.com/) to visualize these execution steps. To use it, [enable tracing for your application](../how-tos/enable-tracing.md). This enables you to do the following:

- [Debug a locally running application](../cloud/how-tos/clone_traces_studio.md).
- [Evaluate the application performance](../agents/evals.md).
- [Monitor the application](https://docs.smith.langchain.com/observability/how_to_guides/dashboards).

To get started, sign up for a free account at [LangSmith](https://smith.langchain.com/).


## Learn more

- [Graph runs in LangSmith](../how-tos/run-id-langsmith.md)
- [LangSmith Observability quickstart](https://docs.smith.langchain.com/observability)
- [Trace with LangGraph](https://docs.smith.langchain.com/observability/how_to_guides/trace_with_langgraph)
- [Tracing conceptual guide](https://docs.smith.langchain.com/observability/concepts#traces)



---
concepts/memory.md
---

---
search:
  boost: 2
---


# Memory

[Memory](../how-tos/memory/add-memory.md) is a system that remembers information about previous interactions. For AI agents, memory is crucial because it lets them remember previous interactions, learn from feedback, and adapt to user preferences. As agents tackle more complex tasks with numerous user interactions, this capability becomes essential for both efficiency and user satisfaction.

This conceptual guide covers two types of memory, based on their recall scope:

- [Short-term memory](#short-term-memory), or [thread](persistence.md#threads)-scoped memory, tracks the ongoing conversation by maintaining message history within a session. LangGraph manages short-term memory as a part of your agent's [state](low_level.md#state). State is persisted to a database using a [checkpointer](persistence.md#checkpoints) so the thread can be resumed at any time. Short-term memory updates when the graph is invoked or a step is completed, and the State is read at the start of each step.

- [Long-term memory](#long-term-memory) stores user-specific or application-level data across sessions and is shared _across_ conversational threads. It can be recalled _at any time_ and _in any thread_. Memories are scoped to any custom namespace, not just within a single thread ID. LangGraph provides [stores](persistence.md#memory-store) ([reference doc](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.BaseStore)) to let you save and recall long-term memories.

![](img/memory/short-vs-long.png)



## Short-term memory

[Short-term memory](../how-tos/memory/add-memory.md#add-short-term-memory) lets your application remember previous interactions within a single [thread](persistence.md#threads) or conversation. A [thread](persistence.md#threads) organizes multiple interactions in a session, similar to the way email groups messages in a single conversation.

LangGraph manages short-term memory as part of the agent's state, persisted via thread-scoped checkpoints. This state can normally include the conversation history along with other stateful data, such as uploaded files, retrieved documents, or generated artifacts. By storing these in the graph's state, the bot can access the full context for a given conversation while maintaining separation between different threads.

### Manage short-term memory

Conversation history is the most common form of short-term memory, and long conversations pose a challenge to today's LLMs. A full history may not fit inside an LLM's context window, resulting in an irrecoverable error. Even if your LLM supports the full context length, most LLMs still perform poorly over long contexts. They get "distracted" by stale or off-topic content, all while suffering from slower response times and higher costs.

Chat models accept context using messages, which include developer provided instructions (a system message) and user inputs (human messages). In chat applications, messages alternate between human inputs and model responses, resulting in a list of messages that grows longer over time. Because context windows are limited and token-rich message lists can be costly, many applications can benefit from using techniques to manually remove or forget stale information.

![](img/memory/filter.png)

For more information on common techniques for managing messages, see the [Add and manage memory](../how-tos/memory/add-memory.md#manage-short-term-memory) guide.


## Long-term memory

[Long-term memory](../how-tos/memory/add-memory.md#add-long-term-memory) in LangGraph allows systems to retain information across different conversations or sessions. Unlike short-term memory, which is **thread-scoped**, long-term memory is saved within custom "namespaces."

Long-term memory is a complex challenge without a one-size-fits-all solution. However, the following questions provide a framework to help you navigate the different techniques:

- [What is the type of memory?](#memory-types) Humans use memories to remember facts ([semantic memory](#semantic-memory)), experiences ([episodic memory](#episodic-memory)), and rules ([procedural memory](#procedural-memory)). AI agents can use memory in the same ways. For example, AI agents can use memory to remember specific facts about a user to accomplish a task.

- [When do you want to update memories?](#writing-memories) Memory can be updated as part of an agent's application logic (e.g., "on the hot path"). In this case, the agent typically decides to remember facts before responding to a user. Alternatively, memory can be updated as a background task (logic that runs in the background / asynchronously and generates memories). We explain the tradeoffs between these approaches in the [section below](#writing-memories).

### Memory types

Different applications require various types of memory. Although the analogy isn't perfect, examining [human memory types](https://www.psychologytoday.com/us/basics/memory/types-of-memory?ref=blog.langchain.dev) can be insightful. Some research (e.g., the [CoALA paper](https://arxiv.org/pdf/2309.02427)) have even mapped these human memory types to those used in AI agents.

| Memory Type | What is Stored | Human Example | Agent Example |
|-------------|----------------|---------------|---------------|
| [Semantic](#semantic-memory) | Facts | Things I learned in school | Facts about a user |
| [Episodic](#episodic-memory) | Experiences | Things I did | Past agent actions |
| [Procedural](#procedural-memory) | Instructions | Instincts or motor skills | Agent system prompt |

#### Semantic memory

[Semantic memory](https://en.wikipedia.org/wiki/Semantic_memory), both in humans and AI agents, involves the retention of specific facts and concepts. In humans, it can include information learned in school and the understanding of concepts and their relationships. For AI agents, semantic memory is often used to personalize applications by remembering facts or concepts from past interactions. 

!!! note

    Semantic memory is different from "semantic search," which is a technique for finding similar content using "meaning" (usually as embeddings). Semantic memory is a term from psychology, referring to storing facts and knowledge, while semantic search is a method for retrieving information based on meaning rather than exact matches.


##### Profile

Semantic memories can be managed in different ways. For example, memories can be a single, continuously updated "profile" of well-scoped and specific information about a user, organization, or other entity (including the agent itself). A profile is generally just a JSON document with various key-value pairs you've selected to represent your domain. 

When remembering a profile, you will want to make sure that you are **updating** the profile each time. As a result, you will want to pass in the previous profile and [ask the model to generate a new profile](https://github.com/langchain-ai/memory-template) (or some [JSON patch](https://github.com/hinthornw/trustcall) to apply to the old profile). This can be become error-prone as the profile gets larger, and may benefit from splitting a profile into multiple documents or **strict** decoding when generating documents to ensure the memory schemas remains valid.

![](img/memory/update-profile.png)

##### Collection

Alternatively, memories can be a collection of documents that are continuously updated and extended over time. Each individual memory can be more narrowly scoped and easier to generate, which means that you're less likely to **lose** information over time. It's easier for an LLM to generate _new_ objects for new information than reconcile new information with an existing profile. As a result, a document collection tends to lead to [higher recall downstream](https://en.wikipedia.org/wiki/Precision_and_recall).

However, this shifts some complexity memory updating. The model must now _delete_ or _update_ existing items in the list, which can be tricky. In addition, some models may default to over-inserting and others may default to over-updating. See the [Trustcall](https://github.com/hinthornw/trustcall) package for one way to manage this and consider evaluation (e.g., with a tool like [LangSmith](https://docs.smith.langchain.com/tutorials/Developers/evaluation)) to help you tune the behavior.

Working with document collections also shifts complexity to memory **search** over the list. The `Store` currently supports both [semantic search](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.query) and [filtering by content](https://langchain-ai.github.io/langgraph/reference/store/#langgraph.store.base.SearchOp.filter).

Finally, using a collection of memories can make it challenging to provide comprehensive context to the model. While individual memories may follow a specific schema, this structure might not capture the full context or relationships between memories. As a result, when using these memories to generate responses, the model may lack important contextual information that would be more readily available in a unified profile approach.

![](img/memory/update-list.png)

Regardless of memory management approach, the central point is that the agent will use the semantic memories to [ground its responses](https://python.langchain.com/docs/concepts/rag/), which often leads to more personalized and relevant interactions.

#### Episodic memory

[Episodic memory](https://en.wikipedia.org/wiki/Episodic_memory), in both humans and AI agents, involves recalling past events or actions. The [CoALA paper](https://arxiv.org/pdf/2309.02427) frames this well: facts can be written to semantic memory, whereas *experiences* can be written to episodic memory. For AI agents, episodic memory is often used to help an agent remember how to accomplish a task. 

In practice, episodic memories are often implemented through [few-shot example prompting](https://python.langchain.com/docs/concepts/few_shot_prompting/), where agents learn from past sequences to perform tasks correctly. Sometimes it's easier to "show" than "tell" and LLMs learn well from examples. Few-shot learning lets you ["program"](https://x.com/karpathy/status/1627366413840322562) your LLM by updating the prompt with input-output examples to illustrate the intended behavior. While various [best-practices](https://python.langchain.com/docs/concepts/#1-generating-examples) can be used to generate few-shot examples, often the challenge lies in selecting the most relevant examples based on user input.




Note that the memory [store](persistence.md#memory-store) is just one way to store data as few-shot examples. If you want to have more developer involvement, or tie few-shots more closely to your evaluation harness, you can also use a [LangSmith Dataset](https://docs.smith.langchain.com/evaluation/how_to_guides/datasets/index_datasets_for_dynamic_few_shot_example_selection) to store your data. Then dynamic few-shot example selectors can be used out-of-the box to achieve this same goal. LangSmith will index the dataset for you and enable retrieval of few shot examples that are most relevant to the user input based upon keyword similarity ([using a BM25-like algorithm](https://docs.smith.langchain.com/how_to_guides/datasets/index_datasets_for_dynamic_few_shot_example_selection) for keyword based similarity). 

See this how-to [video](https://www.youtube.com/watch?v=37VaU7e7t5o) for example usage of dynamic few-shot example selection in LangSmith. Also, see this [blog post](https://blog.langchain.dev/few-shot-prompting-to-improve-tool-calling-performance/) showcasing few-shot prompting to improve tool calling performance and this [blog post](https://blog.langchain.dev/aligning-llm-as-a-judge-with-human-preferences/) using few-shot example to align an LLMs to human preferences.




#### Procedural memory

[Procedural memory](https://en.wikipedia.org/wiki/Procedural_memory), in both humans and AI agents, involves remembering the rules used to perform tasks. In humans, procedural memory is like the internalized knowledge of how to perform tasks, such as riding a bike via basic motor skills and balance. Episodic memory, on the other hand, involves recalling specific experiences, such as the first time you successfully rode a bike without training wheels or a memorable bike ride through a scenic route. For AI agents, procedural memory is a combination of model weights, agent code, and agent's prompt that collectively determine the agent's functionality. 

In practice, it is fairly uncommon for agents to modify their model weights or rewrite their code. However, it is more common for agents to modify their own prompts. 

One effective approach to refining an agent's instructions is through ["Reflection"](https://blog.langchain.dev/reflection-agents/) or meta-prompting. This involves prompting the agent with its current instructions (e.g., the system prompt) along with recent conversations or explicit user feedback. The agent then refines its own instructions based on this input. This method is particularly useful for tasks where instructions are challenging to specify upfront, as it allows the agent to learn and adapt from its interactions.

For example, we built a [Tweet generator](https://www.youtube.com/watch?v=Vn8A3BxfplE) using external feedback and prompt re-writing to produce high-quality paper summaries for Twitter. In this case, the specific summarization prompt was difficult to specify *a priori*, but it was fairly easy for a user to critique the generated Tweets and provide feedback on how to improve the summarization process. 

The below pseudo-code shows how you might implement this with the LangGraph memory [store](persistence.md#memory-store), using the store to save a prompt, the `update_instructions` node to get the current prompt (as well as feedback from the conversation with the user captured in `state["messages"]`), update the prompt, and save the new prompt back to the store. Then, the `call_model` get the updated prompt from the store and uses it to generate a response.

```python

---

**Navigation:** [← Previous](./02-subgraph.md) | [Index](./index.md) | [Next →](./04-node-that-uses-the-instructions.md)
