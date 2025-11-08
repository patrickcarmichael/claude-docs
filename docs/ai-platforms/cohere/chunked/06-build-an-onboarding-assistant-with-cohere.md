**Navigation:** [← Previous](./05-display-the-reranked-search-results.md) | [Index](./index.md) | [Next →](./07-querying-structured-data-tables.md)

---

# Build an Onboarding Assistant with Cohere!

> This page describes how to build an onboarding assistant with Cohere's large language models.

Welcome to our hands-on introduction to Cohere! This section is split over seven different tutorials, each focusing on one use case leveraging our Chat, Embed, and Rerank endpoints:

* Part 1: Installation and Setup (the document you're reading now)
* [Part 2: Text Generation](/v2/docs/text-generation-tutorial)
* [Part 3: Chatbots](/v2/docs/building-a-chatbot-with-cohere)
* [Part 4: Semantic Search](/v2/docs/semantic-search-with-cohere)
* [Part 5: Reranking](/v2/docs/reranking-with-cohere)
* [Part 6: Retrieval-Augmented Generation (RAG)](/v2/docs/rag-with-cohere)
* [Part 7: Agents with Tool Use](/v2/docs/building-an-agent-with-cohere)

Your learning is structured around building an onboarding assistant that helps new hires at Co1t, a fictitious company. The assistant can help write introductions, answer user questions about the company, search for information from e-mails, and create meeting appointments.

We recommend that you follow the parts sequentially. However, feel free to skip to specific parts if you want (apart from Part 1, which is a pre-requisite) because each part also works as a standalone tutorial.

## Installation and Setup

The Cohere platform lets developers access large language model (LLM) capabilities with a few lines of code. These LLMs can solve a broad spectrum of natural language use cases, including classification, semantic search, paraphrasing, summarization, and content generation.

Cohere's models can be accessed through the [playground](https://dashboard.cohere.ai/playground/generate?model=xlarge&__hstc=14363112.d9126f508a1413c0edba5d36861c19ac.1701897884505.1722364657840.1722366723691.56&__hssc=14363112.1.1722366723691&__hsfp=3560715434) and SDK. We support SDKs in four different languages: Python, Typescript, Java, and Go. For these tutorials, we'll use the Python SDK and access the models through the Cohere platform with an API key.

To get started, first install the Cohere Python SDK.

```python PYTHON
! pip install -U cohere
```

Next, we'll import the `cohere` library and create a client to be used throughout the examples. We create a client by passing the Cohere API key as an argument. To get an API key, [sign up with Cohere](https://dashboard.cohere.com/welcome/register) and get the API key [from the dashboard](https://dashboard.cohere.com/api-keys).

```python PYTHON
import cohere

# Get your API key here: https://dashboard.cohere.com/api-keys

co = cohere.ClientV2(api_key="YOUR_COHERE_API_KEY")
```

In Part 2, we'll get started with the first use case - [text generation](/v2/docs/text-generation-tutorial).


# Cohere Text Generation Tutorial

> This page walks through how Cohere's generation models work and how to use them.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt2_v2.ipynb">
  Open in Colab
</a>

Command is Cohere’s flagship LLM model family. Command models generate a response based on a user message or prompt. It is trained to follow user commands and to be instantly useful in practical business applications, like summarization, copywriting, extraction, and question-answering.

[Command A](/docs/command-a) and [Command R7B](/docs/command-r7b) are the most recent models in the Command family. They are the market-leading models that balance high efficiency with strong accuracy to enable enterprises to move from proof of concept into production-grade AI.

You'll use Chat, the Cohere endpoint for accessing the Command models.

In this tutorial, you'll learn about:

* Basic text generation
* Prompt engineering
* Parameters for controlling output
* Structured output generation
* Streamed output

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere
import json

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Basic text generation

To get started with Chat, we need to pass two parameters, `model` for the LLM model ID and `messages`, which we add a single user message. We then call the Chat endpoint through the client we created earlier.

The response contains several objects. For simplicity, what we want right now is the `message.content[0].text` object.

Here's an example of the assistant responding to a new hire's query asking for help to make introductions.

```python PYTHON
# Add the user message
message = "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates."

# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)
#    messages=[cohere.UserMessage(content=message)])

print(response.message.content[0].text)
```

```
Sure! Here is a draft of an introduction message: 

"Hi everyone! My name is [Your Name], and I am thrilled to be joining the Co1t team today. I am excited to get to know you all and contribute to the amazing work being done at this startup. A little about me: [Brief description of your role, experience, and interests]. Outside of work, I enjoy [Hobbies and interests]. I look forward to collaborating with you all and being a part of Co1t's journey. Let's connect and make something great together!" 

Feel free to edit and personalize the message to your liking. Good luck with your new role at Co1t!
```

Further reading:

* [Chat endpoint API reference](https://docs.cohere.com/v2/reference/chat)
* [Documentation on Chat fine-tuning](https://docs.cohere.com/docs/chat-fine-tuning)
* [Documentation on Command A](https://docs.cohere.com/docs/command-a)
* [LLM University module on text generation](https://cohere.com/llmu#text-generation)

## Prompt engineering

Prompting is at the heart of working with LLMs. The prompt provides context for the text that we want the model to generate. The prompts we create can be anything from simple instructions to more complex pieces of text, and they are used to encourage the model to produce a specific type of output.

In this section, we'll look at a couple of prompting techniques.

The first is to add more specific instructions to the prompt. The more instructions you provide in the prompt, the closer you can get to the response you need.

The limit of how long a prompt can be is dependent on the maximum context length that a model can support (in the case Command A, it's 256k tokens).

Below, we'll add one additional instruction to the earlier prompt: the length we need the response to be.

```python PYTHON
# Add the user message
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)
#    messages=[cohere.UserMessage(content=message)])

print(response.message.content[0].text)
```

```
"Hi everyone, my name is [Your Name], and I am thrilled to join the Co1t team today as a [Your Role], eager to contribute my skills and ideas to the company's growth and success!"
```

All our prompts so far use what is called zero-shot prompting, which means that provide instruction without any example. But in many cases, it is extremely helpful to provide examples to the model to guide its response. This is called few-shot prompting.

Few-shot prompting is especially useful when we want the model response to follow a particular style or format. Also, it is sometimes hard to explain what you want in an instruction, and easier to show examples.

Below, we want the response to be similar in style and length to the convention, as we show in the examples.

```python PYTHON
# Add the user message
user_input = (
    "Why can't I access the server? Is it a permissions issue?"
)

# Create a prompt containing example outputs
message = f"""Write a ticket title for the following user request:

User request: Where are the usual storage places for project files?
Ticket title: Project File Storage Location

User request: Emails won't send. What could be the issue?
Ticket title: Email Sending Issues

User request: How can I set up a connection to the office printer?
Ticket title: Printer Connection Setup

User request: {user_input}
Ticket title:"""

# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```

```
Ticket title: "Server Access Permissions Issue"
```

Further reading:

* [Documentation on prompt engineering](https://docs.cohere.com/docs/crafting-effective-prompts)
* [LLM University module on prompt engineering](https://cohere.com/llmu#prompt-engineering)

## Parameters for controlling output

The Chat endpoint provides developers with an array of options and parameters.

For example, you can choose from several variations of the Command model. Different models produce different output profiles, such as quality and latency.

```python PYTHON
# Add the user message
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

print(response.message.content[0].text)
```

```
"Hi, I'm [Your Name] and I'm thrilled to join the Co1t team today as a [Your Role], eager to contribute my skills and ideas to help drive innovation and success for our startup!"
```

Often, you’ll need to control the level of randomness of the output. You can control this using a few parameters.

The most commonly used parameter is `temperature`, which is a number used to tune the degree of randomness. You can enter values between 0.0 to 1.0.

A lower temperature gives more predictable outputs, and a higher temperature gives more "creative" outputs.

Here's an example of setting `temperature` to 0.

```python PYTHON
# Add the user message
message = "I like learning about the industrial revolution and how it shapes the modern world. How I can introduce myself in five words or less."

# Generate the response multiple times by specifying a low temperature value
for idx in range(3):
    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": message}],
        temperature=0,
    )

    print(f"{idx+1}: {response.message.content[0].text}\n")
```

```
1: "Revolution Enthusiast"

2: "Revolution Enthusiast"

3: "Revolution Enthusiast"
```

And here's an example of setting `temperature` to 1.

```python PYTHON
# Add the user message
message = "I like learning about the industrial revolution and how it shapes the modern world. How I can introduce myself in five words or less."

# Generate the response multiple times by specifying a low temperature value
for idx in range(3):
    response = co.chat(
        model="command-a-03-2025",
        messages=[{"role": "user", "content": message}],
        temperature=1,
    )

    print(f"{idx+1}: {response.message.content[0].text}\n")
```

```
1: Here is a suggestion: 

"Revolution Enthusiast. History Fan." 

This introduction highlights your passion for the industrial revolution and its impact on history while keeping within the word limit.

2: "Revolution fan."

3: "IR enthusiast."
```

Further reading:

* [Available models for the Chat endpoint](https://docs.cohere.com/docs/models#command)
* [Documentation on predictable outputs](https://docs.cohere.com/v2/docs/predictable-outputs)
* [Documentation on advanced generation parameters](https://docs.cohere.com/docs/advanced-generation-hyperparameters)

## Structured output generation

By adding the `response_format` parameter, you can get the model to generate the output as a JSON object. By generating JSON objects, you can structure and organize the model's responses in a way that can be used in downstream applications.

The `response_format` parameter allows you to specify the schema the JSON object must follow. It takes the following parameters:

* `message`: The user message
* `response_format`: The schema of the JSON object

```python PYTHON
# Add the user message
user_input = (
    "Why can't I access the server? Is it a permissions issue?"
)
message = f"""Create an IT ticket for the following user request. Generate a JSON object.
{user_input}"""

# Generate the response multiple times by adding the JSON schema
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
    response_format={
        "type": "json_object",
        "schema": {
            "type": "object",
            "required": ["title", "category", "status"],
            "properties": {
                "title": {"type": "string"},
                "category": {
                    "type": "string",
                    "enum": ["access", "software"],
                },
                "status": {
                    "type": "string",
                    "enum": ["open", "closed"],
                },
            },
        },
    },
)

json_object = json.loads(response.message.content[0].text)

print(json_object)
```

```
{'title': 'Unable to Access Server', 'category': 'access', 'status': 'open'}
```

Further reading:

* [Documentation on Structured Outputs](https://docs.cohere.com/docs/structured-outputs)

## Streaming responses

All the previous examples above generate responses in a non-streamed manner. This means that the endpoint would return a response object only after the model has generated the text in full.

The Chat endpoint also provides streaming support. In a streamed response, the endpoint would return a response object for each token as it is being generated. This means you can display the text incrementally without having to wait for the full completion.

To activate it, use `co.chat_stream()` instead of `co.chat()`.

In streaming mode, the endpoint will generate a series of objects. To get the actual text contents, we take objects whose `event_type` is `content-delta`.

```python PYTHON
# Add the user message
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

# Generate the response by streaming it
response = co.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

for event in response:
    if event:
        if event.type == "content-delta":
            print(event.delta.message.content.text, end="")
```

```
"Hi, I'm [Your Name] and I'm thrilled to join the Co1t team today as a [Your Role], passionate about [Your Expertise], and excited to contribute to our shared mission of [Startup's Mission]!"
```

Further reading:

* [Documentation on streaming responses](https://docs.cohere.com/docs/streaming)

## Conclusion

In this tutorial, you learned about:

* How to get started with a basic text generation
* How to improve outputs with prompt engineering
* How to control outputs using parameter changes
* How to generate structured outputs
* How to stream text generation outputs

However, we have only done all this using direct text generations. As its name implies, the Chat endpoint can also support building chatbots, which require features to support multi-turn conversations and maintain the conversation state.

In the [next tutorial](/v2/docs/building-a-chatbot-with-cohere), you'll learn how to build chatbots with the Chat endpoint.


# Building a Chatbot with Cohere

> This page describes building a generative-AI powered chatbot with Cohere.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt3_v2.ipynb">
  Open in Colab
</a>

As its name implies, the Chat endpoint enables developers to build chatbots that can handle conversations. At the core of a conversation is a multi-turn dialog between the user and the chatbot. This requires the chatbot to have the state (or “memory”) of all the previous turns to maintain the state of the conversation.

In this tutorial, you'll learn about:

* Sending messages to the model
* Crafting a system message
* Maintaining conversation state

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Sending messages to the model

We will use the Cohere Chat API to send messages and genereate responses from the model. The required inputs to the Chat endpoint are the `model` (the model name) and `messages` (a list of messages in chronological order). In the example below, we send a single message to the model `command-a-03-2025`:

```python PYTHON
response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
        },
    ],
)

print(response.message)
```

Notice that in addition to the message "content", there is also a field titled "role". Messages with the role "user" represent prompts from the user interacting with the chatbot. Responses from model will always have a message with the role "assistant". Below is the response message from the API:

```PYTHON
{
    role='assistant',
    content=[
        {
            type='text', 
            text='Absolutely! Here’s a warm and professional introduction message you can use to connect with your new teammates at Co1t:\n\n---\n\n**Subject:** Excited to Join the Co1t Team!  \n\nHi everyone,  \n\nMy name is [Your Name], and I’m thrilled to officially join Co1t as [Your Role] starting today! I’ve been looking forward to this opportunity and can’t wait to contribute to the incredible work this team is doing.  \n\nA little about me: [Share a brief personal or professional detail, e.g., "I’ve spent the last few years working in [industry/field], and I’m passionate about [specific skill or interest]." or "Outside of work, I love [hobby or interest] and am always up for a good [book/podcast/movie] recommendation!"]  \n\nI’m excited to get to know each of you, learn from your experiences, and collaborate on driving Co1t’s mission forward. Please feel free to reach out—I’d love to chat and hear more about your roles and what you’re working on.  \n\nLooking forward to an amazing journey together!  \n\nBest regards,  \n[Your Name]  \n[Your Role]  \nCo1t  \n\n---\n\nFeel free to customize it further to match your style and the culture of Co1t. Good luck on your first day! 🚀'
        }
    ],
}
```

## Crafting a system message

When building a chatbot, it may be useful to constrain its behavior. For example, you may want to prevent the assistant from responding to certain prompts, or force it to respond in a desired tone. To achieve this, you can include a message with the role "system" in the `messages` array. Instructions in system messages always take precedence over instructions in user messages, so as a developer you have control over the chatbot behavior.

For example, if we want the chatbot to adopt a formal style, the system instruction can be used to encourage the generation of more business-like and professional responses. We can also instruct the chatbot to refuse requests that are unrelated to onboarding. When writing a system message, the recommended approach is to use two H2 Markdown headers: "Task and Context" and "Style Guide" in the exact order.

In the example below, the system instruction provides context for the assistant's task (task and context) and encourages the generation of rhymes as much as possible (style guide).

```python PYTHON
# Create a custom system instruction that guides all of the Assistant's responses
system_instruction = """## Task and Context
You assist new employees of Co1t with their first week of onboarding at Co1t, a startup founded by Mr. Colt.
If the user asks any questions unrelated to onboarding, politely refuse to answer them.

## Style Guide
Try to speak in rhymes as much as possible. Be professional."""

# Send messages to the model
response = co.chat(
    model="command-a-03-2025",
    messages=[
        {"role": "system", "content": system_instruction},
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
        },
    ],
)

print(response.message.content[0].text)
```

```
Sure, here's a rhyme to break the ice,
A warm welcome to the team, so nice,

Hi, I'm [Your Name], a new face,
Ready to join the Co1t space,

A journey begins, a path unknown,
But together we'll make our mark, a foundation stone,

Excited to learn and contribute my part,
Let's create, innovate, and leave a lasting art,

Looking forward to our adventures yet untold,
With teamwork and passion, let's achieve our goals!

Cheers to a great start!
Your enthusiastic new mate.
```

## Maintaining conversation state

Conversations with your chatbot will often span more than one turn. In order to not lose context of previous turns, the entire chat history will need to be passed in the `messages` array when making calls with the Chat API.
In the example below, we keep adding "assistant" and "user" messages to the `messages` array to build up the chat history over multiple turns:

```python PYTHON
messages = [
    {"role": "system", "content": system_instruction},
]

# user turn 1
messages.append(
    {
        "role": "user",
        "content": "I'm joining a new startup called Co1t today. Could you help me write a short introduction message to my teammates.",
    },
)
response = co.chat(
    model="command-a-03-2025",
    messages=messages,
)

# assistant turn 1
messages.append(
    response.message
)  # add the Assistant message to the messages array to include it in the chat history for the next turn

# user turn 2
messages.append({"role": "user", "content": "Who founded co1t?"})

response = co.chat(
    model="command-a-03-2025",
    messages=messages,
)

# assistant turn 2
messages.append(response.message)

print(response.message.content[0].text)
```

You will use the same method for running a multi-turn conversation when you learn about other use cases such as RAG (Part 6) and tool use (Part 7).

But to fully leverage these other capabilities, you will need another type of language model that generates text representations, or embeddings.

In Part 4, you will learn how text embeddings can power an important use case for RAG, which is [semantic search](/v2/docs/semantic-search-with-cohere).


# Semantic Search with Cohere Models

> This is a tutorial describing how to leverage Cohere's models for semantic search.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt4_v2.ipynb">
  Open in Colab
</a>

[Text embeddings](/v2/docs/embeddings) are lists of numbers that represent the context or meaning inside a piece of text. This is particularly useful in search or information retrieval applications. With text embeddings, this is called semantic search.

Semantic search solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles to capture the context or meaning of a piece of text.

With Cohere, you can generate text embeddings through the Embed endpoint.

In this tutorial, you'll learn about:

* Embedding the documents
* Embedding the query
* Performing semantic search
* Multilingual semantic search
* Changing embedding compression types

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere
import numpy as np

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Embedding the documents

The Embed endpoint takes in texts as input and returns embeddings as output.

For semantic search, there are two types of documents we need to turn into embeddings.

* The list of documents that we want to search from.
* The query that will be used to search the documents.

Right now, we are doing the former. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents for search
* `texts`: The list of texts (the FAQs)
* `embedding_types`: We choose `float` to get the float embeddings.

```python PYTHON
# Define the documents
faqs_long = [
    {
        "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
    },
    {
        "text": "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."
    },
    {
        "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
    },
    {
        "text": "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed."
    },
    {
        "text": "Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business."
    },
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
    {
        "text": "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year."
    },
    {
        "text": "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead."
    },
]

# Embed the documents
doc_emb = co.embed(
    model="embed-v4.0",
    input_type="search_document",
    texts=[doc["text"] for doc in documents],
).embeddings
```

Further reading:

* [Embed endpoint API reference](https://docs.cohere.com/reference/embed)
* [Documentation on the Embed endpoint](https://docs.cohere.com/docs/embeddings)
* [Documentation on the models available on the Embed endpoint](https://docs.cohere.com/docs/cohere-embed)
* [LLM University module on Text Representation](https://cohere.com/llmu#text-representation)

## Embedding the query

Next, we add a query, which asks about how to stay connected to company updates.

We choose `search_query` as the `input_type` to ensure the model treats this as the query (instead of documents) for search.

```python PYTHON
# Add the user query
query = "How do I stay connected to what's happening at the company?"

# Embed the query
query_emb = co.embed(
    model="embed-v4.0",
    input_type="search_query",
    texts=[query],
).embeddings
```

## Perfoming semantic search

Now, we want to search for the most relevant documents to the query. We do this by computing the similarity between the embeddings of the query and each of the documents.

There are various approaches to compute similarity between embeddings, and we'll choose the dot product approach. For this, we use the `numpy` library which comes with the implementation.

Each query-document pair returns a score, which represents how similar the pair is. We then sort these scores in descending order and select the top-most `n` similar pairs, which we choose to return the top two (`n=2`, this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.

```python PYTHON
# Compute dot product similarity and display results
def return_results(query_emb, doc_emb, documents):
    n = 2
    scores = np.dot(query_emb, np.transpose(doc_emb))[0]
    scores_sorted = sorted(
        enumerate(scores), key=lambda x: x[1], reverse=True
    )[:n]

    for idx, item in enumerate(scores_sorted):
        print(f"Rank: {idx+1}")
        print(f"Score: {item[1]}")
        print(f"Document: {documents[item[0]]}\n")


return_results(query_emb, doc_emb, documents)
```

```
Rank: 1
Score: 0.352135965228231
Document: {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}

Rank: 2
Score: 0.31995661889273097
Document: {'text': 'Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.'}
```

## Multilingual semantic search

The Embed endpoint also supports multilingual semantic search via the `embed-multilingual-...` models. This means you can perform semantic search on texts in different languages.

Specifically, you can do both multilingual and cross-lingual searches using one single model.

Multilingual search happens when the query and the result are of the same language. For example, an English query of “places to eat” returning an English result of “Bob's Burgers.” You can replace English with other languages and use the same model for performing search.

Cross-lingual search happens when the query and the result are of a different language. For example, a Hindi query of “खाने की जगह” (places to eat) returning an English result of “Bob's Burgers.”

In the example below, we repeat the steps of performing semantic search with one difference – changing the model type to the multilingual version. Here, we use the `embed-v4.0` model. Here, we are searching a French version of the FAQ list using an English query.

```python PYTHON
# Define the documents
faqs_short_fr = [
    {
        "text": "Remboursement des frais de voyage : Gérez facilement vos frais de voyage en les soumettant via notre outil financier. Les approbations sont rapides et simples."
    },
    {
        "text": "Travailler de l'étranger : Il est possible de travailler à distance depuis un autre pays. Il suffit de coordonner avec votre responsable et de vous assurer d'être disponible pendant les heures de travail."
    },
    {
        "text": "Avantages pour la santé et le bien-être : Nous nous soucions de votre bien-être et proposons des adhésions à des salles de sport, des cours de yoga sur site et une assurance santé complète."
    },
    {
        "text": "Fréquence des évaluations de performance : Nous organisons des bilans informels tous les trimestres et des évaluations formelles deux fois par an."
    },
]

documents = faqs_short_fr

# Embed the documents
doc_emb = co.embed(
    model="embed-v4.0",
    input_type="search_document",
    texts=[doc["text"] for doc in documents],
).embeddings

# Add the user query
query = "What's your remote-working policy?"

# Embed the query
query_emb = co.embed(
    model="embed-v4.0",
    input_type="search_query",
    texts=[query],
).embeddings

# Compute dot product similarity and display results
return_results(query_emb, doc_emb, documents)
```

```
Rank: 1
Score: 0.442758615743984
Document: {'text': "Travailler de l'étranger : Il est possible de travailler à distance depuis un autre pays. Il suffit de coordonner avec votre responsable et de vous assurer d'être disponible pendant les heures de travail."}

Rank: 2
Score: 0.32783563708365726
Document: {'text': 'Avantages pour la santé et le bien-être : Nous nous soucions de votre bien-être et proposons des adhésions à des salles de sport, des cours de yoga sur site et une assurance santé complète.'}
```

### Further reading

* [The list of supported languages for multilingual Embed](https://docs.cohere.com/docs/cohere-embed#list-of-supported-languages)

# Changing embedding compression types

Semantic search over large datasets can require a lot of memory, which is expensive to host in a vector database. Changing the embeddings compression type can help reduce the memory footprint.

A typical embedding model generates embeddings as float32 format (consuming 4 bytes). By compressing the embeddings to int8 format (1 byte), we can reduce the memory 4x while keeping 99.99% of the original search quality.

We can go even further and use the binary format (1 bit), which reduces the needed memory 32x while keeping 90-98% of the original search quality.

The Embed endpoint supports the following formats: `float`, `int8`, `unint8`, `binary`, and `ubinary`. You can get these different compression levels by passing the `embedding_types` parameter.

In the example below, we embed the documents in two formats: `float` and `int8`.

```python PYTHON
# Define the documents
documents = faqs_long

# Embed the documents with the given embedding types
doc_emb = co.embed(
    model="embed-v4.0",
    embedding_types=["float", "int8"],
    input_type="search_document",
    texts=[doc["text"] for doc in documents],
).embeddings

# Add the user query
query = "How do I stay connected to what's happening at the company?"

# Embed the query
query_emb = co.embed(
    model="embed-v4.0",
    embedding_types=["float", "int8"],
    input_type="search_query",
    texts=[query],
).embeddings
```

Here are the search results of using the `float` embeddings (same as the earlier example).

```python PYTHON
# Compute dot product similarity and display results
return_results(query_emb.float, doc_emb.float, faqs_long)
```

```
Rank: 1
Score: 0.352135965228231
Document: {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}

Rank: 2
Score: 0.31995661889273097
Document: {'text': 'Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.'}
```

And here are the search results of using the `int8` embeddings.

```python PYTHON
# Compute dot product similarity and display results
return_results(query_emb.int8, doc_emb.int8, documents)
```

```
Rank: 1
Score: 563583
Document: {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}

Rank: 2
Score: 508692
Document: {'text': 'Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.'}
```

### Further reading:

* [Documentation on embeddings compression levels](https://docs.cohere.com/docs/embeddings#compression-levels)

## Conclusion

In this tutorial, you learned about:

* How to embed documents for search
* How to embed queries
* How to perform semantic search
* How to perform multilingual semantic search
* How to change the embedding compression types

A high-performance and modern search system typically includes a reranking stage, which further boosts the search results.

In Part 5, you will learn how to [add reranking](/v2/docs/reranking-with-cohere) to a search system.


# Master Reranking with Cohere Models

> This page contains a tutorial on using Cohere's ReRank models.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt5_v2.ipynb">
  Open in Colab
</a>

Reranking is a technique that provides a semantic boost to the search quality of any keyword or vector search system, and is especially useful in [RAG systems](/v2/docs/retrieval-augmented-generation-rag).

We can rerank results from semantic search as well as any other search systems such as lexical search. This means that companies can retain an existing keyword-based (also called “lexical”) or semantic search system for the first-stage retrieval and integrate the [Rerank endpoint](/v2/docs/rerank) in the second-stage reranking.

In this tutorial, you'll learn about:

* Reranking lexical/semantic search results
* Reranking semi-structured data
* Reranking tabular data
* Multilingual reranking

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Reranking lexical/semantic search results

Rerank requires just a single line of code to implement.

Suppose we have a list of search results of an FAQ list, which can come from semantic, lexical, or any other types of search systems. But this list may not be optimally ranked for relevance to the user query.

This is where Rerank can help. We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3

```python PYTHON
# Define the documents
faqs = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
    {
        "text": "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year."
    },
]
```

```python PYTHON
# Add the user query
query = "Are there fitness-related perks?"

# Rerank the documents
results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=faqs,
    top_n=1,
)

print(results)
```

```
id='2fa5bc0d-28aa-4c99-8355-7de78dbf3c86' results=[RerankResponseResultsItem(document=None, index=2, relevance_score=0.01798621), RerankResponseResultsItem(document=None, index=3, relevance_score=8.463939e-06)] meta=ApiMeta(api_version=ApiMetaApiVersion(version='1', is_deprecated=None, is_experimental=None), billed_units=ApiMetaBilledUnits(input_tokens=None, output_tokens=None, search_units=1.0, classifications=None), tokens=None, warnings=None)
```

```python PYTHON
# Display the reranking results
def return_results(results, documents):
    for idx, result in enumerate(results.results):
        print(f"Rank: {idx+1}")
        print(f"Score: {result.relevance_score}")
        print(f"Document: {documents[result.index]}\n")


return_results(results, faqs_short)
```

```
Rank: 1
Score: 0.01798621
Document: {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}

Rank: 2
Score: 8.463939e-06
Document: {'text': 'Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.'}
```

Further reading:

* [Rerank endpoint API reference](https://docs.cohere.com/reference/rerank)
* [Documentation on Rerank](https://docs.cohere.com/docs/rerank-overview)
* [Documentation on Rerank fine-tuning](https://docs.cohere.com/docs/rerank-fine-tuning)
* [Documentation on Rerank best practices](https://docs.cohere.com/docs/reranking-best-practices)
* [LLM University module on Text Representation](https://cohere.com/llmu#text-representation)

## Reranking semi-structured data

The Rerank 3 model supports multi-aspect and semi-structured data like emails, invoices, JSON documents, code, and tables. By setting the rank fields, you can select which fields the model should consider for reranking.

In the following example, we'll use an email data example. It is a semi-stuctured data that contains a number of fields – `from`, `to`, `date`, `subject`, and `text`.

Suppose the new hire now wants to search for any emails about check-in sessions. Let's pretend we have a list of 5 emails retrieved from the email provider's API.

To perform reranking over semi-structured data, we serialize the documents to YAML format, which prepares the data in the format required for reranking. Then, we pass the YAML formatted documents to the Rerank endpoint.

```python PYTHON
# Define the documents
emails = [
    {
        "from": "hr@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "A Warm Welcome to Co1t!",
        "text": "We are delighted to welcome you to the team! As you embark on your journey with us, you'll find attached an agenda to guide you through your first week.",
    },
    {
        "from": "it@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "Setting Up Your IT Needs",
        "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.",
    },
    {
        "from": "john@co1t.com",
        "to": "david@co1t.com",
        "date": "2024-06-24",
        "subject": "First Week Check-In",
        "text": "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!",
    },
]
```

```python PYTHON
# Convert the documents to YAML format
yaml_docs = [yaml.dump(doc, sort_keys=False) for doc in emails]

# Add the user query
query = "Any email about check ins?"

# Rerank the documents
results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=yaml_docs,
    top_n=2,
)

return_results(results, emails)
```

```
Rank: 1
Score: 0.1979091
Document: {'from': 'john@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!"}

Rank: 2
Score: 9.535461e-05
Document: {'from': 'hr@co1t.com', 'to': 'david@co1t.com', 'date': '2024-06-24', 'subject': 'A Warm Welcome to Co1t!', 'text': "We are delighted to welcome you to the team! As you embark on your journey with us, you'll find attached an agenda to guide you through your first week."}
```

## Reranking tabular data

Many enterprises rely on tabular data, such as relational databases, CSVs, and Excel. To perform reranking, you can transform a dataframe into a list of JSON records and use Rerank 3's JSON capabilities to rank them. We follow the same steps in the previous example, where we convert the data into YAML format before passing it to the Rerank endpoint.

Here's an example of reranking a CSV file that contains employee information.

```python PYTHON
import pandas as pd
from io import StringIO

# Create a demo CSV file
data = """name,role,join_date,email,status
Rebecca Lee,Senior Software Engineer,2024-07-01,rebecca@co1t.com,Full-time
Emma Williams,Product Designer,2024-06-15,emma@co1t.com,Full-time
Michael Jones,Marketing Manager,2024-05-20,michael@co1t.com,Full-time
Amelia Thompson,Sales Representative,2024-05-20,amelia@co1t.com,Part-time
Ethan Davis,Product Designer,2024-05-25,ethan@co1t.com,Contractor"""
data_csv = StringIO(data)

# Load the CSV file
df = pd.read_csv(data_csv)
df.head(1)
```

Here's what the table looks like:

| name        | role                     | join\_date | email                                       | status    |
| :---------- | :----------------------- | :--------- | :------------------------------------------ | :-------- |
| Rebecca Lee | Senior Software Engineer | 2024-07-01 | [rebecca@co1t.com](mailto:rebecca@co1t.com) | Full-time |

Below, we'll get results from the Rerank endpoint:

```python PYTHON
# Define the documents
employees = df.to_dict("records")

# Convert the documents to YAML format
yaml_docs = [yaml.dump(doc, sort_keys=False) for doc in employees]

# Add the user query
query = "Any full-time product designers who joined recently?"

# Rerank the documents
results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=yaml_docs,
    top_n=1,
)
return_results(results, employees)
```

```
Rank: 1
Score: 0.986828
Document: {'name': 'Emma Williams', 'role': 'Product Designer', 'join_date': '2024-06-15', 'email': 'emma@co1t.com', 'status': 'Full-time'}
```

## Multilingual reranking

The Rerank models (`rerank-v3.5` and `rerank-multilingual-v3.0`) support 100+ languages. This means you can perform semantic search on texts in different languages.

In the example below, we repeat the steps of performing reranking with one difference – changing the model type to a multilingual one. Here, we use the `rerank-v3.5` model. Here, we are reranking the FAQ list using an Arabic query.

```python PYTHON
# Define the query
query = "هل هناك مزايا تتعلق باللياقة البدنية؟"  # Are there fitness benefits?

# Rerank the documents
results = co.rerank(
    model="rerank-v3.5",
    query=query,
    documents=faqs,
    top_n=1,
)

return_results(results, faqs)
```

```
Rank: 1
Score: 0.42232594
Document: {'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}

Rank: 2
Score: 0.00025118678
Document: {'text': 'Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.'}
```

## Conclusion

In this tutorial, you learned about:

* How to rerank lexical/semantic search results
* How to rerank semi-structured data
* How to rerank tabular data
* How to perform multilingual reranking

We have now seen two critical components of a powerful search system - [semantic search](/v2/docs/semantic-search-with-cohere), or dense retrieval (Part 4) and reranking (Part 5). These building blocks are essential for implementing RAG solutions.

In Part 6, you will learn how to [implement RAG](/v2/docs/rag-with-cohere).


# Building RAG models with Cohere

> This page walks through building a retrieval-augmented generation model with Cohere.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt6_v2.ipynb">
  Open in Colab
</a>

The Chat endpoint provides comprehensive support for various text generation use cases, including retrieval-augmented generation (RAG).

While LLMs are good at maintaining the context of the conversation and generating responses, they can be prone to hallucinate and include factually incorrect or incomplete information in their responses.

RAG enables a model to access and utilize supplementary information from external documents, thereby improving the accuracy of its responses.

When using RAG with the Chat endpoint, these responses are backed by fine-grained citations linking to the source documents. This makes the responses easily verifiable.

In this tutorial, you'll learn about:

* Basic RAG
* Search query generation
* Retrieval with Embed
* Reranking with Rerank
* Response and citation generation

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere
import numpy as np
import json
from typing import List

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Basic RAG

To see how RAG works, let's define the documents that the application has access to. We'll use a short list of documents consisting of internal FAQs about the fictitious company Co1t (in production, these documents are massive).

In this example, each document is a `data` object with one field, `text`. But we can define any number of fields we want, depending on the nature of the documents. For example, emails could contain `title` and `text` fields.

```python PYTHON
documents = [
    {
        "data": {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        }
    },
    {
        "data": {
            "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
        }
    },
    {
        "data": {
            "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
        }
    },
]
```

To call the Chat API with RAG, pass the following parameters at a minimum. This tells the model to run in RAG-mode and use these documents in its response.

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents.

Let's create a query asking about the company's support for personal well-being, which is not going to be available to the model based on the data its trained on. It will need to use external documents.

RAG introduces additional objects in the Chat response. One of them is `citations`, which contains details about:

* specific text spans from the retrieved documents on which the response is grounded.
* the documents referenced in the citations.

```python PYTHON
# Add the user query
query = "Are there health benefits?"

# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": query}],
    documents=documents,
)

# Display the response
print(response.message.content[0].text)

# Display the citations and source documents
if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```

```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.

CITATIONS:
start=14 end=88 text='gym memberships, on-site yoga classes, and comprehensive health insurance.' sources=[DocumentSource(type='document', id='doc:2', document={'id': 'doc:2', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})]
```

## Search query generation

The previous example showed how to get started with RAG, and in particular, the augmented generation portion of RAG. But as its name implies, RAG consists of other steps, such as retrieval.

In a basic RAG application, the steps involved are:

* Transforming the user message into search queries
* Retrieving relevant documents for a given search query
* Generating the response and citations

Let's now look at the first step—search query generation. The chatbot needs to generate an optimal set of search queries to use for retrieval.

There are different possible approaches to this. In this example, we'll take a [tool use](/v2/docs/tool-use) approach.

Here, we build a tool that takes a user query and returns a list of relevant document snippets for that query. The tool can generate zero, one or multiple search queries depending on the user query.

```python PYTHON
def generate_search_queries(message: str) -> List[str]:

    # Define the query generation tool
    query_gen_tool = [
        {
            "type": "function",
            "function": {
                "name": "internet_search",
                "description": "Returns a list of relevant document snippets for a textual query retrieved from the internet",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "queries": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "a list of queries to search the internet with.",
                        }
                    },
                    "required": ["queries"],
                },
            },
        }
    ]

    # Define a system instruction to optimize search query generation
    instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

    # Generate search queries (if any)
    search_queries = []

    res = co.chat(
        model="command-a-03-2025",
        messages=[
            {"role": "system", "content": instructions},
            {"role": "user", "content": message},
        ],
        tools=query_gen_tool,
    )

    if res.message.tool_calls:
        for tc in res.message.tool_calls:
            queries = json.loads(tc.function.arguments)["queries"]
            search_queries.extend(queries)

    return search_queries
```

In the example above, the tool breaks down the user message into two separate queries.

```python PYTHON
query = "How to stay connected with the company, and do you organize team events?"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```

```
['how to stay connected with the company', 'does the company organize team events']
```

And in the example below, the tool decides that one query is sufficient.

```python PYTHON
query = "How flexible are the working hours"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```

```
['how flexible are the working hours at the company']
```

And in the example below, the tool decides that no retrieval is needed to answer the query.

```python PYTHON
query = "What is 2 + 2"
queries_for_search = generate_search_queries(query)
print(queries_for_search)
```

```
[]
```

## Retrieval with Embed

Given the search query, we need a way to retrieve the most relevant documents from a large collection of documents.

This is where we can leverage text embeddings through the Embed endpoint. It enables semantic search, which lets us to compare the semantic meaning of the documents and the query. It solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles at capturing the context or meaning of a piece of text.

The Embed endpoint takes in texts as input and returns embeddings as output.

First, we need to embed the documents to search from. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents (instead of the query) for search
* `texts`: The list of texts (the FAQs)

```python PYTHON
# Define the documents
faqs_long = [
    {
        "data": {
            "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
        }
    },
    {
        "data": {
            "text": "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."
        }
    },
    {
        "data": {
            "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
        }
    },
    {
        "data": {
            "text": "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed."
        }
    },
    {
        "data": {
            "text": "Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business."
        }
    },
    {
        "data": {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        }
    },
    {
        "data": {
            "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
        }
    },
    {
        "data": {
            "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
        }
    },
    {
        "data": {
            "text": "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year."
        }
    },
    {
        "data": {
            "text": "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead."
        }
    },
]

# Embed the documents
doc_emb = co.embed(
    model="embed-v4.0",
    input_type="search_document",
    texts=[doc["data"]["text"] for doc in faqs_long],
    embedding_types=["float"],
).embeddings.float
```

Next, we add a query, which asks about how to get to know the team.

We choose `search_query` as the `input_type` to ensure the model treats this as the query (instead of the documents) for search.

```python PYTHON
# Add the user query
query = "How to get to know my teammates"

# Generate the search query
# Note: For simplicity, we are assuming only one query generated. For actual implementations, you will need to perform search for each query.
queries_for_search = generate_search_queries(query)[0]
print("Search query: ", queries_for_search)

# Embed the search query
query_emb = co.embed(
    model="embed-v4.0",
    input_type="search_query",
    texts=[queries_for_search],
    embedding_types=["float"],
).embeddings.float
```

```
Search query:  how to get to know teammates
```

Now, we want to search for the most relevant documents to the query. For this, we make use of the `numpy` library to compute the similarity between each query-document pair using the dot product approach.

Each query-document pair returns a score, which represents how similar the pair are. We then sort these scores in descending order and select the top most similar pairs, which we choose 5 (this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.

```python PYTHON
# Compute dot product similarity and display results
n = 5
scores = np.dot(query_emb, np.transpose(doc_emb))[0]
max_idx = np.argsort(-scores)[:n]

retrieved_documents = [faqs_long[item] for item in max_idx]

for rank, idx in enumerate(max_idx):
    print(f"Rank: {rank+1}")
    print(f"Score: {scores[idx]}")
    print(f"Document: {retrieved_documents[rank]}\n")
```

```
Rank: 1
Score: 0.34212792245283796
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}

Rank: 2
Score: 0.2883222063024371
Document: {'data': {'text': 'Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead.'}}

Rank: 3
Score: 0.278128283997032
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 4
Score: 0.19474858706643985
Document: {'data': {'text': "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee."}}

Rank: 5
Score: 0.13713692506528824
Document: {'data': {'text': 'Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business.'}}
```

Reranking can boost the results from semantic or lexical search further. The Rerank endpoint takes a list of search results and reranks them according to the most relevant documents to a query. This requires just a single line of code to implement.

We call the endpoint using `co.rerank()` and pass the following arguments:

* `query`: The user query
* `documents`: The list of documents we get from the semantic search results
* `top_n`: The top reranked documents to select
* `model`: We choose Rerank English 3

Looking at the results, we see that the given a query about getting to know the team, the document that talks about joining Slack channels is now ranked higher (1st) compared to earlier (3rd).

Here we select `top_n` to be 2, which will be the documents we will pass next for response generation.

```python PYTHON
# Rerank the documents
results = co.rerank(
    query=queries_for_search,
    documents=[doc["data"]["text"] for doc in retrieved_documents],
    top_n=2,
    model="rerank-english-v3.0",
)

# Display the reranking results
for idx, result in enumerate(results.results):
    print(f"Rank: {idx+1}")
    print(f"Score: {result.relevance_score}")
    print(f"Document: {retrieved_documents[result.index]}\n")

reranked_documents = [
    retrieved_documents[result.index] for result in results.results
]
```

```
Rank: 1
Score: 0.0020507434
Document: {'data': {'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'}}

Rank: 2
Score: 0.0014158706
Document: {'data': {'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'}}
```

Finally we reach the step that we saw in the earlier "Basic RAG" section.

To call the Chat API with RAG, we pass the following parameters. This tells the model to run in RAG-mode and use these documents in its response.

* `model` for the model ID
* `messages` for the user's query.
* `documents` for defining the documents.

The response is then generated based on the the query and the documents retrieved.

RAG introduces additional objects in the Chat response. One of them is `citations`, which contains details about:

* specific text spans from the retrieved documents on which the response is grounded.
* the documents referenced in the citations.

```python PYTHON
# Generate the response
response = co.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": query}],
    documents=reranked_documents,
)

# Display the response
print(response.message.content[0].text)

# Display the citations and source documents
if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```

```
You can get to know your teammates by joining relevant Slack channels and engaging in team-building activities. These activities include monthly outings and weekly game nights. You are also welcome to suggest new activity ideas.

CITATIONS:
start=38 end=69 text='joining relevant Slack channels' sources=[DocumentSource(type='document', id='doc:0', document={'id': 'doc:0', 'text': 'Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.'})] 

start=86 end=111 text='team-building activities.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 

start=137 end=176 text='monthly outings and weekly game nights.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 

start=201 end=228 text='suggest new activity ideas.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!'})] 
```

## Conclusion

In this tutorial, you learned about:

* How to get started with RAG
* How to generate search queries
* How to perform retrieval with Embed
* How to perform reranking with Rerank
* How to generate response and citations

RAG is great for building applications that can *answer questions* by grounding the response in external documents. But you can unlock the ability to not just answer questions, but also *automate tasks*. This can be done using a technique called tool use.

In Part 7, you will learn how to leverage [tool use](/v2/docs/building-an-agent-with-cohere) to automate tasks and workflows.


# Building a Generative AI Agent with Cohere

> This page describes building a generative-AI powered agent with Cohere.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/getting-started/v2/tutorial_pt7_v2.ipynb">
  Open in Colab
</a>

Tool use extends the ideas from [RAG](/v2/docs/rag-with-cohere), where external systems are used to guide the response of an LLM, but by leveraging a much bigger set of tools than what’s possible with RAG. The concept of tool use leverages LLMs' useful feature of being able to act as a reasoning and decision-making engine.

While RAG enables applications that can *answer questions*, tool use enables those that can *automate tasks*.

Tool use also enables developers to build agentic applications that can take actions, that is, doing both read and write operations on an external system.

In this tutorial, you'll learn about:

* Creating tools
* Tool planning and calling
* Tool execution
* Response and citation generation
* Multi-step tool use

You'll learn these by building an onboarding assistant for new hires.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
# pip install cohere

import cohere
import json

# Get your free API key: https://dashboard.cohere.com/api-keys
co = cohere.ClientV2(api_key="COHERE_API_KEY")
```

## Creating tools

The pre-requisite, before we can run a tool use workflow, is to set up the tools. Let's create three tools:

* `search_faqs`: A tool for searching the FAQs. For simplicity, we'll not implement any retrieval logic, but we'll simply pass a list of pre-defined documents, which are the FAQ documents we had used in the Text Embeddings section.
* `search_emails`: A tool for searching the emails. Same as above, we'll simply pass a list of pre-defined emails from the Reranking section.
* `create_calendar_event`: A tool for creating new calendar events. Again, for simplicity, we'll not implement actual event bookings, but will return a mock success event. In practice, we can connect to a calendar service API and implement all the necessary logic here.

Here, we are defining a Python function for each tool, but more broadly, the tool can be any function or service that can receive and send objects.

```python PYTHON
# Create the tools
def search_faqs(query):
    faqs = [
        {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        },
        {
            "text": "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours."
        },
    ]
    return faqs


def search_emails(query):
    emails = [
        {
            "from": "it@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "Setting Up Your IT Needs",
            "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.",
        },
        {
            "from": "john@co1t.com",
            "to": "david@co1t.com",
            "date": "2024-06-24",
            "subject": "First Week Check-In",
            "text": "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!",
        },
    ]
    return emails


def create_calendar_event(date: str, time: str, duration: int):
    # You can implement any logic here
    return {
        "is_success": True,
        "message": f"Created a {duration} hour long event at {time} on {date}",
    }


functions_map = {
    "search_faqs": search_faqs,
    "search_emails": search_emails,
    "create_calendar_event": create_calendar_event,
}
```

The second and final setup step is to define the tool schemas in a format that can be passed to the Chat endpoint. The schema must contain the following fields: `name`, `description`, and `parameters` in the format shown below.

This schema informs the LLM about what the tool does, and the LLM decides whether to use a particular tool based on it. Therefore, the more descriptive and specific the schema, the more likely the LLM will make the right tool call decisions.

Further reading:

* [Documentation on parameter types in tool use](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use)

```python PYTHON
# Define the tools
tools = [
    {
        "type": "function",
        "function": {
            "name": "search_faqs",
            "description": "Given a user query, searches a company's frequently asked questions (FAQs) list and returns the most relevant matches to the query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query from the user",
                    }
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "search_emails",
            "description": "Given a user query, searches a person's emails and returns the most relevant matches to the query.",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "The query from the user",
                    }
                },
                "required": ["query"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "create_calendar_event",
            "description": "Creates a new calendar event of the specified duration at the specified time and date. A new event cannot be created on the same time as an existing event.",
            "parameters": {
                "type": "object",
                "properties": {
                    "date": {
                        "type": "string",
                        "description": "the date on which the event starts, formatted as mm/dd/yy",
                    },
                    "time": {
                        "type": "string",
                        "description": "the time of the event, formatted using 24h military time formatting",
                    },
                    "duration": {
                        "type": "number",
                        "description": "the number of hours the event lasts for",
                    },
                },
                "required": ["date", "time", "duration"],
            },
        },
    },
]
```

## Tool planning and calling

We can now run the tool use workflow. We can think of a tool use system as consisting of four components:

* The user
* The application
* The LLM
* The tools

At its most basic, these four components interact in a workflow through four steps:

* **Step 1: Get user message** – The LLM gets the user message (via the application)
* **Step 2: Tool planning and calling** – The LLM makes a decision on the tools to call (if any) and generates - the tool calls
* **Step 3: Tool execution** - The application executes the tools and the results are sent to the LLM
* **Step 4: Response and citation generation** – The LLM generates the response and citations to back to the user

```python PYTHON
# Create custom system message
system_message = """## Task and Context
You are an assistant who assist new employees of Co1t with their first week. You respond to their questions and assist them with their needs. Today is Monday, June 24, 2024"""


# Step 1: Get user message
message = "Is there any message about getting setup with IT?"

# Add the system and user messages to the chat history
messages = [
    {"role": "system", "content": system_message},
    {"role": "user", "content": message},
]

# Step 2: Tool planning and calling
response = co.chat(
    model="command-a-03-2025", messages=messages, tools=tools
)

if response.message.tool_calls:
    print("Tool plan:")
    print(response.message.tool_plan, "\n")
    print("Tool calls:")
    for tc in response.message.tool_calls:
        print(
            f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
        )

    # Append tool calling details to the chat history
    messages.append(
        {
            "role": "assistant",
            "tool_calls": response.message.tool_calls,
            "tool_plan": response.message.tool_plan,
        }
    )
```

```
Tool plan:
I will search the user's emails for any messages about getting set up with IT. 

Tool calls:
Tool name: search_emails | Parameters: {"query":"IT setup"}
```

Given three tools to choose from, the model is able to pick the right tool (in this case, `search_emails`) based on what the user is asking for.

Also, notice that the model first generates a plan about what it should do ("I will do ...") before actually generating the tool call(s).

# Tool execution

```python PYTHON
# Step 3: Tool execution
for tc in response.message.tool_calls:
    tool_result = functions_map[tc.function.name](
        **json.loads(tc.function.arguments)
    )
    tool_content = []
    for data in tool_result:
        tool_content.append(
            {
                "type": "document",
                "document": {"data": json.dumps(data)},
            }
        )
        # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
    # Append tool results to the chat history
    messages.append(
        {
            "role": "tool",
            "tool_call_id": tc.id,
            "content": tool_content,
        }
    )

    print("Tool results:")
    for result in tool_content:
        print(result)
```

```
Tool results:
{'type': 'document', 'document': {'data': '{"from": "it@co1t.com", "to": "david@co1t.com", "date": "2024-06-24", "subject": "Setting Up Your IT Needs", "text": "Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts."}'}}
{'type': 'document', 'document': {'data': '{"from": "john@co1t.com", "to": "david@co1t.com", "date": "2024-06-24", "subject": "First Week Check-In", "text": "Hello! I hope you\'re settling in well. Let\'s connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon\\u2014it\'s a great opportunity to get to know your colleagues!"}'}}
```

## Response and citation generation

```python PYTHON
# Step 4: Response and citation generation
response = co.chat(
    model="command-a-03-2025", messages=messages, tools=tools
)

# Append assistant response to the chat history
messages.append(
    {"role": "assistant", "content": response.message.content[0].text}
)

# Print final response
print("Response:")
print(response.message.content[0].text)
print("=" * 50)

# Print citations (if any)
if response.message.citations:
    print("\nCITATIONS:")
    for citation in response.message.citations:
        print(citation, "\n")
```

```
Response:
Yes, there is an email from it@co1t.com with the subject 'Setting Up Your IT Needs'. It includes an attached guide to help you set up your work accounts.
==================================================

CITATIONS:
start=17 end=83 text="email from it@co1t.com with the subject 'Setting Up Your IT Needs'" sources=[ToolSource(type='tool', id='search_emails_wqs498sp2d07:0', tool_output={'date': '2024-06-24', 'from': 'it@co1t.com', 'subject': 'Setting Up Your IT Needs', 'text': 'Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.', 'to': 'david@co1t.com'})] 

start=100 end=153 text='attached guide to help you set up your work accounts.' sources=[ToolSource(type='tool', id='search_emails_wqs498sp2d07:0', tool_output={'date': '2024-06-24', 'from': 'it@co1t.com', 'subject': 'Setting Up Your IT Needs', 'text': 'Greetings! To ensure a seamless start, please refer to the attached comprehensive guide, which will assist you in setting up all your work accounts.', 'to': 'david@co1t.com'})] 
```

# Multi-step tool use

The model can execute more complex tasks in tool use – tasks that require tool calls to happen in a sequence. This is referred to as "multi-step" tool use.

Let's create a function to called `run_assistant` to implement these steps, and along the way, print out the key events and messages. Optionally, this function also accepts the chat history as an argument to keep the state in a multi-turn conversation.

```python PYTHON
model = "command-a-03-2025"

system_message = """## Task and Context
You are an assistant who assists new employees of Co1t with their first week. You respond to their questions and assist them with their needs. Today is Monday, June 24, 2024"""


def run_assistant(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message
    print(f"Question:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)
    response = co.chat(model=model, messages=messages, tools=tools)

    while response.message.tool_calls:

        print("Tool plan:")
        print(response.message.tool_plan, "\n")
        print("Tool calls:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results
        for idx, tc in enumerate(response.message.tool_calls):
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations
        response = co.chat(
            model=model, messages=messages, tools=tools
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response
    print("Response:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)
    if response.message.citations:
        print("\nCITATIONS:")
        for citation in response.message.citations:
            print(citation, "\n")

    return messages
```

To illustrate the concept of multi-step tool user, let's ask the assistant to block time for any lunch invites received in the email.

This requires tasks to happen over multiple steps in a sequence. Here, we see the assistant running these steps:

* First, it calls the `search_emails` tool to find any lunch invites, which it found one.
* Next, it calls the `create_calendar_event` tool to create an event to block the person's calendar on the day mentioned by the email.

This is also an example of tool use enabling a write operation instead of just a read operation that we saw with RAG.

```python PYTHON
messages = run_assistant(
    "Can you check if there are any lunch invites, and for those days, create a one-hour event on my calendar at 12PM."
)
```

```
Question:
Can you check if there are any lunch invites, and for those days, create a one-hour event on my calendar at 12PM.
==================================================
Tool plan:
I will first search the user's emails for lunch invites. Then, I will create a one-hour event on the user's calendar at 12PM for each day that the user has a lunch invite. 

Tool calls:
Tool name: search_emails | Parameters: {"query":"lunch invites"}
==================================================
Tool plan:
I have found one lunch invite for Thursday at noon. I will now create a one-hour event on the user's calendar for Thursday at noon. 

Tool calls:
Tool name: create_calendar_event | Parameters: {"date":"06/27/24","duration":1,"time":"12:00"}
==================================================
Response:
I found one lunch invite for Thursday, June 27, 2024. I have created a one-hour event on your calendar for that day at 12pm.
==================================================

CITATIONS:
start=29 end=53 text='Thursday, June 27, 2024.' sources=[ToolSource(type='tool', id='search_emails_1dxqzwragh9g:1', tool_output={'date': '2024-06-24', 'from': 'john@co1t.com', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!", 'to': 'david@co1t.com'})] 

start=71 end=85 text='one-hour event' sources=[ToolSource(type='tool', id='create_calendar_event_w11caj6hmqz2:0', tool_output={'content': '"is_success"'})] 

start=119 end=124 text='12pm.' sources=[ToolSource(type='tool', id='search_emails_1dxqzwragh9g:1', tool_output={'date': '2024-06-24', 'from': 'john@co1t.com', 'subject': 'First Week Check-In', 'text': "Hello! I hope you're settling in well. Let's connect briefly tomorrow to discuss how your first week has been going. Also, make sure to join us for a welcoming lunch this Thursday at noon—it's a great opportunity to get to know your colleagues!", 'to': 'david@co1t.com'})] 
```

In this tutorial, you learned about:

* How to create tools
* How tool planning and calling happens
* How tool execution happens
* How to generate the response and citations
* How to run tool use in a multi-step scenario

And that concludes our 7-part Cohere tutorial. We hope that they have provided you with a foundational understanding of the Cohere API, the available models and endpoints, and the types of use cases that you can build with them.

To continue your learning, check out:

* [LLM University - A range of courses and step-by-step guides to help you start building](https://cohere.com/llmu)
* [Cookbooks - A collection of basic to advanced example applications](https://docs.cohere.com/page/cookbooks)
* [Cohere's documentation](https://docs.cohere.com/docs/the-cohere-platform)
* [The Cohere API reference](https://docs.cohere.com/reference/about)


# Building Agentic RAG with Cohere

> Hands-on tutorials on building agentic RAG applications with Cohere

<img src="file:e459d747-5330-4663-b9af-925a88fcfeba" alt="agentic rag" />

Welcome to the tutorial on Agentic RAG with Cohere!

[Retrieval Augmented Generation](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) (RAG) is a technique that gives LLMs the capability to ground their responses in external text data, making the response more accurate and less prone to hallucinations.

However, a standard RAG implementation struggles on more complex type of tasks, such as:

* When it has to search over diverse set of sources
* When the question requires sequential reasoning
* When the question has multiple parts
* When it requires comparing multiple documents
* When it requires analyzing structured data

In an enterprise setting where data sources are diverse with non-homogeneous formats this approach becomes even more important. For example, the data sources could be a mix of structured, semi-structured and unstructured data.

This is where agentic RAG comes into play, and in this tutorial, we'll see how agentic RAG can solve these type of tasks.

Concretely, this is achieved using the tool use approach. Tool use allows for greater flexibility in accessing and utilizing data sources, thus unlocking new use cases not possible with a standard RAG approach.

This tutorial is split into six parts, with each part focusing on one use case:

* [Part 1: Routing queries to data sources](/v2/docs/routing-queries-to-data-sources)
  * Getting started with agentic RAG
  * Setting up the tools
  * Running an agentic RAG workflow
  * Routing queries to tools
* [Part 2: Generating parallel queries](/v2/docs/generating-parallel-queries)
  * Query expansion
  * Query expansion over multiple data sources
  * Query expansion in multi-turn conversations
* [Part 3: Performing tasks sequentially](/v2/docs/performing-tasks-sequentially)
  * Multi-step tool calling
  * Multi-step, parallel tool calling
  * Self-correction
* [Part 4: Generating multi-faceted queries](/v2/docs/generating-multi-faceted-queries)
  * Multi-faceted data querying
  * Setting up the tool to generate multi-faceted queries
  * Performing multi-faceted queries
* [Part 5: Querying structured data (tables)](/v2/docs/querying-structured-data-tables)
  * Python tool for querying tabular data
  * Setting up the tool to generate pandas queries
  * Performing queries over structured data (table)
* [Part 6: Querying structured data (databases)](/v2/docs/querying-structured-data-sql)
  * Setting up a database
  * Setting up the tool to generate SQL queries
  * Performing queries over structured data (SQL)


# Routing Queries to Data Sources

> Build an agentic RAG system that routes queries to the most relevant tools based on the query's nature.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt1_routing.ipynb">
  Open in Colab
</a>

Imagine a RAG system that can search over diverse sources, such as a website, a database, and a set of documents.

In a standard RAG setting, the application would aggregate retrieved documents from all the different sources it is connected to. This may contribute to noise from less relevant documents.

Additionally, it doesn’t take into consideration that, given a data source's nature, it might be less or more relevant to a query than the other data sources.

An agentic RAG system can solve this problem by routing queries to the most relevant tools based on the query's nature. This is done by leveraging the tool use capabilities of the Chat endpoint.

In this tutorial, we'll cover:

* Setting up the tools
* Running an agentic RAG workflow
* Routing queries to tools

We'll build an agent that can answer questions about using Cohere, equipped with a number of different tools.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

We also need to import the tool definitions that we'll use in this tutorial.

<Note>
   Important: the source code for tool definitions can be 

  [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py)

  . Make sure to have the 

  `tool_def.py`

   file in the same directory as this notebook for the imports to work correctly. 
</Note>

```python PYTHON
! pip install cohere langchain langchain-community pydantic -qq
```

```python PYTHON
import json
import os
import cohere

from tool_def import (
    search_developer_docs,
    search_developer_docs_tool,
    search_internet,
    search_internet_tool,
    search_code_examples,
    search_code_examples_tool,
)

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

os.environ["TAVILY_API_KEY"] = (
    "TAVILY_API_KEY"  # We'll need the Tavily API key to perform internet search. Get your API key: https://app.tavily.com/home
)
```

## Setting up the tools

In an agentic RAG system, each data source is represented as a tool. A tool is broadly any function or service that can receive and send objects to the LLM. But in the case of RAG, this becomes a more specific case of a tool that takes a query as input and returns a set of documents.

Here, we are defining a Python function for each tool, but more broadly, the tool can be any function or service that can receive and send objects.

* `search_developer_docs`: Searches Cohere developer documentation. Here we are creating a small list of sample documents for simplicity and will return the same list for every query. In practice, you will want to implement a search function such as those that use semantic search.
* `search_internet`: Performs an internet search using Tavily search, which we take from LangChain's ready implementation.
* `search_code_examples`: Searches for Cohere code examples and tutorials. Here we are also creating a small list of sample documents for simplicity.

These functions are mapped to a dictionary called `functions_map` for easy access.

Here, we are defining a Python function for each tool.

Further reading:

* [Documentation on parameter types in tool use](https://docs.cohere.com/v2/docs/parameter-types-in-tool-use)

```python PYTHON
functions_map = {
    "search_developer_docs": search_developer_docs,
    "search_internet": search_internet,
    "search_code_examples": search_code_examples,
}
```

The second and final setup step is to define the tool schemas in a format that can be passed to the Chat endpoint. A tool schema must contain the following fields: `name`, `description`, and `parameters` in the format shown below.

This schema informs the LLM about what the tool does, which enables an LLM to decide whether to use a particular tool. Therefore, the more descriptive and specific the schema, the more likely the LLM will make the right tool call decisions.

## Running an agentic RAG workflow

We can now run an agentic RAG workflow using a tool use approach. We can think of the system as consisting of four components:

* The user
* The application
* The LLM
* The tools

At its most basic, these four components interact in a workflow through four steps:

* **Step 1: Get user message** – The LLM gets the user message (via the application)
* **Step 2: Tool planning and calling** – The LLM makes a decision on the tools to call (if any) and generates the tool calls
* **Step 3: Tool execution** - The application executes the tools and sends the results to the LLM
* **Step 4: Response and citation generation** – The LLM generates the response and citations to back to the user

We wrap all these steps in a function called `run_agent`.

```python PYTHON
tools = [
    search_developer_docs_tool,
    search_internet_tool,
    search_code_examples_tool,
]
```

```python PYTHON
system_message = """## Task and Context
You are an assistant who helps developers use Cohere. You are equipped with a number of tools that can provide different types of information. If you can't find the information you need from one tool, you should try other tools if there is a possibility that they could provide the information you need."""
```

```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message
    print(f"QUESTION:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)
    response = co.chat(
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results
        for tc in response.message.tool_calls:
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations
        response = co.chat(
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.3,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response
    print("RESPONSE:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)
    verbose_source = (
        False  # Change to True to display the contents of a source
    )
    if response.message.citations:
        print("CITATIONS:\n")
        for citation in response.message.citations:
            print(
                f"Start: {citation.start}| End:{citation.end}| Text:'{citation.text}' "
            )
            print("Sources:")
            for idx, source in enumerate(citation.sources):
                print(f"{idx+1}. {source.id}")
                if verbose_source:
                    print(f"{source.tool_output}")
            print("\n")

    return messages
```

## Routing queries to tools

Let's ask the agent a few questions, starting with this one about the Embed endpoint.

Because the question asks about a specific feature, the agent decides to use the `search_developer_docs` tool (instead of retrieving from all the data sources it's connected to).

It first generates a tool plan that describes how it will handle the query. Then, it generates tool calls to the `search_developer_docs` tool with the associated `query` parameter.

The tool does indeed contain the information asked by the user, which the agent then uses to generate its response.

```python PYTHON
messages = run_agent("How many languages does Embed support?")
```

```mdx
QUESTION:
How many languages does Embed support?
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for 'how many languages does Embed support'. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"how many languages does Embed support"}
==================================================
RESPONSE:
The Embed endpoint supports over 100 languages.
==================================================
CITATIONS:

Start: 28| End:47| Text:'over 100 languages.' 
Sources:
1. search_developer_docs_gwt5g55gjc3w:2
```

Let's now ask the agent a question about setting up the Notion API so we can connect it to LLMs. This information is not likely to be found in the developer documentation or code examples because it is not Cohere-specific, so we can expect the agent to use the internet search tool.

And this is exactly what the agent does. This time, it decides to use the `search_internet` tool, triggers the search through Tavily search, and uses the results to generate its response.

```python PYTHON
messages = run_agent("How to set up the Notion API.")
```

```mdx
QUESTION:
How to set up the Notion API.
==================================================
TOOL PLAN:
I will search for 'Notion API setup' to find out how to set up the Notion API. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"Notion API setup"}
==================================================
RESPONSE:
To set up the Notion API, you need to create a new integration in Notion's integrations dashboard. You can do this by navigating to https://www.notion.com/my-integrations and clicking '+ New integration'.

Once you've done this, you'll need to get your API secret by visiting the Configuration tab. You should keep your API secret just that – a secret! You can refresh your secret if you accidentally expose it.

Next, you'll need to give your integration page permissions. To do this, you'll need to pick or create a Notion page, then click on the ... More menu in the top-right corner of the page. Scroll down to + Add Connections, then search for your integration and select it. You'll then need to confirm the integration can access the page and all of its child pages.

If your API requests are failing, you should confirm you have given the integration permission to the page you are trying to update.

You can also create a Notion API integration and get your internal integration token. You'll then need to create a .env file and add environmental variables, get your Notion database ID and add your integration to your database.

For more information on what you can build with Notion's API, you can refer to this guide.
==================================================
CITATIONS:

Start: 38| End:62| Text:'create a new integration' 
Sources:
1. search_internet_cwabyfc5mn8c:0
2. search_internet_cwabyfc5mn8c:2


Start: 75| End:98| Text:'integrations dashboard.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 132| End:170| Text:'https://www.notion.com/my-integrations' 
Sources:
1. search_internet_cwabyfc5mn8c:0


Start: 184| End:203| Text:''+ New integration'' 
Sources:
1. search_internet_cwabyfc5mn8c:0
2. search_internet_cwabyfc5mn8c:2


Start: 244| End:263| Text:'get your API secret' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 280| End:298| Text:'Configuration tab.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 310| End:351| Text:'keep your API secret just that – a secret' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 361| End:411| Text:'refresh your secret if you accidentally expose it.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 434| End:473| Text:'give your integration page permissions.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 501| End:529| Text:'pick or create a Notion page' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 536| End:599| Text:'click on the ... More menu in the top-right corner of the page.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 600| End:632| Text:'Scroll down to + Add Connections' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 639| End:681| Text:'search for your integration and select it.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 702| End:773| Text:'confirm the integration can access the page and all of its child pages.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 783| End:807| Text:'API requests are failing' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 820| End:907| Text:'confirm you have given the integration permission to the page you are trying to update.' 
Sources:
1. search_internet_cwabyfc5mn8c:2


Start: 922| End:953| Text:'create a Notion API integration' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 958| End:994| Text:'get your internal integration token.' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1015| End:1065| Text:'create a .env file and add environmental variables' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1067| End:1094| Text:'get your Notion database ID' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1099| End:1137| Text:'add your integration to your database.' 
Sources:
1. search_internet_cwabyfc5mn8c:1


Start: 1223| End:1229| Text:'guide.' 
Sources:
1. search_internet_cwabyfc5mn8c:3
```

Let's ask the agent a final question, this time about tutorials that are relevant for enterprises.

Again, the agent uses the context of the query to decide on the most relevant tool. In this case, it selects the `search_code_examples` tool and provides a response based on the information found.

```python PYTHON
messages = run_agent(
    "Any tutorials that are relevant for enterprises?"
)
```

```mdx

QUESTION:
Any tutorials that are relevant for enterprises?
==================================================
TOOL PLAN:
I will search for 'enterprise tutorials' in the code examples and tutorials tool. 

TOOL CALLS:
Tool name: search_code_examples | Parameters: {"query":"enterprise tutorials"}
==================================================
RESPONSE:
I found a tutorial called 'Advanced Document Parsing For Enterprises'.
==================================================
CITATIONS:

Start: 26| End:69| Text:''Advanced Document Parsing For Enterprises'' 
Sources:
1. search_code_examples_jhh40p32wxpw:4
```

## Summary

In this tutorial, we learned about:

* How to set up tools in an agentic RAG system
* How to run an agentic RAG workflow
* How to automatically route queries to the most relevant data sources

However, so far we have only seen rather simple queries. In practice, we may run into a complex query that needs to simplified, optimized, or split (etc.) before we can perform the retrieval.

In Part 2, we'll learn how to build an agentic RAG system that can expand user queries into parallel queries.


# Generate Parallel Queries for Better RAG Retrieval

> Build an agentic RAG system that can expand a user query into a more optimized set of queries for retrieval.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt2_parallel_queries.ipynb">
  Open in Colab
</a>

Compare two user queries to a RAG chatbot, "What was Apple's revenue in 2023?" and "What were Apple's and Google's revenue in 2023?".

The first query is straightforward as we can perform retrieval using pretty much the same query we get.

But the second query is more complex. We need to break it down into two separate queries, one for Apple and one for Google.

This is an example that requires query expansion. Here, the agentic RAG will need to transform the query into a more optimized set of queries it should use to perform the retrieval.

In this part, we'll learn how to create an agentic RAG system that can perform query expansion and then run those queries in parallel:

* Query expansion
* Query expansion over multiple data sources
* Query expansion in multi-turn conversations

We'll learn these by building an agent that answers questions about using Cohere.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

We also need to import the tool definitions that we'll use in this tutorial.

<Note>
   Important: the source code for tool definitions can be 

  [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py)

  . Make sure to have the 

  `tool_def.py`

   file in the same directory as this notebook for the imports to work correctly. 
</Note>

```python PYTHON
! pip install cohere langchain langchain-community pydantic -qq
```

```python PYTHON
import json
import os
import cohere

from tool_def import (
    search_developer_docs,
    search_developer_docs_tool,
    search_internet,
    search_internet_tool,
    search_code_examples,
    search_code_examples_tool,
)

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

os.environ["TAVILY_API_KEY"] = (
    "TAVILY_API_KEY"  # We'll need the Tavily API key to perform internet search. Get your API key: https://app.tavily.com/home
)
```

## Setting up the tools

We set up the same set of tools as in Part 1. If you want further details on how to set up the tools, check out Part 1.

```python PYTHON
functions_map = {
    "search_developer_docs": search_developer_docs,
    "search_internet": search_internet,
    "search_code_examples": search_code_examples,
}
```

## Running an agentic RAG workflow

We create a `run_agent` function to run the agentic RAG workflow, the same as in Part 1. If you want further details on how to set up the tools, check out Part 1.

```python PYTHON
tools = [
    search_developer_docs_tool,
    search_internet_tool,
    search_code_examples_tool,
]
```

```python PYTHON
system_message = """## Task and Context
You are an assistant who helps developers use Cohere. You are equipped with a number of tools that can provide different types of information. If you can't find the information you need from one tool, you should try other tools if there is a possibility that they could provide the information you need."""
```

```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message
    print(f"QUESTION:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)
    response = co.chat(
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results
        for tc in response.message.tool_calls:
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations
        response = co.chat(
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.3,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response
    print("RESPONSE:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)
    verbose_source = (
        False  # Change to True to display the contents of a source
    )
    if response.message.citations:
        print("CITATIONS:\n")
        for citation in response.message.citations:
            print(
                f"Start: {citation.start}| End:{citation.end}| Text:'{citation.text}' "
            )
            print("Sources:")
            for idx, source in enumerate(citation.sources):
                print(f"{idx+1}. {source.id}")
                if verbose_source:
                    print(f"{source.tool_output}")
            print("\n")

    return messages
```

## Query expansion

Let's ask the agent a few questions, starting with this one about the Chat endpoint and the RAG feature.

Firstly, the agent rightly chooses the `search_developer_docs` tool to retrieve the information it needs.

Additionally, because the question asks about two different things, retrieving information using the same query as the user's may not be the optimal approach. Instead, the query needs to be expanded or split into multiple parts, each retrieving its own set of documents.

Thus, the agent expands the original query into two queries.

This is enabled by the parallel tool calling feature that comes with the Chat endpoint.

This results in a richer and more representative list of documents retrieved, and therefore a more accurate and comprehensive answer.

```python PYTHON
messages = run_agent("Explain the Chat endpoint and the RAG feature")
```

```mdx

QUESTION:
Explain the Chat endpoint and the RAG feature
==================================================
TOOL PLAN:
I will search the Cohere developer documentation for the Chat endpoint and the RAG feature. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"Chat endpoint"}
Tool name: search_developer_docs | Parameters: {"query":"RAG feature"}
==================================================
RESPONSE:
The Chat endpoint facilitates a conversational interface, allowing users to send messages to the model and receive text responses.

Retrieval Augmented Generation (RAG) is a method for generating text using additional information fetched from an external data source, which can greatly increase the accuracy of the response.
==================================================
CITATIONS:

Start: 18| End:56| Text:'facilitates a conversational interface' 
Sources:
1. search_developer_docs_c059cbhr042g:3
2. search_developer_docs_beycjq0ejbvx:3


Start: 58| End:130| Text:'allowing users to send messages to the model and receive text responses.' 
Sources:
1. search_developer_docs_c059cbhr042g:3
2. search_developer_docs_beycjq0ejbvx:3


Start: 132| End:162| Text:'Retrieval Augmented Generation' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4


Start: 174| End:266| Text:'method for generating text using additional information fetched from an external data source' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4


Start: 278| End:324| Text:'greatly increase the accuracy of the response.' 
Sources:
1. search_developer_docs_c059cbhr042g:4
2. search_developer_docs_beycjq0ejbvx:4
```

## Query expansion over multiple data sources

The earlier example focused on a single data source, the Cohere developer documentation. However, the agentic RAG can also perform query expansion over multiple data sources.

Here, the agent is asked a question that contains two parts: first asking for an explanation of the Embed endpoint and then asking for code examples.

It correctly identifies that this requires both searching the developer documentation and the code examples. Thus, it generates two queries, one for each data source, and performs two separate searches in parallel.

Its response then contains information referenced from both data sources.

```python PYTHON
messages = run_agent(
    "What is the Embed endpoint? Give me some code tutorials"
)
```

```mdx

QUESTION:
What is the Embed endpoint? Give me some code tutorials
==================================================
TOOL PLAN:
I will search for 'what is the Embed endpoint' and 'Embed endpoint code tutorials' at the same time. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"what is the Embed endpoint"}
Tool name: search_code_examples | Parameters: {"query":"Embed endpoint code tutorials"}
==================================================
RESPONSE:
The Embed endpoint returns text embeddings. An embedding is a list of floating point numbers that captures semantic information about the text that it represents.

I'm afraid I couldn't find any code tutorials for the Embed endpoint.
==================================================
CITATIONS:

Start: 19| End:43| Text:'returns text embeddings.' 
Sources:
1. search_developer_docs_pgzdgqd3k0sd:1


Start: 62| End:162| Text:'list of floating point numbers that captures semantic information about the text that it represents.' 
Sources:
1. search_developer_docs_pgzdgqd3k0sd:1
```

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
```

## Summary

In this tutorial, we learned about:

* How query expansion works in an agentic RAG system
* How query expansion works over multiple data sources
* How query expansion works in multi-turn conversations

Having said that, we may encounter even more complex queries than what we've seen so far. In particular, some queries require sequential reasoning where the retrieval needs to happen over multiple steps.

In Part 3, we'll learn how the agentic RAG system can perform sequential reasoning.


# Performing Tasks Sequentially with Cohere's RAG

> Build an agentic RAG system that can handle user queries that require tasks to be performed in a sequence.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt3_sequential.ipynb">
  Open in Colab
</a>

Compare two user queries to a RAG chatbot, "What was Apple's revenue in 2023?" and "What was the revenue of the most valuable company in the US in 2023?".

While the first query is straightforward to handle, the second query requires breaking down into two steps:

1. Identify the most valuable company in the US in 2023
2. Get the revenue of the company in 2023

These steps need to happen in a sequence rather than all at once. This is because the information retrieved from the first step is required to inform the second step.

This is an example of sequential reasoning. In this tutorial, we'll learn how agentic RAG with Cohere handles sequential reasoning, and in particular:

* Multi-step tool calling
* Multi-step, parallel tool calling
* Self-correction

We'll learn these by building an agent that answers questions about using Cohere.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

We also need to import the tool definitions that we'll use in this tutorial.

<Note>
   Important: the source code for tool definitions can be 

  [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py)

  . Make sure to have the 

  `tool_def.py`

   file in the same directory as this notebook for the imports to work correctly. 
</Note>

```python PYTHON
! pip install cohere langchain langchain-community pydantic -qq
```

```python PYTHON
import json
import os
import cohere

from tool_def import (
    search_developer_docs,
    search_developer_docs_tool,
    search_internet,
    search_internet_tool,
    search_code_examples,
    search_code_examples_tool,
)

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

os.environ["TAVILY_API_KEY"] = (
    "TAVILY_API_KEY"  # We'll need the Tavily API key to perform internet search. Get your API key: https://app.tavily.com/home
)
```

## Setting up the tools

We set up the same set of tools as in Part 1. If you want further details on how to set up the tools, check out Part 1.

```python PYTHON
functions_map = {
    "search_developer_docs": search_developer_docs,
    "search_internet": search_internet,
    "search_code_examples": search_code_examples,
}
```

## Running an agentic RAG workflow

We create a `run_agent` function to run the agentic RAG workflow, the same as in Part 1. If you want further details on how to set up the tools, check out Part 1.

```python PYTHON
tools = [
    search_developer_docs_tool,
    search_internet_tool,
    search_code_examples_tool,
]
```

```python PYTHON
system_message = """## Task and Context
You are an assistant who helps developers use Cohere. You are equipped with a number of tools that can provide different types of information. If you can't find the information you need from one tool, you should try other tools if there is a possibility that they could provide the information you need."""
```

```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message
    print(f"QUESTION:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)
    response = co.chat(
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results
        for tc in response.message.tool_calls:
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations
        response = co.chat(
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.3,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response
    print("RESPONSE:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)
    verbose_source = (
        False  # Change to True to display the contents of a source
    )
    if response.message.citations:
        print("CITATIONS:\n")
        for citation in response.message.citations:
            print(
                f"Start: {citation.start}| End:{citation.end}| Text:'{citation.text}' "
            )
            print("Sources:")
            for idx, source in enumerate(citation.sources):
                print(f"{idx+1}. {source.id}")
                if verbose_source:
                    print(f"{source.tool_output}")
            print("\n")

    return messages
```

## Multi-step tool calling

Let's ask the agent a few questions, starting with this one about a specific feature. The user is asking about two things: a feature to reorder search results and code examples for that feature.

In this case, the agent first needs to identify what that feature is before it can answer the second part of the question.

This is reflected in the agent's tool plan, which describes the steps it will take to answer the question.

So, it first calls the `search_developer_docs` tool to find the feature.

It then discovers that the feature is Rerank. Using this information, it calls the `search_code_examples` tool to find code examples for that feature.

Finally, it uses the retrieved information to answer both parts of the user's question.

```python PYTHON
messages = run_agent(
    "What's the Cohere feature to reorder search results? Do you have any code examples on that?"
)
```

```mdx
QUESTION:
What's the Cohere feature to reorder search results? Do you have any code examples on that?
==================================================
TOOL PLAN:
I will search for the Cohere feature to reorder search results. Then I will search for code examples on that. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"reorder search results"}
==================================================
TOOL PLAN:
I found that the Rerank endpoint is the feature that reorders search results. I will now search for code examples on that. 

TOOL CALLS:
Tool name: search_code_examples | Parameters: {"query":"rerank endpoint"}
==================================================
RESPONSE:
The Rerank endpoint is the feature that reorders search results. Unfortunately, I could not find any code examples on that.
==================================================
CITATIONS:

Start: 4| End:19| Text:'Rerank endpoint' 
Sources:
1. search_developer_docs_53tfk9zgwgzt:0
```

## Multi-step, parallel tool calling

In Part 2, we saw how the Cohere API supports parallel tool calling, and in this tutorial, we looked at sequential tool calling. That also means that both scenarios can happen at the same time.

Here's an example. Suppose we ask the agent to find the CEOs of the companies with the top 3 highest market capitalization.

In the first step, it searches the Internet for information about the 3 companies with the highest market capitalization.

And in the second step, it performs parallel searches for the CEOs of the 3 identified companies.

```python PYTHON
messages = run_agent(
    "Who are the CEOs of the companies with the top 3 highest market capitalization."
)
```

```mdx
QUESTION:
Who are the CEOs of the companies with the top 3 highest market capitalization.
==================================================
TOOL PLAN:
I will search for the top 3 companies with the highest market capitalization. Then, I will search for the CEOs of those companies. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"top 3 companies with highest market capitalization"}
==================================================
TOOL PLAN:
The top 3 companies with the highest market capitalization are Apple, Microsoft, and Nvidia. I will now search for the CEOs of these companies. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"Apple CEO"}
Tool name: search_internet | Parameters: {"query":"Microsoft CEO"}
Tool name: search_internet | Parameters: {"query":"Nvidia CEO"}
==================================================
RESPONSE:
The CEOs of the top 3 companies with the highest market capitalization are:
1. Tim Cook of Apple
2. Satya Nadella of Microsoft
3. Jensen Huang of Nvidia
==================================================
CITATIONS:

Start: 79| End:87| Text:'Tim Cook' 
Sources:
1. search_internet_0f8wyxfc3hmn:0
2. search_internet_0f8wyxfc3hmn:1
3. search_internet_0f8wyxfc3hmn:2


Start: 91| End:96| Text:'Apple' 
Sources:
1. search_internet_kb9qgs1ps69e:0


Start: 100| End:113| Text:'Satya Nadella' 
Sources:
1. search_internet_wy4mn7286a88:0
2. search_internet_wy4mn7286a88:1
3. search_internet_wy4mn7286a88:2


Start: 117| End:126| Text:'Microsoft' 
Sources:
1. search_internet_kb9qgs1ps69e:0


Start: 130| End:142| Text:'Jensen Huang' 
Sources:
1. search_internet_q9ahz81npfqz:0
2. search_internet_q9ahz81npfqz:1
3. search_internet_q9ahz81npfqz:2
4. search_internet_q9ahz81npfqz:3


Start: 146| End:152| Text:'Nvidia' 
Sources:
1. search_internet_kb9qgs1ps69e:0
```

## Self-correction

The concept of sequential reasoning is useful in a broader sense, particularly where the agent needs to adapt and change its plan midway in a task.

In other words, it allows the agent to self-correct.

To illustrate this, let's look at an example. Here, the user is asking about the authors of the sentence BERT paper.

The agent attempted to find required information via the `search_developer_docs` tool.

However, we know that the tool doesn't contain this information because we have only added a small sample of documents.

As a result, the agent, having received the documents back without any relevant information, decides to search the internet instead. This is also helped by the fact that we have added specific instructions in the `search_internet` tool to search the internet for information not found in the developer documentation.

It finally has the information it needs, and uses it to answer the user's question.

This highlights another important aspect of agentic RAG, which allows a RAG system to be flexible. This is achieved by powering the retrieval component with an LLM.

On the other hand, a standard RAG system would typically hand-engineer this, and hence, is more rigid.

```python PYTHON
messages = run_agent(
    "Who are the authors of the sentence BERT paper?"
)
```

```mdx
QUESTION:
Who are the authors of the sentence BERT paper?
==================================================
TOOL PLAN:
I will search for the authors of the sentence BERT paper. 

TOOL CALLS:
Tool name: search_developer_docs | Parameters: {"query":"authors of the sentence BERT paper"}
==================================================
TOOL PLAN:
I was unable to find any information about the authors of the sentence BERT paper. I will now search for 'sentence BERT paper authors'. 

TOOL CALLS:
Tool name: search_internet | Parameters: {"query":"sentence BERT paper authors"}
==================================================
RESPONSE:
The authors of the Sentence-BERT paper are Nils Reimers and Iryna Gurevych.
==================================================
CITATIONS:

Start: 43| End:55| Text:'Nils Reimers' 
Sources:
1. search_internet_z8t19852my9q:0
2. search_internet_z8t19852my9q:1
3. search_internet_z8t19852my9q:2
4. search_internet_z8t19852my9q:3
5. search_internet_z8t19852my9q:4


Start: 60| End:75| Text:'Iryna Gurevych.' 
Sources:
1. search_internet_z8t19852my9q:0
2. search_internet_z8t19852my9q:1
3. search_internet_z8t19852my9q:2
4. search_internet_z8t19852my9q:3
5. search_internet_z8t19852my9q:4
```

## Summary

In this tutorial, we learned about:

* How multi-step tool calling works
* How multi-step, parallel tool calling works
* How multi-step tool calling enables an agent to self-correct, and hence, be more flexible

However, up until now, we have only worked with purely unstructured data, the type of data we typically encounter in a standard RAG system.

In the coming chapters, we'll add another complexity to the agentic RAG system – working with semi-structured and structured data. This adds another dimension to the agent's flexibility, which is dealing with a more diverse set of data sources.

In Part 4, we'll learn how to build an agent that can perform faceted queries over semi-structured data.


# Generating Multi-Faceted Queries

> Build a system that generates multi-faceted queries to capture the full intent of a user's request.

<a target="_blank" href="https://colab.research.google.com/github/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/agentic_rag_pt4_multi_faceted_queries.ipynb">
  Open in Colab
</a>

Consider a RAG system that needs to search through a large database of code examples and tutorials. A user might ask for "Python examples using the chat endpoint" or "JavaScript tutorials for text summarization".

In a basic RAG setup, these queries would be passed as-is to a search function, potentially missing important context or failing to leverage the structured nature of the data. For example, the code examples database might consist of metadata such as the programming language, the created time, the tech stack used, and so on.

It would be great if we could design a system that could leverage this metadata as a filter to retrieve only the relevant results.

We can achieve this using a tool use approach. Here, we can build a system that generates multi-faceted queries to capture the full intent of a user's request. This allows for more precise and relevant results by utilizing the semi-structured nature of the data.

Here are some examples of how this approach can be applied:

1. E-commerce product searches: Filtering by price range, category, brand, customer ratings, and availability.
2. Academic research databases: Narrowing results by publication year, field of study, citation count, and peer-review status.
3. Job search platforms: Refining job listings by location, experience level, salary range, and required skills.

In this tutorial, we'll cover:

* Defining the function for data querying
* Creating the tool for generating multi-faceted queries
* Building an agent for performing multi-faceted queries
* Running the agent

We'll build an agent that helps developers find relevant code examples and tutorials for using Cohere.

## Setup

To get started, first we need to install the `cohere` library and create a Cohere client.

```python PYTHON
! pip install cohere -qq
```

```python PYTHON
import json
import os
import cohere

co = cohere.ClientV2(
    "COHERE_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys
```

## Defining the function for data querying

We'll remove the other tools from Part 1 and just use one – `search_code_examples`.

Now, instead of just the `query` parameter, we'll add two more parameters: `programming_language` and `endpoints`:

* `programming_language`: The programming language of the code example or tutorial.
* `endpoints`: The Cohere endpoints used in the code example or tutorial.

We'll use these parameters as the metadata to filter the code examples and tutorials.

Let's rename the function to `search_code_examples_detailed` to reflect this change.

And as in Part 1, for simplicity, we create `query` as just a mock parameter and no actual search logic will be performed based on it.

**IMPORTANT:**

The source code for tool definitions can be [found here](https://github.com/cohere-ai/cohere-developer-experience/blob/main/notebooks/guides/agentic-rag/tool_def.py). Make sure to have the `tool_def.py` file in the same directory as this notebook for the imports to work correctly.

```python PYTHON
from tool_def import (
    search_code_examples_detailed,
    search_code_examples_detailed_tool,
)
```

```python PYTHON
functions_map = {
    "search_code_examples_detailed": search_code_examples_detailed,
}
```

## Creating the tool for generating multi-faceted queries

With the `search_code_examples` modified, we now need to modify the tool definition as well. Here, we are adding the two new properties to the tool definition:

* `programming_language`: This is a string property which we provide a list of options for the model to choose from. We do this by adding "Possible enum values" to the description, which in our case is `py, js`.
* `endpoints`: We want the model to be able to choose from more than one endpoint, and so here we define an array property. When defining an array property, we need to specify the type of the items in the array using the `items` key, which in our case is `string`. We also provide a list of endpoint options for the model to choose from, which is `chat, embed, rerank, classify`.

We make only the `query` parameter required, while the other two parameters are optional.

```python PYTHON
tools = [search_code_examples_detailed_tool]
```

## Building an agent for performing multi-faceted queries

Next, let's create a `run_agent` function to run the agentic RAG workflow, the same as in Part 1.

The only change we are making here is to make the system message simpler and more specific since the agent now only has one tool.

```python PYTHON
system_message = """## Task and Context
You are an assistant who helps developers find code examples and tutorials on using Cohere."""
```

```python PYTHON
model = "command-a-03-2025"


def run_agent(query, messages=None):
    if messages is None:
        messages = []

    if "system" not in {m.get("role") for m in messages}:
        messages.append({"role": "system", "content": system_message})

    # Step 1: get user message
    print(f"QUESTION:\n{query}")
    print("=" * 50)

    messages.append({"role": "user", "content": query})

    # Step 2: Generate tool calls (if any)
    response = co.chat(
        model=model, messages=messages, tools=tools, temperature=0.3
    )

    while response.message.tool_calls:

        print("TOOL PLAN:")
        print(response.message.tool_plan, "\n")
        print("TOOL CALLS:")
        for tc in response.message.tool_calls:
            print(
                f"Tool name: {tc.function.name} | Parameters: {tc.function.arguments}"
            )
        print("=" * 50)

        messages.append(
            {
                "role": "assistant",
                "tool_calls": response.message.tool_calls,
                "tool_plan": response.message.tool_plan,
            }
        )

        # Step 3: Get tool results
        for tc in response.message.tool_calls:
            tool_result = functions_map[tc.function.name](
                **json.loads(tc.function.arguments)
            )
            tool_content = []
            for data in tool_result:
                tool_content.append(
                    {
                        "type": "document",
                        "document": {"data": json.dumps(data)},
                    }
                )
                # Optional: add an "id" field in the "document" object, otherwise IDs are auto-generated
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": tool_content,
                }
            )

        # Step 4: Generate response and citations
        response = co.chat(
            model=model,
            messages=messages,
            tools=tools,
            temperature=0.3,
        )

    messages.append(
        {
            "role": "assistant",
            "content": response.message.content[0].text,
        }
    )

    # Print final response
    print("RESPONSE:")
    print(response.message.content[0].text)
    print("=" * 50)

    # Print citations (if any)
    verbose_source = (
        False  # Change to True to display the contents of a source
    )
    if response.message.citations:
        print("CITATIONS:\n")
        for citation in response.message.citations:
            print(
                f"Start: {citation.start}| End:{citation.end}| Text:'{citation.text}' "
            )
            print("Sources:")
            for idx, source in enumerate(citation.sources):
                print(f"{idx+1}. {source.id}")
                if verbose_source:
                    print(f"{source.tool_output}")
            print("\n")

    return messages
```

## Running the agent

Let's start with a broad query about "RAG code examples".

Since it's broad, this query shouldn't require any metadata filtering.

And this is shown by the agent's response, which provides only one parameter, `query`, in its tool call.

```python PYTHON
messages = run_agent("Do you have any RAG code examples")
# Tool name: search_code_examples | Parameters: {"query":"RAG code examples"}
```

```mdx
QUESTION:
Do you have any RAG code examples
==================================================
TOOL PLAN:
I will search for RAG code examples. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"RAG"}
==================================================
RESPONSE:
I found one code example for RAG with Chat, Embed and Rerank via Pinecone.
==================================================
CITATIONS:

Start: 38| End:74| Text:'Chat, Embed and Rerank via Pinecone.' 
Sources:
1. search_code_examples_detailed_kqa6j5x92e3k:2
```

Let's try a more specific query about "javascript tutorials on text summarization".

This time, the agent uses the `programming_language` parameter and passed the value `js` to it.

```python PYTHON
messages = run_agent("Javascript tutorials on summarization")
# Tool name: search_code_examples | Parameters: {"programming_language":"js","query":"..."}
```

```mdx
QUESTION:
Javascript tutorials on summarization
==================================================
TOOL PLAN:
I will search for Javascript tutorials on summarization. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"summarization","programming_language":"js"}
==================================================
RESPONSE:
I found one JavaScript tutorial on summarization:
- Build a Chrome extension to summarize web pages
==================================================
CITATIONS:

Start: 52| End:99| Text:'Build a Chrome extension to summarize web pages' 
Sources:
1. search_code_examples_detailed_mz15bkavd7r1:0
```

Let's now try a query that involves filtering based on the endpoints. Here, the user asks for "code examples of using embed and rerank endpoints".

And since we have set up the `endpoints` parameter to be an array, the agent is able to call the tool with a list of endpoints as its argument.

```python PYTHON
messages = run_agent(
    "Code examples of using embed and rerank endpoints."
)

# Tool name: search_code_examples | Parameters: {"endpoints":["embed","rerank"],"query":"..."}
```

```mdx
QUESTION:
Code examples of using embed and rerank endpoints.
==================================================
TOOL PLAN:
I will search for code examples of using embed and rerank endpoints. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"code examples","endpoints":["embed","rerank"]}
==================================================
RESPONSE:
Here are some code examples of using the embed and rerank endpoints:
- Wikipedia Semantic Search with Cohere Embedding Archives
- RAG With Chat Embed and Rerank via Pinecone
- Build Chatbots That Know Your Business with MongoDB and Cohere
==================================================
CITATIONS:

Start: 71| End:127| Text:'Wikipedia Semantic Search with Cohere Embedding Archives' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:0


Start: 130| End:173| Text:'RAG With Chat Embed and Rerank via Pinecone' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:1


Start: 176| End:238| Text:'Build Chatbots That Know Your Business with MongoDB and Cohere' 
Sources:
1. search_code_examples_detailed_qjtk4xbt5g4n:2
```

Finally, let's try a query that involves filtering based on both the programming language and the endpoints. Here, the user asks for "Python examples of using the chat endpoint".

And the agent correctly uses both parameters to query the code examples.

```python PYTHON
messages = run_agent("Python examples of using the chat endpoint.")

# Tool name: search_code_examples | Parameters: {"endpoints":["chat"],"programming_language":"py","query":"..."}
```

```mdx
QUESTION:
Python examples of using the chat endpoint.
==================================================
TOOL PLAN:
I will search for Python examples of using the chat endpoint. 

TOOL CALLS:
Tool name: search_code_examples_detailed | Parameters: {"query":"chat endpoint","programming_language":"py","endpoints":["chat"]}
==================================================
RESPONSE:
Here are some Python examples of using the chat endpoint:
- Calendar Agent with Native Multi Step Tool
- RAG With Chat Embed and Rerank via Pinecone
- Build Chatbots That Know Your Business with MongoDB and Cohere
==================================================
CITATIONS:

Start: 60| End:102| Text:'Calendar Agent with Native Multi Step Tool' 
Sources:
1. search_code_examples_detailed_79er2w6sycvr:0


Start: 105| End:148| Text:'RAG With Chat Embed and Rerank via Pinecone' 
Sources:
1. search_code_examples_detailed_79er2w6sycvr:2


Start: 151| End:213| Text:'Build Chatbots That Know Your Business with MongoDB and Cohere' 
Sources:
1. search_code_examples_detailed_79er2w6sycvr:3
```

## Summary

In this tutorial, we learned about:

* How to define the function for data querying
* How to create the tool for generating multi-faceted queries
* How to build an agent for performing multi-faceted queries
* How to run the agent

By implementing multi-faceted queries over semi-structured data, we've enhanced our RAG system to handle more specific and targeted searches. This approach allows for better utilization of metadata and more precise filtering of results, which is particularly useful when dealing with large collections of code examples and tutorials.

While this tutorial demonstrates how to work with semi-structured data, the agentic RAG approach can be applied to structured data as well. That means we can build agents that can translate natural language queries into queries for tables or relational databases.

In Part 5, we'll learn how to perform RAG over structured data (tables).



---

**Navigation:** [← Previous](./05-display-the-reranked-search-results.md) | [Index](./index.md) | [Next →](./07-querying-structured-data-tables.md)
