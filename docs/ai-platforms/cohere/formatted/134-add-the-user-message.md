---
title: "Cohere Documentation"
description: "Formatted documentation for Cohere"
source: "llms-full.txt"
last_updated: "2025-11-08"
---

## Add the user message

message = "Who is more popular: Nsync or Backstreet Boys?"
messages = [{"role": "user", "content": message}]

response = co.chat(
    model="command-a-03-2025",
    messages=messages,
    documents=documents,
)

print(response.message.content[0].text)
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
        "content": "Who is more popular: Nsync or Backstreet Boys?"
      }
    ],
    "documents": [
      {
        "data": {
          "title": "CSPC: Backstreet Boys Popularity Analysis - ChartMasters",
          "snippet": "At one point, Backstreet Boys defined success: massive albums sales across the globe..."
        }
      },
      {
        "data": {
          "title": "CSPC: NSYNC Popularity Analysis - ChartMasters",
          "snippet": "At the turn of the millennium three teen acts were huge in the US..."
        }
      }
    ]
  }'
```
Example response:
```mdx
Both NSYNC and Backstreet Boys were huge in the US at the turn of the millennium. However, Backstreet Boys achieved a greater level of success than NSYNC. They dominated the music business for a few years all over the world, including in some countries that were traditionally hard to penetrate for Western artists. Their success included massive album sales across the globe, great singles sales, plenty of chart-topping releases, hugely hyped tours and tremendous media coverage.
```
In this RAG setting, Cohere models are trained to generate fine-grained citations, out-of-the-box, alongside their text output. Here, we see a sample list of citations, one for each specific span in its response, where it uses the document(s) to answer the question.

For a deeper dive into the citations feature, see the [RAG citations guide](https://docs.cohere.com/v2/docs/rag-citations).
```python PYTHON
print(response.message.citations)
```
Example response:
```mdx

---

**📚 [Back to Index](./index.md)** | **📄 [Full Version](./documentation.md)** | **🔗 [Original](../llms-full.txt)**
