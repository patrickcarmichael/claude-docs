**Navigation:** [← Previous](./07-querying-structured-data-tables.md) | [Index](./index.md) | [Next →](./09-chat.md)

---

# Teams and Roles on the Cohere Platform

> The document outlines how to work in teams on the Cohere platform, including inviting others, managing roles, and access permissions for Owners and Users.

Working in Teams in the Cohere platform enables users to share API keys and custom models. Access to the platform is managed via two role types, **Owner** and **User**. Below, we outline the process for inviting others to your Team and discuss the difference in access permissions between the two roles.

## Inviting others to your Team

If you sign up with Cohere without being invited to a Team, you automatically become the “Owner” of a Team. To invite others to your team, navigate to the Cohere Dashboard, then click on the “Team” page in the sidebar.

![](file:9c32183f-64e4-46d3-a264-1f2d98b3c998)

### If your teammates do not have existing Cohere accounts

Clicking “+ Invite Teammates” will open a modal where you can send email invites and specify the role that best suits your teammates.

![](file:c413323d-0876-4d55-8df1-9c2793d260e2)

### If your teammates have existing Cohere accounts

Users that already have a Cohere account and are not part of your team cannot be invited to join via the dashboard, but we can migrate them over.

Please reach out to us at [support@cohere.com](mailto:support@cohere.com), letting us know the email address associated with your teammate's account and the email address associated with your Cohere account. We can help from there.

## Role Types

### User

Users have permissions to:

* View all other Team members
* Create and delete custom models
* View, create, copy, and rename Trial API keys
* Make Production API keys (NOTE: Production API keys can only be created after an owner has completed the "Go to Production" form)
* View Production API keys (NOTE: you can *always* see which keys exist, but production keys are only viewable in their entirety when they’re created)
* View Usage history

### Owner

In addition to the above, Owners have permissions to:

* Invite, remove, and change role type of other Team members
* Generate, rename, and delete production API keys
* Complete the “Go to Production” form for your team to receive a production API key. After your team has been approved, you (or users on your team) can create any number of production keys
* View and download invoices
* View and update payment information


# Errors (status codes and description)

> Understand Cohere's HTTP response codes and how to handle errors in various programming languages.

# Http status codes

## 400 - Bad Request

400 responses are sent when the body of the request is not valid. This can happen when required fields are missing, or when the values provided are not valid.

