---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Query expansion in multi-turn conversations

A RAG chatbot needs to be able to infer the user's intent for a given query, sometimes based on a vague context.

This is especially important in multi-turn conversations, where the user's intent may not be clear from a single query.

For example, in the first turn, a user might ask "What is A" and in the second turn, they might ask "Compare that with B and C". So, the agent needs to be able to infer that the user's intent is to compare A with B and C.

Let's see an example of this. First, note that the `run_agent` function is already set up to handle multi-turn conversations. It can take messages from the previous conversation turns and append them to the `messages` list.

In the first turn, the user asks about the Chat endpoint, to which the agent duly responds.
```python PYTHON
messages = run_agent("What is the Chat endpoint?")
```
```mdx

QUESTION:
What is the Chat endpoint?
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for 'Chat endpoint'. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"Chat endpoint"}
==================================================
RESPONSE:
The Chat endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.
==================================================
CITATIONS:

Start: 18| End:130| Text:'facilitates a conversational interface, allowing users to send messages to the model and receive text responses.' 
Sources:
1. search_developer_docs_qx7dht277mg7:3
```
In the second turn, the user asks a question that has two parts: first, how it's different from RAG, and then, for code examples.

We pass the messages from the previous conversation turn to the `run_agent` function.

Because of this, the agent is able to infer that the question is referring to the Chat endpoint even though the user didn't explicitly mention it.

The agent then expands the query into two separate queries, one for the `search_code_examples` tool and one for the `search_developer_docs` tool.
```python PYTHON
messages = run_agent(
    "How is it different from RAG? Also any code tutorials?", messages
)
```
```mdx

QUESTION:
How is it different from RAG? Also any code tutorials?
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for 'Chat endpoint vs RAG' and 'Chat endpoint code tutorials'. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"Chat endpoint vs RAG"}
Tool name: search_code_examples | Parameters: {"query":"Chat endpoint"}
==================================================
RESPONSE:
The Chat endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.

RAG (Retrieval Augmented Generation) is a method for generating text using additional information fetched from an external data source, which can greatly increase the accuracy of the response.

I could not find any code tutorials for the Chat endpoint, but I did find a tutorial on RAG with Chat Embed and Rerank via Pinecone.
==================================================
CITATIONS:

Start: 414| End:458| Text:'RAG with Chat Embed and Rerank via Pinecone.' 
Sources:
1. search_code_examples_h8mn6mdqbrc3:2
```typescript

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
