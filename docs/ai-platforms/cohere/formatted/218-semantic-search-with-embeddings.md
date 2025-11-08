---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Semantic Search with Embeddings

> Examples on how to use the Embed endpoint to perform semantic search (API v2).

This section provides examples on how to use the Embed endpoint to perform semantic search.

Semantic search solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles to capture the context or meaning of a piece of text.
```python PYTHON
import cohere
import numpy as np

co = cohere.ClientV2(
    api_key="YOUR_API_KEY"
)  # Get your free API key: https://dashboard.cohere.com/api-keys

```
The Embed endpoint takes in texts as input and returns embeddings as output.

For semantic search, there are two types of documents we need to turn into embeddings.

* The list of documents to search from.
* The query that will be used to search the documents.

### Step 1: Embed the documents

We call the Embed endpoint using `co.embed()` and pass the required arguments:

* `texts`: The list of texts
* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents for search
* `embedding_types`: We choose `float` to get a float array as the output

### Step 2: Embed the query

Next, we add and embed a query. We choose `search_query` as the `input_type` to ensure the model treats this as the query (instead of documents) for search.

### Step 3: Return the most similar documents

Next, we calculate and sort similarity scores between a query and document embeddings, then display the top N most similar documents. Here, we are using the numpy library for calculating similarity using a dot product approach.

<CodeBlocks>
```python PYTHON
  ### STEP 1: Embed the documents

  # Define the documents

  documents = [
      "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
      "Finding Coffee Spots: For your caffeine fix, head to the break room's coffee machine or cross the street to the café for artisan coffee.",
      "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!",
      "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
  ]

  # Constructing the embed_input object

  embed_input = [
      {"content": [{"type": "text", "text": doc}]} for doc in documents
  ]

  # Embed the documents

  doc_emb = co.embed(
      inputs=embed_input,
      model="embed-v4.0",
      output_dimension=1024,
      input_type="search_document",
      embedding_types=["float"],
  ).embeddings.float

  ### STEP 2: Embed the query

  # Add the user query

  query = "How to connect with my teammates?"

  query_input = [{"content": [{"type": "text", "text": query}]}]

  # Embed the query

  query_emb = co.embed(
      inputs=query_input,
      model="embed-v4.0",
      input_type="search_query",
      output_dimension=1024,
      embedding_types=["float"],
  ).embeddings.float

  ### STEP 3: Return the most similar documents

  # Calculate similarity scores

  scores = np.dot(query_emb, np.transpose(doc_emb))[0]

  # Sort and filter documents based on scores

  top_n = 2
  top_doc_idxs = np.argsort(-scores)[:top_n]

  # Display search results

  for idx, docs_idx in enumerate(top_doc_idxs):
      print(f"Rank: {idx+1}")
      print(f"Document: {documents[docs_idx]}\n")
```
```bash cURL
  # Step 1: Embed the documents

  curl --request POST \
    --url https://api.cohere.ai/v2/embed \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_document",
    "embedding_types": ["float"],
    "output_dimension": 1024,
    "inputs": [
      {
        "content": [
          {
            "type": "text",
            "text": "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged."
          }
        ]
      },
      {
        "content": [
          {
            "type": "text",
            "text": "Finding Coffee Spots: For your caffeine fix, head to the break room'\''s coffee machine or cross the street to the café for artisan coffee."
          }
        ]
      },
      {
        "content": [
          {
            "type": "text",
            "text": "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!"
          }
        ]
      },
      {
        "content": [
          {
            "type": "text",
            "text": "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed."
          }
        ]
      }
    ]
  }'

  # Step 2: Embed the query

  curl --request POST \
    --url https://api.cohere.ai/v2/embed \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_query",
    "embedding_types": ["float"],
    "output_dimension": 1024,
    "inputs": [
      {
        "content": [
          {
            "type": "text",
            "text": "How to connect with my teammates?"
          }
        ]
      }
    ]
  }'
```
</CodeBlocks>

Here's an example output:
```
Rank: 1
Document: Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!

Rank: 2
Document: Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
