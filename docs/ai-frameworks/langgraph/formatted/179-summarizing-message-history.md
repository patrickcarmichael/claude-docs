---
title: "Langgraph: Summarizing message history"
description: "Summarizing message history section of Langgraph documentation"
source: "https://langgraph.com"
last_updated: "2025-11-08"
---

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

---

## Navigation

- [📑 Back to Index](./index.md)
- [📄 Full Documentation](./documentation.md)
- [📝 Original Source](../llms-full.txt)

**Previous:** [← Overwrite the original message history](./178-overwrite-the-original-message-history.md)

**Next:** [How to integrate LangGraph (functional API) with AutoGen, CrewAI, and other frameworks →](./180-how-to-integrate-langgraph-functional-api-with-aut.md)
