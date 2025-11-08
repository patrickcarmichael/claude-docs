---
title: "Langgraph: Overwrite the original message history"
description: "Overwrite the original message history section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← The messages returned by this function will be the input to the LLM.](./177-the-messages-returned-by-this-function-will-be-the.md)

**Next:** [Summarizing message history →](./179-summarizing-message-history.md)
