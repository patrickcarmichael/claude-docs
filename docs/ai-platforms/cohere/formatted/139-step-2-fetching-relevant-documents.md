---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Step 2: Fetching relevant documents

### Retrieval with Embed

Given the search query, we need a way to retrieve the most relevant documents from a large collection of documents.

This is where we can leverage text embeddings through the [Embed endpoint](https://docs.cohere.com/reference/embed).

The Embed endpoint enables semantic search, which lets us to compare the semantic meaning of the documents and the query. It solves the problem faced by the more traditional approach of lexical search, which is great at finding keyword matches, but struggles at capturing the context or meaning of a piece of text.

The Embed endpoint takes in texts as input and returns embeddings as output.

First, we need to embed the documents to search from. We call the Embed endpoint using `co.embed()` and pass the following arguments:

* `model`: Here we choose `embed-v4.0`
* `input_type`: We choose `search_document` to ensure the model treats these as the documents (instead of the query) for search
* `texts`: The list of texts (the FAQs)
* `embedding_types`: We choose the `float` as the embedding type.

<CodeBlocks>
```python PYTHON
  # Define the documents

  documents = [
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
      texts=[doc["data"]["text"] for doc in documents],
      embedding_types=["float"],
  ).embeddings.float
```
```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/embed' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_document",
    "embedding_types": ["float"],
    "texts": [
      "Joining Slack Channels: You will receive an invite via email. Be sure to join relevant channels to stay informed and engaged.",
      "Finding Coffee Spots: For your caffeine fix, head to the break room'\''s coffee machine or cross the street to the café for artisan coffee.",
      "Team-Building Activities: We foster team spirit with monthly outings and weekly game nights. Feel free to suggest new activity ideas anytime!",
      "Working Hours Flexibility: We prioritize work-life balance. While our core hours are 9 AM to 5 PM, we offer flexibility to adjust as needed.",
      "Side Projects Policy: We encourage you to pursue your passions. Just be mindful of any potential conflicts of interest with our business.",
      "Reimbursing Travel Expenses: Easily manage your travel expenses by submitting them through our finance tool. Approvals are prompt and straightforward.",
      "Working from Abroad: Working remotely from another country is possible. Simply coordinate with your manager and ensure your availability during core hours.",
      "Health and Wellness Benefits: We care about your well-being and offer gym memberships, on-site yoga classes, and comprehensive health insurance.",
      "Performance Reviews Frequency: We conduct informal check-ins every quarter and formal performance reviews twice a year.",
      "Proposing New Ideas: Innovation is welcomed! Share your brilliant ideas at our weekly team meetings or directly with your team lead."
    ]
  }'
```
</CodeBlocks>

We choose `search_query` as the `input_type` in the Embed endpoint call. This ensures the model treats this as the query (instead of the documents) for search.

<CodeBlocks>
```python PYTHON
  # Embed the search query

  query_emb = co.embed(
      model="embed-v4.0",
      input_type="search_query",
      texts=search_queries,
      embedding_types=["float"],
  ).embeddings.float
```
```bash cURL
  curl --request POST \
    --url 'https://api.cohere.ai/v2/embed' \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
    "model": "embed-v4.0",
    "input_type": "search_query",
    "embedding_types": ["float"],
    "texts": ["how to get to know your teammates"]
  }'
```
</CodeBlocks>

Now, we want to search for the most relevant documents to the query. For this, we make use of the `numpy` library to compute the similarity between each query-document pair using the dot product approach.

Each query-document pair returns a score, which represents how similar the pair are. We then sort these scores in descending order and select the top most similar pairs, which we choose 5 (this is an arbitrary choice, you can choose any number).

Here, we show the most relevant documents with their similarity scores.
```python PYTHON

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