To resolve this error, consult [the API spec](https://docs.cohere.com/reference/about) to ensure that you are providing the correct fields and values.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                                                                                                                                                                                             |
  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | invalid request: list of documents must not be empty                                                                                                                                                                                                                |
  | invalid request: prompt must be at least 1 token long.                                                                                                                                                                                                              |
  | too many tokens: total number of tokens in the prompt cannot exceed 4081 - received 4292. Try using a shorter prompt, or enabling prompt truncating. See [https://docs.cohere.com/reference/generate](https://docs.cohere.com/reference/generate) for more details. |
  | invalid request: valid input\_type must be provided with the provided model                                                                                                                                                                                         |
  | system turn must be the first in the list                                                                                                                                                                                                                           |
  | invalid request: all elements in history must have a message.                                                                                                                                                                                                       |
  | invalid request: message must be at least 1 token long or tool results must be specified.                                                                                                                                                                           |
  | invalid request: query must not be empty or be only whitespace                                                                                                                                                                                                      |
  | invalid request: model 'command-r' is not supported by the generate API                                                                                                                                                                                             |
  | invalid request: cannot specify both frequency\_penalty and presence\_penalty.                                                                                                                                                                                      |
  | invalid request: only one of 'presence\_penalty' and 'frequency\_penalty' can be specified for this model.                                                                                                                                                          |
  | message must not be empty in a turn                                                                                                                                                                                                                                 |
  | too many tokens: max tokens must be less than or equal to 4096, the maximum output for this model - received 8192.                                                                                                                                                  |
  | invalid request: response\_format is not supported with RAG.                                                                                                                                                                                                        |
  | too many tokens: size limit exceeded by 11326 tokens. Try using shorter or fewer inputs, or setting prompt\_truncation='AUTO'.                                                                                                                                      |
  | invalid request: number of total max chunks (number of documents \* max chunks per doc) must be less than 10000                                                                                                                                                     |
  | invalid request: min classes for classify request is 2 - received 0                                                                                                                                                                                                 |
  | invalid request: Invalid role in chat\_history at index 2. Role must be one of the following: User, Chatbot, System, Tool                                                                                                                                           |
  | invalid request: total number of texts must be at most 96 - received 104                                                                                                                                                                                            |
  | invalid request: temperature must be between 0 and 1.0 inclusive.                                                                                                                                                                                                   |
  | invalid request: presence\_penalty must be between 0 and 1 inclusive.                                                                                                                                                                                               |
  | invalid request: text must be longer than 250 characters                                                                                                                                                                                                            |
  | invalid request: inputs contains an element that is the empty string at index 0                                                                                                                                                                                     |
  | multi step limit reached - set a higher limit                                                                                                                                                                                                                       |
  | invalid request: return\_top\_n is invalid, value must be between 1 and 4                                                                                                                                                                                           |
  | invalid request: document at index 0 cannot be empty                                                                                                                                                                                                                |
  | embedding\_types parameter is required                                                                                                                                                                                                                              |
  | finetuneID is not a valid UUID: ''                                                                                                                                                                                                                                  |
  | invalid request: tool names can only contain certain characters (A-Za-z0-9\_) and can't begin with a digit (provided name: 'xyz').                                                                                                                                  |
  | invalid json syntax: invalid character '\a' in string literal                                                                                                                                                                                                       |
  | invalid request: RAG is not supported for this model.                                                                                                                                                                                                               |
  | tool call id not found in previous tool calls                                                                                                                                                                                                                       |
  | invalid request: each unique label must have at least 2 examples. Not enough examples for: awr\_report, create\_user, tablespace\_usage                                                                                                                             |
  | invalid request: multi step is not supported by the provided model: command.                                                                                                                                                                                        |
  | invalid request: invalid API version was passed in, for more information please refer to [https://docs.cohere.com/versioning-reference](https://docs.cohere.com/versioning-reference)                                                                               |
  | document does not have a 'snippet' or a 'text' field that can be used for chunking and reranking                                                                                                                                                                    |
  | finetuned model with name xyz is not ready for serving                                                                                                                                                                                                              |
  | invalid request: required 'text' param is missing or empty.                                                                                                                                                                                                         |
  | invalid request: rank\_fields cannot be empty, it must either contain at least one field or be omitted                                                                                                                                                              |
  | schema must be an object                                                                                                                                                                                                                                            |
  | a model parameter is required for this endpoint.                                                                                                                                                                                                                    |
  | cannot have duplicate tool ids                                                                                                                                                                                                                                      |
  | too many tokens: multi-hop prompt is too long even after truncation                                                                                                                                                                                                 |
  | connectors failed with continue on failure disabled: connector xyz failed with message 'failed to get auth token: user is not authenticated for connector xyz'                                                                                                      |
  | invalid request: the 'tool\_1' tool must have at least a description, input, or output.                                                                                                                                                                             |
  | tool call id must be provided with tool message                                                                                                                                                                                                                     |
  | invalid request: images must be used with input\_type=image                                                                                                                                                                                                         |
  | invalid request: format must be one of 'paragraph', or 'bullets'.                                                                                                                                                                                                   |
  | invalid request: finetuned model is not compatible with RAG functionality                                                                                                                                                                                           |
  | required field name not found in properties                                                                                                                                                                                                                         |
  | property title must have a type                                                                                                                                                                                                                                     |
  | tool call must be of type function                                                                                                                                                                                                                                  |
  | invalid request: length must be one of 'short', 'medium', or 'long'.                                                                                                                                                                                                |
  | invalid request: duplicate document ID adfasd at index 1 and 0                                                                                                                                                                                                      |
  | too many tokens: minimal context could not be added to prompt (size limit exceeded by 280 tokens)                                                                                                                                                                   |
  | invalid request: raw prompting is not supported with the following parameter(s): connectors, documents, search\_queries\_only, tools.                                                                                                                               |
  | invalid request: max\_tokens can only be 0 if return\_likelihoods is set to 'ALL' and prompt is longer than 1 token.                                                                                                                                                |
</details>

## 401 - Unauthorized

401 responses are sent when the API key is missing, invalid or has expired. To resolve this error, ensure that you are providing a valid API key.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                                                                    |
  | ------------------------------------------------------------------------------------------------------------------------------------------ |
  | no api key supplied                                                                                                                        |
  | invalid api token                                                                                                                          |
  | Your API key has expired. Please create a production key at dashboard.cohere.com or reach out to your contact at Cohere to continue usage. |
</details>

## 402 - Payment Required

402 responses are sent when the account has reached its billing limit. To resolve these errors, [add or update](https://dashboard.cohere.com/billing?tab=payment) a payment method.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                                                                                                                                                                                                                                               |
  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | Please add or update your payment method at [https://dashboard.cohere.com/billing?tab=payment](https://dashboard.cohere.com/billing?tab=payment) to continue                                                                                                                                                          |
  | Maximum billing reached for this API key as set in your dashboard, please go to [https://dashboard.cohere.com/billing?tab=payment](https://dashboard.cohere.com/billing?tab=payment) to increase your maximum amount to continue using this API key. Your billing capacity will reset at the beginning of next month. |
</details>

## 404 - Not Found

404 responses are sent when the requested resource is not found. This can happen when the model, dataset, or connector ID is incorrect, or when the resource has been deleted.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                               |
  | ----------------------------------------------------------------------------------------------------- |
  | model 'xyz' not found, make sure the correct model ID was used and that you have access to the model. |
  | 404 page not found                                                                                    |
  | resource not found: no messages found with conversation id models                                     |
  | failed to find org by org id                                                                          |
  | connector 'web-search' not found.                                                                     |
  | finetuned model xyz not found                                                                         |
  | dataset with id texts not found                                                                       |
  | connector '' not found.                                                                               |
  | dataset with id my-dataset-id not found                                                               |
  | finetuned model xyz not found                                                                         |
</details>

## 429 - Too Many Requests

429 responses are sent when the rate limit has been exceeded. Please consult the [rate limit documentation](https://docs.cohere.com/v2/docs/rate-limits) to understand the limits and how to avoid these errors.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                                                                                                                                                                                                                                                                                                                                                                                           |
  | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
  | You are past the per minute request limit, please wait and try again later.                                                                                                                                                                                                                                                                                                                                                       |
  | You are using a Trial key, which is limited to 40 API calls / minute. You can continue to use the Trial key for free or upgrade to a Production key with higher rate limits at '[https://dashboard.cohere.com/api-keys](https://dashboard.cohere.com/api-keys)'. Contact us on '[https://discord.gg/XW44jPfYJu](https://discord.gg/XW44jPfYJu)' or email us at [support@cohere.com](mailto:support@cohere.com) with any questions |
  | Please wait and try again later                                                                                                                                                                                                                                                                                                                                                                                                   |
  | trial token rate limit exceeded, limit is 100000 tokens per minute                                                                                                                                                                                                                                                                                                                                                                |
</details>

## 499 - Request Cancelled

499 responses are sent when a user cancels the request. To resolve these errors, try the request again.

<details>
  <summary>
    Example error responses
  </summary>

  | message                                                 |
  | ------------------------------------------------------- |
  | request cancelled                                       |
  | streaming error - scroll down for more streaming errors |
  | failed to get rerank inference: request cancelled       |
  | request cancelled by user                               |
</details>

## 500 - Server Error

500 responses are sent when there is an unexpected internal server error. To resolve these errors, please contact support via [email](mailto:support@cohere.com) or [discord](https://discord.gg/XW44jPfYJu) with details about your request and use case.


# Migrating From API v1 to API v2

> The document serves as a reference for developers looking to update their existing Cohere API v1 implementations to the new v2 standard.

This guide serves as a reference for developers looking to update their code that uses Cohere API v1 in favor of the new v2 standard. It outlines the key differences and necessary changes when migrating from Cohere API v1 to v2 and the various aspects of the API, including chat functionality, RAG (Retrieval-Augmented Generation), and tool use. Each section provides code examples for both v1 and v2, highlighting the structural changes in request formats, response handling, and new features introduced in v2.

```python PYTHON
# ! pip install -U cohere

import cohere

# instantiating the old client
co_v1 = cohere.Client(api_key="<YOUR API KEY>")

# instantiating the new client
co_v2 = cohere.ClientV2(api_key="<YOUR API KEY>")
```

# General

* v2: `model` is a required field for Embed, Rerank, Classify, and Chat.

# Embed

* v2: `embedding_types` is a required field for Embed.

# Chat

## Messages

* Message structure:
  * v1: uses separate `preamble` and `message` parameters.
  * v2: uses a single `messages` parameter consisting of a list of roles (`system`, `user`, `assistant`, or `tool`). The `system` role in v2 replaces the `preamble` parameter in v1.

* Chat history:
  * v1: manages the chat history via the `chat_history` parameter.
  * v2: manages the chat history via the `messages` list.

**v1**

```python PYTHON
res = co_v1.chat(
    model="command-a-03-2025",
    preamble="You respond in concise sentences.",
    chat_history=[
        {"role": "user", "message": "Hello"},
        {
            "role": "chatbot",
            "message": "Hi, how can I help you today?",
        },
    ],
    message="I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates?",
)

print(res.text)
```

```
Excited to join the team at Co1t, where I look forward to contributing my skills and collaborating with everyone to drive innovation and success.
```

**v2**

```python PYTHON
res = co_v2.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "system",
            "content": "You respond in concise sentences.",
        },
        {"role": "user", "content": "Hello"},
        {
            "role": "assistant",
            "content": "Hi, how can I help you today?",
        },
        {
            "role": "user",
            "content": "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates.",
        },
    ],
)

print(res.message.content[0].text)
```

```
Excited to join the team at Co1t, bringing my passion for innovation and a background in [your expertise] to contribute to the company's success!
```

## Response content

* v1: Accessed via `text`
* v2: Accessed via `message.content[0].text`

**v1**

```python PYTHON
res = co_v1.chat(model="command-a-03-2025", message="What is 2 + 2")

print(res.text)
```

```
The answer is 4.
```

**v2**

```python PYTHON
res = co_v2.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": "What is 2 + 2"}],
)

print(res.message.content[0].text)
```

```
The answer is 4.
```

## Streaming

* Events containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

**v1**

```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

res = co_v1.chat_stream(model="command-a-03-2025", message=message)

for chunk in res:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
```

```
"Hi, I'm [your name] and I'm thrilled to join the Co1t team today as a [your role], eager to contribute my skills and ideas to help drive innovation and success for our startup!"
```

**v2**

```python PYTHON
message = "I'm joining a new startup called Co1t today. Could you help me write a one-sentence introduction message to my teammates."

res = co_v2.chat_stream(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
)

for chunk in res:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
```

```
"Hi everyone, I'm thrilled to join the Co1t team today and look forward to contributing my skills and ideas to drive innovation and success!"
```

# RAG

## Documents

* v1: the `documents` parameter supports a list of objects with multiple fields per document.
* v2: the `documents` parameter supports a few different options for structuring documents:
  * List of objects with `data` object: same as v1 described above, but each document passed as a `data` object (with an optional `id` field to be used in citations).
  * List of objects with `data` string (with an optional `id` field to be used in citations).
  * List of strings.

**v1**

```python PYTHON
# Define the documents
documents_v1 = [
    {
        "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
    },
    {
        "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
    },
]

# The user query
message = "Are there fitness-related benefits?"

# Generate the response
res_v1 = co_v1.chat(
    model="command-a-03-2025",
    message=message,
    documents=documents_v1,
)

print(res_v1.text)
```

```
Yes, there are fitness-related benefits. We offer gym memberships, on-site yoga classes, and comprehensive health insurance.
```

**v2**

```python PYTHON
# Define the documents
documents_v2 = [
    {
        "data": {
            "text": "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward."
        }
    },
    {
        "data": {
            "text": "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance."
        }
    },
]

# The user query
message = "Are there fitness-related benefits?"

# Generate the response
res_v2 = co_v2.chat(
    model="command-a-03-2025",
    messages=[{"role": "user", "content": message}],
    documents=documents_v2,
)

print(res_v2.message.content[0].text)
```

```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.
```

The following is a list of the the different options for structuring documents for RAG in v2.

```python PYTHON
documents_v2 = [
    # List of objects with data string
    {
        "id": "123",
        "data": "I love penguins. they are fluffy",
    },
    # List of objects with data object
    {
        "id": "456",
        "data": {
            "text": "I love penguins. they are fluffy",
            "author": "Abdullah",
            "create_date": "09021989",
        },
    },
    # List of strings
    "just a string",
]
```

## Citations

* Citations access:
  * v1: `citations`
  * v2: `message.citations`
* Cited documents access:
  * v1: `documents`
  * v2: as part of `message.citations`, in the `sources` field

**v1**

```python PYTHON
# Yes, there are fitness-related benefits. We offer gym memberships, on-site yoga classes, and comprehensive health insurance.

print(res_v1.citations)
print(res_v1.documents)
```

```
[ChatCitation(start=50, end=124, text='gym memberships, on-site yoga classes, and comprehensive health insurance.', document_ids=['doc_1'])]

[{'id': 'doc_1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'}]
```

**v2**

```python PYTHON
# Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.

print(res_v2.message.citations)
```

```
[Citation(start=14, end=88, text='gym memberships, on-site yoga classes, and comprehensive health insurance.', sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})])]
```

## Search query generation

* v1: Uses `search_queries_only` parameter
* v2: Supported via tools. We recommend using the v1 API for this functionality in order to leverage the `force_single_step` feature. Support in v2 will be coming soon.

## Connectors

* v1: Supported via the [`connectors` parameter](/v1/docs/overview-rag-connectors)
* v2: Supported via user-defined tools.

## Web search

* v1: Supported via the `web-search` connector in the `connectors` parameter
* v2: Supported via user-defined tools.

**v1**

Uses the web search connector to search the internet for information relevant to the user's query.

```python PYTHON
res_v1 = co_v1.chat(
    message="who won euro 2024",
    connectors=[{"id": "web-search"}],
)

print(res_v1.text)
```

```
Spain won the UEFA Euro 2024, defeating England 2-1 in the final.
```

**v2**

Web search functionality is supported via tools.

```python PYTHON
# Any search engine can be used. This example uses the Tavily API.
from tavily import TavilyClient

tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])


# Create a web search function
def web_search(queries: list[str]) -> list[dict]:

    documents = []

    for query in queries:
        response = tavily_client.search(query, max_results=2)

        results = [
            {
                "title": r["title"],
                "content": r["content"],
                "url": r["url"],
            }
            for r in response["results"]
        ]

        for idx, result in enumerate(results):
            document = {"id": str(idx), "data": result}
            documents.append(document)

    return documents


# Define the web search tool
web_search_tool = [
    {
        "type": "function",
        "function": {
            "name": "web_search",
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

# The user query
query = "who won euro 2024"

# Define a system message to optimize search query generation
instructions = "Write a search query that will find helpful information for answering the user's question accurately. If you need more than one search query, write a list of search queries. If you decide that a search is very unlikely to find information that would be useful in constructing a response to the user, you should instead directly answer."

messages = [
    {"role": "system", "content": instructions},
    {"role": "user", "content": query},
]

model = "command-a-03-2025"

# Generate search queries (if any)
response = co_v2.chat(
    model=model, messages=messages, tools=web_search_tool
)

search_queries = []

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
        tool_result = web_search(**json.loads(tc.function.arguments))
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
    response = co_v2.chat(
        model=model, messages=messages, tools=web_search_tool
    )

print(response.message.content[0].text)
```

```
Tool plan:
I will search for 'who won euro 2024' to find out who won the competition. 

Tool calls:
Tool name: web_search | Parameters: {"queries":["who won euro 2024"]}
==================================================
Spain won the 2024 European Championship. They beat England in the final, with substitute Mikel Oyarzabal scoring the winning goal.
```

## Streaming

* Event containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

* Events containing citations:
  * v1: `chunk.event_type == "citation-generation"`
  * v2: `chunk.type == "citation-start"`

* Accessing citations:
  * v1: `chunk.citations`
  * v2: `chunk.delta.message.citations`

**v1**

```python PYTHON
message = "Are there fitness-related benefits?"

res_v1 = co_v1.chat_stream(
    model="command-a-03-2025",
    message=message,
    documents=documents_v1,
)

for chunk in res_v1:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
    if chunk.event_type == "citation-generation":
        print(f"\n{chunk.citations}")
```

```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance as part of our health and wellness benefits.

[ChatCitation(start=14, end=87, text='gym memberships, on-site yoga classes, and comprehensive health insurance', document_ids=['doc_1'])]

[ChatCitation(start=103, end=132, text='health and wellness benefits.', document_ids=['doc_1'])]
```

**v2**

```python PYTHON
message = "Are there fitness-related benefits?"

messages = [{"role": "user", "content": message}]

res_v2 = co_v2.chat_stream(
    model="command-a-03-2025",
    messages=messages,
    documents=documents_v2,
)

for chunk in res_v2:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
        if chunk.type == "citation-start":
            print(f"\n{chunk.delta.message.citations}")
```

```
Yes, we offer gym memberships, on-site yoga classes, and comprehensive health insurance.

start=14 end=88 text='gym memberships, on-site yoga classes, and comprehensive health insurance.' sources=[DocumentSource(type='document', id='doc:1', document={'id': 'doc:1', 'text': 'Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.'})]
```

# Tool use

## Tool definition

* v1: uses Python types to define tools.
* v2: uses JSON schema to define tools.

**v1**

```python PYTHON
def get_weather(location):
    return {"temperature": "20C"}


functions_map = {"get_weather": get_weather}

tools_v1 = [
    {
        "name": "get_weather",
        "description": "Gets the weather of a given location",
        "parameter_definitions": {
            "location": {
                "description": "The location to get weather, example: San Francisco, CA",
                "type": "str",
                "required": True,
            }
        },
    },
]
```

**v2**

```python PYTHON
def get_weather(location):
    return [{"temperature": "20C"}]
    # You can return a list of objects e.g. [{"url": "abc.com", "text": "..."}, {"url": "xyz.com", "text": "..."}]


functions_map = {"get_weather": get_weather}

tools_v2 = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "gets the weather of a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "the location to get weather, example: San Fransisco, CA",
                    }
                },
                "required": ["location"],
            },
        },
    },
]
```

## Tool calling

* Response handling
  * v1: Tool calls accessed through `response.tool_calls`
  * v2: Tool calls accessed through `response.message.tool_calls`

* Chat history management
  * v1: Tool calls stored in the response's `chat_history`
  * v2: Append the tool call details (`tool_calls` and `tool_plan`) to the `messages` list

**v1**

```python PYTHON
message = "What's the weather in Toronto?"

res_v1 = co_v1.chat(
    model="command-a-03-2025", message=message, tools=tools_v1
)

print(res_v1.tool_calls)
```

```
[ToolCall(name='get_weather', parameters={'location': 'Toronto'})]
```

**v2**

```python PYTHON
messages = [
    {"role": "user", "content": "What's the weather in Toronto?"}
]

res_v2 = co_v2.chat(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

if res_v2.message.tool_calls:
    messages.append(
        {
            "role": "assistant",
            "tool_calls": res_v2.message.tool_calls,
            "tool_plan": res_v2.message.tool_plan,
        }
    )

    print(res_v2.message.tool_calls)
```

```
[ToolCallV2(id='get_weather_k88p0m8504w5', type='function', function=ToolCallV2Function(name='get_weather', arguments='{"location":"Toronto"}'))]
```

## Tool call ID

* v1: Tool calls do not emit tool call IDs
* v2: Tool calls emit tool call IDs. This will help the model match tool results to the right tool call.

**v1**

```python PYTHON
tool_results = [
    {
        "call": {
            "name": "<tool name>",
            "parameters": {"<param name>": "<param value>"},
        },
        "outputs": [{"<key>": "<value>"}],
    },
]
```

**v2**

```python PYTHON
messages = [
    {
        "role": "tool",
        "tool_call_id": "123",
        "content": [
            {
                "type": "document",
                "document": {
                    "id": "123",
                    "data": {"<key>": "<value>"},
                },
            }
        ],
    }
]
```

## Response generation

* Tool execution: Chat history management
  * v1: Append `call` and `outputs` to the chat history
  * v2: Append `tool_call_id` and `tool_content` to `messages` to the chat history

* Tool execution: Tool results
  * v1: Passed as `tool_results` parameter
  * v2: Incorporated into the `messages` list as tool responses

* User message
  * v1: Set as empty (`""`)
  * v2: No action required

**v1**

```python PYTHON
tool_content_v1 = []
if res_v1.tool_calls:
    for tc in res_v1.tool_calls:
        tool_call = {"name": tc.name, "parameters": tc.parameters}
        tool_result = functions_map[tc.name](**tc.parameters)
        tool_content_v1.append(
            {"call": tool_call, "outputs": [tool_result]}
        )

res_v1 = co_v1.chat(
    model="command-a-03-2025",
    message="",
    tools=tools_v1,
    tool_results=tool_content_v1,
    chat_history=res_v1.chat_history,
)

print(res_v1.text)
```

```
It is currently 20°C in Toronto.
```

**v2**

```python PYTHON
if res_v2.message.tool_calls:
    for tc in res_v2.message.tool_calls:
        tool_result = functions_map[tc.function.name](
            **json.loads(tc.function.arguments)
        )
        tool_content_v2 = []
        for data in tool_result:
            tool_content_v2.append(
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
                "content": tool_content_v2,
            }
        )

res_v2 = co_v2.chat(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

print(res_v2.message.content[0].text)
```

```
It's 20°C in Toronto.
```

## Citations

* Citations access:
  * v1: `citations`
  * v2: `message.citations`
* Cited tools access:
  * v1: `documents`
  * v2: as part of `message.citations`, in the `sources` field

**v1**

```python PYTHON
print(res_v1.citations)
print(res_v1.documents)
```

```
[ChatCitation(start=16, end=20, text='20°C', document_ids=['get_weather:0:2:0'])]

[{'id': 'get_weather:0:2:0', 'temperature': '20C', 'tool_name': 'get_weather'}]
```

**v2**

```python PYTHON
print(res_v2.message.citations)
```

```
[Citation(start=5, end=9, text='20°C', sources=[ToolSource(type='tool', id='get_weather_k88p0m8504w5:0', tool_output={'temperature': '20C'})])]
```

## Streaming

* Event containing content:
  * v1: `chunk.event_type == "text-generation"`
  * v2: `chunk.type == "content-delta"`

* Accessing response content:
  * v1: `chunk.text`
  * v2: `chunk.delta.message.content.text`

* Events containing citations:
  * v1: `chunk.event_type == "citation-generation"`
  * v2: `chunk.type == "citation-start"`

* Accessing citations:
  * v1: `chunk.citations`
  * v2: `chunk.delta.message.citations`

**v1**

```python PYTHON
tool_content_v1 = []
if res_v1.tool_calls:
    for tc in res_v1.tool_calls:
        tool_call = {"name": tc.name, "parameters": tc.parameters}
        tool_result = functions_map[tc.name](**tc.parameters)
        tool_content_v1.append(
            {"call": tool_call, "outputs": [tool_result]}
        )

res_v1 = co_v1.chat_stream(
    message="",
    tools=tools_v1,
    tool_results=tool_content_v1,
    chat_history=res_v1.chat_history,
)

for chunk in res_v1:
    if chunk.event_type == "text-generation":
        print(chunk.text, end="")
    if chunk.event_type == "citation-generation":
        print(f"\n{chunk.citations}")
```

```
It's 20°C in Toronto.

[ChatCitation(start=5, end=9, text='20°C', document_ids=['get_weather:0:2:0', 'get_weather:0:4:0'])]
```

**v2**

```python PYTHON
if res_v2.message.tool_calls:
    for tc in res_v2.message.tool_calls:
        tool_result = functions_map[tc.function.name](
            **json.loads(tc.function.arguments)
        )
        tool_content_v2 = []
        for data in tool_result:
            tool_content_v2.append(
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
                "content": tool_content_v2,
            }
        )

res_v2 = co_v2.chat_stream(
    model="command-a-03-2025", messages=messages, tools=tools_v2
)

for chunk in res_v2:
    if chunk:
        if chunk.type == "content-delta":
            print(chunk.delta.message.content.text, end="")
        elif chunk.type == "citation-start":
            print(f"\n{chunk.delta.message.citations}")
```

```
It's 20°C in Toronto.

start=5 end=9 text='20°C' sources=[ToolSource(type='tool', id='get_weather_k88p0m8504w5:0', tool_output={'temperature': '20C'})]
```

## Citation quality (both RAG and tool use)

* v1: controlled via `citation_quality` parameter
* v2: controlled via `citation_options` parameter (with `mode` as a key)

# Unsupported features in v2

The following v1 features are not supported in v2:

* General chat
  * `conversation_id` parameter (chat history is now managed by the developer via the `messages` parameter)
* RAG
  * `search_queries_only` parameter
  * `connectors` parameter
  * `prompt_truncation` parameter
* Tool use
  * `force_single_step` parameter (all tool calls are now multi-step by default)


# Using Cohere models via the OpenAI SDK

> The document serves as a guide for Cohere's Compatibility API, which allows developers to seamlessly use Cohere's models using OpenAI's SDK.

The Compatibility API allows developers to use Cohere’s models through OpenAI’s SDK.

It makes it easy to switch existing OpenAI-based applications to use Cohere’s models while still maintaining the use of OpenAI SDK — no big refactors needed.

The supported libraries are:

* TypeScript / JavaScript
* Python
* .NET
* Java (beta)
* Go (beta)

This is a quickstart guide to help you get started with the Compatibility API.

## Installation

First, install the OpenAI SDK and import the package.

Then, create a client and configure it with the compatibility API base URL and your Cohere API key.

<Tabs>
  <Tab title="Python">
    ```bash
    pip install openai
    ```

    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )
    ```
  </Tab>

  <Tab title="TypeScript">
    ```bash
    npm install openai
    ```

    ```typescript TYPESCRIPT

    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
    });
    ```
  </Tab>
</Tabs>

## Basic chat completions

Here’s a basic example of using the Chat Completions API.

<Tabs>
  <Tab title="Python">
    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.chat.completions.create(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming.",
            },
        ],
    )

    print(completion.choices[0].message)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Write a haiku about recursion in programming.",
            },
        ]
    });

    console.log(completion.choices[0].message);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
        {
            "role": "user", 
            "content": "Write a haiku about recursion in programming."
        }
        ]
    }'
    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```mdx
ChatCompletionMessage(content="Recursive loops,\nUnraveling code's depths,\nEndless, yet complete.", refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

## Chat with streaming

To stream the response, set the `stream` parameter to `True`.

<Tabs>
  <Tab title="Python">
    ```python
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    stream = client.chat.completions.create(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Write a haiku about recursion in programming.",
            },
        ],
        stream=True,
    )

    for chunk in stream:
        print(chunk.choices[0].delta.content or "", end="")
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Write a haiku about recursion in programming.",
            },
        ],
        stream: true,
    });

    for await (const chunk of completion) {
        console.log(chunk.choices[0].delta.content);
    }
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
        {
            "role": "user",
            "content": "Write a haiku about recursion in programming."
        }
        ],
        "stream": true
    }'
    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```mdx
Recursive call,
Unraveling, line by line,
Solving, then again.
```

## State management

For state management, use the `messages` parameter to build the conversation history.

You can include a system message via the `developer` role and the multiple chat turns between the `user` and `assistant`.

<Tabs>
  <Tab title="Python">
    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.chat.completions.create(
        messages=[
            {
                "role": "developer",
                "content": "You must respond in the style of a pirate.",
            },
            {
                "role": "user",
                "content": "What's 2 + 2.",
            },
            {
                "role": "assistant",
                "content": "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!",
            },
            {
                "role": "user",
                "content": "Add 30 to that.",
            },
        ],
        model="command-a-03-2025",
    )

    print(completion.choices[0].message)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "developer", 
                content: "You must respond in the style of a pirate."
            },
            {
                role: "user",
                content: "What's 2 + 2.",
            },
            {
                role: "assistant",
                content: "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!",
            },
            {
                role: "user",
                content: "Add 30 to that.",
            }
        ],
        stream: true,
    });

    for await (const chunk of completion) {
        console.log(chunk.choices[0].delta.content);
    }
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
        {
            "role": "developer",
            "content": "You must respond in the style of a pirate."
        },
        {
            "role": "user",
            "content": "What'\''s 2 + 2."
        },
        {
            "role": "assistant", 
            "content": "Arrr, matey! 2 + 2 be 4, just like a doubloon in the sea!"
        },
        {
            "role": "user",
            "content": "Add 30 to that."
        }
        ]
    }'
    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```mdx
ChatCompletionMessage(content='Aye aye, captain! 4 + 30 be 34, a treasure to behold!', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

## Structured outputs

The Structured Outputs feature allows you to specify the schema of the model response. It guarantees that the response will strictly follow the schema.

To use it, set the `response_format` parameter to the JSON Schema of the desired output.

<Tabs>
  <Tab title="Python">
    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    completion = client.beta.chat.completions.parse(
        model="command-a-03-2025",
        messages=[
            {
                "role": "user",
                "content": "Generate a JSON describing a book.",
            }
        ],
        response_format={
            "type": "json_object",
            "schema": {
                "type": "object",
                "properties": {
                    "title": {"type": "string"},
                    "author": {"type": "string"},
                    "publication_year": {"type": "integer"},
                },
                "required": ["title", "author", "publication_year"],
            },
        },
    )

    print(completion.choices[0].message.content)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "user",
                content: "Generate a JSON describing a book.",
            }
        ],
        response_format: {
            type: "json_object",
            schema: {
                type: "object",
                properties: {
                    title: {type: "string"},
                    author: {type: "string"},
                    publication_year: {type: "integer"},
                },
                required: ["title", "author", "publication_year"],
            },
        }
    });

    console.log(completion.choices[0].message);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
        {
            "role": "user",
            "content": "Generate a JSON describing a book."
        }
        ],
        "response_format": {
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
            "title": {"type": "string"},
            "author": {"type": "string"},
            "publication_year": {"type": "integer"}
            },
            "required": ["title", "author", "publication_year"]
        }
        }
    }'
    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```
{
    "title": "The Great Gatsby",
    "author": "F. Scott Fitzgerald",
    "publication_year": 1925
}
```

