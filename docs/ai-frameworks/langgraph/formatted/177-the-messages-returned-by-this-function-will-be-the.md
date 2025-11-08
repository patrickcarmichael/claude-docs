---
title: "Langgraph: The messages returned by this function will be the input to the LLM."
description: "The messages returned by this function will be the input to the LLM. section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← This function will be added as a new node in ReAct agent graph](./176-this-function-will-be-added-as-a-new-node-in-react.md)

**Next:** [Overwrite the original message history →](./178-overwrite-the-original-message-history.md)
