---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Handling connection for 8080

```
Leave that running in the background, and up a new terminal session to execute a test request. In the next few sections, we'll include examples of appropriate requests for the major Cohere models.

**Example Usage**

Here are the `bash` commands you can run to use the Embed English, Embed Multilingual, Rerank English, Rerank Multilingual, and Command models through Kubernetes.

<CodeBlocks>
```Text Embed English
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing embeddings in english"], "input_type": "classification"}'

  # {"id":"2ffe4bca-8664-4456-b858-1b3b15411f2c","embeddings":[[-0.5019531,-2.0917969,-1.6220703,-1.2919922,-0.80029297,1.3173828,1.4677734,-1.7763672,0.03869629,1.9033203...}

```
```Text Embed Multilingual
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/embed --data-raw '{"texts": ["testing multilingual embeddings"], "input_type": "classification"}'

  # {"id":"2eab88e7-5906-44e1-9644-01893a70f1e7","texts":["testing multilingual embeddings"],"embeddings":[[-0.022094727,-0.0121154785,0.037628174,-0.0026988983,-0.0129776,0.013305664,0.005458832,-0.03161621,-0.019744873,-0.026290894,0.017333984,-0.02444458,0.01953125...

```
```Text Rerank English
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  # {"id":"a547bcc5-a243-42dd-8617-d12a7944c164","results":[{"index":1,"relevance_score":0.9734939},{"index":2,"relevance_score":0.73772544}]}

```
```Text Rerank Multilingual
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/rerank --data-raw '{"documents": [{"text": "orange"},{"text": "Ottawa"},{"text": "Toronto"},{"text": "Ontario"}],"query": "what is the capital of Canada","top_n": 2}'

  # {"id":"8abeacf2-e657-415c-bab3-ac593e67e8e5","results":[{"index":1,"relevance_score":0.6124835},{"index":2,"relevance_score":0.5305253}],"meta":{"api_version":{"version":"2022-12-06"},"billed_units":{"search_units":1}}}

```
```Text Command
  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{"query":"Docker is good because"}'

  {
    "response_id": "dc182f8d-2db1-4b13-806c-e1bcea17f864",
    "text": "Docker is a powerful tool for developing,..."
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "chat_history": [
          {"role": "USER", "message": "Who discovered gravity?"},
          {"role": "CHATBOT", "message": "The man who is widely credited with discovering gravity is Sir Isaac Newton"}
      ],
      "message": "What year was he born?"
  }'

  {
    "response_id": "7938d788-f800-4f9b-a12c-72a96b76a6d6",
    "text": "Sir Isaac Newton was born in Woolsthorpe, England, on January 4, 1643. He was an English physicist, mathematician, astronomer, and natural philosopher who is widely recognized as one of the most...",
    ...
  }

  curl --header "Content-Type: application/json" --request POST http://localhost:8080/chat --data-raw '{
      "message": "tell me about penguins",
      "return_chatlog": true,
      "documents": [
        {
          "title": "Tall penguins",
          "snippet": "Emperor penguins are the tallest",
          "url": "http://example.com/foo"
        },
        {
          "title": "Tall penguins",
          "snippet": "Baby penguins are the tallest",
          "url": "https://example.com/foo"
        }
      ],
      "mode": "augmented_generation"
  }'

  {
    "response_id": "8a9f55f6-26aa-455e-bc4c-3e93d4b0d9e6",
    "text": "Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins?",
    "generation_id": "65ef2270-46bb-427d-b54c-2e5f4d7daa90",
    "chatlog": "User: tell me about penguins\nChatbot: Penguins are a group of flightless birds that live in the Southern Hemisphere. There are many different types of penguins, including the Emperor penguin, which is the tallest of the penguin species. Baby penguins are also known to be the tallest species of penguin. \n\nWould you like to know more about the different types of penguins? ",
    "token_count": {
      "prompt_tokens": 435,
      "response_tokens": 68,
      "total_tokens": 503
    },
    "meta": {
      "api_version": {
        "version": "2022-12-06"
      },
      "billed_units": {
        "input_tokens": 4,
        "output_tokens": 68
      }
    },
    "citations": [
      {
        "start": 15,
        "end": 40,
        "text": "group of flightless birds",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 58,
        "end": 78,
        "text": "Southern Hemisphere.",
        "document_ids": [
          "doc_1"
        ]
      },
      {
        "start": 137,
        "end": 152,
        "text": "Emperor penguin",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 167,
        "end": 174,
        "text": "tallest",
        "document_ids": [
          "doc_0"
        ]
      },
      {
        "start": 238,
        "end": 265,
        "text": "tallest species of penguin.",
        "document_ids": [
          "doc_1"
        ]
      }
    ],
    "documents": [
      {
        "id": "doc_1",
        "snippet": "Baby penguins are the tallest",
        "title": "Tall penguins",
        "url": "https://example.com/foo"
      },
      {
        "id": "doc_0",
        "snippet": "Emperor penguins are the tallest",
        "title": "Tall penguins",
        "url": "http://example.com/foo"
      }
    ]
  }
```
</CodeBlocks>

Remember that this is only an illustrative deployment. Feel free to modify it as needed to accommodate your environment.

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