## Tool use (function calling)

You can utilize the tool use feature by passing a list of tools to the `tools` parameter in the API call.

Specifying the `strict` parameter to `True` in the tool calling step will guarantee that every generated tool call follows the specified tool schema.

<Tabs>
  <Tab title="Python">
    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key="COHERE_API_KEY",
    )

    tools = [
        {
            "type": "function",
            "function": {
                "name": "get_flight_info",
                "description": "Get flight information between two cities or airports",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_origin": {
                            "type": "string",
                            "description": "The departure airport, e.g. MIA",
                        },
                        "loc_destination": {
                            "type": "string",
                            "description": "The destination airport, e.g. NYC",
                        },
                    },
                    "required": ["loc_origin", "loc_destination"],
                },
            },
        }
    ]

    messages = [
        {"role": "developer", "content": "Today is April 30th"},
        {
            "role": "user",
            "content": "When is the next flight from Miami to Seattle?",
        },
        {
            "role": "assistant",
            "tool_calls": [
                {
                    "function": {
                        "arguments": '{ "loc_destination": "Seattle", "loc_origin": "Miami" }',
                        "name": "get_flight_info",
                    },
                    "id": "get_flight_info0",
                    "type": "function",
                }
            ],
        },
        {
            "role": "tool",
            "name": "get_flight_info",
            "tool_call_id": "get_flight_info0",
            "content": "Miami to Seattle, May 1st, 10 AM.",
        },
    ]

    completion = client.chat.completions.create(
        model="command-a-03-2025",
        messages=messages,
        tools=tools,
        temperature=0.7,
    )

    print(completion.choices[0].message)
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const completion = await openai.chat.completions.create({
        model: "command-a-03-2025",
        messages: [
            {
                role: "developer", 
                content: "Today is April 30th"
            },
            {
                role: "user",
                content: "When is the next flight from Miami to Seattle?"
            },
            {
                role: "assistant",
                tool_calls: [
                    {
                        function: {
                            arguments: '{ "loc_destination": "Seattle", "loc_origin": "Miami" }',
                            name: "get_flight_info"
                        },
                        id: "get_flight_info0",
                        type: "function"
                    }
                ]
            },
            {
                role: "tool",
                name: "get_flight_info",
                tool_call_id: "get_flight_info0", 
                content: "Miami to Seattle, May 1st, 10 AM."
            }
        ],
        tools: [
            {
                type: "function",
                function: {
                    name: "get_flight_info",
                    description: "Get flight information between two cities or airports",
                    parameters: {
                        type: "object",
                        properties: {
                            loc_origin: {
                                type: "string",
                                description: "The departure airport, e.g. MIA"
                            },
                            loc_destination: {
                                type: "string",
                                description: "The destination airport, e.g. NYC"
                            }
                        },
                        required: ["loc_origin", "loc_destination"]
                    }
                }
            }
        ],
        temperature: 0.7
    });

    console.log(completion.choices[0].message);
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/chat/completions \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "command-a-03-2025",
        "messages": [
            {
            "role": "developer",
            "content": "Today is April 30th"
        },
        {
            "role": "user",
            "content": "When is the next flight from Miami to Seattle?"
        },
            {
            "role": "assistant",
            "tool_calls": [
                {
                    "function": {
                        "arguments": "{ \"loc_destination\": \"Seattle\", \"loc_origin\": \"Miami\" }",
                        "name": "get_flight_info"
                    },
                    "id": "get_flight_info0",
                    "type": "function"
                }
            ]
        },
        {
            "role": "tool",
            "name": "get_flight_info",
            "tool_call_id": "get_flight_info0",
            "content": "Miami to Seattle, May 1st, 10 AM."
        }],
        "tools": [
        {
            "type": "function",
            "function": {
                "name":"get_flight_info",
                "description": "Get flight information between two cities or airports",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "loc_origin": {
                            "type": "string",
                            "description": "The departure airport, e.g. MIA"
                        },
                        "loc_destination": {
                            "type": "string",
                            "description": "The destination airport, e.g. NYC"
                        }
                    },
                    "required": ["loc_origin", "loc_destination"]
                }
            }
            }
        ],
        "temperature": 0.7
    }'
    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```mdx
ChatCompletionMessage(content='The next flight from Miami to Seattle is on May 1st, 10 AM.', refusal=None, role='assistant', audio=None, function_call=None, tool_calls=None)
```

