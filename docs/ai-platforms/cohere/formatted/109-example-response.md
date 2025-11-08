---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Example response

{
  "name": "Emma Johnson",
  "age": 32
}
```
<Info title="Important">
  When using  `{ "type": "json_object" }` your `message` should always explicitly instruct the model to generate a JSON (eg: *"Generate a JSON ..."*) . Otherwise the model may end up getting stuck generating an infinite stream of characters and eventually run out of context length.
</Info>

<Note title="Note">
  This feature is currently not supported in [RAG](https://docs.cohere.com/docs/retrieval-augmented-generation-rag) mode.
</Note>

#### JSON Schema mode

In JSON Schema mode, you can optionally define a schema as part of the `response_format`  parameter. A [JSON Schema](https://json-schema.org/specification) is a way to describe the structure of the JSON object you want the LLM to generate.

This forces the LLM to stick to this schema, thus giving you greater control over the output.

For example, let's say you want the LLM to generate a JSON object with specific keys for a book, such as "title," "author," and "publication\_year." Your API request might look like this:

<CodeBlocks>
```python PYTHON
  import cohere

  co = cohere.ClientV2(api_key="YOUR API KEY")

  res = co.chat(
      model="command-a-03-2025",
      messages=[
          {
              "role": "user",
              "content": "Generate a JSON describing a book, with the fields 'title' and 'author' and 'publication_year'",
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

  print(res.message.content[0].text)
```
```bash cURL
  curl --request POST \
    --url https://api.cohere.ai/v2/chat \
    --header 'accept: application/json' \
    --header 'content-type: application/json' \
    --header "Authorization: bearer $CO_API_KEY" \
    --data '{
      "model": "command-a-03-2025",
      "messages": [
        {
          "role": "user",
          "content": "Generate a JSON describing a book, with the fields '\''title'\'' and '\''author'\'' and '\''publication_year'\''"
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
</CodeBlocks>

In this schema, we defined three keys ("title," "author," "publication\_year") and their expected data types ("string" and "integer"). The LLM will generate a JSON object that adheres to this structure.
```

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
