---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Run chatbot

We can now run the chatbot. For this, we create a `run_chatbot` function that accepts the user message and the history of the conversation, if available.
```python PYTHON
def run_chatbot(query, messages=None):
    if messages is None:
        messages = []

    messages.append({"role": "user", "content": query})

    # Retrieve document chunks and format

    documents = vectorstore.retrieve(query)
    documents_formatted = []
    for doc in documents:
        documents_formatted.append({"data": doc})

    # Use document chunks to respond

    response = co_chat.chat(
        model="model",  # Pass a dummy string

        messages=messages,
        documents=documents_formatted,
    )

    # Print the chatbot response, citations, and documents

    print("\nRESPONSE:\n")
    print(response.message.content[0].text)

    if response.message.citations:
        print("\nCITATIONS:\n")
        for citation in response.message.citations:
            print("-" * 20)
            print(
                "start:",
                citation.start,
                "end:",
                citation.end,
                "text:",
                citation.text,
            )
            print("SOURCES:")
            print(citation.sources)

    # Add assistant response to messages

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    return messages
```
Here is a sample conversation consisting of a few turns.
```python PYTHON
messages = run_chatbot("Hello, I have a question")
```
```mdx
RESPONSE:

Hello there! How can I help you today?
```
```python PYTHON
messages = run_chatbot("How to provide examples in prompts", messages)
```
```
RESPONSE:

There are a few ways to provide examples in prompts.

One way is to provide a few relevant and diverse examples in the prompt. This can help steer the LLM towards a high-quality solution. Good examples condition the model to the expected response type and style.

Another way is to provide specific examples to work from. For example, instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.

In addition to giving correct examples, including negative examples with a clear indication of why they are wrong can help the LLM learn to distinguish between correct and incorrect responses.

CITATIONS:

--------------------
start: 68 end: 126 text: provide a few relevant and diverse examples in the prompt.
SOURCES:
[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Few-shot Prompting\n\nUnlike the zero-shot examples above, few-shot prompting is a technique that provides a model with examples of the task being performed before asking the specific question to be answered. We can steer the LLM toward a high-quality solution by providing a few relevant and diverse examples in the prompt. Good examples condition the model to the expected response type and style.', 'title': 'Advanced Prompt Engineering Techniques', 'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'})]
--------------------
start: 136 end: 187 text: help steer the LLM towards a high-quality solution.
SOURCES:
[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Few-shot Prompting\n\nUnlike the zero-shot examples above, few-shot prompting is a technique that provides a model with examples of the task being performed before asking the specific question to be answered. We can steer the LLM toward a high-quality solution by providing a few relevant and diverse examples in the prompt. Good examples condition the model to the expected response type and style.', 'title': 'Advanced Prompt Engineering Techniques', 'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'})]
--------------------
start: 188 end: 262 text: Good examples condition the model to the expected response type and style.
SOURCES:
[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Few-shot Prompting\n\nUnlike the zero-shot examples above, few-shot prompting is a technique that provides a model with examples of the task being performed before asking the specific question to be answered. We can steer the LLM toward a high-quality solution by providing a few relevant and diverse examples in the prompt. Good examples condition the model to the expected response type and style.', 'title': 'Advanced Prompt Engineering Techniques', 'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'})]
--------------------
start: 282 end: 321 text: provide specific examples to work from.
SOURCES:
[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Incorporating Example Outputs\n\nLLMs respond well when they have specific examples to work from. For example, instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.', 'title': 'Crafting Effective Prompts', 'url': 'https://docs.cohere.com/docs/crafting-effective-prompts'})]
--------------------
start: 335 end: 485 text: instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.
SOURCES:
[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Incorporating Example Outputs\n\nLLMs respond well when they have specific examples to work from. For example, instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.', 'title': 'Crafting Effective Prompts', 'url': 'https://docs.cohere.com/docs/crafting-effective-prompts'})]
--------------------
start: 527 end: 679 text: including negative examples with a clear indication of why they are wrong can help the LLM learn to distinguish between correct and incorrect responses.
SOURCES:
[DocumentSource(type='document', id='doc:2', document={'id': 'doc:2', 'text': 'In addition to giving correct examples, including negative examples with a clear indication of why they are wrong can help the LLM learn to distinguish between correct and incorrect responses. Ordering the examples can also be important; if there are patterns that could be picked up on that are not relevant to the correctness of the question, the model may incorrectly pick up on those instead of the semantics of the question itself.', 'title': 'Advanced Prompt Engineering Techniques', 'url': 'https://docs.cohere.com/docs/advanced-prompt-engineering-techniques'})]
```
```python PYTHON
messages = run_chatbot(
    "What do you know about 5G networks?", messages
)
```
```mdx
RESPONSE:

I'm sorry, I could not find any information about 5G networks.
```
```python PYTHON
for message in messages:
    print(message, "\n")
```
```mdx
{'role': 'user', 'content': 'Hello, I have a question'} 

{'role': 'assistant', 'content': 'Hello! How can I help you today?'} 

{'role': 'user', 'content': 'How to provide examples in prompts'} 

{'role': 'assistant', 'content': 'There are a few ways to provide examples in prompts.\n\nOne way is to provide a few relevant and diverse examples in the prompt. This can help steer the LLM towards a high-quality solution. Good examples condition the model to the expected response type and style.\n\nAnother way is to provide specific examples to work from. For example, instead of asking for the salient points of the text and using bullet points “where appropriate”, give an example of what the output should look like.\n\nIn addition to giving correct examples, including negative examples with a clear indication of why they are wrong can help the LLM learn to distinguish between correct and incorrect responses.'} 

{'role': 'user', 'content': 'What do you know about 5G networks?'} 

{'role': 'assistant', 'content': "I'm sorry, I could not find any information about 5G networks."} 
```
There are a few observations worth pointing out:

* Direct response: For user messages that don’t require retrieval (“Hello, I have a question”), the chatbot responds directly without requiring retrieval.
* Citation generation: For responses that do require retrieval ("What's the difference between zero-shot and few-shot prompting"), the endpoint returns the response together with the citations. These are fine-grained citations, which means they refer to specific spans of the generated text.
* Response synthesis: The model can decide if none of the retrieved documents provide the necessary information to answer a user message. For example, when asked the question, “What do you know about 5G networks”, the chatbot retrieves external information from the index. However, it doesn’t use any of the information in its response as none of it is relevant to the question.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