## Embeddings

You can generate text embeddings Embeddings API by passing a list of strings as the `input` parameter. You can also specify in `encoding_format` the format of embeddings to be generated. Can be either `float` or `base64`.

<Tabs>
  <Tab title="Python">
    ```python PYTHON
    from openai import OpenAI

    client = OpenAI(
        base_url="https://api.cohere.ai/compatibility/v1",
        api_key=COHERE_API_KEY,
    )

    response = client.embeddings.create(
        input=["Hello world!"],
        model="embed-v4.0",
        encoding_format="float",
    )

    print(
        response.data[0].embedding[:5]
    )  # Display the first 5 dimensions
    ```
  </Tab>

  <Tab title="TypeScript">
    ```typescript TYPESCRIPT
    import OpenAI from "openai";

    const openai = new OpenAI({
        baseURL: "https://api.cohere.ai/compatibility/v1",
        apiKey: "COHERE_API_KEY",
        });

    const response = await openai.embeddings.create({
        input: ["Hello world!"],
        model: "embed-v4.0",
        encoding_format: "float"
    });

    console.log(response.data[0].embedding.slice(0, 5)); // Display the first 5 dimensions
    ```
  </Tab>

  <Tab title="cURL">
    ```bash
    curl --request POST \
        --url https://api.cohere.ai/compatibility/v1/embeddings \
        --header 'Authorization: Bearer COHERE_API_KEY' \
        --header 'Content-Type: application/json' \
        --data '{
        "model": "embed-v4.0",
        "input": ["Hello world!"],
        "encoding_format": "float"
    }'

    ```
  </Tab>
</Tabs>

Example response (via the Python SDK):

```mdx
[0.0045051575, 0.046905518, 0.025543213, 0.009651184, -0.024993896]
```

## Supported parameters

The following is the list supported parameters in the Compatibility API, including those that are not explicitly demonstrated in the examples above:

### Chat completions

* `model`
* `messages`
* `stream`
* `reasoning_effort` (Only "none" and "high" are currently supported.)
* `response_format`
* `tools`
* `temperature`
* `max_tokens`
* `stop`
* `seed`
* `top_p`
* `frequency_penalty`
* `presence_penalty`

<Warning title="Note">
  Currently, only **`none`** and **`high`** are supported for `reasoning_effort`.\
  These correspond to enabling or disabling `thinking` in the Cohere Chat API.\
  Passing **`medium`** or **`low`** is **not supported** at this time.
</Warning>

### Embeddings

* `input`
* `model`
* `encoding_format`

## Unsupported parameters

The following parameters are not supported in the Compatibility API:

### Chat completions

* `store`
* `metadata`
* `logit_bias`
* `top_logprobs`
* `n`
* `modalities`
* `prediction`
* `audio`
* `service_tier`
* `parallel_tool_calls`

### Embeddings

* `dimensions`
* `user`

### Cohere-specific parameters

Parameters that are uniquely available on the Cohere API but not on the OpenAI SDK are not supported.

Chat endpoint:

* `connectors`
* `documents`
* `citation_options`
* ...[more here](https://docs.cohere.com/reference/chat)

Embed endpoint:

* `input_type`
* `images`
* `truncate`
* ...[more here](https://docs.cohere.com/reference/embed)



---

**Navigation:** [← Previous](./07-querying-structured-data-tables.md) | [Index](./index.md) | [Next →](./09-chat.md)
